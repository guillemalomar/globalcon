import os

DIPLOMAS_PATH = "DATA/DIPLOMAS"
DIPLOMAS_PATH_NOCOMPETE = "DATA/DIPLOMAS_NOCOMPETE"

DATA_FOLDERS = {
    "global": [
        "DATA",
    ],
    "calculator": [
        "DATA/RESULTS",
        "DATA/RESULTS_NOCOMPETE",
    ],
    "diplomas": [
        DIPLOMAS_PATH,
        DIPLOMAS_PATH_NOCOMPETE,
    ],
    "globalset_list": [
        "DATA/GLOBALSET_LISTS",
    ]
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
