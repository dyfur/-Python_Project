import random

def spark_chat(user_input):
    text = user_input.lower()

    # GREETINGS
    if any(g in text for g in ["hi", "hello", "hey", "yo"]):
        return random.choice([
            "Spark waves his tail! Hi friend! ⚡🐱",
            "Hello! Ready to learn some electronics?",
            "Hey hey! Spark is here and glowing!"
        ])

    # LED
    if "led" in text:
        return random.choice([
            "LEDs have a long leg (+) and a short leg (-). Long leg goes to the Arduino pin!",
            "If your LED doesn't work, flip it! LEDs only work in one direction.",
            "Remember: LEDs need a resistor or they go *boom* 💥⚡"
        ])

    # RESISTOR
    if "resistor" in text or "ohm" in text:
        return random.choice([
            "A resistor slows down the current so your LED stays safe.",
            "Think of a resistor like a traffic light for electricity.",
            "More ohms = less current. Less ohms = more current!"
        ])

    # BUZZER
    if "buzzer" in text or "sound" in text:
        return random.choice([
            "Buzzers have + and - pins. + goes to a digital pin!",
            "If your buzzer is quiet, try a different frequency.",
            "Spark loves buzzers! Beep beep! 🎵"
        ])

    # BUTTON
    if "button" in text or "switch" in text:
        return random.choice([
            "Buttons connect two points when pressed. Simple but powerful!",
            "Try using INPUT_PULLUP so your button works without extra resistors.",
            "Buttons are like Spark's paws — press to activate! 🐾"
        ])

    # WOKWI HELP
    if "wokwi" in text or "where" in text or "start" in text:
        return random.choice([
            "Choose Arduino Uno in Wokwi — the blue board with the USB port!",
            "Press R to rotate components in Wokwi!",
            "Click a pin, then click a component leg to connect a wire!"
        ])

    # CODE HELP
    if "code" in text or "setup" in text or "loop" in text:
        return random.choice([
            "setup() runs once. loop() runs forever!",
            "Use pinMode(pin, OUTPUT) in setup() to prepare your LED.",
            "Use digitalWrite(pin, HIGH) in loop() to turn things on!"
        ])

    # HINT ESCALATION
    if "hint" in text or "help me" in text:
        return random.choice([
            "Try checking your wiring! Long leg to the pin, short leg to GND.",
            "Spark thinks a resistor might be missing…",
            "If you're stuck, Spark can show a diagram! Just say 'diagram'."
        ])

    # DIAGRAM REQUEST
    if "diagram" in text:
        return "Spark can show ASCII diagrams! Later you can add real photos too."

    # FALLBACK
    return random.choice([
        "Spark tilts his head… hmm, I don’t know that yet, but I can learn! ⚡",
        "Try asking about LEDs, resistors, buzzers, buttons, or Arduino!",
        "Spark doesn’t understand… but Spark believes in you! 💛"
    ])
