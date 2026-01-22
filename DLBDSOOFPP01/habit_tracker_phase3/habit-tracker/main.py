from tracker import HabitTracker
from storage import Storage
from predefined import PredefinedHabitsLoader
from datetime import datetime
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for better compatibility


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def export_habits_to_html(habits, filename="habits_report.html"):
    """
    Export habits to an HTML file with formatted table.
    """
    if not habits:
        print("No habits to export.")
        return
    
    try:
        html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Habit Tracker Report</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 10px;
        }
        .date {
            text-align: center;
            color: #666;
            margin-bottom: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th {
            background-color: #4CAF50;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: bold;
            border: 1px solid #ddd;
        }
        td {
            padding: 10px 12px;
            border: 1px solid #ddd;
            text-align: left;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #f0f0f0;
        }
        .daily {
            background-color: #e3f2fd;
        }
        .weekly {
            background-color: #f3e5f5;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Habit Tracker Report</h1>
        <p class="date">Generated on: """ + datetime.now().strftime("%B %d, %Y at %H:%M") + """</p>
        
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Category</th>
                    <th>Frequency</th>
                    <th>Duration</th>
                    <th>Start Date</th>
                    <th>Marked off</th>
                    <th>Last Completed</th>
                    <th>Current Streak</th>
                    <th>Longest Streak</th>
                </tr>
            </thead>
            <tbody>
"""
        
        for habit in habits:
            habit_dict = habit.to_dict()
            
            last_completed = (
                habit_dict["last_completed"].strftime("%Y/%m/%d")
                if habit_dict["last_completed"]
                else "—"
            )
            
            duration_str = str(habit_dict["duration"]) if habit_dict["duration"] else "—"
            freq_class = habit_dict["frequency"].lower()
            
            html_content += f"""                <tr class="{freq_class}">
                    <td><strong>{habit_dict["name"]}</strong></td>
                    <td>{habit_dict["category"]}</td>
                    <td>{habit_dict["frequency"].capitalize()}</td>
                    <td>{duration_str}</td>
                    <td>{habit_dict["start_date"]}</td>
                    <td>{habit_dict["marked_off"]}</td>
                    <td>{last_completed}</td>
                    <td><strong>{habit_dict["streak"]}</strong></td>
                    <td><strong>{habit_dict["longest_streak"]}</strong></td>
                </tr>
"""
        
        html_content += """            </tbody>
        </table>
    </div>
</body>
</html>"""
        
        with open(filename, 'w', encoding='utf-8') as htmlfile:
            htmlfile.write(html_content)
        
        print(f"✓ Habits exported to '{filename}' successfully!")
        print(f"   Open the file in your browser to view the formatted table.")
        return filename
    except Exception as e:
        print(f"❌ Error exporting habits: {e}")


def print_habits_compact(habits):
    """
    Display habits in a simple, compact format without table wrapping.
    """
    if not habits:
        print("No habits found.")
        return
    
    print("\n📋 YOUR HABITS:\n")
    print(f"{'#':<3} {'Name':<15} {'Category':<10} {'Freq':<7} {'Days':<5} {'Current':<8} {'Best':<6}")
    print("=" * 65)
    
    for idx, habit in enumerate(habits, 1):
        habit_dict = habit.to_dict()
        duration_str = str(habit_dict["duration"]) if habit_dict["duration"] else "—"
        freq_short = "D" if habit_dict["frequency"] == "daily" else "W"
        
        print(
            f"{idx:<3} {habit_dict['name']:<15} {habit_dict['category']:<10} "
            f"{freq_short:<7} {duration_str:<5} {habit_dict['streak']:<8} "
            f"{habit_dict['longest_streak']:<6}"
        )


def plot_habit_progress(habit, filename=None):
    """
    Create a line chart showing cumulative completions over time for a specific habit.
    """
    if not habit.completions:
        print(f"No completion data for {habit.name}.")
        return
    
    try:
        from datetime import datetime, timedelta
        
        # Sort completions by date
        dates = sorted(set(c.date() for c in habit.completions))
        
        if not dates:
            print(f"No completion data for {habit.name}.")
            return
        
        # Calculate cumulative completions
        cumulative = []
        count = 0
        date_range = []
        
        # Create a continuous date range from first to last completion
        end_date = dates[-1]
        current = dates[0]
        
        while current <= end_date:
            date_range.append(current)
            if current in dates:
                count += 1
            cumulative.append(count)
            current += timedelta(days=1)
        
        # Create figure and axis
        fig, ax = plt.subplots(figsize=(14, 6))
        
        # Plot the cumulative line
        ax.plot(date_range, cumulative, linewidth=2.5, color='#4CAF50', marker='o', markersize=6, alpha=0.8)
        ax.fill_between(date_range, cumulative, alpha=0.3, color='#4CAF50')
        
        # Customize chart
        ax.set_xlabel('Date', fontsize=12, fontweight='bold')
        ax.set_ylabel('Cumulative Completions', fontsize=12, fontweight='bold')
        ax.set_title(f'Progress Over Time: {habit.name}', fontsize=14, fontweight='bold', pad=20)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Format x-axis to show dates nicely
        ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
        plt.xticks(rotation=45, ha='right')
        
        # Add statistics box
        total_completions = len(habit.completions)
        unique_days = len(dates)  # Count unique days, not total completions
        days_active = (dates[-1] - dates[0]).days + 1
        completion_rate = (unique_days / days_active * 100) if days_active > 0 else 0
        
        stats_text = f'Total: {total_completions} | Unique Days: {unique_days} | Days Active: {days_active} | Rate: {completion_rate:.1f}%'
        ax.text(0.5, 0.95, stats_text, transform=ax.transAxes, 
               ha='center', va='top', fontsize=10, 
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        # Adjust layout
        plt.tight_layout()
        
        # Save if filename provided
        if filename:
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"\n✓ Progress chart saved as '{filename}'")
        else:
            default_filename = f"{habit.name.replace(' ', '_')}_progress.png"
            plt.savefig(default_filename, dpi=300, bbox_inches='tight')
            print(f"\n✓ Progress chart saved as '{default_filename}'")
        
        # Display the figure
        plt.show()
        
    except Exception as e:
        print(f"❌ Error creating progress chart: {e}")
        import traceback
        traceback.print_exc()


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
        print("📋 1. Show all habits (Compact view)")
        print("📊 2. Export habits to HTML table")
        print("📈 3. Habit Progress Over Time")
        print("💔 4. Show broken habits")
        print("🔥 5. Show current streak for all habits")
        print("⏱️  6. Show habits by frequency")
        print("🏆 7. Show longest streak (all)")
        print("🎯 8. Show longest streak (specific)")
        print("↩️  0. Back")

        choice = input("👉 Choose: ").strip()

        if choice == "1":
            clear_screen()
            print("Those are all habits :")
            habits = tracker.get_all_habits()
            if habits:
                print_habits_compact(habits)
            else:
                print("No habits found.")
            input("\nPress Enter to continue...")
            
        elif choice == "2":
            habits = tracker.get_all_habits()
            export_habits_to_html(habits)
            input("\nPress Enter to continue...")
            
        elif choice == "3":
            habits = tracker.get_all_habits()
            if not habits:
                print("No habits found. Create some habits first!")
            else:
                print("\nAvailable habits:")
                for idx, h in enumerate(habits, 1):
                    print(f"{idx}. {h.name}")
                
                try:
                    habit_choice = input("\nEnter habit number or name: ").strip()
                    
                    # Try to match by number first
                    selected_habit = None
                    try:
                        idx = int(habit_choice) - 1
                        if 0 <= idx < len(habits):
                            selected_habit = habits[idx]
                    except ValueError:
                        # Try to match by name
                        for h in habits:
                            if h.name.lower() == habit_choice.lower():
                                selected_habit = h
                                break
                    
                    if selected_habit:
                        print(f"\nGenerating progress chart for '{selected_habit.name}'...")
                        plot_habit_progress(selected_habit)
                    else:
                        print("❌ Habit not found.")
                except Exception as e:
                    print(f"❌ Error: {e}")
            
            input("\nPress Enter to continue...")
            
        elif choice == "4":    
            print("\n💔 Broken Habits Analysis:\n")
            broken_habits = tracker.get_broken_habits()
            
            if not broken_habits:
                print("✓ Great news! No broken habits!")
                print("\nAll your habits are up to date:")
                all_habits = tracker.get_all_habits()
                for h in all_habits:
                    last_completed = h.get_last_completion()
                    if last_completed:
                        last_date = last_completed.strftime("%Y/%m/%d")
                        print(f"  • {h.name}: Last completed on {last_date}")
                    else:
                        print(f"  • {h.name}: Never completed")
            else:
                print(f"Found {len(broken_habits)} broken habit(s):\n")
                for h in broken_habits:
                    last_completed = h.get_last_completion()
                    last_date = last_completed.strftime("%Y/%m/%d") if last_completed else "Never"
                    period = "daily" if h.frequency == "daily" else "weekly"
                    print(f"  ❌ {h.name} ({period})")
                    print(f"     Last completed: {last_date}")
                    print()
            
            input("Press Enter to continue...")

        elif choice == "5":
            habits = tracker.get_all_habits()
            for h in habits:
                print(f"{h.name}: {h.get_current_streak()}")
            input("\nPress Enter to continue...")

        elif choice == "6":
            freq = input("daily or weekly: ")
            habits = tracker.get_habits_by_periodicity(freq)
            for h in habits:
                print(h)
            input("\nPress Enter to continue...")

        elif choice == "7":
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
            

        elif choice == "8":
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
            duration = input("Duration (in days): ")
            
            # Convert duration to int, or None if empty
            try:
                duration = int(duration) if duration.strip() else None
            except ValueError:
                duration = None
            
            tracker.create_habit(name, category, frequency, duration)
            
            # Display enhanced feedback
            freq_display = "Daily" if frequency.lower() == "daily" else "Weekly"
            print()
            print(f"✅ Habit \"{name}\" created successfully!")
            if duration:
                print(f"📅 Scheduled for: {duration} days")
            print(f"🎯 Frequency: {freq_display}")
            print()
            input("↩️  Press Enter to return to dashboard...")

        # ---- CHECK OFF HABIT ----
        elif choice == "2":
            name = input("Habit name to check off: ")
            try:
                tracker.check_off(name)
                
                # Get the habit to display details
                habits = tracker.get_all_habits()
                habit = next((h for h in habits if h.name == name), None)
                
                # Display enhanced feedback
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                current_streak = habit.get_current_streak() if habit else 0
                
                print()
                print("✅ Check Off Habit")
                print("────────────────────────────────────────")
                print()
                print(f"Habit name: {name}")
                print()
                print(f"⏰ Timestamp: {timestamp}")
                print()
                print(f"🎉 Habit \"{name}\" checked off!")
                print("Keep going 💪")
                print()
                if habit:
                    streak_unit = "day" if current_streak == 1 else "days"
                    print(f"Current Streak: {current_streak} {streak_unit}")
                print()
            except ValueError as e:
                print(e)
            input("↩️  Press Enter to return to dashboard...")

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
