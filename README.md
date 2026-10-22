# Inventory Pro v3 (Advanced OOP System) 

A robust, console-based inventory management application built in Python, designed to showcase advanced **Object-Oriented Programming (OOP)** principles, clean architecture, and reliable input validation.

## Key Features
- **Inheritance & Polymorphism:** A base `Product` class extended by specialized subclasses (`Electronic`, `PerishableProduct`), utilizing `super()` and dynamic method overriding (`get_details`).
- **Strict Encapsulation:** Protected attributes safely controlled through `@property` getters and setters.
- **Composition-Based Management:** A dedicated `Inventory` class maintaining session state and handling business logic.
- **Robust Interactive CLI:** Clean user interface powered by infinite loops (`while`), modern conditional routing (`match-case`), and error handling (`try-except`) to prevent runtime crashes.

## Technologies
- Python 3.x
