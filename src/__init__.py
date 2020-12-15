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
    "Core cards": "Amount of core cards owned",
    "Original art": "1 if owned, 0 otherwise",
    "Testprint": "1 of owned, 0 if not owned & doesn't exist, -1 if not owned & exists",
    "Gamma playtest": "1 of owned, 0 if not owned & doesn't exist, -1 if not owned & exists",
    "Delta playtest": "1 of owned, 0 if not owned & doesn't exist, -1 if not owned & exists",
    "Epsilon playtest": "1 of owned, 0 if not owned & doesn't exist, -1 if not owned & exists",
    "Other playtests": "Amount of other playtests owned",
    "Original artist alters": "Amount of original artist alters owned",
    "Artist Proof": "Amount of artist proofs owned",
    "Summer": "1 of owned, 0 if not owned & doesn't exist, -1 if not owned & exists",
    "Revised alpha-cut": "1 of owned, 0 if not owned & doesn't exist, -1 if not owned & exists",
    "Fourth alpha-cut": "1 of owned, 0 if not owned & doesn't exist, -1 if not owned & exists",
    "Miscut": "Amount of miscuts owned",
    "Miscut NFC": "Amount of NFC miscuts owned",
    "Offcenters": "Amount of offcenters owned",
    "Crimped": "Amount of crimps owned",
    "Albino": "Amount of albinos owned",
    "Signed": "Amount of signed cards owned",
    "Graded BGS 8.5": "Amount of BGS8.5's owned",
    "Graded BGS 9": "Amount of BGS9's owned",
    "Graded BGS 9.5": "Amount of BGS9.5's owned",
    "Graded BGS 10": "Amount of BGS10's owned",
    "Graded PSA 9": "Amount of PSA9's owned",
    "Graded PSA 10": "Amount of PSA10's owned",
    "Other rarities": "Amount of other rarities owned",
}
