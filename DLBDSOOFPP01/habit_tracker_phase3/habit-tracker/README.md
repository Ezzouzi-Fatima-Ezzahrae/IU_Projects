# Habit-tracking-application 

<h2> IU projects </h2>

# Habit Tracking App (Python Backend)

A command-line habit tracking application built with Python.
It helps users build consistency by tracking habits, managing streaks,
and analyzing long-term behavior using clean, testable logic.

The application focuses on core habit tracking functionality and does not include any
graphical user interface.

---

## Features

- Create and manage multiple habits
- Support for daily and weekly habit periodicity
- Check off habits at any point in time
- Automatic detection of broken habits
- Streak tracking based on consecutive completed periods
- Functional analytics module providing:
  - A list of all tracked habits
  - A list of habits by periodicity
  - The longest streak across all habits
  - The longest streak for a specific habit
- Persistent storage using SQLite
- Command Line Interface (CLI) for user interaction

---

## Project Structure


```
habit-tracker/
├── analytics.py     # Functional analytics module
├── habit.py         # Habit class (core habit logic)
├── tracker.py       # Application controller
├── storage.py       # SQLite persistence layer
├── predefined.py    # Predefined habits and test data
├── main.py          # CLI entry point
├── habits.db        # SQLite database (auto-generated)
├── tests/
│   ├── test_habit.py
│   ├── test_analytics.py
│   └── test_storage.py
├── requirements.txt
└── README.md

```

## Requirements

- Before to start make sure that you have Python 3.9+ on your device 

or you can download it: https://www.python.org/downloads/

- Git (optional, for version control)

- Visual Studio Code (recommended)

- pytest (for running tests)

- Important packages:

  pytest~=7.2.0 "pip install -U pytest"

- How to Run the Application

- From the project root directory, run:

  python main.py


## 🚀 Installation & Setup

1. Clone the repository:
   ```bash
      git clone  https://github.com/Fati03-AI/habit-tracking.git

## Predefined Habits and Test Data

On first startup, the application automatically loads 5 predefined habits:

- At least one daily habit

- At least one weekly habit

Each predefined habit includes example tracking data for a period of 4 weeks.
This data contains missed days and broken streaks and serves as a test fixture
for validating the analytics functionality.
  

## Habit Streak Logic

A habit must be completed at least once during its defined period:

- Daily habits must be completed once per day

- Weekly habits must be completed once every 7 days

If a habit is not completed within its period, the habit is considered broken
and the current streak resets to zero. A streak represents the number of
consecutive completed periods without breaking the habit.



# Contributing

This is my first Python project. Your feedback, ideas, and contributions are welcomed!

## License
This project is licensed under the MIT License.

## Author
Fatima Ezzahrae Ezzouzi
