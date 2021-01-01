APP_NAME = "GlobalCon Calculator"

WEIGHTS = {
    "Completed": 50,
    "Core cards": 1,
    "Original art": 100,
    "Testprint": 13,  # if exists and not in global, put -1
    "Gamma playtest": 15,  # if exists and not in global, put -1
    "Delta playtest": 12,  # if exists and not in global, put -1
    "Epsilon playtest": 10,  # if exists and not in global, put -1
    "Other playtests": 8,
    "Original artist alters": 15,
    "Artist Proof": 10,
    "Summer": 10,  # if exists and not in global, put -1
    "Revised alpha-cut": 5,  # if exists and not in global, put -1
    "Fourth alpha-cut": 5,
    "Square corners": 5,
    "Miscut": 10,
    "Miscut NFC": 4,
    "Offcenters": 3,
    "Crimped": 10,
    "Albino": 10,
    "Signed": 2,
    "Graded BGS 8.5": 4,
    "Graded BGS 9": 8,
    "Graded BGS 9.5": 14,
    "Graded BGS 10": 22,
    "Graded PSA 9": 7,
    "Graded PSA 10": 10,
    "Other rarities": 3,
}

LOGO_FILE = "documentation/GlobalCon_logo.png"

FONT = "Helvetica 14 bold"

RESULTS_FOLDER = "DATA/RESULTS"

DEFAULT_MESSAGES = {
    "Completed": "1 if completed, 0 otherwise",
    "Core cards": "Amount of core cards owned (max 500)",
    "Original art": "Amount of original arts owned (max 10)",
    "Testprint": "Owned testprints, 0 if not owned & doesn't exist, -1 if not owned & exists",
    "Gamma playtest": "1 of owned, 0 if not owned & doesn't exist, -1 if not owned & exists",
    "Delta playtest": "1 of owned, 0 if not owned & doesn't exist, -1 if not owned & exists",
    "Epsilon playtest": "1 of owned, 0 if not owned & doesn't exist, -1 if not owned & exists",
    "Other playtests": "Amount of other playtests owned (max 10)",
    "Original artist alters": "Amount of original artist alters owned (max 10)",
    "Artist Proof": "Amount of different artist proofs owned (max 30)",
    "Summer": "Owned summer cards, 0 if not owned & doesn't exist, -1 if not owned & exists",
    "Revised alpha-cut": "1 if owned, 0 if not owned & doesn't exist, -1 if not owned & exists",
    "Fourth alpha-cut": "1 if owned, 0 if not owned & doesn't exist, -1 if not owned & exists",
    "Square corners": "1 if owned, 0 if not owned & doesn't exist, -1 if not owned & exists",
    "Miscut": "Amount of miscuts owned (max 4)",
    "Miscut NFC": "Amount of NFC miscuts owned (max 4)",
    "Offcenters": "Amount of offcenters owned (max 4)",
    "Crimped": "Amount of crimps owned (max 4)",
    "Albino": "Amount of albinos owned (max 4)",
    "Signed": "Amount of signed cards owned (max 10)",
    "Graded BGS 8.5": "Amount of BGS8.5's owned (max 4)",
    "Graded BGS 9": "Amount of BGS9's owned (max 4)",
    "Graded BGS 9.5": "Amount of BGS9.5's owned (max 4)",
    "Graded BGS 10": "Amount of BGS10's owned (max 4)",
    "Graded PSA 9": "Amount of PSA9's owned (max 4)",
    "Graded PSA 10": "Amount of PSA10's owned (max 4)",
    "Other rarities": "Amount of other rarities owned (max 50)",
}

RANGES = {
    "Completed": [0, 1],
    "Core cards": [0, 500],
    "Original art": [0, 10],
    "Testprint": [-1, 5],
    "Gamma playtest": [-1, 1],
    "Delta playtest": [-1, 1],
    "Epsilon playtest": [-1, 1],
    "Other playtests": [0, 10],
    "Original artist alters": [0, 10],
    "Artist Proof": [0, 30],
    "Summer": [-1, 4],
    "Revised alpha-cut": [-1, 1],
    "Fourth alpha-cut": [-1, 1],
    "Square corners": [-1, 1],
    "Miscut": [0, 4],
    "Miscut NFC": [0, 4],
    "Offcenters": [0, 4],
    "Crimped": [0, 4],
    "Albino": [0, 4],
    "Signed": [0, 10],
    "Graded BGS 8.5": [0, 4],
    "Graded BGS 9": [0, 4],
    "Graded BGS 9.5": [0, 4],
    "Graded BGS 10": [0, 4],
    "Graded PSA 9": [0, 4],
    "Graded PSA 10": [0, 4],
    "Other rarities": [0, 50],
}
