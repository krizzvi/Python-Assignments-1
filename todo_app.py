import os
def load_tasks(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r') as f:
        lines = f.readlines()
    return [eval(line.strip()) for line in lines]

def save_tasks(filepath, tasks):
    with open(filepath, 'w') as f:
        for task in tasks:
            f.write(str(task) + "\n")
