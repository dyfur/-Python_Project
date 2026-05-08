import tkinter as tk
import webbrowser

root = tk.Tk()
root.title("Electronics with Spark")
root.geometry("600x750")
root.configure(bg="#f7c6ff")

# ---------------------------------------------------
# PROJECT DATA
# ---------------------------------------------------
projects = [
    {
        "title": "LED Circuit",
        "steps": [
            "Step 1: Take an LED. The long leg is the positive side (anode).",
            "Step 2: Place the LED into the breadboard in two different rows.",
            "Step 3: Connect the long leg to Arduino pin 13.",
            "Step 4: Connect the short leg to GND using a 220Ω resistor."
        ],
        "sim_url": "https://wokwi.com/projects/new/arduino-uno"
    },
    {
        "title": "Buzzer",
        "steps": [
            "Step 1: Take a piezo buzzer. Look for the + and - symbols.",
            "Step 2: Place the buzzer into the breadboard.",
            "Step 3: Connect the + pin to Arduino pin 8.",
            "Step 4: Connect the - pin to GND."
        ],
        "sim_url": "https://wokwi.com/projects/new/arduino-uno"
    },
    {
        "title": "Light Sensor (LDR)",
        "steps": [
            "Step 1: Take an LDR (light sensor).",
            "Step 2: Place the LDR into the breadboard.",
            "Step 3: Connect one side of the LDR to 5V.",
            "Step 4: Connect the other side to A0 and to GND using a 10kΩ resistor."
        ],
        "sim_url": "https://wokwi.com/projects/new/arduino-uno"
    }
]
