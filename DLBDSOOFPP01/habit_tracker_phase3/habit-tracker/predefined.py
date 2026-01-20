from datetime import datetime, timedelta
from habit import Habit

class PredefinedHabitsLoader:
    """
    Loads predefined habits and 4 weeks 
    of tracking data into the system.
    This data is used as a test fixture 
    for analytics and validation.
    """

    def load(self, storage):
      # If habits already exist, do NOT insert again
            if len(storage.get_all_habits()) > 0:
              return
            habits = [
                     Habit("Drink Water", "Health", "daily"),
                     Habit("Read Book", "Mind", "daily"),
                     Habit("Morning Walk", "Fitness", "daily"),
                     Habit("Gym", "Fitness", "weekly"),
                     Habit("Call Family", "Social", "weekly")
                    ]


            habit_ids = {}

       
             # Store habits
            for habit in habits:
                habit_id = storage.add_habit(habit)
                habit_ids[habit.name] = habit_id

                today = datetime.today()

              # --- DAILY HABITS ---
            for i in range(28):   # 4 weeks
               day = today - timedelta(days=i)

               if i not in [3, 10, 17]:  # simulate missed days
                storage.add_completion(habit_ids["Drink Water"], day)

               if i not in [5, 6, 20]:
                storage.add_completion(habit_ids["Read Book"], day)

               if i % 2 == 0:   # walk every other day
                storage.add_completion(habit_ids["Morning Walk"], day)

        # --- WEEKLY HABITS ---
            for i in range(4):
               week = today - timedelta(days=i * 7)
  
               storage.add_completion(habit_ids["Gym"], week)

               if i != 2:   # miss one week
                  storage.add_completion(habit_ids["Call Family"], week)
"""| Requirement         | Fulfilled |
 | ------------------- | --------- |
  | 5 predefined habits | Yes       |
| Daily + weekly      | Yes       |
| 4 weeks of data     | Yes       |
| Missed days         | Yes       |
| Broken streaks      | Yes       |
| Streaks exist       | Yes       |
| Testable            | Yes       |
"""