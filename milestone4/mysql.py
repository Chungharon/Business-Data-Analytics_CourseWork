from typing import Literal, Optional
"""
Student Signup Form - Tkinter GUI with MySQL Integration
========================================================
STEP-BY-STEP MySQL SETUP:
--------------------------
1. Install MySQL connector:
   pip install mysql-connector-python

2. Create MySQL database and table:
   Run these SQL commands in your MySQL client:

   CREATE DATABASE student_db;
   USE student_db;

   CREATE TABLE students (
       id INT AUTO_INCREMENT PRIMARY KEY,
       first_name VARCHAR(50) NOT NULL,
       last_name VARCHAR(50) NOT NULL,
       gender VARCHAR(10) NOT NULL,
       unit_math TINYINT(1) DEFAULT 0,
       unit_science TINYINT(1) DEFAULT 0,
       unit_english TINYINT(1) DEFAULT 0,
       unit_history TINYINT(1) DEFAULT 0,
       unit_cs TINYINT(1) DEFAULT 0,
       unit_art TINYINT(1) DEFAULT 0,
       total_units INT DEFAULT 0,
       registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );

3. Update DB_CONFIG below with your MySQL credentials.
4. Run this script: python student_signup.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


DB_CONFIG = {
    "host":     "localhost",
    "user":     "root",          # your MySQL username
    "password": "your_password", # your MySQL password
    "database": "student_db"
}

try:
    import mysql.connector
    MYSQL_AVAILABLE = True
except ImportError:
    MYSQL_AVAILABLE = False


def get_db_connection():
    """Open and return a MySQL connection using DB_CONFIG."""
    if not MYSQL_AVAILABLE:
        raise RuntimeError(
            "mysql-connector-python is not installed.\n"
            "Run:  pip install mysql-connector-python"
        )
    import mysql.connector
    return mysql.connector.connect(**DB_CONFIG)


def insert_student(data: dict) -> bool:
    """
    Insert a student record into the MySQL table.
    Returns True on success, False on failure.
    """
    sql = """
        INSERT INTO students
            (first_name, last_name, gender,
             unit_math, unit_science, unit_english,
             unit_history, unit_cs, unit_art, total_units)
        VALUES
            (%(first_name)s, %(last_name)s, %(gender)s,
             %(math)s, %(science)s, %(english)s,
             %(history)s, %(cs)s, %(art)s, %(total_units)s)
    """
    try:
        conn   = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as exc:
        messagebox.showerror("Database Error", str(exc))
        return False


# ─────────────────────────────────────────
# Colour Palette
# ─────────────────────────────────────────
BG_MAIN    = "#1B2A4A"   # deep navy — form background
BG_CARD    = "#243559"   # slightly lighter card panels
BG_FIELD   = "#2E4270"   # entry field background
ACCENT     = "#4A90D9"   # bright blue accent
ACCENT2    = "#5BC0BE"   # teal highlight
TEXT_LIGHT = "#EAF0FB"   # primary text
TEXT_DIM   = "#8FA8CC"   # secondary / placeholder text
BTN_SUBMIT = "#4A90D9"
BTN_CLEAR  = "#E05C5C"
BTN_TEXT   = "#FFFFFF"


# ─────────────────────────────────────────
# Main Application
# ─────────────────────────────────────────
class StudentSignupApp(tk.Tk):
    UNITS = ["Mathematics", "Science", "English", "History", "Computer Science", "Art"]
    UNIT_KEYS = ["math", "science", "english", "history", "cs", "art"]

    def __init__(self):
        super().__init__()
        self.title("Student Registration Portal")
        self.geometry("680x780")
        self.resizable(False, False)
        self.configure(bg=BG_MAIN)

        # ── Variables ──────────────────────────────
        self.first_name_var = tk.StringVar()
        self.last_name_var  = tk.StringVar()
        self.gender_var     = tk.StringVar(value="Male")
        self.unit_vars      = {key: tk.BooleanVar() for key in self.UNIT_KEYS}

        self._build_ui()

    # ── UI Builder ─────────────────────────────────
    def _build_ui(self):
        # ── Header ────────────────────────────────
        header = tk.Frame(self, bg=ACCENT, pady=18)
        header.pack(fill="x")
        tk.Label(header, text="🎓  Student Registration",
                 font=("Helvetica", 20, "bold"),
                 bg=ACCENT, fg=BTN_TEXT).pack()
        tk.Label(header, text="Complete the form below to register",
                 font=("Helvetica", 10),
                 bg=ACCENT, fg="#D0E4FF").pack()

        # ── Scrollable body ───────────────────────
        body = tk.Frame(self, bg=BG_MAIN, padx=40, pady=20)
        body.pack(fill="both", expand=True)

        # ── Personal Details card ─────────────────
        self._section(body, "Personal Details")

        row1 = tk.Frame(body, bg=BG_MAIN)
        row1.pack(fill="x", pady=(0, 12))
        self._field(row1, "First Name", self.first_name_var, side="left")
        tk.Frame(row1, bg=BG_MAIN, width=20).pack(side="left")
        self._field(row1, "Last Name",  self.last_name_var,  side="left")

        # ── Gender ────────────────────────────────
        self._section(body, "Gender")
        gender_frame = tk.Frame(body, bg=BG_CARD, bd=0, relief="flat",
                                padx=16, pady=12)
        gender_frame.pack(fill="x", pady=(0, 16))

        for g in ("Male", "Female", "Non-binary", "Prefer not to say"):
            tk.Radiobutton(
                gender_frame, text=g, variable=self.gender_var, value=g,
                bg=BG_CARD, fg=TEXT_LIGHT, activebackground=BG_CARD,
                activeforeground=ACCENT2, selectcolor=BG_MAIN,
                font=("Helvetica", 11), padx=14
            ).pack(side="left")

        # ── Units ─────────────────────────────────
        self._section(body, "Units Registered")
        units_frame = tk.Frame(body, bg=BG_CARD, padx=16, pady=12)
        units_frame.pack(fill="x", pady=(0, 16))

        for col, (label, key) in enumerate(zip(self.UNITS, self.UNIT_KEYS)):
            r, c = divmod(col, 3)
            cb = tk.Checkbutton(
                units_frame, text=label,
                variable=self.unit_vars[key],
                bg=BG_CARD, fg=TEXT_LIGHT,
                activebackground=BG_CARD, activeforeground=ACCENT2,
                selectcolor=BG_MAIN,
                font=("Helvetica", 11), padx=8, pady=4
            )
            cb.grid(row=r, column=c, sticky="w", padx=6, pady=2)

        # ── Status / info bar ─────────────────────
        self.status_var = tk.StringVar(
            value="⚡ MySQL: " + ("Connected (library found)" if MYSQL_AVAILABLE else "mysql-connector not installed")
        )
        status_color = ACCENT2 if MYSQL_AVAILABLE else "#E05C5C"
        tk.Label(body, textvariable=self.status_var,
                 font=("Helvetica", 9, "italic"),
                 bg=BG_MAIN, fg=status_color).pack(anchor="w", pady=(0, 14))

        # ── Buttons ───────────────────────────────
        btn_frame = tk.Frame(body, bg=BG_MAIN)
        btn_frame.pack(fill="x")

        self._button(btn_frame, "✖  Clear Form",  BTN_CLEAR,  self.clear_form).pack(side="left",  expand=True, fill="x", padx=(0, 10))
        self._button(btn_frame, "✔  Submit",       BTN_SUBMIT, self.submit_form).pack(side="right", expand=True, fill="x", padx=(10, 0))

        # ── Footer ────────────────────────────────
        tk.Label(self,
                 text="©️ 2026 Student Portal  |  Powered by Python + MySQL",
                 font=("Helvetica", 8), bg=BG_MAIN, fg=TEXT_DIM
                 ).pack(pady=(6, 10))

    def _section(self, parent, title):
        f = tk.Frame(parent, bg=BG_MAIN)
        f.pack(fill="x", pady=(10, 4))
        tk.Label(f, text=title.upper(),
                 font=("Helvetica", 9, "bold"),
                 bg=BG_MAIN, fg=ACCENT2).pack(side="left")
        tk.Frame(f, bg=ACCENT2, height=1).pack(side="left", fill="x",
                                                expand=True, padx=(8, 0), pady=6)

    def _field(self, parent, label, variable, side="top"):
        wrap = tk.Frame(parent, bg=BG_MAIN)
        wrap.pack(side=side, fill="x", expand=True)
        tk.Label(wrap, text=label, font=("Helvetica", 10, "bold"),
                 bg=BG_MAIN, fg=TEXT_DIM).pack(anchor="w")
        entry = tk.Entry(wrap, textvariable=variable,
                         bg=BG_FIELD, fg=TEXT_LIGHT,
                         insertbackground=TEXT_LIGHT,
                         relief="flat", font=("Helvetica", 12),
                         bd=0, highlightthickness=2,
                         highlightbackground=BG_FIELD,
                         highlightcolor=ACCENT)
        entry.pack(fill="x", ipady=7, pady=(2, 0))

    def _button(self, parent, text, color, command):
        return tk.Button(
            parent, text=text, command=command,
            bg=color, fg=BTN_TEXT, activebackground=color,
            activeforeground=BTN_TEXT,
            font=("Helvetica", 12, "bold"),
            relief="flat", bd=0, cursor="hand2",
            pady=12
        )

    # ── Actions ────────────────────────────────────
    def clear_form(self):
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.gender_var.set("Male")
        for var in self.unit_vars.values():
            var.set(False)
        self.status_var.set("Form cleared.")

    def submit_form(self):
        first = self.first_name_var.get().strip()
        last  = self.last_name_var.get().strip()

        # ── Validation ────────────────────────────
        if not first or not last:
            messagebox.showwarning("Missing Info", "Please enter both first and last name.")
            return

        selected_units = [k for k, v in self.unit_vars.items() if v.get()]
        if not selected_units:
            messagebox.showwarning("No Units", "Please select at least one unit.")
            return

        # ── Build data dict ───────────────────────
        data = {
            "first_name":  first,
            "last_name":   last,
            "gender":      self.gender_var.get(),
            "total_units": len(selected_units),
            **{k: int(v.get()) for k, v in self.unit_vars.items()}
        }

        # ── Try DB insert; fall back to local log ─
        if MYSQL_AVAILABLE:
            success = insert_student(data)
            if success:
                self._show_success(data, db_saved=True)
        else:
            # Demo mode — print to console & show summary
            print(f"\n[{datetime.now():%Y-%m-%d %H:%M:%S}] New registration (demo mode):")
            for k, v in data.items():
                print(f"  {k}: {v}")
            self._show_success(data, db_saved=False)

    def _show_success(self, data, db_saved):
        units_list = [
            label for label, key in zip(self.UNITS, self.UNIT_KEYS)
            if data[key]
        ]
        mode = "✅ Saved to MySQL database." if db_saved else "ℹ️  Demo mode — not saved to DB."
        msg = (
            f"Registration Successful!\n\n"
            f"Name   : {data['first_name']} {data['last_name']}\n"
            f"Gender : {data['gender']}\n"
            f"Units  : {', '.join(units_list)}\n"
            f"Total  : {data['total_units']} unit(s)\n\n"
            f"{mode}"
        )
        messagebox.showinfo("Success", msg)
        self.status_var.set(
            f"Last registered: {data['first_name']} {data['last_name']} "
            f"— {data['total_units']} unit(s)"
        )
        self.clear_form()


# ─────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────
if __name__ == "__main__":
    app = StudentSignupApp()
    app.mainloop()