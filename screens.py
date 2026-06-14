import tkinter as tk
import itertools

from project_data import build_project_ui
from essay_page import build_essay_page
from history import build_history_ui
from quiz import build_quiz_ui

CRT_DARK = "#0A0F0D"
NEON_PINK = "#FF4DA6"
NEON_BLUE = "#4DDCFF"
NEON_YELLOW = "#FFE066"
NEON_GREEN = "#00FF88"


def build_ui(root):
    root.configure(bg=CRT_DARK)

    # HEADER
    spark_label = tk.Label(
        root,
        text="/\\_/\\\n(0 - 0)\n/ = \\",
        font=("Courier New", 30, "bold"),
        bg=CRT_DARK,
        fg=NEON_PINK
    )
    spark_label.pack(pady=0)

    tk.Label(
        root,
        text="ELECTRONICS WITH SPARK",
        font=("Courier New", 22, "bold"),
        bg=CRT_DARK,
        fg=NEON_GREEN
    ).pack(pady=5)

    tk.Label(
        root,
        text="THE TIME‑TRAVELING LEARNING CAT",
        font=("Courier New", 12),
        bg=CRT_DARK,
        fg=NEON_BLUE
    ).pack(pady=0)


    spark_speech = tk.Label(
        root,
        text="",
        font=("Courier New", 12),
        bg=CRT_DARK,
        fg=NEON_GREEN,
        wraplength=700,
        height=2
    )
    spark_speech.pack(pady=10)

    # Function Spark uses to “talk”
    def spark_say(text):
        spark_speech.config(text=text)

    # Spark animation
    spark_frames = itertools.cycle([
        "/\\_/\\\n(0 - 0)\n/ = \\",
        "/\\_/\\\n(0 - 0)\n/ = \\ "
    ])

    def animate_spark():
        spark_label.config(text=next(spark_frames))
        root.after(300, animate_spark)

    animate_spark()

    # MAIN FRAMES
    home_frame = tk.Frame(root, bg=CRT_DARK)

    def show_frame(frame):
        frame.tkraise()

    # Build all pages
    project_frame, steps_frame, completed_frame = build_project_ui(
        root, show_frame, home_frame, spark_say
    )
    essay_frame, update_essay = build_essay_page(root, show_frame, home_frame)
    history_frame = build_history_ui(root, show_frame, home_frame, update_essay, essay_frame)
    quiz_frame, final_quiz_frame = build_quiz_ui(root, show_frame, home_frame, spark_label)

    # All frames placed BELOW the Spark header + speech bar
    for frame in (
        home_frame, project_frame, steps_frame, completed_frame,
        history_frame, essay_frame, quiz_frame, final_quiz_frame
    ):
        frame.place(x=0, y=200, relwidth=1, relheight=1)

    # HOME SCREEN
    def neon_button(parent, text, color, command, w=350, h=80):
        box = tk.Frame(
            parent,
            bg=CRT_DARK,
            highlightthickness=3,
            highlightbackground=color,
            width=w,
            height=h
        )
        box.pack_propagate(False)

        tk.Button(
            box,
            text=text,
            font=("Courier New", 16, "bold"),
            fg=color,
            bg=CRT_DARK,
            bd=0,
            command=command
        ).pack(fill="both", expand=True)

        return box

    tk.Label(
        home_frame,
        text="MAIN MENU",
        font=("Courier New", 26, "bold"),
        fg=NEON_GREEN,
        bg=CRT_DARK
    ).pack(pady=20)

    neon_button(home_frame, "PROJECT", NEON_BLUE, lambda: show_frame(project_frame)).pack(pady=15)
    neon_button(home_frame, "HISTORY MODE", NEON_PINK, lambda: show_frame(history_frame)).pack(pady=15)
    neon_button(home_frame, "QUIZ MODE", NEON_YELLOW, lambda: show_frame(quiz_frame)).pack(pady=15)

    tk.Label(
        home_frame,
        text="© 2026 Spark Labs – Retro Edition",
        font=("Courier New", 12),
        fg=NEON_GREEN,
        bg=CRT_DARK
    ).pack(pady=20)

    show_frame(home_frame)
