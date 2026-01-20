import sys
import os

# Make project root importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from storage import Storage
from predefined import PredefinedHabitsLoader
from analytics import (
    get_all_habits,
    get_habits_by_periodicity,
    get_longest_streak_all,
    get_longest_streak_for_habit
)


@pytest.fixture
def test_db():
    storage = Storage(":memory:")   # SQLite in RAM
    loader = PredefinedHabitsLoader()
    loader.load(storage)
    return storage


def test_get_all_habits(test_db):
    habits = get_all_habits(test_db.get_all_habits())
    assert len(habits) == 5


def test_daily_habits(test_db):
    habits = test_db.get_all_habits()
    daily = get_habits_by_periodicity(habits, "daily")
    assert len(daily) == 3


def test_weekly_habits(test_db):
    habits = test_db.get_all_habits()
    weekly = get_habits_by_periodicity(habits, "weekly")
    assert len(weekly) == 2


def test_longest_streak_all(test_db):
    habits = test_db.get_all_habits()
    longest = get_longest_streak_all(habits)
    assert longest > 0


def test_longest_streak_specific(test_db):
    habits = test_db.get_all_habits()
    streak = get_longest_streak_for_habit(habits, "Drink Water")
    assert streak >= 7
"""
Using :memory: makes tests:

fast /clean/independent/repeatable

No files. No pollution. No ghosts
| Requirement          | Where             |
| -------------------- | ----------------- |
| Functional analytics | analytics.py      |
| Test fixtures        | predefined.py     |
| Analytics tested     | test_analytics.py |
| No UI                | CLI only          |
| DB persistence       | sqlite3           |
| Daily & Weekly       | Yes               |
"""