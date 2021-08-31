import os
import tkinter as tk
from PIL import ImageTk, Image

from src import (
    APP_NAME,
    WEIGHTS,
    RESULTS_FOLDER,
    RESULTS_NOCOMPETE_FOLDER,
    FONT,
    LOGO_FILE,
    DEFAULT_MESSAGES,
    RANGES,
)
from src.data import current_instance
from src.utilities import fetch


class Calculator:
    def __init__(self):
        super().__init__()

        new_root = tk.Tk()

        image = Image.open(LOGO_FILE)
        image = image.resize((250, 250), Image.ANTIALIAS)
        current_instance.img = ImageTk.PhotoImage(image)
        panel = tk.Label(new_root, image=current_instance.img, background="white")
        panel.pack(side="left")

        self.root = new_root
        self.root.geometry("979x810+%d+%d" % (0, 0))
        self.root.config(background="white")
        self.total = 0
        self.fields = None
        self.owner = None
        self.card = None

        self.init_ui()

    def init_ui(self):
        """
        This method initializes the GUI.
        """
        self.root.title(APP_NAME)

        self.form_fields()

        self.root.bind(
            "<Return>", (lambda event, e=self.fields: self.calculate_result())
        )
        self.form_buttons()

    def form_fields(self):
        fields = []

        labels = {}
        rows = {}
        entries = {}
        info = {}

        set_metadata = tk.Frame(self.root, bg="white")
        v = tk.StringVar(self.root, value=current_instance.globalset_metadata[0])
        entry_owner = tk.Entry(set_metadata, textvariable=v, fg="grey", bg="#255")
        self.owner = entry_owner
        self.owner.bind("<FocusIn>", self.handle_focus_in_owner)

        v = tk.StringVar(self.root, value=current_instance.globalset_metadata[1])
        entry_card = tk.Entry(set_metadata, textvariable=v, fg="grey", bg="#255")
        self.card = entry_card
        self.card.bind("<FocusIn>", self.handle_focus_in_card)

        entry_owner.pack()
        entry_card.pack()
        set_metadata.pack()

        for index, (item, value) in enumerate(WEIGHTS.items()):
            rows[index] = tk.Frame(self.root, bg="white")
            labels[index] = tk.Label(
                rows[index], width=15, text=item, anchor="w", fg="black", bg="white"
            )

            v = tk.StringVar(self.root, value=current_instance.last_values.get(item, 0))
            entries[index] = tk.Entry(
                rows[index], textvariable=v, fg="black", bg="white", width=3
            )

            v = tk.StringVar(
                self.root,
                value=current_instance.last_info.get(item, DEFAULT_MESSAGES[item]),
            )
            info[index] = tk.Entry(
                rows[index], textvariable=v, fg="black", bg="white", width=58
            )

            rows[index].pack(side=tk.TOP, padx=5, pady=0)
            labels[index].pack(side=tk.LEFT)
            entries[index].pack(side=tk.LEFT, expand=tk.NO)
            info[index].pack(side=tk.LEFT, expand=tk.NO)

            fields.append((item, entries[index], info[index]))
        self.fields = fields

    def form_buttons(self):
        b0 = tk.Button(
            self.root,
            text="Save&Compete",
            command=(lambda e=self.fields: self.store_compete_data()),
            fg="black",
        )
        b0.pack(side=tk.LEFT, padx=3, pady=3)
        b1 = tk.Button(
            self.root,
            text="Save",
            command=(lambda e=self.fields: self.store_data()),
            fg="black",
        )
        b1.pack(side=tk.LEFT, padx=3, pady=3)
        b2 = tk.Button(
            self.root,
            text="Show",
            command=(lambda e=self.fields: self.calculate_result()),
            fg="black",
        )
        b2.pack(side=tk.LEFT, padx=3, pady=3)
        b3 = tk.Button(
            self.root,
            text="Clean",
            command=(lambda e=self.fields: self.clean()),
            fg="black",
        )
        b3.pack(side=tk.LEFT, padx=3, pady=3)
        b4 = tk.Button(self.root, text="Quit", command=self.root.quit, fg="black")
        b4.pack(side=tk.LEFT, padx=3, pady=3)

    def calculate_result(self):
        fetch(self.fields, self.owner, self.card)
        current_instance.total = 0
        error = False
        try:
            for item, entry, _ in self.fields:
                current_instance.total += self.evaluate(entry.get(), item)
        except ValueError:
            current_instance.total = "Error: Wrong input."
            error = True
        self.root.destroy()

        new_root = Calculator()
        res = tk.Label(new_root.root)
        if error:
            res.configure(
                text=f"{current_instance.total}",
                font="Helvetica 14 bold",
                fg="red",
                bg="white",
            )
        else:
            res.configure(
                text=f"Result: {current_instance.total}",
                font="Helvetica 14 bold",
                fg="black",
                bg="white",
            )
        res.pack(side=tk.RIGHT)
        return error, new_root

    @staticmethod
    def evaluate(entry, item):
        entry_value = min(max(int(entry), RANGES[item][0]), RANGES[item][1])
        return WEIGHTS[item] * entry_value

    def store_compete_data(self):
        result_error, new_root = self.calculate_result()
        if result_error:
            return
        gs_own = str.title(current_instance.globalset_metadata[0])
        if gs_own == "GlobalSet Owner":
            res = tk.Label(new_root.root)
            res.configure(
                text=f"Error: Specify Owner", font=FONT, fg="black", bg="white"
            )
            res.pack(side=tk.RIGHT)
            return
        gs_card = str.title(current_instance.globalset_metadata[1])
        if gs_card == "GlobalSet Card":
            res = tk.Label(new_root.root)
            res.configure(
                text=f"Error: Specify Card", font=FONT, fg="black", bg="white"
            )
            res.pack(side=tk.RIGHT)
            return
        if not os.path.exists(RESULTS_FOLDER):
            os.makedirs(RESULTS_FOLDER)
        with open(
            f"{RESULTS_FOLDER}/"
            f"{current_instance.total}_"
            f'{gs_own.replace(" ", "")}_'
            f'{gs_card.replace(" ", "")}.txt',
            "w",
        ) as f:
            for key, value in current_instance.last_values.items():
                additional_info = (
                    current_instance.last_info[key]
                    if current_instance.last_info[key] != DEFAULT_MESSAGES[key]
                    else ""
                )
                f.write(
                    f"{key}: {min(max(int(value), RANGES[key][0]), RANGES[key][1])}"
                    f" / {additional_info}\n"
                )
            if result_error:
                f.write("\nError: Wrong input.")
            else:
                f.write(f"\nResult: {current_instance.total}")

    def store_data(self):
        fetch(self.fields, self.owner, self.card)
        self.root.destroy()
        new_root = Calculator()
        res = tk.Label(new_root.root)
        res.configure(
            text=f"Saved",
            font="Helvetica 14 bold",
            fg="black",
            bg="white",
        )
        res.pack(side=tk.RIGHT)
        gs_own = str.title(current_instance.globalset_metadata[0])
        if gs_own == "GlobalSet Owner":
            res = tk.Label(new_root.root)
            res.configure(
                text=f"Error: Specify Owner", font=FONT, fg="black", bg="white"
            )
            res.pack(side=tk.RIGHT)
            return
        gs_card = str.title(current_instance.globalset_metadata[1])
        if gs_card == "GlobalSet Card":
            res = tk.Label(new_root.root)
            res.configure(
                text=f"Error: Specify Card", font=FONT, fg="black", bg="white"
            )
            res.pack(side=tk.RIGHT)
            return
        if not os.path.exists(RESULTS_NOCOMPETE_FOLDER):
            os.makedirs(RESULTS_NOCOMPETE_FOLDER)
        with open(
            f"{RESULTS_NOCOMPETE_FOLDER}/"
            f'{gs_own.replace(" ", "")}_'
            f'{gs_card.replace(" ", "")}.txt',
            "w",
        ) as f:
            for key, value in current_instance.last_values.items():
                additional_info = (
                    current_instance.last_info[key]
                    if current_instance.last_info[key] != DEFAULT_MESSAGES[key]
                    else ""
                )
                f.write(
                    f"{key}: {min(max(int(value), RANGES[key][0]), RANGES[key][1])}"
                    f" / {additional_info}\n"
                )
            f.write(f"\nSAVED")

    def clean(self):
        current_instance.globalset_metadata[0] = "GlobalSet Owner"
        current_instance.globalset_metadata[1] = "GlobalSet Card"
        current_instance.last_info = {}
        current_instance.last_values = {}

        self.root.destroy()

        _ = Calculator()

    def handle_focus_in_owner(self, _):
        self.owner.delete(0, tk.END)
        self.owner.config(fg="yellow")

    def handle_focus_in_card(self, _):
        self.card.delete(0, tk.END)
        self.card.config(fg="yellow")
