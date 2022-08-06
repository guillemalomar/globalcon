from globalcon_tools.calculator.calculator import Calculator
from globalcon_tools.diplomas.create_diplomas import create_all_diplomas
from globalcon_tools.globalset_list.create_globalset_list import generate_list

AVAILABLE_MODES = [
    "Calculate Score",
    "Generate Diplomas",
    "Generate Globalset List",
]

if __name__ == "__main__":
    desired_mode = 0
    while desired_mode not in range(1, 4):
        print("Please enter the desired tool to use:")
        for ind, value in enumerate(AVAILABLE_MODES):
            print(f"{ind + 1} - {value}")
        try:
            desired_mode = int(input())
        except Exception:
            pass
        if desired_mode not in range(1, 4):
            print("Please enter an available mode")

    if desired_mode == 1:
        root = Calculator()
        root.root.mainloop()
    if desired_mode == 2:
        create_all_diplomas()
    if desired_mode == 3:
        generate_list()
