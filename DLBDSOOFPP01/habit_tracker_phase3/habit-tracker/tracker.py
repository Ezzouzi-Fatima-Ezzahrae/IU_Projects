from habit import Habit
from analytics import (
    get_all_habits,
    get_habits_by_periodicity,
    get_longest_streak_all,
    get_longest_streak_for_habit
)


class HabitTracker:
    """
    Central controller of the habit tracking system.
    """

    def __init__(self, storage):
        self.storage = storage

    # -----------------------------
    # Creation
    # -----------------------------

    def create_habit(self, name, category, frequency, duration=None):
        """
        Create a new habit and store it.
        """
        habit = Habit(
            #habit_id=None,
            name=name,
            category=category,
            frequency=frequency,
            duration=duration,
           # created_at=None
        )
        habit_id = self.storage.add_habit(habit)
        habit.id = habit_id
       

    # -----------------------------
    # Check-off
    # -----------------------------

    def check_off(self, habit_name):
        """
        Mark a habit as completed.
        """
        habits = self.storage.get_all_habits()
        habit = next((h for h in habits if h.name == habit_name), None)

        if not habit:
            raise ValueError("Habit not found")

        habit.add_completion()
        self.storage.add_completion(habit.id, habit.completions[-1])

    # -----------------------------
    # Querying
    # -----------------------------

    def get_all_habits(self):
        """
        Return all habits.
        """
        habits = self.storage.get_all_habits()
        return get_all_habits(habits)
    
    def get_current_streak_for_habit(self, habit_name):
        habits = self.storage.get_all_habits()

        for habit in habits:
            if habit.name == habit_name:
                return habit.get_current_streak()

        return 0
    def get_broken_habits(self):
        habits = self.storage.get_all_habits()
        return [h for h in habits if h.is_broken()]


    def get_habits_by_periodicity(self, freq):
        """
        Return habits filtered by frequency.
        """
        habits = self.storage.get_all_habits()
        return get_habits_by_periodicity(habits, freq)

    def get_longest_streak_all(self):
        """
        Return the longest streak among all habits.
        """
        habits = self.storage.get_all_habits()
        return get_longest_streak_all(habits)

    def get_longest_streak_for_habit(self, name):
        """
        Return the longest streak for one habit.
        """
        habits = self.storage.get_all_habits()
        return get_longest_streak_for_habit(habits, name)
    

    def edit_habit(self,habit_name,answer,new_value):
        habits=self.storage.get_all_habits()
        
        for habit in habits:
            if  habit.name.strip().lower() == habit_name.strip().lower():

                habit.edit(answer,new_value)
                self.storage.update_habit(habit.id,answer,new_value)
                return True
            
        return False     
   # User asks → Habit found → object updated → database updated
    def delete_habit(self,habit_name):
        habits=self.storage.get_all_habits()
        for habit in habits:
            if habit.name.strip().lower() == habit_name.strip().lower():
               
                self.storage.delete_habit(habit.id)
                return True
        return False    

        
"""

clean API that users understand
for edit : 
User edits name
  ↓
Tracker finds correct habit (case-safe)
  ↓
Habit object updated
  ↓
SQLite row updated using habit.id
  ↓
Next time habits are loaded → correct name appears

"""