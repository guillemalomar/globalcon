from globalcon_tools.calculator.data import current_instance


def fetch(entries, owner, card):
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        current_instance.last_values[field] = text
        info = entry[2].get()
        current_instance.last_info[field] = info
    current_instance.globalset_metadata = [owner.get(), card.get()]
