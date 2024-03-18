resource "azurerm_kubernetes_cluster" "pc" {
  name                = "${local.prefix}-cluster"
  location            = azurerm_resource_group.pc.location
  resource_group_name = azurerm_resource_group.pc.name
  dns_prefix          = "${local.prefix}-cluster"
  kubernetes_version  = var.k8s_version

  oidc_issuer_enabled       = true
  workload_identity_enabled = true


  default_node_pool {
    name                 = "agentpool"
    vm_size              = "Standard_DS2_v2"
    node_count           = var.aks_node_count
    vnet_subnet_id       = azurerm_subnet.node_subnet.id
    orchestrator_version = var.k8s_version
  }

  identity {
    type = "SystemAssigned"
  }

  azure_active_directory_role_based_access_control {
    managed            = true
    azure_rbac_enabled = true
  }

  tags = {
    Environment = var.environment
    ManagedBy   = "AI4E"
  }
}

# Workload Identity for tiler access to the Azure Maps account
resource "azurerm_user_assigned_identity" "tiler" {
  name                = "id-${local.prefix}"
  location            = var.region
  resource_group_name = azurerm_resource_group.pc.name
}

resource "azurerm_federated_identity_credential" "tiler" {
  name                = "federated-id-${local.prefix}"
  resource_group_name = azurerm_resource_group.pc.name
  audience            = ["api://AzureADTokenExchange"]
  issuer              = azurerm_kubernetes_cluster.pc.oidc_issuer_url
  subject             = "system:serviceaccount:pc:planetary-computer-tiler"
  parent_id           = azurerm_user_assigned_identity.tiler.id
  timeouts {}
}

resource "azurerm_role_assignment" "cluster-identity-maps-render-token" {
  scope                = azurerm_maps_account.azmaps.id
  role_definition_name = "Azure Maps Search and Render Data Reader"
  principal_id         = azurerm_user_assigned_identity.tiler.principal_id

}

# add the role to the identity the kubernetes cluster was assigned
resource "azurerm_role_assignment" "network" {
  scope                = azurerm_resource_group.pc.id
  role_definition_name = "Network Contributor"
  principal_id         = azurerm_kubernetes_cluster.pc.identity[0].principal_id
}
