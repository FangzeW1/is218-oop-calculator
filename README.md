# OOP Calculator

This project is a command-line calculator written in Python using object-oriented programming. It supports addition and subtraction, maintains a calculation history, allows calculations to be removed from history, and handles invalid user inputs.

# Setup

Clone the repository and enter the project directory:

```bash
git clone git@github.com:FangzeW1/is218-oop-calculator.git
cd is218-oop-calculator

# Create and Activate Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

# Install Required Packages
python -m pip install -r requirements.txt

# Run the Calculator
python -m calculator

Available commands are:
- add - Add two numbers
- subtract - Subtract the second number from the first
- history - Display calculation history
- remove - Remove a calculation from history
- help - Display available commands
- exit - Exit the calculator

#Run the Tests
python -m pytest

# Continuous Integration
GitHub Actions runs the test suite in a fresh Ubuntu environment using Python 3.11, 3.12, 3.13, and 3.14. This verifies that the calculator and its tests work across the required Python versions.

# REFLECTION

# Where would Multiply Belong?
Multiply would be another calculation class alongside Add and Subtract. It would implement the same calculation interface and provide its own get_result() behavior. The CLI would need to register the new multiply command and include it in the help text. Tests would also be added to verify multiplication results and its use through the CLI. History would not need any multiplication-specific logic because it stores Calculation objects through their common interface. It does not need to know which particular operation each object performs.

# What contract could email and text-message notification objects share through send()?
Email and text-message notification objects could share a common notification interface that requires a send() method. Each class could implement send() differently while other parts of the program could work with either notification through the same interface.

# What design knowledge transfers to another language?
Object-oriented ideas such as abstraction, encapsulation, inheritance, polymorphism, and separating responsibilities can transfer to other programming languages. Testing principles and designing classes around clear interfaces can also transfer. However, I would still need to learn the new language's syntax and runtime rules, such as how it handles classes, interfaces, exceptions, types, and packages.

