# 🌱 Habit Tracker Application - Complete Documentation

A command-line habit tracking application that helps users build consistency by tracking habits, managing streaks, and analyzing long-term behavior using clean, testable Python logic.

---

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Architecture & File Structure](#architecture--file-structure)
3. [Application Flow](#application-flow)
4. [Data Models](#data-models)
5. [Feature Breakdown](#feature-breakdown)
6. [Database Schema](#database-schema)
7. [Usage Guide](#usage-guide)

---

## Project Overview

**Purpose:** Build a habit tracking system that helps users maintain consistency through daily/weekly habit monitoring.

**Technology Stack:**
- **Language:** Python 3.14+
- **Database:** SQLite3
- **Visualization:** Matplotlib
- **Architecture Pattern:** MVC (Model-View-Controller)

**Key Features:**
- ✅ Create and manage multiple habits
- ✅ Track daily and weekly periodicity
- ✅ Check off completions anytime
- ✅ Automatic streak calculation
- ✅ Broken habit detection
- ✅ Progress visualization with charts
- ✅ HTML report export
- ✅ Persistent SQLite storage

---

## Architecture & File Structure

```
habit-tracker/
├── main.py                 # CLI interface & visualization
├── tracker.py              # Business logic controller
├── habit.py                # Habit model & core logic
├── storage.py              # SQLite persistence layer
├── analytics.py            # Functional analytics utilities
├── predefined.py           # Test fixtures & sample data
├── habits.db               # SQLite database (auto-created)
├── habits_report.html      # Generated HTML reports
├── tests/
│   ├── test_habit.py       # Unit tests for Habit class
│   ├── test_storage.py     # Unit tests for Storage
│   └── test_analytics.py   # Integration tests
├── __pycache__/            # Python cache
└── PROJECT_DOCUMENTATION.md  # This file

```

---

## Application Flow

### 1. Main Application Startup Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION START                        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │  Initialize Storage    │
        │  (SQLite DB: habits.db)│
        └────────────┬───────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │ Initialize HabitTracker│
        │  (Business Logic)      │
        └────────────┬───────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │ Load Predefined Habits │
        │  (5 sample habits)     │
        └────────────┬───────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │  Display Main Menu     │
        │  (Wait for user input) │
        └────────────┬───────────┘
                     │
         ┌───────────┼───────────┐
         │           │           │
         ▼           ▼           ▼
      (1)Create  (2)Check   (3)Analytics
      (4)Edit    (5)Delete  (0)Exit
```

### 2. User Interaction Flow

```
┌────────────────────────────────────────────────────────────┐
│              USER SELECTS OPTION FROM MENU                 │
└────────────────┬───────────────────────────────────────────┘
                 │
    ┌────────────┼────────────┬────────────┬─────────────┐
    │            │            │            │             │
    ▼            ▼            ▼            ▼             ▼
  CREATE       CHECK         EDIT        DELETE       ANALYTICS
   HABIT        OFF          HABIT        HABIT          MENU
    │            │            │            │             │
    ├─Input      ├─Input      ├─Input      ├─Input       ├─Display
    │ name       │ habit      │ habit      │ habit       │ options
    │ category   │ name       │ name       │ name        │
    │ frequency  │            ├─Choose    │             ├─Select
    │ duration   ├─Validate   │ field to  │ ├─Validate  │ view:
    │            │ habit      │ edit      │ │ habit     │ 1. Compact
    ├─Create     │            │ (name/    │ │           │ 2. HTML
    │ Habit obj  ├─Add        │ category/ │ ├─Delete    │ 3. Chart
    │            │ completion │ frequency)│ │ from DB   │ 4. Broken
    ├─Store in   │            │           │ │           │ 5. Streaks
    │ database   ├─Save to    ├─Validate ├─Success    │ 6. By freq
    │            │ database   │ new      │ message    │ 7. Longest
    └─Success    │            │ value    │             │ 8. Custom
      message    └─Update     │           └─Return to  └─Return to
                   Habit obj  ├─Update      menu        main menu
                   & database │ Habit obj
                   └─Return   ├─Save to
                     to menu   database
                              └─Return
                                to menu
```

### 3. Habit Completion Check-off Flow

```
┌──────────────────────────────────────┐
│  User enters: "Check off a habit"    │
└────────────┬─────────────────────────┘
             │
             ▼
    ┌────────────────────┐
    │ Get all habits     │
    │ from storage       │
    └────────┬───────────┘
             │
             ▼
    ┌────────────────────┐
    │ Display list of    │
    │ habit names        │
    └────────┬───────────┘
             │
             ▼
    ┌────────────────────┐
    │ User inputs        │
    │ habit name         │
    └────────┬───────────┘
             │
             ▼
    ┌────────────────────────┐
    │ Search for matching    │
    │ habit (case-insensitive)│
    └────────┬────────────────┘
             │
    ┌────────┴────────┐
    │                 │
    ▼                 ▼
 FOUND              NOT FOUND
   │                  │
   ▼                  ▼
Create         Show error
completion     message
timestamp      │
   │           ▼
   ▼        Return to
Add to      main menu
Habit obj
   │
   ▼
Save to
database
   │
   ▼
Show success
message
   │
   ▼
Return to
main menu
```

---

## Data Models

### Habit Class Structure

| Property | Type | Description |
|----------|------|-------------|
| `id` | Integer | Primary key (assigned by database) |
| `name` | String | Habit name (unique) |
| `category` | String | Category (e.g., "Health", "Fitness") |
| `frequency` | String | "daily" or "weekly" |
| `duration` | Integer | Expected duration in days |
| `created_at` | DateTime | When habit was created |
| `completions` | List[DateTime] | All completion timestamps |

### Habit Methods

| Method | Returns | Purpose |
|--------|---------|---------|
| `add_completion()` | None | Record a completion |
| `is_broken()` | Boolean | Check if missed its period |
| `get_current_streak()` | Integer | Consecutive periods completed |
| `get_longest_streak()` | Integer | Best streak ever achieved |
| `get_last_completion()` | DateTime | Most recent completion |
| `get_marked_off_count()` | Integer | Total completions |
| `to_dict()` | Dict | Convert to dictionary format |

---

## Database Schema

### Habits Table

```sql
CREATE TABLE habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    category TEXT,
    frequency TEXT,
    duration INTEGER,
    created_at TIMESTAMP
);
```

| Column | Type | Constraints | Purpose |
|--------|------|-------------|---------|
| `id` | INTEGER | PRIMARY KEY | Unique identifier |
| `name` | TEXT | UNIQUE | Habit name |
| `category` | TEXT | - | Classification |
| `frequency` | TEXT | - | "daily" or "weekly" |
| `duration` | INTEGER | - | Duration in days |
| `created_at` | TIMESTAMP | - | Creation date |

### Completions Table

```sql
CREATE TABLE completions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    habit_id INTEGER,
    completed_at TIMESTAMP,
    FOREIGN KEY (habit_id) REFERENCES habits(id)
);
```

| Column | Type | Constraints | Purpose |
|--------|------|-------------|---------|
| `id` | INTEGER | PRIMARY KEY | Record ID |
| `habit_id` | INTEGER | FOREIGN KEY | Links to habit |
| `completed_at` | TIMESTAMP | - | When completed |

---

## Feature Breakdown

### 1. Habit Creation

**Flow:**
```
User Input → Validate → Create Habit Object → Store in DB → Assign ID
```

**Data Collected:**
- Name (required, must be unique)
- Category (optional classification)
- Frequency (daily or weekly)
- Duration (in days)

**Validation:**
- Name and frequency are required
- Name must be unique
- Frequency must be "daily" or "weekly"

### 2. Habit Check-off

**Flow:**
```
Find Habit → Create Completion Timestamp → Add to Habit.completions → Save to DB
```

**Logic:**
- Records current datetime when habit is marked complete
- Multiple completions allowed per day
- Completions stored with habit_id reference

### 3. Streak Calculation

#### Current Streak Logic:

```python
For DAILY habits:
  step = 1 day
  Check: (today - last_completion) >= 1 day

For WEEKLY habits:
  step = 7 days
  Check: (today - last_completion) >= 7 days
```

**Flow:**
```
Get all completion dates (unique) → Sort → Walk backwards → Count consecutive periods

If broken (missed a period) → Reset to 0
Otherwise → Continue counting
```

**Example (Daily Habit):**
```
Completions: Jan 1, Jan 2, Jan 3, Jan 4, __ (Jan 5 MISSED)

Streak Status:
- Jan 4: streak = 4
- Jan 5: streak = 0 (broke the chain)
- Jan 6: streak = 1 (new chain started)
```

### 4. Broken Habit Detection

**Definition:** A habit is "broken" if it hasn't been completed within its required period.

```python
if (today - last_completion) >= step:
    habit.is_broken() = True
else:
    habit.is_broken() = False
```

| Frequency | Max Days Allowed | Triggers Broken When |
|-----------|-----------------|----------------------|
| Daily | 1 day | 2 days pass without completion |
| Weekly | 7 days | 8 days pass without completion |

### 5. Analytics & Visualization

#### Analytics Functions:

| Function | Input | Output | Purpose |
|----------|-------|--------|---------|
| `get_all_habits()` | List[Habit] | List[Habit] | Return all habits |
| `get_broken_habits()` | List[Habit] | List[Habit] | Filter broken ones |
| `get_habits_by_periodicity()` | habits, frequency | List[Habit] | Filter by daily/weekly |
| `get_longest_streak_all()` | List[Habit] | Integer | Best streak overall |
| `get_longest_streak_for_habit()` | habits, name | Integer | Best streak for one |

#### Progress Chart:

```
Generates matplotlib line chart showing:
- X-axis: Date range (first to last completion)
- Y-axis: Cumulative completions
- Statistics box: Total, Unique Days, Days Active, Completion Rate

Formula:
  Rate = (Unique Days / Days Active) × 100%
  
Example:
  Completed 28 days out of 28 available = 100%
  Completed 20 days out of 28 available = 71.4%
```

### 6. HTML Report Export

**Generated File:** `habits_report.html`

**Contents:**
- Professional styled table
- All habit information
- Current streak, longest streak
- Color-coded by frequency (daily=blue, weekly=purple)
- Timestamp of generation

---

## Feature Comparison Table

| Feature | Daily Habits | Weekly Habits |
|---------|------------|--------------|
| **Required Period** | 1 day | 7 days |
| **Completions Checked** | Every 24 hours | Every 7 days |
| **Streak Reset Trigger** | 2 days no completion | 8 days no completion |
| **Completion Count** | Can be multiple per day | Usually 1 per week |
| **Typical Examples** | Exercise, Meditation, Reading | Family call, Laundry |
| **Test Data (4 weeks)** | 28 days of data | 4 weeks of data |

---

## Predefined Test Data

**5 Sample Habits Loaded on Startup:**

| Habit | Type | Frequency | Duration | Missed Days | Test Pattern |
|-------|------|-----------|----------|-------------|--------------|
| Drink Water | Health | Daily | 30 days | [3, 10, 17] | 3 breaks |
| Read Book | Mind | Daily | 90 days | [5, 6, 20] | 3 breaks |
| Morning Walk | Fitness | Daily | 60 days | - | Every 2nd day |
| Gym | Fitness | Weekly | 60 days | - | All 4 weeks |
| Call Family | Social | Weekly | 90 days | Week 2 | Miss 1 week |

---

## Application Menu Flow

```
┌─────────────────────────────────────┐
│   MAIN MENU                         │
├─────────────────────────────────────┤
│ 1. Create a new habit               │
│ 2. Check off a habit                │
│ 3. Analytics                        │
│ 4. Edit habit                       │
│ 5. Delete habit                     │
│ 0. Exit                             │
└─────────────────────────────────────┘
         │
         └──────► ANALYTICS MENU ◄──────┐
                                         │
                    ┌─────────────────────────────────────┐
                    │ ANALYTICS SUBMENU                   │
                    ├─────────────────────────────────────┤
                    │ 1. Show all habits (Compact view)   │
                    │ 2. Export habits to HTML table      │
                    │ 3. Habit Progress Over Time         │
                    │ 4. Show broken habits               │
                    │ 5. Show current streak for all      │
                    │ 6. Show habits by frequency         │
                    │ 7. Show longest streak (all)        │
                    │ 8. Show longest streak (specific)   │
                    │ 0. Back to main menu                │
                    └─────────────────────────────────────┘
```

---

## Usage Guide

### Starting the Application

```bash
cd habit-tracker
python main.py
```

### Creating a Habit

```
Choose: 1
Habit name: Morning Jog
Category: Fitness
Frequency (daily/weekly): daily
Duration (in days): 60
✅ Habit created successfully.
```

### Checking Off a Habit

```
Choose: 2
Habit name to check off: Morning Jog
🎉 Habit checked off! Keep going 💪
```

### Viewing Analytics

```
Choose: 3
(Submenu appears)
Choose: 1        # View all habits
Choose: 2        # Export to HTML
Choose: 3        # View progress chart
Choose: 4        # See broken habits
... etc
```

### Editing a Habit

```
Choose: 4
Habit name: Morning Jog
Edit(name/category/frequency): frequency
new value: weekly
✏️ Habit updated.
```

### Deleting a Habit

```
Choose: 5
Habit name: Morning Jog
🗑️ Habit deleted.
```

---

## File Dependencies

```
main.py
├── imports: tracker, storage, predefined, datetime, os, matplotlib
├── uses: HabitTracker, Storage, PredefinedHabitsLoader
└── calls: All UI functions

tracker.py
├── imports: habit, analytics
├── uses: Habit class, analytics functions
└── provides: HabitTracker controller

habit.py
├── imports: datetime, timedelta
└── provides: Habit model with all logic

storage.py
├── imports: sqlite3, habit, datetime
├── uses: Habit class
└── manages: Database operations

analytics.py
├── imports: None (pure functions)
└── provides: Functional analytics utilities

predefined.py
├── imports: datetime, habit
├── uses: Habit class
└── provides: Test fixtures

tests/
├── test_habit.py: Tests Habit class
├── test_storage.py: Tests Storage layer
└── test_analytics.py: Tests analytics functions
```

---

## Data Flow Diagram

```
┌──────────────┐
│   User (CLI) │
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│   main.py        │
│  (UI & Display)  │
└──────┬───────────┘
       │
       ▼
┌──────────────────────┐
│   tracker.py         │
│  (Business Logic)    │
└──────┬───────────────┘
       │
    ┌──┴──┐
    │     │
    ▼     ▼
┌────────────┐  ┌────────────┐
│ habit.py   │  │analytics.py│
│ (Model)    │  │(Utilities) │
└────────────┘  └────────────┘
    │
    ▼
┌──────────────────┐
│   storage.py     │
│(Persistence)    │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│   habits.db      │
│  (SQLite DB)     │
└──────────────────┘
```

---

## State Transitions

### Habit Lifecycle

```
                    CREATE
                      │
                      ▼
    ┌─────────────────────────────────┐
    │  ACTIVE                         │
    │  (No missed periods)            │
    │                                 │
    │  Streak: Incrementing           │
    │  Status: Up to date             │
    └──────────┬──────────────────────┘
               │
        Missing period?
               │
               ▼
    ┌─────────────────────────────────┐
    │  BROKEN                         │
    │  (Missed required period)       │
    │                                 │
    │  Streak: Reset to 0             │
    │  Status: At Risk                │
    └──────────┬──────────────────────┘
               │
        Complete now?
               │
               ▼
    ┌─────────────────────────────────┐
    │  RECOVERING                     │
    │  (Rebuilding streak)            │
    │                                 │
    │  Streak: Starting fresh (1+)    │
    │  Status: Back on track          │
    └─────────────────────────────────┘
```

---

## Key Algorithms

### Streak Calculation

```python
def get_current_streak(self):
    if not self.completions:
        return 0
    
    dates = sorted(set(c.date() for c in self.completions))
    today = datetime.now().date()
    
    step = timedelta(days=1) if daily else timedelta(days=7)
    
    last_period = dates[-1]
    if today - last_period >= step:
        return 0  # Broken
    
    streak = 1
    current = last_period
    
    while (current - step) in dates:
        current -= step
        streak += 1
    
    return streak
```

### Longest Streak Calculation

```python
def get_longest_streak(self):
    if not self.completions:
        return 0
    
    dates = sorted(set(c.date() for c in self.completions))
    
    step = timedelta(days=1) if daily else timedelta(days=7)
    
    longest = 1
    current = 1
    
    for i in range(1, len(dates)):
        if dates[i] - dates[i-1] == step:
            current += 1
            longest = max(longest, current)
        else:
            current = 1
    
    return longest
```

---

## Summary Table

| Aspect | Details |
|--------|---------|
| **Language** | Python 3.14+ |
| **Database** | SQLite3 |
| **Architecture** | MVC Pattern |
| **Main Components** | 6 files + tests |
| **User Interface** | CLI (Command-line) |
| **Supported Frequencies** | Daily, Weekly |
| **Visualization** | Matplotlib charts |
| **Export Formats** | HTML reports |
| **Test Coverage** | Unit & Integration tests |
| **Data Persistence** | SQLite database |

---

## Getting Started Checklist

- [ ] Python 3.9+ installed
- [ ] Navigate to project directory
- [ ] Run: `python main.py`
- [ ] Predefined habits auto-loaded
- [ ] Start creating and tracking habits!

---

**Created:** January 21, 2026  
**Version:** 1.0  
**Author:** Fatima Ezzahrae Ezzouzi
