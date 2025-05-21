import datetime
def write_log(filepath, message):
    with open(filepath, 'a') as f:
        f.write(f"{datetime.datetime.now()}: {message}\n")
