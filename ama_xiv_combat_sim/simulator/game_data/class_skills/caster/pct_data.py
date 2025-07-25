from ama_xiv_combat_sim.simulator.game_data.specific_skills import (
    SpecificSkills,
)

all_pct_skills = SpecificSkills()

ALL_DATA = {
    "Fire in Red": {
        90: {"potency": {"7.0": 380, "7.2": 450}},
        100: {"potency": {"7.0": 440, "7.2": 520}},
    },
    "Aero in Green": {
        90: {"potency": {"7.0": 420, "7.2": 490}},
        100: {"potency": {"7.0": 480, "7.2": 560}},
    },
    "Water in Blue": {
        90: {"potency": {"7.0": 460, "7.2": 530}},
        100: {"potency": {"7.0": 520, "7.2": 600}},
    },
    "Fire II in Red": {
        90: {"potency": {"7.0": 100, "7.2": 150}},
        100: {"potency": {"7.0": 120, "7.2": 180}},
    },
    "Mog of the Ages": {
        90: {
            "potency": {"7.0": 1300, "7.2": 1000},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        },
        100: {
            "potency": {"7.0": 1300, "7.2": 1000},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        },
    },
    "Pom Muse": {
        90: {
            "potency": {"7.0": 1100, "7.2": 800},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        },
        100: {
            "potency": {"7.0": 1100, "7.2": 800},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        },
    },
    "Winged Muse": {
        90: {
            "potency": {"7.0": 1100, "7.2": 800},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        },
        100: {
            "potency": {"7.0": 1100, "7.2": 800},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        },
    },
    "Aero II in Green": {
        90: {"potency": {"7.0": 120, "7.2": 170}},
        100: {"potency": {"7.0": 140, "7.2": 200}},
    },
    "Water II in Blue": {
        90: {"potency": {"7.0": 140, "7.2": 190}},
        100: {"potency": {"7.0": 160, "7.2": 220}},
    },
    "Hammer Stamp": {
        90: {
            "potency": {"7.0": 520, "7.2": 460},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        },
        100: {
            "potency": {"7.0": 560, "7.2": 480},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        },
    },
    "Blizzard in Cyan": {
        90: {"potency": {"7.0": 700, "7.2": 790}},
        100: {"potency": {"7.0": 800, "7.2": 900}},
    },
    "Blizzard II in Cyan": {
        90: {"potency": {"7.0": 220}},
        100: {"potency": {"7.0": 240, "7.2": 360}},
    },
    "Stone in Yellow": {
        90: {"potency": {"7.0": 740, "7.2": 830}},
        100: {"potency": {"7.0": 840, "7.2": 940}},
    },
    "Thunder in Magenta": {
        90: {"potency": {"7.0": 780, "7.2": 870}},
        100: {"potency": {"7.0": 880, "7.2": 980}},
    },
    "Stone II in Yellow": {
        90: {"potency": {"7.0": 240, "7.2": 350}},
        100: {"potency": {"7.0": 260, "7.2": 380}},
    },
    "Thunder II in Magenta": {
        90: {"potency": {"7.0": 260, "7.2": 370}},
        100: {"potency": {"7.0": 280, "7.2": 400}},
    },
    "Holy in White": {
        90: {
            "potency": {"7.0": 460, "7.2": 530},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.65},
        },
        100: {
            "potency": {"7.0": 520, "7.2": 600},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.65},
        },
    },
    "Hammer Brush": {
        90: {
            "potency": {"7.0": 580, "7.2": 500},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        },
        100: {
            "potency": {"7.0": 620, "7.2": 520},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        },
    },
    "Polishing Hammer": {
        90: {
            "potency": {"7.0": 640, "7.2": 540},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        },
        100: {
            "potency": {"7.0": 680, "7.2": 560},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        },
    },
    "Comet in Black": {
        90: {
            "potency": {"7.0": 780, "7.2": 870},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.65},
        },
        100: {
            "potency": {"7.0": 880, "7.2": 980},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.65},
        },
    },
    "Rainbow Drip": {100: {"potency": {"7.0": 1000}}},
    "Clawed Muse": {
        100: {
            "potency": {"7.0": 1100, "7.2": 800},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        }
    },
    "Fanged Muse": {
        100: {
            "potency": {"7.0": 1100, "7.2": 800},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        }
    },
    "Retribution of the Madeen": {
        100: {
            "potency": {"7.0": 1400, "7.2": 1100},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        }
    },
    "Star Prism": {
        100: {
            "potency": {"7.0": 1400, "7.2": 1100},
            "aoe_dropoff": {"7.0": 0.6, "7.2": 0.7},
        }
    },
}

for k, v in ALL_DATA.items():
    all_pct_skills.add_skill_data(k, v)
