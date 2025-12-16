import string
import tkinter as tk
from tkinter import ttk

MIN_LENGTH = 8
SPECIAL_CHARS = string.punctuation


def check_password_strength(password: str) -> tuple[str, list[str]]:
    missing = []

    if len(password) < MIN_LENGTH:
        missing.append(f"at least {MIN_LENGTH} characters")
    if not any(c.islower() for c in password):
        missing.append("a lowercase letter")
    if not any(c.isupper() for c in password):
        missing.append("an uppercase letter")
    if not any(c.isdigit() for c in password):
        missing.append("a digit")
    if not any(c in SPECIAL_CHARS for c in password):
        missing.append("a special character")

    satisfied = 5 - len(missing)

    if satisfied <= 2:
        strength = "WEAK"
    elif satisfied in (3, 4):
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, missing


def on_check_click():
    password = entry_pwd.get()
    strength, missing = check_password_strength(password)

    # Set color based on strength
    if strength == "WEAK":
        color = "red"
    elif strength == "MEDIUM":
        color = "orange"
    else:
        color = "green"

    label_strength.config(text=f"Strength: {strength}", foreground=color)

    if missing:
        advice = "Improve by adding:\n- " + "\n- ".join(missing)
    else:
        advice = "Great! Your password meets all criteria."

    text_feedback.config(state="normal")
    text_feedback.delete("1.0", tk.END)
    text_feedback.insert(tk.END, advice)
    text_feedback.config(state="disabled")


# ---------------- GUI setup ----------------

root = tk.Tk()
root.title("🛡️Password Complexity Checker")

root.geometry("420x260")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding=15)
main_frame.pack(fill="both", expand=True)

label_title = ttk.Label(
    main_frame,
    text="Password Complexity Checker",
    font=("Segoe UI", 14, "bold")
)
label_title.pack(pady=(0, 10))

label_pwd = ttk.Label(main_frame, text="Enter password:")
label_pwd.pack(anchor="w")

entry_pwd = ttk.Entry(main_frame, show="*", width=40)
entry_pwd.pack(fill="x", pady=5)

btn_check = ttk.Button(main_frame, text="Check Strength", command=on_check_click)
btn_check.pack(pady=5)

label_strength = ttk.Label(main_frame, text="Strength: ", font=("Segoe UI", 11, "bold"))
label_strength.pack(pady=(5, 2))

text_feedback = tk.Text(main_frame, height=5, wrap="word")
text_feedback.pack(fill="both", expand=True)
text_feedback.config(state="disabled")

root.mainloop()
