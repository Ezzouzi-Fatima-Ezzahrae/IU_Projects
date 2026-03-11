import pytest
from datetime import datetime, timedelta
from domain.habit import Habit


def test_add_completion():
    habit = Habit("Drink Water", "Health", "daily")

    habit.add_completion()

    assert habit.get_marked_off_count() == 1


def test_last_completion():
    habit = Habit("Read", "Mind", "daily")

    time = datetime(2025, 1, 1)
    habit.add_completion(time)

    assert habit.get_last_completion() == time


def test_current_streak_daily():
    habit = Habit("Study", "Mind", "daily")

    habit.add_completion(datetime.now() - timedelta(days=2))
    habit.add_completion(datetime.now() - timedelta(days=1))
    habit.add_completion(datetime.now())

    assert habit.get_current_streak() == 3


def test_longest_streak():
    habit = Habit("Workout", "Fitness", "daily")

    habit.add_completion(datetime(2025,1,1))
    habit.add_completion(datetime(2025,1,2))
    habit.add_completion(datetime(2025,1,3))

    assert habit.get_longest_streak() == 3


def test_is_broken_daily():
    habit = Habit("Meditation", "Mind", "daily")

    habit.add_completion(datetime.now() - timedelta(days=3))

    assert habit.is_broken() is True


def test_edit_habit_name():
    habit = Habit("Run", "Fitness", "daily")

    habit.edit("name", "Morning Run")

    assert habit.name == "Morning Run"