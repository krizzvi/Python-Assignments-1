def add_expense(tracker, day, amount):
    tracker[day] = tracker.get(day, 0) + amount

def weekly_summary(tracker):
    return sum(tracker.values())
