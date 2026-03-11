import pytest
from infrastructure.storage import Storage
from domain.habit import Habit
from datetime import datetime


def test_add_habit(tmp_path):
    db = tmp_path / "test.db"

    storage = Storage(str(db))

    habit = Habit("Run", "Fitness", "daily")

    habit_id = storage.add_habit(habit)

    assert habit_id is not None


def test_get_all_habits(tmp_path):
    db = tmp_path / "test.db"

    storage = Storage(str(db))

    habit = Habit("Read", "Mind", "daily")
    storage.add_habit(habit)

    habits = storage.get_all_habits()

    assert len(habits) == 1
    assert habits[0].name == "Read"


def test_add_completion(tmp_path):
    db = tmp_path / "test.db"

    storage = Storage(str(db))

    habit = Habit("Drink Water", "Health", "daily")

    habit_id = storage.add_habit(habit)

    storage.add_completion(habit_id, datetime.now())

    completions = storage.get_completions(habit_id)

    assert len(completions) == 1


def test_delete_habit(tmp_path):
    db = tmp_path / "test.db"

    storage = Storage(str(db))

    habit = Habit("Gym", "Fitness", "weekly")

    habit_id = storage.add_habit(habit)

    storage.delete_habit(habit_id)

    habits = storage.get_all_habits()

    assert len(habits) == 0