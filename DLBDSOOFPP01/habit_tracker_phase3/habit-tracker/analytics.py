
"""
Analytics module
Pure functional analytics on habit data.

"""
def get_all_habits(habits):
    """
    Return all tracked habits.
    """
    
    return habits

def get_broken_habits(habits):
    return list(filter(lambda h: h.is_broken(), habits))

def get_habits_by_periodicity(habits, frequency):
    """
    Return habits filtered by frequency ('daily' or 'weekly').
    """
    return [h for h in habits if h.frequency == frequency]


def get_longest_streak_for_habit(habits, habit_name):
    """
    Return the longest streak for a specific habit.
    """
    for habit in habits:
        if habit.name == habit_name:
            return habit.get_longest_streak()
    return 0


def get_longest_streak_all(habits):
    """
    Return the longest streak among all habits.
    """
    return max((h.get_longest_streak() for h in habits),default=0)


