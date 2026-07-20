BODY_PARTS = [
    "Knee",
    "Hip",
    "Shoulder",
    "Hand/Wrist",
    "Foot/Ankle",
    "Spine"
]

ISSUE_TYPES = [
    "Fracture",
    "Joint Replacement",
    "Sports Medicine",
    "General"
]

LOCATIONS = [
    {
        "code": "MAIN",
        "name": "Main Campus"
    },
    {
        "code": "NORTH",
        "name": "North Clinic"
    },
    {
        "code": "WEST",
        "name": "Westside Office"
    }
]

DOCTORS = [

    {
        "name": "Dr. Maria Chen",
        "accepting_new": True,

        "locations": [
            "MAIN"
        ],

        "capabilities": [
            ("Knee", "Joint Replacement"),
            ("Knee", "Sports Medicine"),
            ("Hip", "Joint Replacement")
        ]
    },

    {
        "name": "Dr. James Walsh",
        "accepting_new": True,

        "locations": [
            "NORTH"
        ],

        "capabilities": [
            ("Knee", "Fracture"),
            ("Knee", "Sports Medicine"),
            ("Foot/Ankle", "Fracture")
        ]
    },

    {
        "name": "Dr. Aisha Patel",
        "accepting_new": False,

        "locations": [
            "MAIN"
        ],

        "capabilities": [
            ("Hip", "Joint Replacement"),
            ("Spine", "General")
        ]
    },

    {
        "name": "Dr. Robert Kim",
        "accepting_new": True,

        "locations": [
            "WEST"
        ],

        "capabilities": [
            ("Hand/Wrist", "Fracture"),
            ("Hand/Wrist", "Sports Medicine"),
            ("Shoulder", "Sports Medicine")
        ]
    },

    {
        "name": "Dr. Linda Torres",
        "accepting_new": True,

        "locations": [
            "MAIN",
            "NORTH"
        ],

        "capabilities": [
            ("Shoulder", "Sports Medicine"),
            ("Knee", "Joint Replacement"),
            ("Hip", "General")
        ]
    },

    {
        "name": "Dr. David Nguyen",
        "accepting_new": True,

        "locations": [
            "NORTH"
        ],

        "capabilities": [
            ("Foot/Ankle", "Fracture"),
            ("Hand/Wrist", "General")
        ]
    },

    {
        "name": "Dr. Sarah O'Brien",
        "accepting_new": False,

        "locations": [
            "WEST"
        ],

        "capabilities": [
            ("Spine", "Fracture")
        ]
    },

    {
        "name": "Dr. Michael Brooks",
        "accepting_new": True,

        "locations": [
            "MAIN"
        ],

        "capabilities": [
            ("Knee", "Joint Replacement"),
            ("Shoulder", "Joint Replacement"),
            ("Shoulder", "Sports Medicine")
        ]
    },

    {
        "name": "Dr. Priya Sharma",
        "accepting_new": True,

        "locations": [
            "NORTH"
        ],

        "capabilities": [
            ("Hip", "Fracture"),
            ("Foot/Ankle", "Joint Replacement")
        ]
    },

    {
        "name": "Dr. Thomas Reed",
        "accepting_new": False,

        "locations": [
            "WEST"
        ],

        "capabilities": [
            ("Hand/Wrist", "Sports Medicine"),
            ("Spine", "General")
        ]
    },

    {
        "name": "Dr. Elena Vasquez",
        "accepting_new": True,

        "locations": [
            "MAIN",
            "WEST"
        ],

        "capabilities": [
            ("Knee", "Fracture"),
            ("Knee", "Sports Medicine"),
            ("Knee", "Joint Replacement"),
            ("Hip", "Sports Medicine"),
            ("Hip", "Joint Replacement"),
            ("Shoulder", "Fracture")
        ]
    },

    {
        "name": "Dr. Carlos Mendez",
        "accepting_new": True,

        "locations": [
            "NORTH"
        ],

        "capabilities": [
            ("Foot/Ankle", "Joint Replacement"),
            ("Spine", "General")
        ]
    }

]