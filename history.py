import tkinter as tk
import webbrowser

CRT_DARK = "#0A0F0D"
NEON_PINK = "#FF4DA6"
NEON_BLUE = "#4DDCFF"
NEON_YELLOW = "#FFE066"
CRT_GREEN = "#00FF88"

# ---------------------------------------------------
# 
# ---------------------------------------------------
history_eras = {
    "1920": {
        "title": "1920 – The Radio Age",
        "text": "Radios used vacuum tubes instead of chips."
    },
    "1960": {
        "title": "1960 – Space Race Electronics",
        "text": "Electronics helped rockets reach space."
    },
    "1980": {
        "title": "1980 – Arcade Machines",
        "text": "Games lived in big arcade cabinets."
    },
    "2020": {
        "title": "2020 – Microcontrollers",
        "text": "Tiny boards control everything."
    }
}

# ---------------------------------------------------
# HISTORY UI
# ---------------------------------------------------
def build_history_ui(root, show_frame, home_frame, update_essay, essay_frame):
    history_frame = tk.Frame(root, bg=CRT_DARK)

    title = tk.Label(
        history_frame,
        text="HISTORY MODE",
        font=("Courier New", 20, "bold"),
        fg=NEON_YELLOW,
        bg=CRT_DARK
    )
    title.pack(pady=20)

    subtitle = tk.Label(
        history_frame,
        text="Choose an era to learn about.",
        font=("Courier New", 14),
        fg=NEON_BLUE,
        bg=CRT_DARK
    )
    subtitle.pack(pady=10)

    def neon_button(text, command):
        btn = tk.Button(
            history_frame,
            text=text,
            font=("Courier New", 16, "bold"),
            fg=CRT_GREEN,
            bg=CRT_DARK,
            bd=3,
            relief="ridge",
            command=command,
            width=40
        )
        btn.pack(pady=10)

    # Create buttons for each era
    for era_key, era_data in history_eras.items():
        neon_button(
            era_data["title"],
            lambda k=era_key: (update_essay(k), show_frame(essay_frame))
        )


    row = tk.Frame(history_frame, bg=CRT_DARK)
    row.pack(pady=20)

    tk.Button(
        row,
        text="OPEN WIKIPEDIA PAGE FOR MORE",
        font=("Courier New", 16, "bold"),
        fg=NEON_PINK,
        bg=CRT_DARK,
        bd=3,
        relief="ridge",
        command=lambda: webbrowser.open("https://en.wikipedia.org/wiki/History_of_electronics")
    ).grid(row=0, column=0, padx=20)

    tk.Button(
        row,
        text="BACK TO HOME",
        font=("Courier New", 16, "bold"),
        fg=NEON_PINK,
        bg=CRT_DARK,
        bd=3,
        relief="ridge",
        command=lambda: show_frame(home_frame)
    ).grid(row=0, column=1, padx=20)

    return history_frame
