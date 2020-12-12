from PIL import ImageTk, Image
from tkinter import Tk
import tkinter as tk

from config import APP_NAME, WEIGHTS, LOGO_FILE, FONT, RESULTS_FOLDER


total = 0
last_values = {}
last_info = {}
img = None
globalset_metadata = ['GlobalSet Owner', 'GlobalSet Card']


def fetch(entries, owner, card):
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        global last_values
        last_values[field] = text
        info = entry[2].get()
        global last_info
        last_info[field] = info
    global globalset_metadata
    globalset_metadata = [owner.get(), card.get()]


class Simulation:

    def __init__(self, init_root):
        super().__init__()

        self.root = init_root
        self.root.geometry("890x810+%d+%d" % (0, 0))
        self.root.config(background='white')
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

        self.root.bind('<Return>', (lambda event, e=self.fields: self.calculate_result()))
        self.form_buttons()

    def form_fields(self):
        fields = []

        labels = {}
        rows = {}
        entries = {}
        info = {}

        set_metadata = tk.Frame(self.root, bg='white')
        global globalset_metadata
        v = tk.StringVar(self.root, value=globalset_metadata[0])
        entry_owner = tk.Entry(set_metadata, textvariable=v, fg='white', bg='#255')
        self.owner = entry_owner
        v = tk.StringVar(self.root, value=globalset_metadata[1])
        entry_card = tk.Entry(set_metadata, textvariable=v, fg='white', bg='#255')
        self.card = entry_card
        entry_owner.pack()
        entry_card.pack()
        set_metadata.pack()

        for index, (item, value) in enumerate(WEIGHTS.items()):
            rows[index] = tk.Frame(self.root, bg='white')
            labels[index] = tk.Label(rows[index], width=15, text=item, anchor='w', fg='black', bg='white')

            global last_values
            v = tk.StringVar(self.root, value=last_values.get(item, 0))
            entries[index] = tk.Entry(rows[index], textvariable=v, fg='black', bg='white', width=3)

            global last_info
            v = tk.StringVar(self.root, value=last_info.get(item, ""))
            info[index] = tk.Entry(rows[index], textvariable=v, fg='black', bg='white', width=50)

            rows[index].pack(side=tk.TOP, padx=5, pady=0)
            labels[index].pack(side=tk.LEFT)
            entries[index].pack(side=tk.LEFT, expand=tk.NO)
            info[index].pack(side=tk.LEFT, expand=tk.NO)

            fields.append((item, entries[index], info[index]))
        self.fields = fields

    def form_buttons(self):
        b0 = tk.Button(
            self.root,
            text='Save',
            command=(lambda e=self.fields: self.store_data()),
            fg='black'
        )
        b0.pack(side=tk.LEFT, padx=3, pady=3)
        b1 = tk.Button(
            self.root,
            text='Show',
            command=(lambda e=self.fields: self.calculate_result()),
            fg='black'
        )
        b1.pack(side=tk.LEFT, padx=3, pady=3)
        b2 = tk.Button(
            self.root,
            text='Clean',
            command=(lambda e=self.fields: self.clean()),
            fg='black'
        )
        b2.pack(side=tk.LEFT, padx=3, pady=3)
        b3 = tk.Button(
            self.root,
            text='Quit',
            command=self.root.quit,
            fg='black'
        )
        b3.pack(side=tk.LEFT, padx=3, pady=3)

    def calculate_result(self):
        fetch(self.fields, self.owner, self.card)
        global total
        total = 0
        error = False
        try:
            for item, entry, _ in self.fields:
                self.evaluate(entry.get(), item)
        except ValueError:
            total = "Error: Wrong input."
            error = True
        self.root.destroy()

        new_root, new_app = create_new_instance()
        res = tk.Label(new_app.root)
        if error:
            res.configure(text=f"{total}", font='Helvetica 14 bold', fg="red", bg="white")
        else:
            res.configure(text=f"Result: {total}", font='Helvetica 14 bold', fg="black", bg="white")
        res.pack(side=tk.RIGHT)
        return error, new_root, new_app

    @staticmethod
    def evaluate(entry, item):
        entry_value = int(entry)
        global total
        total += WEIGHTS[item] * entry_value

    def store_data(self):
        result_error, new_root, new_app = self.calculate_result()
        if result_error:
            return
        global globalset_metadata
        gs_own = globalset_metadata[0]
        if gs_own == "GlobalSet Owner":
            res = tk.Label(new_root)
            res.configure(text=f"Error: Specify Owner", font=FONT, fg="black", bg="white")
            res.pack(side=tk.RIGHT)
            return
        gs_card = globalset_metadata[1]
        if gs_card == "GlobalSet Card":
            res = tk.Label(new_root)
            res.configure(text=f"Error: Specify Card", font=FONT, fg="black", bg="white")
            res.pack(side=tk.RIGHT)
            return
        global total
        with open(f'{RESULTS_FOLDER}/{total}_{gs_own.replace(" ", "")}_{gs_card.replace(" ", "")}.txt', 'w') as f:
            global last_values
            global last_info
            for key, value in last_values.items():
                f.write(f'{key}: {value} / {last_info[key]}\n')
            if result_error:
                f.write("\nError: Wrong input.")
            else:
                f.write(f'\nResult: {total}')

    def clean(self):
        global globalset_metadata
        globalset_metadata[0] = "GlobalSet Owner"
        globalset_metadata[1] = "GlobalSet Card"
        global last_info
        last_info = {}
        global last_values
        last_values = {}

        self.root.destroy()

        _, _ = create_new_instance()


def create_new_instance():
    new_root = Tk()

    image = Image.open(LOGO_FILE)
    image = image.resize((250, 250), Image.ANTIALIAS)
    global img
    img = ImageTk.PhotoImage(image)
    panel = tk.Label(new_root, image=img, background='white')
    panel.pack(side="left")

    new_app = Simulation(new_root)
    return new_root, new_app


if __name__ == "__main__":
    root, app = create_new_instance()
    root.mainloop()
