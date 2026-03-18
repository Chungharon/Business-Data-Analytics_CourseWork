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



   CREATE DATABASE IF NOT EXISTS student_db;
   USE student_db;

   CREATE TABLE IF NOT EXISTS users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       first_name VARCHAR(50) NOT NULL,
       last_name VARCHAR(50) NOT NULL,
       contact_number VARCHAR(15) NOT NULL,
       email VARCHAR(100) UNIQUE NOT NULL,
       password VARCHAR(255) NOT NULL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );

   CREATE TABLE IF NOT EXISTS students (
       id INT AUTO_INCREMENT PRIMARY KEY,
       user_id INT,
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
       registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       FOREIGN KEY (user_id) REFERENCES users(id)
   );

3. Update DB_CONFIG below with your MySQL credentials.
4. Run this script: python student_signup.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


DB_CONFIG = {
    "host":     "localhost",
    "user":     "root",        
    "password": "dse8084/2021", 
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


def register_user(data: dict) -> bool:
    """Insert a new user into the users table."""
    sql = """
        INSERT INTO users (first_name, last_name, contact_number, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(contact_number)s, %(email)s, %(password)s)
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as exc:
        messagebox.showerror("Signup Error", f"Email might already be registered.\nDetails: {exc}")
        return False

def login_user(email, password) -> Optional[dict]:
    """Verify user credentials and return user info if successful."""
    sql = "SELECT id, first_name, last_name FROM users WHERE email = %s AND password = %s"
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, (email, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user
    except Exception as exc:
        messagebox.showerror("Login Error", str(exc))
        return None

def insert_student(data: dict) -> bool:
    """
    Insert a student record into the MySQL table.
    Returns True on success, False on failure.
    """
    sql = """
        INSERT INTO students
            (user_id, first_name, last_name, gender,
             unit_math, unit_science, unit_english,
             unit_history, unit_cs, unit_art, total_units)
        VALUES
            (%(user_id)s, %(first_name)s, %(last_name)s, %(gender)s,
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

BG_MAIN    = "#1B2A4A"   
BG_CARD    = "#243559"   
BG_FIELD   = "#2E4270"   
ACCENT     = "#4A90D9"   
ACCENT2    = "#5BC0BE"   
TEXT_LIGHT = "#EAF0FB"  
TEXT_DIM   = "#8FA8CC" 
BTN_SUBMIT = "#4A90D9"
BTN_CLEAR  = "#E05C5C"
BTN_TEXT   = "#FFFFFF"


# ─────────────────────────────────────────
# Auth Application (Login/Signup)
# ─────────────────────────────────────────

class AuthApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Portal - Login")
        self.geometry("450x650")
        self.resizable(False, False)
        self.configure(bg=BG_MAIN)
        
        self.is_login_mode = True
        self._build_ui()

    def _build_ui(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Header
        header = tk.Frame(self, bg=ACCENT, pady=20)
        header.pack(fill="x")
        title_text = "Login" if self.is_login_mode else "Sign Up"
        tk.Label(header, text=title_text, font=("Helvetica", 22, "bold"), bg=ACCENT, fg=BTN_TEXT).pack()
        
        body = tk.Frame(self, bg=BG_MAIN, padx=40, pady=30)
        body.pack(fill="both", expand=True)

        if not self.is_login_mode:
            # First & Last Name
            name_row = tk.Frame(body, bg=BG_MAIN)
            name_row.pack(fill="x", pady=(0, 15))
            
            self.fn_var = tk.StringVar()
            self._field(name_row, "First Name", self.fn_var, side="left")
            tk.Frame(name_row, bg=BG_MAIN, width=15).pack(side="left")
            self.ln_var = tk.StringVar()
            self._field(name_row, "Last Name", self.ln_var, side="left")

            # Contact Number
            self.contact_var = tk.StringVar()
            self._field(body, "Contact Number", self.contact_var)
            tk.Frame(body, bg=BG_MAIN, height=15).pack()

        # Email
        self.email_var = tk.StringVar()
        self._field(body, "Email Address", self.email_var)
        tk.Frame(body, bg=BG_MAIN, height=15).pack()

        # Password
        self.pass_var = tk.StringVar()
        self._field(body, "Password", self.pass_var, show="*")
        tk.Frame(body, bg=BG_MAIN, height=25).pack()

        # Action Button
        btn_text = "LOGIN" if self.is_login_mode else "REGISTER"
        cmd = self.handle_login if self.is_login_mode else self.handle_signup
        tk.Button(body, text=btn_text, command=cmd, bg=ACCENT, fg=BTN_TEXT,
                  font=("Helvetica", 12, "bold"), relief="flat", pady=12, cursor="hand2").pack(fill="x")

        # Toggle mode
        toggle_text = "Don't have an account? Sign Up" if self.is_login_mode else "Already have an account? Login"
        tk.Button(body, text=toggle_text, command=self.toggle_mode, bg=BG_MAIN, fg=ACCENT2,
                  font=("Helvetica", 10), relief="flat", cursor="hand2", activebackground=BG_MAIN, activeforeground=ACCENT).pack(pady=20)

    def _field(self, parent, label, variable, side="top", show=None):
        wrap = tk.Frame(parent, bg=BG_MAIN)
        wrap.pack(side=side, fill="x", expand=True)
        tk.Label(wrap, text=label, font=("Helvetica", 10, "bold"), bg=BG_MAIN, fg=TEXT_DIM).pack(anchor="w")
        entry = tk.Entry(wrap, textvariable=variable, show=show, bg=BG_FIELD, fg=TEXT_LIGHT, relief="flat", 
                         font=("Helvetica", 12), bd=0, highlightthickness=2, highlightbackground=BG_FIELD, highlightcolor=ACCENT)
        entry.pack(fill="x", ipady=7, pady=(2, 0))

    def toggle_mode(self):
        self.is_login_mode = not self.is_login_mode
        self.title(f"Student Portal - {'Login' if self.is_login_mode else 'Sign Up'}")
        self._build_ui()

    def handle_signup(self):
        data = {
            "first_name": self.fn_var.get().strip(),
            "last_name": self.ln_var.get().strip(),
            "contact_number": self.contact_var.get().strip(),
            "email": self.email_var.get().strip(),
            "password": self.pass_var.get()
        }
        if not all(data.values()):
            messagebox.showwarning("Incomplete", "Please fill in all fields.")
            return
        
        if register_user(data):
            messagebox.showinfo("Success", "Account created! Please login.")
            self.toggle_mode()

    def handle_login(self):
        email = self.email_var.get().strip()
        password = self.pass_var.get()
        
        user = login_user(email, password)
        if user:
            self.destroy() # Close login window
            StudentSignupApp(user).mainloop()
        else:
            messagebox.showerror("Failed", "Invalid email or password.")

# ─────────────────────────────────────────
# Main Application Dashboard
# ─────────────────────────────────────────

class StudentSignupApp(tk.Tk):
    UNITS = ["Mathematics", "Science", "English", "History", "Computer Science", "Art"]
    UNIT_KEYS = ["math", "science", "english", "history", "cs", "art"]

    def __init__(self, user):
        super().__init__()
        self.user = user
        self.title("Student Registration Portal - Dashboard")
        self.geometry("680x820")
        self.resizable(False, False)
        self.configure(bg=BG_MAIN)

        # ── Variables ──────────────────────────────
        self.first_name_var = tk.StringVar(value=user['first_name'])
        self.last_name_var  = tk.StringVar(value=user['last_name'])
        self.gender_var     = tk.StringVar(value="Male")
        self.unit_vars      = {key: tk.BooleanVar() for key in self.UNIT_KEYS}

        self._build_ui()

    # ── UI Builder ─────────────────────────────────
    def _build_ui(self):
        # ── Header ────────────────────────────────
        header = tk.Frame(self, bg=ACCENT, pady=18)
        header.pack(fill="x")
        tk.Label(header, text="🎓  Student Dashboard",
                 font=("Helvetica", 20, "bold"),
                 bg=ACCENT, fg=BTN_TEXT).pack()
        tk.Label(header, text=f"Welcome back, {self.user['first_name']}! Select your units below.",
                 font=("Helvetica", 10),
                 bg=ACCENT, fg="#D0E4FF").pack()

        # ── Scrollable body ───────────────────────
        body = tk.Frame(self, bg=BG_MAIN, padx=40, pady=20)
        body.pack(fill="both", expand=True)

        # ── Personal Details card ─────────────────
        self._section(body, "Profile Info")

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
            value="⚡ MySQL: " + ("Connected" if MYSQL_AVAILABLE else "Database Offline")
        )
        status_color = ACCENT2 if MYSQL_AVAILABLE else "#E05C5C"
        tk.Label(body, textvariable=self.status_var,
                 font=("Helvetica", 9, "italic"),
                 bg=BG_MAIN, fg=status_color).pack(anchor="w", pady=(0, 14))

        # ── Buttons ───────────────────────────────
        btn_frame = tk.Frame(body, bg=BG_MAIN)
        btn_frame.pack(fill="x")

        self._button(btn_frame, "✖  Clear",  BTN_CLEAR,  self.clear_form).pack(side="left",  expand=True, fill="x", padx=(0, 10))
        self._button(btn_frame, "✔  Save Units",       BTN_SUBMIT, self.submit_form).pack(side="right", expand=True, fill="x", padx=(10, 0))

        # ── Footer ────────────────────────────────
        tk.Label(self,
                 text="©️ 2026 Student Portal  |  Secure Login Enabled",
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
        # We don't clear name as it's from profile
        self.gender_var.set("Male")
        for var in self.unit_vars.values():
            var.set(False)
        self.status_var.set("Form cleared.")

    def submit_form(self):
        selected_units = [k for k, v in self.unit_vars.items() if v.get()]
        if not selected_units:
            messagebox.showwarning("No Units", "Please select at least one unit.")
            return

        # ── Build data dict ───────────────────────
        data = {
            "user_id":     self.user['id'],
            "first_name":  self.first_name_var.get().strip(),
            "last_name":   self.last_name_var.get().strip(),
            "gender":      self.gender_var.get(),
            "total_units": len(selected_units),
            **{k: int(v.get()) for k, v in self.unit_vars.items()}
        }

        # ── Try DB insert ──
        if MYSQL_AVAILABLE:
            success = insert_student(data)
            if success:
                self._show_success(data, db_saved=True)
        else:
            self._show_success(data, db_saved=False)

    def _show_success(self, data, db_saved):
        units_list = [
            label for label, key in zip(self.UNITS, self.UNIT_KEYS)
            if data[key]
        ]
        mode = "Saved to your profile." if db_saved else "Demo mode — not saved."
        msg = (
            f"Registration Successful!\n\n"
            f"Name   : {data['first_name']} {data['last_name']}\n"
            f"Gender : {data['gender']}\n"
            f"Units  : {', '.join(units_list)}\n"
            f"Total  : {data['total_units']} unit(s)\n\n"
            f"{mode}"
        )
        messagebox.showinfo("Success", msg)
        self.status_var.set(f"Units saved for {data['first_name']}.")
        # self.clear_form() # Optional: keep data visible


# ─────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────

if __name__ == "__main__":
    auth = AuthApp()
    auth.mainloop()