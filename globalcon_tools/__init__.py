import os

GLOBAL_PATH = "DATA"
CALCULATOR_PATH = f"{GLOBAL_PATH}/RESULTS"
CALCULATOR_PATH_NOCOMPETE = f"{GLOBAL_PATH}/RESULTS_NOCOMPETE"
DIPLOMAS_PATH = f"{GLOBAL_PATH}/DIPLOMAS"
DIPLOMAS_PATH_NOCOMPETE = f"{GLOBAL_PATH}/DIPLOMAS_NOCOMPETE"
GLOBALSETLIST_PATH = f"{GLOBAL_PATH}/GLOBALSET_LISTS"

DATA_FOLDERS = {
    "global": [
        GLOBAL_PATH,
    ],
    "calculator": [
        CALCULATOR_PATH,
        CALCULATOR_PATH_NOCOMPETE,
    ],
    "diplomas": [
        DIPLOMAS_PATH,
        DIPLOMAS_PATH_NOCOMPETE,
    ],
    "globalset_list": [
        GLOBALSETLIST_PATH,
    ],
}


def create_global_folder():
    for folder_path in DATA_FOLDERS["global"]:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)


def create_data_folders(folder_paths):
    create_global_folder()
    for folder_path in DATA_FOLDERS[folder_paths]:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
