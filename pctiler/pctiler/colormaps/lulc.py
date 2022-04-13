from typing import Dict

from rio_tiler.types import ColorMapType

lulc_colormaps: Dict[str, ColorMapType] = {
    "ai4g-lulc": {
        0: (0, 0, 0, 0),
        1: (0, 197, 255, 255),
        2: (0, 168, 132, 255),
        3: (38, 115, 0, 255),
        4: (76, 230, 0, 255),
        5: (163, 255, 115, 255),
        6: (255, 170, 0, 255),
        7: (255, 0, 0, 255),
        8: (156, 156, 156, 255),
        9: (0, 0, 0, 255),
        10: (115, 115, 0, 255),
        11: (230, 230, 0, 255),
        12: (255, 255, 115, 255),
        13: (197, 0, 255, 25),
    },
    "esa-worldcover": {
        0: (0, 0, 0, 0),
        10: (0, 100, 0, 255),
        20: (255, 187, 34, 255),
        30: (255, 255, 76, 255),
        40: (240, 150, 255, 255),
        50: (250, 0, 0, 255),
        60: (180, 180, 180, 255),
        70: (240, 240, 240, 255),
        80: (0, 100, 200, 255),
        90: (0, 150, 160, 255),
        95: (0, 207, 117, 255),
        100: (250, 230, 160, 255),
    },
    "io-lulc": {
        0: (0, 0, 0, 0),
        1: (65, 155, 223, 255),
        2: (57, 125, 73, 255),
        3: (136, 176, 83, 255),
        4: (122, 135, 198, 255),
        5: (228, 150, 53, 255),
        6: (223, 195, 90, 255),
        7: (196, 40, 27, 255),
        8: (165, 155, 143, 255),
        9: (168, 235, 255, 255),
        10: (97, 97, 97, 255),
    },
    "io-lulc-9-class": {
        0: (0, 0, 0, 0),
        1: (65, 155, 223, 255),
        2: (57, 125, 73, 255),
        3: (136, 176, 83, 0),
        4: (122, 135, 198, 255),
        5: (228, 150, 53, 255),
        6: (223, 195, 90, 0),
        7: (196, 40, 27, 255),
        8: (165, 155, 143, 255),
        9: (168, 235, 255, 255),
        10: (97, 97, 97, 255),
        11: (227, 226, 195, 255),
    },
    "gap-lulc": {
        0: (255, 255, 255, 0),
        1: (0, 132, 125, 255),
        2: (0, 132, 125, 255),
        3: (0, 132, 125, 255),
        4: (30, 224, 159, 255),
        5: (43, 211, 53, 255),
        6: (43, 211, 53, 255),
        7: (43, 211, 53, 255),
        8: (179, 250, 176, 255),
        9: (41, 146, 45, 255),
        10: (41, 146, 45, 255),
        11: (41, 146, 45, 255),
        12: (41, 146, 45, 255),
        13: (41, 146, 45, 255),
        14: (41, 146, 45, 255),
        15: (41, 146, 45, 255),
        16: (41, 146, 45, 255),
        17: (41, 146, 45, 255),
        18: (41, 191, 0, 255),
        19: (41, 191, 0, 255),
        20: (41, 191, 0, 255),
        21: (41, 191, 0, 255),
        22: (41, 191, 0, 255),
        23: (41, 191, 0, 255),
        24: (41, 191, 0, 255),
        25: (41, 191, 0, 255),
        26: (41, 191, 0, 255),
        27: (41, 191, 0, 255),
        28: (41, 191, 0, 255),
        29: (41, 191, 0, 255),
        30: (100, 191, 0, 255),
        31: (100, 191, 0, 255),
        32: (100, 191, 0, 255),
        33: (168, 191, 45, 255),
        34: (168, 191, 45, 255),
        35: (168, 191, 45, 255),
        36: (168, 191, 45, 255),
        37: (168, 191, 45, 255),
        38: (168, 191, 45, 255),
        39: (31, 156, 92, 255),
        40: (31, 156, 92, 255),
        41: (31, 156, 92, 255),
        42: (31, 156, 92, 255),
        43: (31, 156, 92, 255),
        44: (31, 156, 92, 255),
        45: (31, 156, 92, 255),
        46: (0, 156, 143, 255),
        47: (0, 156, 143, 255),
        48: (31, 156, 80, 255),
        49: (31, 156, 80, 255),
        50: (0, 156, 133, 255),
        51: (0, 156, 133, 255),
        52: (0, 156, 133, 255),
        53: (0, 156, 133, 255),
        54: (99, 120, 92, 255),
        55: (99, 120, 92, 255),
        56: (99, 120, 92, 255),
        57: (99, 120, 92, 255),
        58: (99, 120, 92, 255),
        59: (135, 156, 92, 255),
        60: (38, 173, 0, 255),
        61: (38, 173, 0, 255),
        62: (38, 173, 0, 255),
        63: (38, 173, 0, 255),
        64: (38, 173, 0, 255),
        65: (38, 173, 0, 255),
        66: (38, 173, 0, 255),
        67: (38, 173, 0, 255),
        68: (38, 173, 0, 255),
        69: (38, 173, 0, 255),
        70: (38, 173, 0, 255),
        71: (38, 173, 0, 255),
        72: (38, 173, 0, 255),
        73: (38, 173, 0, 255),
        74: (38, 173, 0, 255),
        75: (38, 173, 0, 255),
        76: (38, 173, 0, 255),
        77: (38, 173, 0, 255),
        78: (38, 173, 0, 255),
        79: (38, 173, 0, 255),
        80: (38, 173, 0, 255),
        81: (38, 173, 0, 255),
        82: (38, 173, 0, 255),
        83: (38, 173, 0, 255),
        84: (38, 173, 0, 255),
        85: (38, 173, 0, 255),
        86: (38, 173, 0, 255),
        87: (38, 173, 0, 255),
        88: (38, 173, 0, 255),
        89: (110, 115, 0, 255),
        90: (110, 115, 0, 255),
        91: (110, 115, 0, 255),
        92: (110, 115, 0, 255),
        93: (54, 130, 0, 255),
        94: (54, 130, 0, 255),
        95: (54, 130, 0, 255),
        96: (54, 130, 0, 255),
        97: (54, 130, 0, 255),
        98: (54, 130, 0, 255),
        99: (54, 130, 0, 255),
        100: (54, 130, 0, 255),
        101: (54, 130, 0, 255),
        102: (54, 130, 0, 255),
        103: (38, 115, 0, 255),
        104: (38, 115, 0, 255),
        105: (38, 115, 0, 255),
        106: (38, 115, 0, 255),
        107: (38, 115, 0, 255),
        108: (38, 115, 0, 255),
        109: (38, 115, 0, 255),
        110: (38, 115, 0, 255),
        111: (38, 115, 0, 255),
        112: (38, 115, 0, 255),
        113: (38, 115, 0, 255),
        114: (38, 115, 0, 255),
        115: (99, 105, 0, 255),
        116: (99, 105, 0, 255),
        117: (99, 105, 0, 255),
        118: (99, 105, 0, 255),
        119: (99, 105, 0, 255),
        120: (38, 110, 0, 255),
        121: (38, 110, 0, 255),
        122: (38, 110, 0, 255),
        123: (38, 110, 0, 255),
        124: (38, 110, 0, 255),
        125: (38, 110, 0, 255),
        126: (38, 110, 0, 255),
        127: (38, 110, 0, 255),
        128: (38, 110, 0, 255),
        129: (38, 110, 0, 255),
        130: (38, 115, 87, 255),
        131: (38, 115, 87, 255),
        132: (38, 115, 87, 255),
        133: (38, 115, 87, 255),
        134: (38, 115, 87, 255),
        135: (38, 115, 87, 255),
        136: (0, 84, 0, 255),
        137: (0, 84, 0, 255),
        138: (0, 84, 0, 255),
        139: (0, 84, 0, 255),
        140: (0, 84, 0, 255),
        141: (0, 84, 0, 255),
        142: (0, 84, 0, 255),
        143: (0, 84, 0, 255),
        144: (0, 84, 0, 255),
        145: (0, 69, 0, 255),
        146: (0, 69, 0, 255),
        147: (0, 69, 0, 255),
        148: (0, 69, 0, 255),
        149: (0, 69, 0, 255),
        150: (0, 69, 0, 255),
        151: (0, 69, 0, 255),
        152: (0, 69, 0, 255),
        153: (0, 69, 0, 255),
        154: (0, 99, 20, 255),
        155: (0, 99, 20, 255),
        156: (0, 99, 20, 255),
        157: (0, 99, 20, 255),
        158: (0, 99, 20, 255),
        159: (0, 69, 50, 255),
        160: (0, 69, 50, 255),
        161: (0, 69, 50, 255),
        162: (0, 69, 50, 255),
        163: (0, 69, 50, 255),
        164: (0, 69, 50, 255),
        165: (0, 84, 69, 255),
        166: (0, 84, 69, 255),
        167: (0, 84, 69, 255),
        168: (0, 84, 69, 255),
        169: (0, 84, 69, 255),
        170: (0, 84, 69, 255),
        171: (0, 84, 69, 255),
        172: (0, 84, 69, 255),
        173: (0, 84, 69, 255),
        174: (0, 84, 69, 255),
        175: (79, 133, 120, 255),
        176: (79, 133, 120, 255),
        177: (79, 133, 120, 255),
        178: (79, 133, 120, 255),
        179: (79, 133, 120, 255),
        180: (79, 133, 120, 255),
        181: (79, 133, 120, 255),
        182: (102, 125, 22, 255),
        183: (102, 125, 22, 255),
        184: (102, 125, 22, 255),
        185: (102, 125, 22, 255),
        186: (89, 125, 22, 255),
        187: (89, 125, 22, 255),
        188: (89, 125, 22, 255),
        189: (89, 125, 22, 255),
        190: (0, 97, 115, 255),
        191: (0, 97, 115, 255),
        192: (0, 97, 115, 255),
        193: (0, 97, 115, 255),
        194: (0, 97, 115, 255),
        195: (0, 87, 130, 255),
        196: (0, 87, 130, 255),
        197: (0, 87, 130, 255),
        198: (0, 87, 130, 255),
        199: (0, 87, 130, 255),
        200: (0, 87, 130, 255),
        201: (0, 87, 130, 255),
        202: (0, 87, 130, 255),
        203: (0, 87, 130, 255),
        204: (102, 97, 150, 255),
        205: (102, 97, 150, 255),
        206: (102, 97, 150, 255),
        207: (102, 97, 150, 255),
        208: (102, 97, 150, 255),
        209: (102, 97, 150, 255),
        210: (102, 97, 150, 255),
        211: (102, 97, 150, 255),
        212: (102, 97, 150, 255),
        213: (52, 156, 121, 255),
        214: (52, 156, 121, 255),
        215: (52, 156, 121, 255),
        216: (52, 156, 121, 255),
        217: (52, 156, 121, 255),
        218: (52, 156, 121, 255),
        219: (52, 156, 121, 255),
        220: (52, 156, 121, 255),
        221: (52, 156, 121, 255),
        222: (52, 156, 121, 255),
        223: (52, 156, 121, 255),
        224: (52, 156, 121, 255),
        225: (52, 156, 121, 255),
        226: (52, 156, 121, 255),
        227: (52, 156, 121, 255),
        228: (52, 156, 121, 255),
        229: (52, 156, 121, 255),
        230: (52, 156, 121, 255),
        231: (52, 156, 121, 255),
        232: (52, 156, 121, 255),
        233: (52, 156, 121, 255),
        234: (52, 156, 121, 255),
        235: (52, 156, 121, 255),
        236: (52, 156, 163, 255),
        237: (52, 156, 163, 255),
        238: (52, 156, 163, 255),
        239: (52, 156, 163, 255),
        240: (52, 156, 163, 255),
        241: (0, 112, 156, 255),
        242: (0, 112, 156, 255),
        243: (0, 112, 156, 255),
        244: (0, 112, 156, 255),
        245: (0, 112, 156, 255),
        246: (0, 112, 156, 255),
        247: (0, 112, 156, 255),
        248: (0, 112, 156, 255),
        249: (0, 112, 156, 255),
        250: (0, 112, 156, 255),
        251: (0, 112, 156, 255),
        252: (0, 112, 156, 255),
        253: (52, 156, 161, 255),
        254: (0, 156, 122, 255),
        255: (0, 156, 122, 255),
        256: (0, 156, 122, 255),
        257: (0, 156, 122, 255),
        258: (0, 156, 122, 255),
        259: (0, 156, 122, 255),
        260: (0, 156, 122, 255),
        261: (0, 156, 122, 255),
        262: (0, 156, 122, 255),
        263: (0, 156, 122, 255),
        264: (0, 156, 122, 255),
        265: (7, 134, 129, 255),
        266: (7, 134, 129, 255),
        267: (7, 134, 129, 255),
        268: (7, 134, 129, 255),
        269: (7, 134, 129, 255),
        270: (7, 134, 129, 255),
        271: (7, 134, 129, 255),
        272: (7, 134, 129, 255),
        273: (7, 134, 161, 255),
        274: (7, 134, 161, 255),
        275: (7, 134, 161, 255),
        276: (7, 134, 161, 255),
        277: (51, 147, 163, 255),
        278: (51, 147, 163, 255),
        279: (51, 147, 163, 255),
        280: (51, 147, 163, 255),
        281: (51, 147, 163, 255),
        282: (51, 147, 163, 255),
        283: (51, 147, 163, 255),
        284: (51, 147, 163, 255),
        285: (77, 79, 38, 255),
        286: (77, 79, 38, 255),
        287: (77, 79, 38, 255),
        288: (0, 88, 120, 255),
        289: (0, 89, 77, 255),
        290: (246, 138, 18, 255),
        291: (246, 138, 18, 255),
        292: (246, 138, 18, 255),
        293: (201, 255, 240, 255),
        294: (201, 255, 240, 255),
        295: (201, 255, 240, 255),
        296: (242, 118, 18, 255),
        297: (242, 118, 18, 255),
        298: (242, 118, 18, 255),
        299: (242, 118, 18, 255),
        300: (242, 118, 18, 255),
        301: (242, 118, 18, 255),
        302: (242, 118, 18, 255),
        303: (200, 118, 18, 255),
        304: (237, 215, 141, 255),
        305: (237, 215, 141, 255),
        306: (245, 190, 99, 255),
        307: (245, 190, 99, 255),
        308: (245, 190, 99, 255),
        309: (245, 190, 99, 255),
        310: (245, 190, 99, 255),
        311: (245, 190, 99, 255),
        312: (245, 190, 99, 255),
        313: (245, 190, 99, 255),
        314: (245, 190, 99, 255),
        315: (245, 190, 99, 255),
        316: (246, 191, 99, 255),
        317: (246, 191, 99, 255),
        318: (246, 191, 150, 255),
        319: (246, 191, 150, 255),
        320: (246, 191, 150, 255),
        321: (246, 191, 150, 255),
        322: (246, 190, 99, 255),
        323: (246, 190, 99, 255),
        324: (194, 156, 100, 255),
        325: (194, 156, 100, 255),
        326: (194, 156, 100, 255),
        327: (194, 156, 100, 255),
        328: (194, 130, 54, 255),
        329: (194, 130, 54, 255),
        330: (225, 201, 100, 255),
        331: (225, 201, 100, 255),
        332: (201, 153, 100, 255),
        333: (201, 153, 100, 255),
        334: (201, 153, 100, 255),
        335: (201, 153, 100, 255),
        336: (201, 153, 100, 255),
        337: (201, 153, 100, 255),
        338: (201, 153, 100, 255),
        339: (201, 153, 100, 255),
        340: (201, 153, 100, 255),
        341: (246, 163, 102, 255),
        342: (240, 163, 102, 255),
        343: (240, 163, 102, 255),
        344: (240, 163, 102, 255),
        345: (246, 163, 90, 255),
        346: (246, 163, 90, 255),
        347: (246, 163, 90, 255),
        348: (246, 163, 90, 255),
        349: (246, 163, 90, 255),
        350: (246, 163, 90, 255),
        351: (246, 163, 90, 255),
        352: (246, 163, 90, 255),
        353: (246, 163, 102, 255),
        354: (246, 163, 102, 255),
        355: (246, 163, 102, 255),
        356: (238, 201, 113, 255),
        357: (238, 201, 113, 255),
        358: (238, 201, 113, 255),
        359: (238, 201, 113, 255),
        360: (209, 201, 113, 255),
        361: (209, 201, 113, 255),
        362: (246, 196, 102, 255),
        363: (246, 196, 102, 255),
        364: (207, 135, 102, 255),
        365: (207, 135, 102, 255),
        366: (246, 196, 166, 255),
        367: (246, 196, 166, 255),
        368: (246, 196, 166, 255),
        369: (255, 229, 74, 255),
        370: (201, 150, 117, 255),
        371: (201, 150, 117, 255),
        372: (201, 150, 117, 255),
        373: (201, 150, 117, 255),
        374: (201, 150, 117, 255),
        375: (201, 150, 117, 255),
        376: (201, 150, 117, 255),
        377: (201, 150, 117, 255),
        378: (201, 150, 117, 255),
        379: (201, 150, 117, 255),
        380: (165, 134, 89, 255),
        381: (165, 134, 89, 255),
        382: (165, 134, 89, 255),
        383: (165, 135, 90, 255),
        384: (165, 135, 90, 255),
        385: (165, 135, 90, 255),
        386: (165, 135, 61, 255),
        387: (165, 135, 61, 255),
        388: (165, 135, 61, 255),
        389: (165, 135, 61, 255),
        390: (165, 135, 61, 255),
        391: (165, 135, 61, 255),
        392: (165, 135, 61, 255),
        393: (165, 135, 61, 255),
        394: (165, 135, 61, 255),
        395: (112, 150, 86, 255),
        396: (112, 150, 86, 255),
        397: (112, 150, 86, 255),
        398: (112, 175, 186, 255),
        399: (112, 175, 86, 255),
        400: (112, 175, 86, 255),
        401: (112, 175, 227, 255),
        402: (112, 175, 227, 255),
        403: (112, 175, 227, 255),
        404: (112, 175, 227, 255),
        405: (112, 175, 180, 255),
        406: (112, 175, 180, 255),
        407: (112, 175, 180, 255),
        408: (112, 175, 180, 255),
        409: (112, 175, 180, 255),
        410: (112, 175, 180, 255),
        411: (112, 175, 180, 255),
        412: (112, 175, 180, 255),
        413: (112, 175, 180, 255),
        414: (112, 175, 180, 255),
        415: (112, 175, 180, 255),
        416: (111, 214, 227, 255),
        417: (111, 214, 227, 255),
        418: (111, 214, 227, 255),
        419: (111, 214, 227, 255),
        420: (111, 214, 227, 255),
        421: (111, 214, 227, 255),
        422: (140, 175, 227, 255),
        423: (140, 175, 227, 255),
        424: (140, 175, 227, 255),
        425: (140, 175, 227, 255),
        426: (140, 175, 227, 255),
        427: (140, 175, 227, 255),
        428: (100, 175, 227, 255),
        429: (0, 194, 196, 255),
        430: (0, 194, 196, 255),
        431: (0, 194, 196, 255),
        432: (0, 194, 196, 255),
        433: (0, 194, 196, 255),
        434: (0, 194, 195, 255),
        435: (0, 194, 195, 255),
        436: (0, 194, 195, 255),
        437: (0, 237, 252, 255),
        438: (0, 237, 252, 255),
        439: (0, 237, 252, 255),
        440: (0, 237, 252, 255),
        441: (0, 237, 252, 255),
        442: (112, 175, 200, 255),
        443: (112, 175, 200, 255),
        444: (112, 175, 200, 255),
        445: (125, 189, 199, 255),
        446: (163, 189, 232, 255),
        447: (163, 189, 232, 255),
        448: (163, 189, 232, 255),
        449: (163, 189, 232, 255),
        450: (163, 189, 232, 255),
        451: (163, 189, 232, 255),
        452: (163, 189, 232, 255),
        453: (163, 189, 232, 255),
        454: (163, 189, 232, 255),
        455: (163, 189, 255, 255),
        456: (163, 189, 214, 255),
        457: (163, 189, 214, 255),
        458: (163, 189, 214, 255),
        459: (163, 189, 214, 255),
        460: (210, 180, 140, 255),
        461: (210, 180, 140, 255),
        462: (210, 180, 140, 255),
        463: (210, 180, 140, 255),
        464: (210, 180, 140, 255),
        465: (210, 180, 140, 255),
        466: (210, 180, 140, 255),
        467: (210, 180, 140, 255),
        468: (210, 180, 140, 255),
        469: (210, 180, 140, 255),
        470: (219, 196, 184, 255),
        471: (219, 196, 184, 255),
        472: (219, 196, 184, 255),
        473: (219, 196, 184, 255),
        474: (219, 196, 184, 255),
        475: (210, 180, 139, 255),
        476: (210, 180, 139, 255),
        477: (179, 173, 171, 255),
        478: (209, 186, 180, 255),
        479: (209, 186, 180, 255),
        480: (209, 186, 180, 255),
        481: (209, 186, 180, 255),
        482: (209, 186, 180, 255),
        483: (209, 186, 180, 255),
        484: (176, 150, 125, 255),
        485: (176, 150, 125, 255),
        486: (199, 174, 168, 255),
        487: (207, 209, 168, 255),
        488: (207, 209, 168, 255),
        489: (207, 209, 168, 255),
        490: (207, 209, 168, 255),
        491: (207, 209, 168, 255),
        492: (156, 181, 125, 255),
        493: (156, 181, 125, 255),
        494: (156, 181, 125, 255),
        495: (156, 181, 125, 255),
        496: (222, 212, 145, 255),
        497: (222, 212, 145, 255),
        498: (222, 212, 145, 255),
        499: (222, 212, 145, 255),
        500: (237, 224, 242, 255),
        501: (235, 217, 230, 255),
        502: (235, 217, 230, 255),
        503: (235, 217, 230, 255),
        504: (235, 207, 201, 255),
        505: (235, 207, 201, 255),
        506: (235, 207, 201, 255),
        507: (235, 207, 201, 255),
        508: (194, 224, 18, 255),
        509: (64, 224, 237, 255),
        510: (64, 224, 237, 255),
        511: (0, 197, 255, 255),
        512: (0, 197, 255, 255),
        513: (0, 143, 255, 255),
        514: (214, 214, 214, 255),
        515: (214, 214, 214, 255),
        516: (214, 214, 214, 255),
        517: (194, 201, 191, 255),
        518: (194, 201, 191, 255),
        519: (194, 201, 191, 255),
        520: (194, 201, 191, 255),
        521: (194, 201, 191, 255),
        522: (194, 201, 191, 255),
        523: (194, 201, 191, 255),
        524: (194, 201, 191, 255),
        525: (194, 201, 191, 255),
        526: (194, 201, 180, 255),
        527: (194, 201, 180, 255),
        528: (194, 201, 180, 255),
        529: (200, 200, 200, 255),
        530: (150, 150, 150, 255),
        531: (150, 150, 150, 255),
        532: (150, 150, 150, 255),
        533: (150, 150, 150, 255),
        534: (150, 150, 150, 255),
        535: (229, 229, 224, 255),
        536: (194, 201, 200, 255),
        537: (194, 201, 200, 255),
        538: (84, 89, 87, 255),
        539: (84, 89, 87, 255),
        540: (84, 89, 87, 255),
        541: (84, 89, 87, 255),
        542: (111, 116, 114, 255),
        543: (111, 116, 114, 255),
        544: (111, 116, 114, 255),
        545: (111, 116, 114, 255),
        546: (111, 116, 114, 255),
        547: (111, 116, 114, 255),
        548: (111, 116, 114, 255),
        549: (236, 120, 241, 255),
        550: (237, 189, 242, 255),
        551: (237, 189, 242, 255),
        552: (140, 143, 145, 255),
        553: (140, 143, 145, 255),
        554: (140, 143, 145, 255),
        555: (254, 219, 193, 255),
        556: (254, 254, 193, 255),
        557: (254, 254, 193, 255),
        558: (161, 69, 156, 255),
        559: (161, 69, 156, 255),
        560: (161, 69, 156, 255),
        561: (161, 69, 156, 255),
        562: (161, 69, 156, 255),
        563: (161, 69, 156, 255),
        564: (161, 69, 156, 255),
        565: (135, 46, 38, 255),
        566: (135, 46, 38, 255),
        567: (135, 46, 38, 255),
        568: (135, 46, 38, 255),
        569: (135, 46, 38, 255),
        570: (135, 46, 38, 255),
        571: (135, 46, 38, 255),
        572: (135, 46, 38, 255),
        573: (135, 46, 38, 255),
        574: (135, 46, 38, 255),
        575: (135, 46, 38, 255),
        576: (135, 46, 38, 255),
        577: (0, 45, 194, 255),
        578: (0, 45, 194, 255),
        579: (0, 45, 194, 255),
        580: (224, 18, 66, 255),
        581: (201, 77, 66, 255),
        582: (201, 77, 66, 255),
        583: (201, 77, 66, 255),
        584: (201, 77, 66, 255),
    },
    "nrcan-lulc": {
        0: (0, 0, 0, 0),
        1: (0, 61, 0, 255),
        2: (147, 155, 112, 255),
        3: (0, 0, 0, 255),
        4: (0, 0, 0, 255),
        5: (20, 140, 61, 255),
        6: (91, 117, 43, 255),
        7: (0, 0, 0, 255),
        8: (178, 137, 51, 255),
        9: (0, 0, 0, 255),
        10: (224, 206, 137, 255),
        11: (155, 117, 137, 255),
        12: (186, 211, 84, 255),
        13: (63, 137, 114, 255),
        14: (107, 163, 137, 255),
        15: (229, 173, 102, 255),
        16: (168, 170, 173, 255),
        17: (219, 33, 38, 255),
        18: (76, 112, 163, 255),
        19: (255, 249, 255, 25),
    },
}
