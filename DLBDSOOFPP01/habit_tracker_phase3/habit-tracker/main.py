from tracker import HabitTracker
from storage import Storage
from predefined import PredefinedHabitsLoader


def show_menu():
    """
    Displays the main dashboard menu.
    """
    print("\n=== 🌱  Daily Check-in Dashboard  🌱  ===")
    print("➕  1. Create a new habit")
    print("✅  2. Check off a habit")
    print("📊  3. Analytics")
    print("✏️   4. Edit habit")
    print("🗑️   5. Delete habit")
    print("🚪  0. Exit")

def show_analytics_menu(tracker):
    while True:
        print("\n             📊  Analytics  📊     ")
        print("📋 1. Show all habits")
        print("💔  2. show broken habits: ")
        print("🔥 3. Show current streak for all habits")
        print("⏱️  4. Show habits by frequency")
        print("🏆 5. Show longest streak (all)")
        print("🎯 6. Show longest streak (specific)")
        print("↩️  0. Back")

        choice = input("👉 Choose: ").strip()

        if choice == "1":
            print("Those are all habits :")
            habits = tracker.get_all_habits()
            for h in habits:
                print(h)
            input("\nPress Enter to continue...")
            '''
        elif choice == "2":
            habits = tracker.get_all_habits()
            for h in habits:
                print(f"{h.name}: {h.get_broken_habits()}")
            input("\nPress Enter to continue...")    
            '''
        elif choice == "2":    
            print("💔 Broken habits:")
            for h in tracker.get_broken_habits():
                print(h.name)
            input("\nPress Enter to continue...")

        elif choice == "3":
            habits = tracker.get_all_habits()
            for h in habits:
                print(f"{h.name}: {h.get_current_streak()}")
            input("\nPress Enter to continue...")

        elif choice == "3":
            freq = input("daily or weekly: ")
            habits = tracker.get_habits_by_periodicity(freq)
            for h in habits:
                print(h)
            input("\nPress Enter to continue...")

        elif choice == "4":
            habits = tracker.get_all_habits()
            if not habits:
               print("No habits found.")
            else:
                  # Find the habit with the longest streak
                longest_habit = max(habits, key=lambda h: h.get_longest_streak())
                print(
                    f"🏆 Longest streak: {longest_habit.get_longest_streak()}🏆 "
                    f"({longest_habit.name})"
                )
                input("\nPress Enter to continue...")
            

        elif choice == "5":
            name = input("Habit name: ")
            print("Longest streak:", tracker.get_longest_streak_for_habit(name))
            input("\nPress Enter to continue...")

        elif choice == "0":
            break   # 👈 goes back to main menu




def main():
    """
    Entry point of the application.
    """

    # 1. Initialize storage (SQLite database)
    storage = Storage()

    # 2. Initialize tracker (controller)
    tracker = HabitTracker(storage)

    # 3. Load predefined habits (only once at startup)
    loader = PredefinedHabitsLoader()
    loader.load(storage)

    # 4. Start the main interaction loop
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        # ---- CREATE HABIT ----
        if choice == "1":
            name = input("Habit name: ")
            category = input("Category: ")
            frequency = input("Frequency (daily/weekly): ")
            tracker.create_habit(name, category, frequency)
            print("✅ Habit created successfully.")
            input("\n↩️ Press Enter to return to dashboard...")

        # ---- CHECK OFF HABIT ----
        elif choice == "2":
            name = input("Habit name to check off: ")
            try:
                tracker.check_off(name)
                print("🎉 Habit checked off! Keep going 💪")
            except ValueError as e:
                print(e)
            input("\n↩️ Press Enter to return to dashboard...")

        # ---- Analytics ----
        
        elif choice == "3":
             show_analytics_menu(tracker)

        
        #-----Edit a habit ----
        elif choice=="4":
            name=input("Habit name:")
            answer=input("Edit(name/category/frequency):")
            new_value=input("new value:")
 
            if tracker.edit_habit(name,answer,new_value):
               print("✏️ Habit updated.")
            else:
               print("❌ Habit not found.")
            input("\n↩️Press Enter to return to dashboard...")
   
         #-----Delete a habit ----
        elif choice=="5":
            name=input("Habit name:")
        
            if tracker.delete_habit(name):
               print("🗑️ Habit deleted.")
            else:
               print("❌ Habit not deleted.")
            input("\n↩️ Press Enter to go back...")


        # ---- EXIT ----
        elif choice == "0":
            print("\n🌟 Thanks for using the Habit Tracker!")
            print("👋 Goodbye — see you tomorrow!")
            break

        # ---- INVALID INPUT ----
        else:
            print("⚠️ Invalid option. Please try again.")


# Required Python entry point
if __name__ == "__main__":
    main()
