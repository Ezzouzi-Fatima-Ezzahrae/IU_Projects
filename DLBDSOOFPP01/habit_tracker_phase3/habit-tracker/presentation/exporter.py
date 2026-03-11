from datetime import datetime

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
