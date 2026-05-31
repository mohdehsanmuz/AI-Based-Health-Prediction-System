import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# ---------------- LOAD MODEL ----------------

model = joblib.load("model/health_model.pkl")

# ---------------- CREATE WINDOW ----------------

root = tk.Tk()

root.title("AI Health Prediction System")

root.geometry("850x700")

root.configure(bg="#0f172a")

# ---------------- TITLE ----------------

title = tk.Label(
    root,
    text="🩺 AI-Based Health Prediction System",
    font=("Arial", 28, "bold"),
    bg="#0f172a",
    fg="white"
)

title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Predict health condition using Temperature and Pulse Rate",
    font=("Arial", 14),
    bg="#0f172a",
    fg="#cbd5e1"
)

subtitle.pack()

# ---------------- INSTRUCTION SECTION ----------------

instruction_title = tk.Label(
    root,
    text="📋 Instructions",
    font=("Arial", 20, "bold"),
    bg="#0f172a",
    fg="#22d3ee"
)

instruction_title.pack(pady=15)

instructions = tk.Label(
    root,
    text=
    "• Enter valid Temperature and Pulse values\n"
    "• Temperature range: 97°F to 105°F\n"
    "• Pulse Rate range: 60 BPM to 150 BPM\n"
    "• Click Predict button to get health condition\n"
    "• Invalid values will show warning message",
    font=("Arial", 12),
    justify="left",
    bg="#0f172a",
    fg="white"
)

instructions.pack()

# ---------------- INPUT FRAME ----------------

frame = tk.Frame(
    root,
    bg="#1e293b",
    padx=40,
    pady=40
)

frame.pack(pady=30)

# ---------------- TEMPERATURE ----------------

temp_label = tk.Label(
    frame,
    text="🌡 Temperature (°F) [97 - 105]",
    font=("Arial", 15, "bold"),
    bg="#1e293b",
    fg="white"
)

temp_label.grid(row=0, column=0, pady=15, sticky="w")

temp_entry = tk.Entry(
    frame,
    font=("Arial", 15),
    width=20
)

temp_entry.grid(row=0, column=1, pady=15)

# ---------------- PULSE RATE ----------------

pulse_label = tk.Label(
    frame,
    text="❤️ Pulse Rate (BPM) [60 - 150]",
    font=("Arial", 15, "bold"),
    bg="#1e293b",
    fg="white"
)

pulse_label.grid(row=1, column=0, pady=15, sticky="w")

pulse_entry = tk.Entry(
    frame,
    font=("Arial", 15),
    width=20
)

pulse_entry.grid(row=1, column=1, pady=15)

# ---------------- RESULT LABEL ----------------

result_label = tk.Label(
    root,
    text="Prediction Result Will Appear Here",
    font=("Arial", 22, "bold"),
    bg="#0f172a",
    fg="white"
)

result_label.pack(pady=25)

# ---------------- HEALTH MESSAGE ----------------

health_message = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="#0f172a",
    fg="white"
)

health_message.pack()

# ---------------- PREDICTION FUNCTION ----------------

def predict_health():

    try:

        temp = float(temp_entry.get())

        pulse = float(pulse_entry.get())

        # ---------- VALIDATION ----------

        if temp < 97 or temp > 105:

            result_label.config(
                text="❌ Invalid Temperature Data",
                fg="orange"
            )

            health_message.config(
                text="Please enter temperature between 97°F and 105°F",
                fg="orange"
            )

            return

        if pulse < 60 or pulse > 150:

            result_label.config(
                text="❌ Invalid Pulse Rate Data",
                fg="orange"
            )

            health_message.config(
                text="Please enter pulse rate between 60 BPM and 150 BPM",
                fg="orange"
            )

            return

        # ---------- PREDICTION ----------

        data = np.array([[temp, pulse]])

        prediction = model.predict(data)

        result = prediction[0]

        # ---------- HEALTHY ----------

        if result == "Healthy":

            result_label.config(
                text="✅ HEALTHY",
                fg="#22c55e"
            )

            health_message.config(
                text=
                "Patient condition is stable.\n"
                "Maintain healthy lifestyle and regular monitoring.",
                fg="#22c55e"
            )

        # ---------- MODERATE ----------

        elif result == "Moderate":

            result_label.config(
                text="⚠ MODERATE",
                fg="#facc15"
            )

            health_message.config(
                text=
                "Patient condition requires observation.\n"
                "Take rest, stay hydrated, and consult doctor if symptoms continue.",
                fg="#facc15"
            )

        # ---------- SERIOUS ----------

        elif result == "Serious":

            result_label.config(
                text="🚨 SERIOUS",
                fg="#ef4444"
            )

            health_message.config(
                text=
                "Critical health condition detected.\n"
                "Immediate medical attention is recommended.",
                fg="#ef4444"
            )

        # ---------- UNMATCHED ----------

        else:

            result_label.config(
                text="❌ Unmatched Data",
                fg="orange"
            )

            health_message.config(
                text=
                "Entered data does not match trained healthcare patterns.",
                fg="orange"
            )

    except:

        result_label.config(
            text="❌ Invalid Input",
            fg="orange"
        )

        health_message.config(
            text="Please enter valid numeric values only.",
            fg="orange"
        )

# ---------------- PREDICT BUTTON ----------------

predict_button = tk.Button(
    root,
    text="🔍 Predict Health Condition",
    font=("Arial", 18, "bold"),
    bg="#14b8a6",
    fg="white",
    padx=25,
    pady=12,
    command=predict_health
)

predict_button.pack(pady=20)

# ---------------- HEALTH TIPS ----------------

tips_title = tk.Label(
    root,
    text="💡 Health Tips",
    font=("Arial", 20, "bold"),
    bg="#0f172a",
    fg="#22d3ee"
)

tips_title.pack(pady=15)

tips = tk.Label(
    root,
    text=
    "• Drink enough water daily\n"
    "• Maintain healthy body temperature\n"
    "• Exercise regularly\n"
    "• Take proper sleep and rest\n"
    "• Consult doctor for persistent symptoms",
    font=("Arial", 12),
    justify="left",
    bg="#0f172a",
    fg="white"
)

tips.pack()

# ---------------- FOOTER ----------------

footer = tk.Label(
    root,
    text="Developed using Python, Tkinter, and Machine Learning",
    font=("Arial", 10),
    bg="#0f172a",
    fg="#94a3b8"
)

footer.pack(side="bottom", pady=20)

# ---------------- RUN APPLICATION ----------------

root.mainloop()