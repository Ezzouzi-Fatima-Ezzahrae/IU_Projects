from datetime import datetime, timedelta


class Habit:
    """
    Represents a single habit 
    """

    def __init__(self, name,category, frequency,created_at=None):
        self.id = None                # assigned by Storage
        self.name = name 
        self.category = category 
        self.frequency = frequency 


        if isinstance(created_at, str):
            self.created_at = datetime.fromisoformat(created_at)
        else:
            self.created_at = created_at if created_at else datetime.now()   

        self.completions = []

    # -----------------------------
    # Completion logic
    # -----------------------------

    def add_completion(self, completion_time=None):
        """
        Marks this habit as completed at a given time.
        """
        if completion_time is None:
            completion_time = datetime.now()

        self.completions.append(completion_time)
        
    
    def is_broken(self,today=None):
         """
         Returns True if the habit was missed in at least one required period.
         """
         if not self.completions:
            return True

         if today is None:
            today = datetime.now().date()

         last_completion = max(c.date() for c in self.completions)

         step = timedelta(days=1) if self.frequency == "daily" else timedelta(days=7)

         return (today - last_completion) >= step
    # --------
    # EDIT
    # --------
    def edit(self,answer,new_value):
         if answer=="name":
          self.name=new_value
         elif answer=="category":
          self.category=new_value
         elif answer=="frequency":
          self.frequency=new_value    

    # CURRENT STREAK 
    # ---------------
    def get_current_streak(self):
        """
        Returns the current streak of consecutive completed periods.
        """
        if not self.completions:
           return 0

        dates = sorted(set(c.date() for c in self.completions))
        today = datetime.now().date()

        step = timedelta(days=1) if self.frequency == "daily" else timedelta(days=7)

        # Determine the last valid period
        last_period = dates[-1]

        # If the current period has no completion → streak = 0
        if today - last_period >= step:
            return 0

        streak = 1
        current = last_period

        # Walk backwards through consecutive periods
        while (current - step) in dates:
           current -= step
           streak += 1

        return streak

    def get_longest_streak(self):
       if not self.completions:
        return 0

       dates = sorted(set(c.date() for c in self.completions))

       step = timedelta(days=1) if self.frequency == "daily" else timedelta(days=7)

       longest = 1
       current = 1

       for i in range(1, len(dates)):
           if dates[i] - dates[i - 1] == step:
              current += 1
              longest = max(longest, current)
           else:
              current = 1
 
       return longest


   
    
    # -----------------------------
    # Utility
    # -----------------------------

    def to_dict(self):
        """
        Convert habit to dictionary for storage or analytics.
        """
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "frequency": self.frequency,
            "created_at": self.created_at,
            "completions": [c.isoformat() for c in self.completions]
        }
   
    def __str__(h):  #Turns a Habit object into pretty text , it makes CLI output readable & friendly 
        freq_icon = "📅 " if h.frequency == "daily" else "🗓️ "
        

        return(
                 f"   {h.name}\n"
            
                 f"   {freq_icon} {h.frequency.capitalize()} | 🏷️  {h.category}\n"
                 f"   🔥 Current streak: {h.get_current_streak()}\n"
                 f"   🏆 Longest streak: {h.get_longest_streak()}\n"
               )



    def __repr__(self):  # technical representation for debugging and logging 
       return self.__str__() 


   
 
"""
This class:

stores timestamps

supports daily and weekly habits

calculates streaks

works with SQLite

feeds analytics functions
"""