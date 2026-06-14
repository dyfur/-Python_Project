import random

def spark_chat(hint):
    text = hint.lower()

    # LED HINTS
    if "led" in text:
        return random.choice([
            "Check the LED direction: long leg to the Arduino pin, short leg to GND.",
            "If the LED doesn't light, flip it — LEDs only work one way.",
            "Make sure you used a resistor so the LED doesn’t burn out."
        ])

    # BUTTON HINTS
    if "button" in text or "switch" in text:
        return random.choice([
            "One side of the button must go to GND.",
            "Use INPUT_PULLUP so the button works without extra resistors.",
            "If the button does nothing, check that the pin is set as INPUT_PULLUP."
        ])

    # BUZZER HINTS
    if "buzzer" in text or "beep" in text:
        return random.choice([
            "Make sure + of the buzzer goes to the Arduino pin.",
            "Try a different frequency if the buzzer is too quiet.",
            "Check that the buzzer ground is connected properly."
        ])

    # WOKWI HINTS
    if "wokwi" in text or "simulator" in text:
        return random.choice([
            "Check your wiring in Wokwi — one wrong pin can break the circuit.",
            "If Wokwi shows an error, look at the console for clues.",
            "Make sure your code pin numbers match your wiring."
        ])

    
    return random.choice([
        "Double‑check your wiring and pin numbers.",
        "Try following the step again slowly.",
        "Look closely at the breadboard rows — mistakes hide there."
    ])

def ask_spark(prompt):
    return spark_chat(prompt)
