designFile = "C:/Users/Public/Documents/Altium/Projects/RAD_GIT/RadHard/Electronics/AltiumProject/Rad_hard_git/PDNAnalyzer_Output/radhard/odb.tgz"

powerNets = ["NetC3_2"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "load",
"power_pins": [ ("J3", "5") ],
"ground_pins": [ ("J3", "9"), ("J3", "6"), ("J3", "SH2"), ("J3", "SH1") ],
"current": 4,
"Rpin": 0.04,
}
,
{
"id": "1",
"type": "source",
"power_pins": [ ("Q5", "3") ],
"ground_pins": [ ("U1", "4") ],
"voltage": 14,
"Rpin": 0,
}
,
{
"id": "2",
"type": "source",
"power_pins": [ ("Q7", "3") ],
"ground_pins": [ ("U1", "4") ],
"voltage": 14,
"Rpin": 0,
}
]


voltage_regulators = []


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 4, 'Thickness': 2.54E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'INT1__GND_', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.7, 'Thickness': 0.0004572},
        {'name': 'INT2__SIGN_', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-4', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'SUBSTRATE-5', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'INT3__SIGN_', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-6', 'DielectricConstant': 4.7, 'Thickness': 0.0004572},
        {'name': 'INT4__PWR_', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-7', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'SUBSTRATE-8', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 4, 'Thickness': 2.54E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
