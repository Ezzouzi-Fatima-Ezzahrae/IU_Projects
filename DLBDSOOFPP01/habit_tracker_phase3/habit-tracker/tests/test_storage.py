import sys
import os

# Make project root importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from storage import Storage
from habit import Habit
from datetime import datetime


def test_store_and_load_habit():
    storage = Storage(":memory:")

    habit = Habit("Read", "Mind", "daily")
    storage.add_habit(habit)

    habits = storage.get_all_habits()
    assert len(habits) == 1
    assert habits[0].name == "Read"


def test_store_completion():
    storage = Storage(":memory:")

    habit = Habit("001","Drink Water", "Health", "daily")
    habit_id = storage.add_habit(habit)

    now = datetime.now()
    storage.add_completion(habit_id, now)

    completions = storage.get_completions(habit_id)
    assert len(completions) == 1
