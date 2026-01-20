import sqlite3
from habit import Habit
from datetime import datetime


sqlite3.register_adapter(datetime, lambda d: d.isoformat())
sqlite3.register_converter("timestamp", lambda s: datetime.fromisoformat(s.decode()))

class Storage: 
    """
    Handles all persistence using SQLite.
 
    """

    def __init__(self, db_name="habits.db"):
       
        self.conn = sqlite3.connect(
        db_name,check_same_thread=False,     # tells SQLite:“I know what I’m doing — allow multi-thread access”
        detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
        )
        self.create_tables()

    # -------------------------
    # Schema
    # -------------------------

    def create_tables(self):

        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            category TEXT,
            frequency TEXT,
            created_at TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS completions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER,
            completed_at TIMESTAMP,
            FOREIGN KEY (habit_id) REFERENCES habits(id)
        )
        """
                        )

        self.conn.commit()

    # -------------------------
    # Habit Operations
    # -------------------------

    def add_habit(self, habit):
        """
        Insert a new habit into the database.
        """

        if not habit.name or not habit.frequency:
          raise ValueError("Habit must have a name and frequency")

        cursor = self.conn.cursor()
        try:
          cursor.execute("""          
               INSERT INTO habits (name, category, frequency, created_at)
               VALUES (?, ?, ?, ?)
        """, (
            habit.name,
            habit.category,
            habit.frequency,
            habit.created_at   
                      )
        )

          self.conn.commit()
          return cursor.lastrowid
        except sqlite3.IntegrityError:
            return None

    def get_all_habits(self):
        """
        Load all habits and their completions.
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM habits")
        habit_rows = cursor.fetchall()

        habits = []

        for row in habit_rows:
            habit_id, name, category, frequency, created_at = row

            completions = self.get_completions(habit_id)

            habit = Habit(
               
                name=name,
                category=category,
                frequency=frequency,
                created_at=created_at
            )
            habit.id=habit_id
            habit.completions = completions
            habits.append(habit)


        return habits

    # -------------------------
    # Completion Operations
    # -------------------------

    def add_completion(self, habit_id, completed_at):
        """
        Store a habit completion.
        """
        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO completions (habit_id, completed_at)
        VALUES (?, ?)
        """, (habit_id, completed_at))

        self.conn.commit()

    def get_completions(self, habit_id):
        """
        Get all completion timestamps for a habit.
        """
        cursor = self.conn.cursor()

        cursor.execute("""
        SELECT completed_at FROM completions
        WHERE habit_id = ?
        ORDER BY completed_at
        """, (habit_id,))

        rows = cursor.fetchall()

        return [datetime.fromisoformat(row[0]) for row in rows]
    
    def update_habit(self, habit_id, answer, new_value):  # Edit operation
        cursor = self.conn.cursor()
        if answer not in ("name", "category", "frequency"):
           raise ValueError("Invalid field")

        query = f"UPDATE habits SET {answer} = ? WHERE id = ?"
        cursor.execute(query, (new_value, habit_id))
        self.conn.commit()


    def delete_habit(self, habit_id): # delete from storage 
        cursor = self.conn.cursor()

        cursor.execute("""
        DELETE FROM completions
        WHERE habit_id = ?
        """, (habit_id,))

        cursor.execute("""
        DELETE FROM habits
        WHERE id = ?
        """, (habit_id,))

        self.conn.commit()


