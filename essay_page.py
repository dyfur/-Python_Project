import tkinter as tk
import webbrowser

CRT_DARK = "#0A0F0D"
NEON_PINK = "#FF4DA6"
NEON_BLUE = "#4DDCFF"
NEON_YELLOW = "#FFE066"

ESSAYS = {
    "1920": {
        "title": "1920 – The Radio Age",
        "text": (
            "Radios used vacuum tubes instead of chips.\n"
            "Spark: \"People listened to music with giant boxes!\""
        ),
        "names": (
            "- Guglielmo Marconi\n"
            "- Lee de Forest\n"
            "- Reginald Fessenden"
        ),
        "wiki": "https://en.wikipedia.org/wiki/History_of_radio"
    },
    "1960": {
        "title": "1960 – Space Race Electronics",
        "text": (
            "Electronics helped rockets reach space.\n"
            "Spark: \"Circuits went to the stars!\""
        ),
        "names": (
            "- Wernher von Braun\n"
            "- Margaret Hamilton\n"
            "- Jack Kilby"
        ),
        "wiki": "https://en.wikipedia.org/wiki/Space_Race"
    },
    "1980": {
        "title": "1980 – Arcade Machines",
        "text": (
            "Games lived in big arcade cabinets.\n"
            "Spark: \"Beep boop high scores!\""
        ),
        "names": (
            "- Toru Iwatani\n"
            "- Nolan Bushnell\n"
            "- Shigeru Miyamoto"
        ),
        "wiki": "https://en.wikipedia.org/wiki/Golden_age_of_arcade_video_games"
    },
    "2020": {
        "title": "2020 – Microcontrollers",
        "text": (
            "Tiny boards control everything.\n"
            "Spark: \"Even your toaster can be smart!\""
        ),
        "names": (
            "- Massimo Banzi\n"
            "- Eben Upton\n"
            "- Grace Hopper"
        ),
        "wiki": "https://en.wikipedia.org/wiki/Microcontroller"
    }
}

def build_essay_page(root, show_frame, history_frame):
    essay_frame = tk.Frame(root, bg=CRT_DARK)


    # ERA title (dynamic)
    era_title_label = tk.Label(
        essay_frame,
        text="",
        font=("Courier New", 18, "bold"),
        fg=NEON_YELLOW,
        bg=CRT_DARK
    )
    era_title_label.pack(pady=10)

    row = tk.Frame(essay_frame, bg=CRT_DARK)
    row.pack(pady=20)

    left_box = tk.Frame(
        row,
        bg=CRT_DARK,
        highlightthickness=3,
        highlightbackground="white",
        width=350,
        height=250
    )
    left_box.grid(row=0, column=0, padx=20)
    left_box.pack_propagate(False)

    left_label = tk.Label(
        left_box,
        text="",
        font=("Courier New", 14),
        fg=NEON_BLUE,
        bg=CRT_DARK,
        wraplength=300,
        justify="left"
    )
    left_label.pack(fill="both", expand=True, padx=10, pady=10)

    right_box = tk.Frame(
        row,
        bg=CRT_DARK,
        highlightthickness=3,
        highlightbackground="white",
        width=250,
        height=250
    )
    right_box.grid(row=0, column=1, padx=20)
    right_box.pack_propagate(False)

    right_title = tk.Label(
        right_box,
        text="Names:",
        font=("Courier New", 16, "bold"),
        fg=NEON_YELLOW,
        bg=CRT_DARK
    )
    right_title.pack(pady=5)

    right_label = tk.Label(
        right_box,
        text="",
        font=("Courier New", 14),
        fg=NEON_BLUE,
        bg=CRT_DARK,
        justify="left"
    )
    right_label.pack(pady=5)

    
    button_row = tk.Frame(essay_frame, bg=CRT_DARK)
    button_row.pack(pady=20)

    wiki_btn = tk.Button(
        button_row,
        text="OPEN WIKIPEDIA PAGE",
        font=("Courier New", 16, "bold"),
        fg=NEON_PINK,
        bg=CRT_DARK,
        bd=3,
        relief="ridge"
    )
    wiki_btn.grid(row=0, column=0, padx=21)

    back_btn = tk.Button(
        button_row,
        text="BACK TO HOME",
        font=("Courier New", 16, "bold"),
        fg=NEON_PINK,
        bg=CRT_DARK,
        bd=3,
        relief="ridge",
        command=lambda: show_frame(history_frame)
    )
    back_btn.grid(row=0, column=1, padx=21)

    
    def update_essay(era_key):
        era = ESSAYS[era_key]
        era_title_label.config(text=era["title"])
        left_label.config(text=era["text"])
        right_label.config(text=era["names"])
        wiki_btn.config(command=lambda: webbrowser.open(era["wiki"]))

    return essay_frame, update_essay

