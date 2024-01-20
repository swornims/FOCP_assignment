import sys


def file_validation(file):
    """Checks if the file contents can be opened else returns an error."""
    try:
        with open(file, 'r') as file:
            return file_analyze(file)
    except FileNotFoundError:
        print(f'Cannot open "{file}"!')


def file_analyze(file):
    our_cat_visits = 0
    other_cat_visits = 0
    total_time = 0
    visit_duration = []

    for line in file:
        if line == 'END':
            break

        cat_type, entry, exit = line.strip().split(',')
        duration = int(exit) - int(entry)

        if cat_type[0] == 'O':
            our_cat_visits += 1
            total_time += duration
            visit_duration.append(duration)
        elif cat_type[0] == 'T':
            other_cat_visits += 1

    average_duration = total_time / our_cat_visits
    longest_visit = max(visit_duration)
    shortest_visit = min(visit_duration)

    return print(f"""
Log File Analysis
==================

Cat Visits: {our_cat_visits}
Other Cats: {other_cat_visits}

Total Time in House: {total_time // 60} Hours, {total_time % 60} Minutes
Average Visit Length: {round(average_duration)} Minutes
Longest Visit: {longest_visit} Minutes
Shortest Visit: {shortest_visit} Minutes
    """)


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 0:
        print("Missing command line argument!")
    else:
        file_validation(args[0])
