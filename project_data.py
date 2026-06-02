projects = [
    {
        "title": "Blinking LED",
        "era": "Modern Basics",
        "steps": [
            "Step 1: Place an LED on the breadboard. Long leg = +.",
            "Step 2: Connect the long leg to Arduino pin 13.",
            "Step 3: Connect the short leg to GND using a 220Ω resistor.",
            "Step 4: Upload the Blink code in Wokwi to make it flash!"
        ],
        "sim_url": "https://wokwi.com/projects/new/arduino-uno"
    },
    {
        "title": "Traffic Light",
        "era": "City Streets",
        "steps": [
            "Step 1: Place 3 LEDs: Red, Yellow, Green.",
            "Step 2: Connect Red to pin 13, Yellow to pin 12, Green to pin 11.",
            "Step 3: Connect all short legs to GND with resistors.",
            "Step 4: Run the traffic light code in Wokwi!"
        ],
        "sim_url": "https://wokwi.com/projects/new/arduino-uno"
    },
    {
        "title": "Buzzer Doorbell",
        "era": "Home Gadgets",
        "steps": [
            "Step 1: Place a buzzer on the breadboard.",
            "Step 2: Connect + to pin 8 and - to GND.",
            "Step 3: Add a pushbutton between pin 2 and GND.",
            "Step 4: Press the button in Wokwi to ring the bell!"
        ],
        "sim_url": "https://wokwi.com/projects/new/arduino-uno"
    }
]

hints = {
    "Blinking LED": [
        "Hint: The long leg of the LED must go to pin 13.",
        "Hint: Make sure the LED legs are in different rows.",
        "Hint: The resistor must go between the short leg and GND.",
        "Hint: In Wokwi, try the built‑in Blink example!"
    ],
    "Traffic Light": [
        "Hint: Red = pin 13, Yellow = pin 12, Green = pin 11.",
        "Hint: Each LED needs its own resistor.",
        "Hint: Check that each LED is in its own row.",
        "Hint: Try slowing down the delay to see the sequence clearly."
    ],
    "Buzzer Doorbell": [
        "Hint: The + pin of the buzzer goes to pin 8.",
        "Hint: The button must connect to GND on one side.",
        "Hint: Use INPUT_PULLUP in code so the button works.",
        "Hint: Try holding the button to hear a longer beep!"
    ]
}


