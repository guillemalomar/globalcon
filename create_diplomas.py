import fpdf
from fpdf import FPDF
import os
import re

CENTER_X = 146
CENTER_Y = 102.5

DIPLOMAS_PATH = "DATA/DIPLOMAS"


class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page(orientation='L')
        self.set_draw_color(0, 80, 180)
        self.set_text_color(50, 50, 50)
        # self.add_background()
        self.border()
        self.titles()

    def border(self):
        self.set_line_width(1.0)
        self.set_draw_color(0)
        self.rect(5.0, 5.0, 287.0, 200.0)
        self.rect(8.0, 8.0, 281.0, 194.0)

    def titles(self):
        self.set_xy(CENTER_X, CENTER_Y)
        self.add_font('moria citadel', '', 'MoriaCitadel.TTF', uni=True)
        self.set_font('moria citadel', '', size=46)
        self.cell(w=-8.0, h=-150.0, align='C', txt="GlobalCon 2020", border=0)

    def organizers(self):
        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font('moria citadel', '', size=20)
        self.set_text_color(50, 50, 50)
        self.cell(w=155.0, h=87.0, align='C', txt="The Organizers", border=0)

    def add_name(self, competitor_to_add):
        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font('moria citadel', '', size=26)
        self.set_text_color(50, 50, 50)
        self.cell(w=-8.0, h=-108.0, align='C', txt="Competitor name", border=0)

        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font(family='Arial', style='B', size=32)
        self.set_text_color(50, 50, 50)
        self.cell(w=-8.0, h=-86.0, align='C', txt=competitor_to_add, border=0)

    def add_card(self, card_name):
        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font('moria citadel', '', size=26)
        self.set_text_color(50, 50, 50)
        self.cell(w=-8.0, h=-51.0, align='C', txt="Competitor card", border=0)

        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font(family='Arial', style='B', size=32)
        self.set_text_color(50, 50, 50)
        self.cell(w=-8.0, h=-29.0, align='C', txt=card_name, border=0)

    def add_position(self, position, total):
        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font('moria citadel', '', size=26)
        self.set_text_color(50, 50, 50)
        self.cell(w=-8.0, h=6.0, align='C', txt="Position", border=0)

        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font(family='Arial', style='B', size=32)
        self.set_text_color(50, 50, 50)
        self.cell(w=-8.0, h=28.0, align='C', txt=f'{position} / {total}', border=0)

    def add_points(self, points):
        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font('moria citadel', '', size=26)
        self.set_text_color(50, 50, 50)
        self.cell(w=-8.0, h=63.0, align='C', txt="Points", border=0)

        self.set_xy(CENTER_X, CENTER_Y)
        self.set_font(family='Arial', style='B', size=32)
        self.set_text_color(50, 50, 50)
        self.cell(w=-8.0, h=85.0, align='C', txt=f'{points}', border=0)

    def add_background(self):
        self.set_xy(0.0, 0.0)
        self.image("documentation/Background.png", link='', type='', w=297, h=210, x=0, y=0)

    def add_logo(self):
        self.set_xy(30.0, 115.0)
        self.image("documentation/GlobalCon_border.png", link='', type='', w=70, h=70)


competitors = [f for f in os.listdir("DATA/RESULTS")
               if os.path.isfile(os.path.join("DATA/RESULTS", f))]
competitors.sort(reverse=True)

if not os.path.exists(f"{DIPLOMAS_PATH}"):
    os.makedirs(f"{DIPLOMAS_PATH}")

total_competitors = len(competitors)
previous_points = 10000
previous_position = 1
for ind, competitor in enumerate(competitors, 1):
    competitor_data = competitor[:-4].split('_')
    competitor_points = competitor_data[0]
    competitor_name = ' '.join(re.findall('[A-Z][^A-Z]*', competitor_data[1]))
    competitor_card = ' '.join(re.findall('[A-Z][^A-Z]*', competitor_data[2]))

    pdf = PDF()
    pdf.add_name(competitor_name)
    pdf.add_card(competitor_card)

    if competitor_points == previous_points:
        final_position = previous_position
    else:
        final_position = ind
    pdf.add_position(final_position, total_competitors)
    pdf.add_points(competitor_points)
    pdf.organizers()
    pdf.add_logo()

    pdf.output(
        f'{DIPLOMAS_PATH}/{final_position}_{competitor_data[1]}_{competitor_data[2]}.pdf',
        'F')

    previous_points = competitor_points
    previous_position = final_position
