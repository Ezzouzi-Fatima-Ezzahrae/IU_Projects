from datetime import datetime
import os

EXPORT_DIR = "exports"

def ensure_export_dir():
    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)


def export_habits_to_html(habits, filename=None):
    """
    Export habits to an HTML file with formatted table.
    """
    if not habits:
        print("No habits to export.")
        return
    
    try:
        ensure_export_dir()

        # ✅ Auto-generate filename with timestamp
        if filename is None:
            filename = f"habits_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

        filepath = os.path.join(EXPORT_DIR, filename)

        html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Habit Tracker Report</title>
    <style>
        body { font-family: Arial; background-color: #f5f5f5; margin: 20px; }
        .container { background: white; padding: 20px; border-radius: 8px; }
        table { width: 100%; border-collapse: collapse; }
        th { background: #4CAF50; color: white; padding: 10px; }
        td { padding: 8px; border: 1px solid #ddd; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Habit Tracker Report</h1>
        <p>Generated on: """ + datetime.now().strftime("%B %d, %Y at %H:%M") + """</p>
        <table>
            <tr>
                <th>Name</th>
                <th>Category</th>
                <th>Frequency</th>
                <th>Current Streak</th>
            </tr>
"""

        for habit in habits:
            h = habit.to_dict()
            html_content += f"""
            <tr>
                <td>{h['name']}</td>
                <td>{h['category']}</td>
                <td>{h['frequency']}</td>
                <td>{h['streak']}</td>
            </tr>
"""

        html_content += """
        </table>
    </div>
</body>
</html>
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"✓ Exported to {filepath}")
        return filepath

    except Exception as e:
        print(f"❌ Error exporting habits: {e}")