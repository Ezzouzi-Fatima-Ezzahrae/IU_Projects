import sys
import os

# Make project root importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from habit import Habit
from datetime import datetime, timedelta


def test_new_habit_starts_active():
    h = Habit("Study", "School", "daily")
    assert h.state == "Active"


def test_checkoff_adds_completion():
    h = Habit("Study", "School", "daily")
    today = datetime.today()
    h.add_completion(today)
    assert any(c.date() == today.date() for c in h.completions)


def test_streak_increases():
    h = Habit("Study", "School", "daily")

    today = datetime.today()
    h.add_completion(today)
    h.add_completion(today - timedelta(days=1))
    h.add_completion(today - timedelta(days=2))

    assert h.get_streak() == 3


def test_breaking_streak_changes_state():
    h = Habit("Study", "School", "daily")

    h.add_completion(datetime.today() - timedelta(days=2))
    h.update_state(datetime.today())

    assert h.state == "At Risk"
"""What this proves:

habits start Active

completions get stored

streak math works

missing days change state

This is behavioral correctness."""