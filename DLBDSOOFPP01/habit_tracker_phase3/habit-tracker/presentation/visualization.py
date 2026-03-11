import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import timedelta
import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for better compatibility


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
