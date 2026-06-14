import tkinter as tk
import json

CRT_DARK = "#0A0F0D"
NEON_PINK = "#FF4DA6"
NEON_BLUE = "#4DDCFF"
NEON_YELLOW = "#FFE066"
CRT_GREEN = "#00FF88"


def build_quiz_ui(root, show_frame, home_frame, spark_label):
    quiz_frame = tk.Frame(root, bg=CRT_DARK)
    final_frame = tk.Frame(root, bg=CRT_DARK)

    
    with open("data/quiz.json", "r") as f:
        quiz_questions = json.load(f)

    quiz_index = {"value": 0}
    score = {"value": 0}

    # Title
    tk.Label(
        quiz_frame,
        text="QUIZZES",
        font=("Courier New", 22, "bold"),
        fg=NEON_PINK,
        bg=CRT_DARK
    ).pack(pady=10)

    # Question label
    question_label = tk.Label(
        quiz_frame,
        text="",
        font=("Courier New", 16, "bold"),
        fg=NEON_BLUE,
        bg=CRT_DARK,
        wraplength=500
    )
    question_label.pack(pady=20)

    # Feedback
    feedback_label = tk.Label(
        quiz_frame,
        text="",
        font=("Courier New", 14),
        fg=CRT_GREEN,
        bg=CRT_DARK,
        wraplength=500
    )
    feedback_label.pack(pady=15)

    # Spark face update
    def update_spark():
        n = quiz_index["value"] + 1
        s = score["value"]
        spark_label.config(text=f"/\\_/\\\n({s} - {n})\n/ = \\")

    # Load question
    def load_quiz():
        q = quiz_questions[quiz_index["value"]]
        question_label.config(text=f"Question {quiz_index['value']+1}: {q['question']}")
        feedback_label.config(text="")
        btn_A.config(text=f"A: {q['A']}")
        btn_B.config(text=f"B: {q['B']}")
        btn_C.config(text=f"C: {q['C']}")
        update_spark()

    # Check answer
    def check_answer(choice):
        correct = quiz_questions[quiz_index["value"]]["correct"]

        if choice == correct:
            score["value"] += 1
            spark_label.config(text="/\\_/\\\n(^ - ^)\n/ = \\")
            feedback_label.config(text=f"Spark: \"{choice} is correct!\"")
        else:
            spark_label.config(text="/\\_/\\\n(@ - @)\n/ = \\")
            feedback_label.config(text=f"Spark: \"Not quite! The correct answer is {correct}.\"")

        root.after(1000, update_spark)

    # Buttons A/B/C
    btn_A = tk.Button(quiz_frame, command=lambda: check_answer("A"))
    btn_B = tk.Button(quiz_frame, command=lambda: check_answer("B"))
    btn_C = tk.Button(quiz_frame, command=lambda: check_answer("C"))

    for btn, color in [(btn_A, NEON_BLUE), (btn_B, NEON_YELLOW), (btn_C, NEON_PINK)]:
        btn.config(
            font=("Courier New", 16, "bold"),
            fg=color,
            bg=CRT_DARK,
            activeforeground=color,
            activebackground=CRT_DARK,
            highlightthickness=2,
            highlightbackground="white",
            width=50
        )
        btn.pack(pady=10)

    # Next question
    def next_question():
        if quiz_index["value"] < len(quiz_questions) - 1:
            quiz_index["value"] += 1
            load_quiz()
        else:
            show_final()

    nav = tk.Frame(quiz_frame, bg=CRT_DARK)
    nav.pack(pady=20)

    tk.Button(
        nav,
        text="NEXT QUESTION",
        font=("Courier New", 16, "bold"),
        fg=CRT_GREEN,
        bg=CRT_DARK,
        command=next_question
    ).grid(row=0, column=0, padx=20)

    tk.Button(
        nav,
        text="BACK TO HOME",
        font=("Courier New", 16, "bold"),
        fg=NEON_PINK,
        bg=CRT_DARK,
        command=lambda: show_frame(home_frame)
    ).grid(row=0, column=1, padx=20)

    load_quiz()

    # Final page
    score_label = tk.Label(final_frame, font=("Courier New", 16), fg=NEON_BLUE, bg=CRT_DARK)
    score_label.pack(pady=20)

    # Back to home button
    tk.Button(
        final_frame,
        text="BACK TO HOME",
        font=("Courier New", 16, "bold"),
        fg=NEON_PINK,
        bg=CRT_DARK,
        bd=3,
        relief="ridge",
        command=lambda: show_frame(home_frame)
    ).pack(pady=20)

    def show_final():
        score_label.config(text=f"Your Score: {score['value']}/{len(quiz_questions)}")
        show_frame(final_frame)

    return quiz_frame, final_frame