from fpdf import FPDF
import os
import re

CENTER_X = 146
CENTER_Y = 102.5


class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page(orientation='L')
        self.set_draw_color(0, 80, 180)
        self.set_text_color(50, 50, 50)
        self.add_background()
        self.border()
        self.titles()

    def border(self):
        self.set_line_width(1.0)
        self.set_draw_color(0)
        self.rect(5.0, 5.0, 287.0, 200.0)
        self.rect(8.0, 8.0, 281.0, 194.0)

    def titles(self):
        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font(family='Arial', style='B', size=42)
        self.cell(w=-8.0, h=-150.0, align='C', txt="GlobalCon 2020", border=0)

    def organizers(self):
        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font(family='Arial', style='B', size=28)
        self.set_text_color(50, 50, 50)
        self.cell(w=100.0, h=70.0, align='C', txt="The Organizers", border=0)

    def add_name(self, participant_name):
        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font(family='Arial', style='B', size=28)
        self.set_text_color(50, 50, 50)
        self.cell(w=-8.0, h=-110.0, align='C', txt="Participant name", border=0)

        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font(family='Arial', style='B', size=32)
        self.set_text_color(50, 50, 50)
        self.cell(w=-8.0, h=-90.0, align='C', txt=participant_name, border=0)

    def add_card(self, card_name):
        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font(family='Arial', style='B', size=28)
        self.set_text_color(50, 50, 50)
        self.cell(w=-8.0, h=-60.0, align='C', txt="Participant name", border=0)

        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font(family='Arial', style='B', size=32)
        self.set_text_color(50, 50, 50)
        self.cell(w=-8.0, h=-40.0, align='C', txt=card_name, border=0)

    def add_position(self, position, total):
        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font(family='Arial', style='B', size=28)
        self.set_text_color(50, 50, 50)
        self.cell(w=-8.0, h=-10.0, align='C', txt="Position", border=0)

        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font(family='Arial', style='B', size=32)
        self.set_text_color(50, 50, 50)
        self.cell(w=-8.0, h=10.0, align='C', txt=f'{position} / {total}', border=0)

    def add_background(self):
        self.set_xy(0.0, 0.0)
        self.image("Background.png", link='', type='', w=297, h=210, x=0, y=0)

    def add_logo(self):
        self.set_xy(30.0, 115.0)
        self.image("GlobalCon_logo.png", link='', type='', w=70, h=70)


participants = [f for f in os.listdir("RESULTS")
                if os.path.isfile(os.path.join("RESULTS", f))]

if not os.path.exists("DIPLOMAS"):
    os.makedirs("DIPLOMAS")

total_participants = len(participants)
for ind, participant in enumerate(participants, 1):
    participant_data = participant[:-4].split('_')
    participant_name = ' '.join(re.findall('[A-Z][^A-Z]*', participant_data[1]))
    participant_card = ' '.join(re.findall('[A-Z][^A-Z]*', participant_data[2]))

    pdf = PDF()
    pdf.add_name(participant_name)
    pdf.add_card(participant_card)
    pdf.add_position(ind, total_participants)
    pdf.organizers()
    pdf.add_logo()

    pdf.output(f'DIPLOMAS/{ind}_{participant_data[1]}_{participant_data[2]}.pdf', 'F')
