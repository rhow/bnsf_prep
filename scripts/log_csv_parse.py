from collections import Counter

log = [
    "2024-11-01T12:00:00Z alice LOGIN",
    "2024-11-01T12:04:00Z bob LOGIN",
    "2024-11-01T12:10:00Z alice LOGOUT",
    "2024-11-01T12:00:00Z alice LOGIN",
    "2024-11-01T12:04:00Z bob LOGIN",
    "2024-11-01T12:10:00Z alice LOGOUT",
    "2024-11-01T12:00:00Z alice LOGIN",
    "2024-11-01T12:04:00Z bob LOGIN",
    "2024-11-01T12:10:00Z alice LOGOUT",
    "2024-11-01T12:00:00Z alice LOGIN",
    "2024-11-01T12:04:00Z bob LOGIN",
    "2024-11-01T12:10:00Z alice LOGOUT",
]


def event_count_counter(input: list) -> dict:
    events = [line.split(" ")[2] for line in input]

    return Counter(events)

def event_count(input: list) -> dict:
    events = {}

    for e in input:
        tokens = e.split(" ")
        e = tokens[2]
        events[e] = events.get(e, 0) + 1

    return events


results = event_count_counter(log)
print(results)
