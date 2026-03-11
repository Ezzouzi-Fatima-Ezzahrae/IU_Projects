from domain.habit import Habit
from domain.analytics import (
    get_all_habits,
    get_broken_habits,
    get_habits_by_periodicity,
    get_longest_streak_for_habit,
    get_longest_streak_all
)
from datetime import datetime, timedelta


def test_get_all_habits():
    habits = [
        Habit("Read", "Mind", "daily"),
        Habit("Gym", "Fitness", "weekly")
    ]

    result = get_all_habits(habits)

    assert len(result) == 2


def test_get_habits_by_periodicity():
    habits = [
        Habit("Read", "Mind", "daily"),
        Habit("Gym", "Fitness", "weekly")
    ]

    daily = get_habits_by_periodicity(habits, "daily")

    assert len(daily) == 1
    assert daily[0].name == "Read"


def test_get_broken_habits():
    habit = Habit("Drink Water", "Health", "daily")

    habit.add_completion(datetime.now() - timedelta(days=3))

    habits = [habit]

    broken = get_broken_habits(habits)

    assert len(broken) == 1


def test_get_longest_streak_for_habit():
    habit = Habit("Study", "Mind", "daily")

    habit.add_completion(datetime(2025,1,1))
    habit.add_completion(datetime(2025,1,2))
    habit.add_completion(datetime(2025,1,3))

    result = get_longest_streak_for_habit([habit], "Study")

    assert result == 3


def test_get_longest_streak_all():
    habit1 = Habit("Read", "Mind", "daily")
    habit2 = Habit("Gym", "Fitness", "weekly")

    habit1.add_completion(datetime(2025,1,1))
    habit1.add_completion(datetime(2025,1,2))

    habit2.add_completion(datetime(2025,1,1))

    result = get_longest_streak_all([habit1, habit2])

    assert result == 2