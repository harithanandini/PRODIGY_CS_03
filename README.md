This code is a nice, clean Tkinter GUI for checking password strength. Here is a README you can use.

Overview
This project is a simple desktop application that checks the complexity of a password using a graphical user interface built with Tkinter. The app evaluates a password against common security rules and gives both a strength label and improvement tips.

Features 

Checks for:

  >Minimum length of 8 characters

  >At least one lowercase letter

  >At least one uppercase letter

  >At least one digit

  >At least one special character (from Python’s string.punctuation)

Classifies passwords as WEAK, MEDIUM, or STRONG.

Color‑coded strength label:

  >Red for WEAK

  >Orange for MEDIUM

  >Green for STRONG

Text area with suggestions showing exactly which criteria are missing.

How It Works
The core function check_password_strength(password) returns:

 >strength: one of "WEAK", "MEDIUM", or "STRONG", based on how many of the five rules are satisfied.

  >missing: a list of human‑readable messages for each unmet criterion.

The GUI:

  >Takes the password from an entry field (masked with *).

  >On clicking Check Strength, calls check_password_strength.

  >Updates a label with the strength and color, and a read‑only text box with advice.

Requirements
  >Python 3.10+ (any recent Python 3 version should work)

  >Standard library only (uses tkinter and string, no external dependencies)

How to Run
  1.Save the script as password_checker_gui.py.

  2.Make sure Python is installed and added to PATH.

  3.Open a terminal or command prompt in the folder containing the file.

  4.Run:

bash
python password_checker_gui.py


The Password Complexity Checker window will open. Enter any password and click Check Strength to see the result.