import json
import tkinter as tk
import webbrowser

from spark_chatbot import ask_spark
from PIL import Image, ImageTk


CRT_DARK = "#0A0F0D"
NEON_PINK = "#FF4DA6"
NEON_BLUE = "#4DDCFF"
NEON_YELLOW = "#FFE066"
NEON_GREEN = "#00FF88"

with open("data/projects.json", "r", encoding="utf-8") as f:
    projects = json.load(f)["projects"]


def build_project_ui(root, show_frame, home_frame, spark_say):
    project_frame = tk.Frame(root, bg=CRT_DARK)
    steps_frame = tk.Frame(root, bg=CRT_DARK)
    completed_frame = tk.Frame(root, bg=CRT_DARK)

    current_project = {"data": None}
    step_index = {"value": 0}
    hint_counter = {"count": 0}

    # Hint step
    step_hints = {
        "Blinking LED": [
            "Check that the long leg of the LED goes to pin 13.",
            "Make sure the resistor is connected to the short leg.",
            "If the LED doesn’t blink, try flipping it — LEDs are directional.",
            "Use the Blink example in Wokwi to test your wiring."
        ],

        "Temperature Control": [
            "The middle pin of the potentiometer must go to A0.",
            "SDA goes to A4 and SCL goes to A5 on the Arduino.",
            "If the LCD is blank, check the I2C address (usually 0x27).",
            "Turn the potentiometer slowly to see temperature changes."
        ],
        "Traffic Light System": [
            "Place the LEDs vertically: Red, Yellow, Green.",
            "Check that Red → 13, Yellow → 12, Green → 11.",
            "Each LED needs its own resistor to GND.",
            "Use delays in your code so the sequence is visible."
        ]
    }

    image_hints = {
        "Blinking LED": [
            "images/Led1from1.png",
            "images/Led2from1.png"
        ],
        "Temperature Control": [
            "images/TemperatureControl1.png",
            "images/TemperatureControl2.png",
            "images/TemperatureControl3.png"
        ],
        "Traffic Light System": [
            "images/TrafficLight1.png",
            "images/TrafficLight2.png",
            "images/TrafficLight3.png",
            "images/TrafficLight4.png"
        ]
    }

    def neon_button(parent, text, color, command, w=200, h=60):
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
            wraplength=w - 20,
            bd=0,
            command=command
        ).pack(fill="both", expand=True)

        return box

    tk.Label(
        project_frame,
        text="PROJECTS",
        font=("Courier New", 26, "bold"),
        fg=NEON_GREEN,
        bg=CRT_DARK
    ).pack(pady=20)

    def open_project(project):
        current_project["data"] = project
        step_index["value"] = 0
        hint_counter["count"] = 0
        spark_say(f"Let's explore {project['title']} from the {project['era']} era!")
        show_frame(steps_frame)
        reset_step_screen()

    for p in projects:
        neon_button(
            project_frame,
            p["title"],
            p.get("button_color", NEON_BLUE),
            command=lambda proj=p: open_project(proj)
        ).pack(pady=15)

    neon_button(
        project_frame,
        "BACK TO HOME",
        NEON_PINK,
        lambda: show_frame(home_frame)
    ).pack(pady=20)

    step_title = tk.Label(
        steps_frame,
        text="",
        font=("Courier New", 20, "bold"),
        fg=NEON_PINK,
        bg=CRT_DARK
    )
    step_title.pack(pady=20)

    # Fun fact and step
    fact_step_frame = tk.Frame(steps_frame, bg=CRT_DARK)
    fact_step_frame.pack(pady=10)

    fact_label = tk.Label(
        fact_step_frame,
        text="",
        font=("Courier New", 14, "bold"),
        fg=NEON_BLUE,
        bg=CRT_DARK,
        wraplength=500,
        justify="center"
    )
    fact_label.pack(pady=5)

    step_label = tk.Label(
        fact_step_frame,
        text="",
        font=("Courier New", 16),
        fg=NEON_GREEN,
        bg=CRT_DARK,
        wraplength=500,
        justify="center"
    )
    step_label.pack(pady=10)

    hint_label = tk.Label(
        steps_frame,
        text="",
        font=("Courier New", 12),
        fg=NEON_YELLOW,
        bg=CRT_DARK,
        wraplength=500,
        justify="center"
    )
    hint_label.pack(pady=10)

    # Navigation buttons
    nav = tk.Frame(steps_frame, bg=CRT_DARK)
    nav.pack(pady=20)

    neon_button(nav, "BACK", NEON_BLUE, lambda: prev_step()).grid(row=0, column=0, padx=10)
    neon_button(nav, "HINT", NEON_YELLOW, lambda: show_hint()).grid(row=0, column=1, padx=10)
    neon_button(nav, "NEXT", NEON_GREEN, lambda: next_step()).grid(row=0, column=2, padx=10)

    bottom_nav = tk.Frame(steps_frame, bg=CRT_DARK)
    bottom_nav.pack(pady=10)

    neon_button(
        bottom_nav,
        "OPEN SIMULATOR",
        NEON_PINK,
        lambda: webbrowser.open(current_project["data"]["sim_url"]),
        w=200, h=60
    ).grid(row=0, column=0, padx=10)

    neon_button(
        bottom_nav,
        "BACK TO HOME",
        NEON_PINK,
        lambda: show_frame(home_frame),
        w=200, h=60
    ).grid(row=0, column=1, padx=10)

    def reset_step_screen():
        project = current_project["data"]
        step_index["value"] = 0
        hint_counter["count"] = 0
        step_title.config(text=project["title"])
        update_step()

    def update_step():
        project = current_project["data"]
        i = step_index["value"]

        fact_label.config(text=f"FACT: {project['fun_fact']}")
        step_label.config(text=f"Step {i+1}: {project['steps'][i]}")
        hint_label.config(text="")

    def next_step():
        project = current_project["data"]
        if step_index["value"] < len(project["steps"]) - 1:
            step_index["value"] += 1
            hint_counter["count"] = 0
            update_step()
        else:
            show_frame(completed_frame)

    def prev_step():
        if step_index["value"] > 0:
            step_index["value"] -= 1
            hint_counter["count"] = 0
            update_step()

    
    def open_image_popup(img_path):
        try:
            popup = tk.Toplevel()
            popup.title("Hint Image")

            # Make popup BIG
            popup.geometry("800x600")
            popup.configure(bg=CRT_DARK)

            # Load and resize image
            img = Image.open(img_path)
            img = img.resize((800, 590))
            tk_img = ImageTk.PhotoImage(img)

            img_label = tk.Label(popup, image=tk_img, bg=CRT_DARK)
            img_label.image = tk_img
            img_label.pack(padx=20, pady=20)

            tk.Button(
                popup,
                text="CLOSE",
                font=("Courier New", 16, "bold"),
                fg=NEON_PINK,
                bg=CRT_DARK,
                bd=0,
                command=popup.destroy
            ).pack(pady=10)

        except Exception as e:
            hint_label.config(text=f"Could not load image: {e}")

    def show_image_hint(project_title):
        img_list = image_hints.get(project_title)

        if not img_list:
            hint_label.config(text="Super hint image not set yet.")
            return

        img_path = img_list[step_index["value"] % len(img_list)]
        open_image_popup(img_path)

    def show_hint():
        project = current_project["data"]
        if project is None:
            hint_label.config(text="Pick a project first.")
            return

        i = step_index["value"]
        title = project["title"]

        hint_counter["count"] += 1
        count = hint_counter["count"]

        if count == 1:
            try:
                prompt = f"hint: {title} step {i+1}: {project['steps'][i]}"
                hint_text = ask_spark(prompt)
                hint_label.config(text="Hint: " + hint_text)
            except Exception:
                hint_label.config(text="Hint: Spark is confused… check your wiring!")
            return

        if count == 2:
            hints_for_project = step_hints.get(title, [])
            if i < len(hints_for_project):
                hint_label.config(text="Hint: " + hints_for_project[i])
            else:
                hint_label.config(text="Hint: Check your wiring and pin numbers.")
            return

        hint_label.config(text="Super Hint: opening image…")
        show_image_hint(title)

    tk.Label(
        completed_frame,
        text="PROJECT COMPLETE!",
        font=("Courier New", 22, "bold"),
        fg=NEON_GREEN,
        bg=CRT_DARK
    ).pack(pady=20)

    neon_button(
        completed_frame,
        "BACK TO HOME",
        NEON_PINK,
        lambda: show_frame(home_frame)
    ).pack(pady=20)

    return project_frame, steps_frame, completed_frame
