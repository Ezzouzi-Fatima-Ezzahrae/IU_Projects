from application.tracker import HabitTracker
from infrastructure.storage import Storage
from application.predefined import PredefinedHabitsLoader

from presentation.exporter import export_habits_to_html
from presentation.visualization import plot_habit_progress
from presentation.display import print_habits_compact
from presentation.analytics_menu import show_analytics_menu

from utils.clear_screen import clear_screen
from datetime import datetime

def show_menu(tracker):
    print("\n=== 🌱 Daily Check-in Dashboard 🌱 ===\n")

    habits = tracker.get_all_habits()

    if habits:
        print_habits_compact(habits)

        total = len(habits)
        completed_today = sum(
            1 for h in habits 
            if any(c.date() == datetime.today().date() for c in h.completions)
        )

        print(f"\n📊 Summary: {completed_today}/{total} habits completed today")

    else:
        print("⚠️ No habits yet.\n")

    print("\nActions:")
    print("➕  1. Create a new habit")
    print("✅  2. Check off a habit")
    print("📊  3. Analytics")
    print("✏️   4. Edit habit")
    print("🗑️   5. Delete habit")
    print("🚪  0. Exit")

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
        clear_screen()  # <-- Clear before showing the menu
    
        show_menu(tracker)
        choice = input("Choose an option: ").strip()

        if choice == "1":  # Create habit
            clear_screen()  # <-- Clear before creating habit
            name = input("Habit name: ")
            category = input("Category: ")
            frequency = input("Frequency (daily/weekly): ")
            duration = input("Duration (in days, optional): ").strip()
            duration = int(duration) if duration else None
            tracker.create_habit(name, category, frequency, duration)
            print(f"\n✅ Habit '{name}' created! Frequency: {frequency.capitalize()}, Duration: {duration or '∞'} days")
            input("↩️ Press Enter to return to dashboard...")

        elif choice == "2":  # Check off habit
            clear_screen()  # <-- Clear before checking off habit
            name = input("Habit name to check off: ")
            try:
                tracker.check_off(name)
                habit = next((h for h in tracker.get_all_habits() if h.name == name), None)
                print(f"\n✅ {name} checked off! Current streak: {habit.get_current_streak() if habit else 0}")
            except ValueError as e:
                print(e)
            input("↩️ Press Enter to return to dashboard...")

        elif choice == "3":  # Analytics
            clear_screen()  # <-- Clear before entering analytics menu
            
            show_analytics_menu(tracker)

        elif choice == "4":  # Edit habit
            clear_screen()  # <-- Clear before editing habit
            name = input("Habit name: ")
            field = input("Edit (name/category/frequency): ").strip()
            value = input("New value: ").strip()
            if tracker.edit_habit(name, field, value):
                print("✏️ Habit updated.")
            else:
                print("❌ Habit not found.")
            input("↩️ Press Enter to return to dashboard...")

        elif choice == "5":  # Delete habit
            clear_screen()  # <-- Clear before deleting habit
            name = input("Habit name: ")
            if tracker.delete_habit(name):
                print("🗑️ Habit deleted.")
            else:
                print("❌ Habit not deleted.")
            input("↩️ Press Enter to go back...")

        elif choice == "0":
            clear_screen()  # <-- Clear before exiting
            print("\n🌟 Thanks for using Habit Tracker! Goodbye!")
            break

        else:
            print("⚠️ Invalid option. Please try again.")
            input("\n↩️ Press Enter to return to dashboard...")
            
if __name__ == "__main__":
    main()