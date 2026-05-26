import tkinter as tk
import itertools
import webbrowser
import random

from project_data import projects, hints
from spark_chatbot import spark_chat


# ---------------------------------------------------
# COLORS
# ---------------------------------------------------
CRT_GREEN = "#00FF88"
CRT_DARK = "#0A0F0D"
NEON_PINK = "#FF4DA6"
NEON_BLUE = "#4DDCFF"
NEON_YELLOW = "#FFE066"


# ---------------------------------------------------
# BUILD UI (CALLED FROM main.py)
# ---------------------------------------------------
def build_ui(root):
    root.configure(bg=CRT_DARK)

    # ---------------------------------------------------
    # HEADER
    # ---------------------------------------------------
    spark_label = tk.Label(
        root,
        text="/\\_/\\\n(0 - 0)\n/ = \\",
        font=("Courier New", 30, "bold"),
        bg=CRT_DARK,
        fg=NEON_PINK
    )
    spark_label.pack(pady=5)

    title_label = tk.Label(
        root,
        text="ELECTRONICS WITH SPARK",
        font=("Courier New", 22, "bold"),
        bg=CRT_DARK,
        fg=CRT_GREEN
    )
    title_label.pack(pady=2)

    subtitle_label_top = tk.Label(
        root,
        text="THE TIME‑TRAVELING LEARNING CAT",
        font=("Courier New", 12),
        bg=CRT_DARK,
        fg=NEON_BLUE
    )
    subtitle_label_top.pack(pady=2)

    # Spark talking bar
    spark_speech = tk.Label(
        root,
        text="",
        font=("Courier New", 12),
        bg=CRT_DARK,
        fg=CRT_GREEN,
        wraplength=500,
        height=2
    )
    spark_speech.pack(side="bottom", fill="x")

    def spark_say(text):
        spark_speech.config(text=text)

    # Spark animation frames
    spark_frames = itertools.cycle([
        "/\\_/\\\n(0 - 0)\n/ = \\",
        "/\\_/\\\n(0 - 0)\n/ = \\ ",
        "/\\_/\\\n(0 - 0)\n/ = \\",
        "/\\_/\\\n(0 - 0)\n/ = \\ ",
    ])

    def animate_spark():
        spark_label.config(text=next(spark_frames))
        root.after(300, animate_spark)

    animate_spark()

    # ---------------------------------------------------
    # FRAMES
    # ---------------------------------------------------
    home_frame = tk.Frame(root, bg=CRT_DARK)
    project_frame = tk.Frame(root, bg=CRT_DARK)
    steps_frame = tk.Frame(root, bg=CRT_DARK)
    completed_frame = tk.Frame(root, bg=CRT_DARK)
    history_frame = tk.Frame(root, bg=CRT_DARK)
    quiz_frame = tk.Frame(root, bg=CRT_DARK)

    for frame in (home_frame, project_frame, steps_frame, completed_frame, history_frame, quiz_frame):
        frame.place(x=0, y=200, relwidth=1, relheight=1)

    def show_frame(frame):
        frame.tkraise()

    # ---------------------------------------------------
    # HOME SCREEN
    # ---------------------------------------------------
    current_project = {"data": None}
    step_index = {"value": 0}

    # ⭐ neon_button with width/height support
    def neon_button(parent, text, color, command, w=350, h=80):
        box = tk.Frame(
            parent,
            bg=CRT_DARK,
            highlightthickness=3,
            highlightbackground="white",
            width=w,
            height=h
        )
        box.pack_propagate(False)

        btn = tk.Button(
            box,
            text=text,
            font=("Courier New", 16, "bold"),
            fg=color,
            bg=CRT_DARK,
            activeforeground=color,
            activebackground=CRT_DARK,
            bd=0,
            highlightthickness=0,
            command=command
        )
        btn.pack(fill="both", expand=True)
        return box

    home_title = tk.Label(
        home_frame,
        text="MAIN MENU",
        font=("Courier New", 26, "bold"),
        fg=CRT_GREEN,
        bg=CRT_DARK
    )
    home_title.pack(pady=40)

    neon_button(home_frame, "PROJECT", NEON_BLUE, lambda: show_frame(project_frame)).pack(pady=20)
    neon_button(home_frame, "HISTORY MODE", NEON_YELLOW, lambda: show_frame(history_frame)).pack(pady=20)
    neon_button(home_frame, "QUIZ", NEON_PINK, lambda: show_frame(quiz_frame)).pack(pady=20)

    footer = tk.Label(
        home_frame,
        text="© 2026 Spark Labs – Retro Edition",
        font=("Courier New", 12),
        fg=CRT_GREEN,
        bg=CRT_DARK
    )
    footer.pack(pady=20)

    # ---------------------------------------------------
    # PROJECT SCREEN
    # ---------------------------------------------------
    neon_button(project_frame, "PROJECT", NEON_BLUE, lambda: None).pack(pady=15)

    def open_project(index):
        current_project["data"] = projects[index]
        spark_say(f"Great choice! Let's travel to the world of {current_project['data']['era']} ")
        show_frame(steps_frame)
        reset_step_screen()

    for i, project in enumerate(projects):
        neon_button(
            project_frame,
            project["title"],
            NEON_PINK if i == 0 else (NEON_BLUE if i == 1 else NEON_YELLOW),
            lambda i=i: open_project(i)
        ).pack(pady=15)

    # ---------------------------------------------------
    # STEP SCREEN 
    # ---------------------------------------------------

    step_title_block = neon_button(steps_frame, "", NEON_PINK, lambda: None)
    step_title_block.pack(pady=20)
    step_title_label = step_title_block.winfo_children()[0]

    fun_fact_label = tk.Label(
        steps_frame,
        text="FUN FACT...",
        font=("Courier New", 12),
        fg=NEON_BLUE,
        bg=CRT_DARK
    )
    fun_fact_label.pack(pady=10)

    step_text_block = tk.Frame(
        steps_frame,
        bg=CRT_DARK,
        highlightthickness=3,
        highlightbackground="white",
        width=800,
        height=100
    )
    step_text_block.pack_propagate(False)
    step_text_block.pack(pady=20)
    step_text_block.pack_forget()

    step_text_label = tk.Label(
        step_text_block,
        text="",
        font=("Courier New", 14),
        bg=CRT_DARK,
        fg=NEON_BLUE,
        wraplength=350,
        justify="left"
    )
    step_text_label.pack(fill="both", expand=True, padx=7, pady=7)

    start_block = neon_button(steps_frame, "START PROJECT", NEON_BLUE, lambda: start_project())
    start_block.pack(pady=20)

    back_home_block = neon_button(steps_frame, "BACK TO HOME", NEON_PINK, lambda: show_frame(home_frame))
    back_home_block.pack(pady=20)

    button_row = tk.Frame(steps_frame, bg=CRT_DARK)
    button_row.pack(pady=15)
    button_row.pack_forget()

    back_block = neon_button(button_row, "BACK", NEON_BLUE, lambda: prev_step(), w=150, h=60)
    hint_block = neon_button(button_row, "HINT", NEON_YELLOW, lambda: show_hint(), w=150, h=60)
    next_block = neon_button(button_row, "NEXT", CRT_GREEN, lambda: next_step(), w=150, h=60)

    back_block.grid(row=0, column=0, padx=15)
    hint_block.grid(row=0, column=1, padx=15)
    next_block.grid(row=0, column=2, padx=15)

    sim_block = neon_button(steps_frame, "OPEN SIMULATOR", NEON_PINK, lambda: open_sim(), w=300, h=60)
    sim_block.pack(pady=15)
    sim_block.pack_forget()

    def reset_step_screen():
        step_index["value"] = 0
        step_title_label.config(text=current_project["data"]["title"])
        step_text_block.pack_forget()
        button_row.pack_forget()
        sim_block.pack_forget()
        start_block.pack(pady=20)
        back_home_block.pack(pady=20)

    def start_project():
        start_block.pack_forget()
        back_home_block.pack_forget()
        step_text_block.pack(pady=20)
        button_row.pack(pady=10)
        sim_block.pack(pady=10)
        update_step()

    def update_step():
        step_num = step_index["value"] + 1
        step_title_label.config(text=current_project["data"]["title"])
        step_text_label.config(text=f"Step {step_num}:\n\n{current_project['data']['steps'][step_index['value']]}")

    def next_step():
        if step_index["value"] < len(current_project["data"]["steps"]) - 1:
            step_index["value"] += 1
            update_step()
        else:
            show_completed()

    def prev_step():
        if step_index["value"] > 0:
            step_index["value"] -= 1
            update_step()

    def show_hint():
        project_name = current_project["data"]["title"]
        hint_text = hints[project_name][step_index["value"]]
        spark_say(hint_text)

    def open_sim():
        webbrowser.open(current_project["data"]["sim_url"])

    # ---------------------------------------------------
    # COMPLETED SCREEN
    # ---------------------------------------------------
    completed_title = tk.Label(
        completed_frame,
        text="",
        font=("Courier New", 18, "bold"),
        bg=CRT_DARK,
        fg=CRT_GREEN
    )
    completed_title.pack(pady=20)

    tk.Label(
        completed_frame,
        text="You completed the project!",
        font=("Courier New", 12),
        bg=CRT_DARK,
        fg=NEON_BLUE
    ).pack(pady=10)

    tk.Button(
        completed_frame,
        text="BACK TO HOME",
        font=("Courier New", 14, "bold"),
        width=18,
        bg=CRT_DARK,
        fg=NEON_PINK,
        bd=3,
        relief="ridge",
        command=lambda: show_frame(home_frame)
    ).pack(pady=20)

    def show_completed():
        completed_title.config(text=f"You finished {current_project['data']['title']}!")
        spark_say("Great job! Spark is proud of you ")
        show_frame(completed_frame)

    # ---------------------------------------------------
    # HISTORY MODE SCREEN
    # ---------------------------------------------------
    history_title = tk.Label(
        history_frame,
        text="HISTORY MODE",
        font=("Courier New", 20, "bold"),
        fg=NEON_YELLOW,
        bg=CRT_DARK
    )
    history_title.pack(pady=20)

    history_text = tk.Label(
        history_frame,
        text="Choose an era to learn about.",
        font=("Courier New", 14),
        fg=NEON_BLUE,
        bg=CRT_DARK,
        wraplength=500,
        justify="center"
    )
    history_text.pack(pady=10)

    neon_button(history_frame, "1920 – The Radio Age", CRT_GREEN,
                lambda: set_history_text(
                    "Radios used vacuum tubes instead of chips.\nSpark: \"People listened to music with giant boxes!\""
                ), w=400, h=50).pack(pady=10)

    neon_button(history_frame, "1960 – Space Race Electronics", CRT_GREEN,
                lambda: set_history_text(
                    "Electronics helped rockets reach space.\nSpark: \"Circuits went to the stars!\""
                ), w=400, h=50).pack(pady=10)

    neon_button(history_frame, "1980 – Arcade Machines", CRT_GREEN,
                lambda: set_history_text(
                    "Games lived in big arcade cabinets.\nSpark: \"Beep boop high scores!\""
                ), w=400, h=50).pack(pady=10)

    neon_button(history_frame, "2020 – Microcontrollers", CRT_GREEN,
                lambda: set_history_text(
                    "Tiny boards control everything.\nSpark: \"Even your toaster can be smart!\""
                ), w=400, h=50).pack(pady=10)

    # ⭐ FIXED TWO BUTTON ROW
    wiki_row = tk.Frame(history_frame, bg=CRT_DARK)
    wiki_row.pack(pady=20)

    neon_button(
        wiki_row,
        "OPEN WIKIPEDIA PAGE FOR MORE",
        NEON_PINK,
        lambda: webbrowser.open("https://en.wikipedia.org/wiki/History_of_electronics"),
        w=400, h=50
    ).grid(row=0, column=0, padx=10)

    neon_button(
        wiki_row,
        "BACK TO HOME",
        NEON_PINK,
        lambda: show_frame(home_frame),
        w=400, h=50
    ).grid(row=0, column=1, padx=10)

    # ---------------------------------------------------
    # QUIZ SCREEN
    # ---------------------------------------------------
    quiz_title = tk.Label(
        quiz_frame,
        text="QUIZZES",
        font=("Courier New", 22, "bold"),
        fg=NEON_PINK,
        bg=CRT_DARK
    )
    quiz_title.pack(pady=10)

    quiz_spark_label = spark_label

    question_label = tk.Label(
        quiz_frame,
        text="",
        font=("Courier New", 16, "bold"),
        fg=NEON_BLUE,
        bg=CRT_DARK,
        wraplength=500,
        justify="left"
    )
    question_label.pack(pady=20)

    feedback_label = tk.Label(
        quiz_frame,
        text="",
        font=("Courier New", 14),
        fg=CRT_GREEN,
        bg=CRT_DARK,
        wraplength=500,
        justify="left"
    )
    feedback_label.pack(pady=15)

    quiz_questions = [
        {
            "question": "What does a resistor do?",
            "A": "It slows down current",
            "B": "It makes LEDs brighter",
            "C": "It stores electricity",
            "correct": "A"
        },
        {
            "question": "What does an LED do?",
            "A": "It makes sound",
            "B": "It lights up",
            "C": "It stores data",
            "correct": "B"
        }
    ]

    quiz_index = {"value": 0}

    def update_spark_normal():
        n = quiz_index["value"] + 1
        quiz_spark_label.config(text=f"/\\_/\\\n(0 - {n})\n/ = \\")

    def load_quiz():
        q = quiz_questions[quiz_index["value"]]
        question_label.config(text=f"Question {quiz_index['value']+1}: {q['question']}")
        feedback_label.config(text="")
        btn_A.config(text=f"A: {q['A']}")
        btn_B.config(text=f"B: {q['B']}")
        btn_C.config(text=f"C: {q['C']}")
        update_spark_normal()

    def check_answer(choice):
        correct = quiz_questions[quiz_index["value"]]["correct"]

        if choice == correct:
            quiz_spark_label.config(text="/\\_/\\\n(^ - ^)\n/ = \\")
            feedback_label.config(text=f"Spark: \"{choice} is correct!\"")
        else:
            quiz_spark_label.config(text="/\\_/\\\n(@ - @)\n/ = \\")
            feedback_label.config(text=f"Spark: \"Not quite! The correct answer is {correct}.\"")

        root.after(1000, update_spark_normal)

    btn_A = tk.Button(
        quiz_frame,
        text="A:",
        font=("Courier New", 16, "bold"),
        fg=NEON_BLUE,
        bg=CRT_DARK,
        activeforeground=NEON_BLUE,
        activebackground=CRT_DARK,
        highlightthickness=2,
        highlightbackground="white",
        bd=0,
        width=25,
        command=lambda: check_answer("A")
    )
    btn_A.pack(pady=10)

    btn_B = tk.Button(
        quiz_frame,
        text="B:",
        font=("Courier New", 16, "bold"),
        fg=NEON_YELLOW,
        bg=CRT_DARK,
        activeforeground=NEON_YELLOW,
        activebackground=CRT_DARK,
        highlightthickness=2,
        highlightbackground="white",
        bd=0,
        width=25,
        command=lambda: check_answer("B")
    )
    btn_B.pack(pady=10)

    btn_C = tk.Button(
        quiz_frame,
        text="C:",
        font=("Courier New", 16, "bold"),
        fg=NEON_PINK,
        bg=CRT_DARK,
        activeforeground=NEON_PINK,
        activebackground=CRT_DARK,
        highlightthickness=2,
        highlightbackground="white",
        bd=0,
        width=25,
        command=lambda: check_answer("C")
    )
    btn_C.pack(pady=10)

    def next_question():
        if quiz_index["value"] < len(quiz_questions) - 1:
            quiz_index["value"] += 1
            load_quiz()
        else:
            feedback_label.config(text="Spark: \"Quiz completed! You did great!\"")

    neon_button(quiz_frame, "NEXT QUESTION", CRT_GREEN, next_question).pack(pady=20)
    neon_button(quiz_frame, "BACK TO HOME", NEON_PINK, lambda: show_frame(home_frame)).pack(pady=10)

    load_quiz()

    # ---------------------------------------------------
    # START APP
    # ---------------------------------------------------
    spark_say("Choose a project to begin! Spark is ready to learn with you ")
    show_frame(home_frame)