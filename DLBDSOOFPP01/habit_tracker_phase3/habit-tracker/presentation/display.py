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
