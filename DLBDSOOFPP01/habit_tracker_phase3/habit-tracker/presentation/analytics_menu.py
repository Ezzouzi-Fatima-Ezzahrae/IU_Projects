# analytics_menu.py
from presentation.display import print_habits_compact
from presentation.exporter import export_habits_to_html
from presentation.visualization import plot_habit_progress
from utils.clear_screen import clear_screen
from datetime import datetime

def show_analytics_menu(tracker):
    while True:
        print("\n📊  Analytics  📊")
        print("1. Show all habits (Compact view)")
        print("2. Export habits to HTML table")
        print("3. Habit progress over time")
        print("4. Show broken habits")
        print("5. Show current streak for all habits")
        print("6. Show habits by frequency")
        print("7. Show longest streak (all habits)")
        print("8. Show longest streak (specific habit)")
        print("0. Back")
        choice = input("👉 Choose: ").strip()

        if choice == "1":
            clear_screen()
            habits = tracker.get_all_habits()
            print_habits_compact(habits)
            input("\nPress Enter to continue...")

        elif choice == "2":
            habits = tracker.get_all_habits()
            export_habits_to_html(habits)
            input("\nPress Enter to continue...")

        elif choice == "3":
            habits = tracker.get_all_habits()
            if not habits:
                print("No habits found. Create some first!")
            else:
                print("\nAvailable habits:")
                for idx, h in enumerate(habits, 1):
                    print(f"{idx}. {h.name}")
                habit_choice = input("\nEnter habit number or name: ").strip()
                selected_habit = None
                try:
                    idx = int(habit_choice) - 1
                    if 0 <= idx < len(habits):
                        selected_habit = habits[idx]
                except ValueError:
                    for h in habits:
                        if h.name.lower() == habit_choice.lower():
                            selected_habit = h
                            break
                if selected_habit:
                    plot_habit_progress(selected_habit)
                else:
                    print("❌ Habit not found.")
            input("\nPress Enter to continue...")

        elif choice == "4":  # Broken habits
            broken = tracker.get_broken_habits()
            if not broken:
                print("✓ No broken habits! Keep it up 💪")
            else:
                print(f"❌ {len(broken)} broken habit(s):")
                for h in broken:
                    last = h.get_last_completion()
                    last_date = last.strftime("%Y/%m/%d") if last else "Never"
                    period = "daily" if h.frequency=="daily" else "weekly"
                    print(f"  • {h.name} ({period}) - Last completed: {last_date}")
            input("\nPress Enter to continue...")

        elif choice == "5":  # Current streaks
            for h in tracker.get_all_habits():
                print(f"{h.name}: {h.get_current_streak()}")
            input("\nPress Enter to continue...")

        elif choice == "6":  # Habits by frequency
            freq = input("Enter frequency (daily/weekly): ").strip().lower()
            habits = tracker.get_habits_by_periodicity(freq)
            if habits:
                print_habits_compact(habits)
            else:
                print(f"No {freq} habits found.")
            input("\nPress Enter to continue...")

        elif choice == "7":  # Longest streak (all)
            habits = tracker.get_all_habits()
            if habits:
                longest = max(habits, key=lambda h: h.get_longest_streak())
                print(f"🏆 Longest streak: {longest.get_longest_streak()} ({longest.name})")
            else:
                print("No habits found.")
            input("\nPress Enter to continue...")

        elif choice == "8":  # Longest streak (specific)
            name = input("Habit name: ").strip()
            print(f"Longest streak: {tracker.get_longest_streak_for_habit(name)}")
            input("\nPress Enter to continue...")

        elif choice == "0":
            break

        else:
            print("⚠️ Invalid option. Please try again.")