ATM Management System

A simple and professional Python-based ATM Management System designed to simulate basic ATM operations through a command-line interface.

The project allows users to select an account, authenticate using a PIN, and perform common banking operations such as withdrawal, deposit, and balance checking. It also provides both English and Hindi language options.

Features :

* English & Hindi Interface — Use the ATM in either English or Hindi.
* Two Account Types — Supports Saving Account and Current Account.
* PIN Authentication — A PIN is required before performing transactions or checking balance.
* Cash Withdrawal — Withdraw money while following the account’s withdrawal limit and available balance.
* Cash Deposit — Deposit money into the selected account.
* Balance Checking — View the current account balance after PIN verification.
* Menu Navigation — Easily move between account operations and return to the main menu.
* Exit Option — Safely exit the ATM system when finished.

Account Details :

Account	Initial            Balance	               Withdrawal Limit
Saving Account	           ₹50,000	                    ₹10,000
Current Account	           ₹1,50,000	                  ₹25,000

Demo PIN: 2401

These values are predefined in the program for demonstration purposes.

How the System Works :

1. The program displays the ATM welcome screen.
2. The user selects English, Hindi, or Exit.
3. The user selects either a Saving Account or Current Account.
4. The user chooses an operation:
    * Withdraw
    * Deposit
    * Check Balance
    * Back
5. The system verifies the user’s PIN.
6. If the PIN is correct, the requested operation is performed.
7. The updated balance is displayed where applicable.
8. The user can continue with another transaction or exit the system.

Technologies Used :

* Python 3
* Command-Line Interface (CLI)
* match-case
* while loops
* Conditional statements
* Variables and arithmetic operations
* User input handling

Project Structure :

ATM-Management-System/
│
├── ATM_Management_System_Professional.py
└── README.md

How to Run :

1. Install Python

Make sure Python 3.10 or newer is installed on your computer.

Check the installation:

python --version

2. Clone the Repository

git clone https://github.com/TanishTiwari/ATM-Management-System.git

3. Open the Project Folder

cd ATM-Management-System

4. Run the Program

python ATM_Management_System_Professional.py

Important Note :

This is an educational ATM simulation, not a real banking application. Account balances and the PIN are stored directly in the Python program, so changes are not permanently saved after the program is closed.

For a real-world system, features such as database storage, encrypted PINs, transaction history, user accounts, and stronger security would be required.

Future Improvements :

Possible future versions can include:

* Database integration
* Multiple customer accounts
* Transaction history
* PIN change functionality
* Fund transfer
* Mini statement generation
* Secure PIN encryption
* Account lock after multiple incorrect PIN attempts
* Graphical User Interface (GUI)

Author ---

Tanish Tiwari

Project: ATM Management System
Language: Python
Type: Educational / Console-Based Application
