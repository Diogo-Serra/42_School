#!/usr/bin/env python3

import random
import time


def game_event_stream(total_events):
    """Yield game events one by one (streaming, no big list in memory)."""
    scripted_events = [
        {"player": "alice", "level": 5, "action": "killed monster"},
        {"player": "bob", "level": 12, "action": "found treasure"},
        {"player": "charlie", "level": 8, "action": "leveled up"},
]
    for event in scripted_events[:total_events]:
        yield event

    players = [
        "alice", "bob", "charlie", "diana", "eve",
        "frank", "grace", "henry", "ivy", "jack",
    ]
    actions = [
        "killed monster", "found treasure", "leveled up", "completed quest"
    ]

    for _ in range(len(scripted_events), total_events):
        yield {
            "player": random.choice(players),
            "level": random.randint(1, 20),
            "action": random.choice(actions),
        }


def filter_events(event_stream, condition):
    """Yield only events that satisfy the given condition."""
    for event in event_stream:
        if condition(event):
            yield event


def process_stream(event_stream):
    """Process a stream and return analytics without storing all events."""
    total_events = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0
    for event in event_stream:
        total_events += 1
        if total_events <= 3:
            print(
                f"Event {total_events}: Player {event['player']} "
                f"(level {event['level']}) {event['action']}"
            )
        if event["level"] >= 10:
            high_level_players += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        if event["action"] == "leveled up":
            level_up_events += 1

    print("...")
    return {
        "total_events": total_events,
        "high_level_players": high_level_players,
        "treasure_events": treasure_events,
        "level_up_events": level_up_events,
    }


def fibonacci_stream():
    """Infinite Fibonacci generator."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_stream():
    """Infinite prime number generator (simple trial division)."""
    number = 2
    while True:
        is_prime = True
        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            yield number
        number += 1


def take_first(generator, count):
    """Read the first N values from a generator."""
    values = []
    for _ in range(count):
        values.append(next(generator))
    return values


def main():
    print("=== Game Data Stream Processor ===")
    total_events = 1000
    print(f"Processing {total_events} game events...")

    random.seed(42)
    start = time.time()
    analytics = process_stream(game_event_stream(total_events))
    elapsed = time.time() - start

    print("=== Stream Analytics ===")
    print(f"Total events processed: {analytics['total_events']}")
    print(f"High-level players (10+): {analytics['high_level_players']}")
    print(f"Treasure events: {analytics['treasure_events']}")
    print(f"Level-up events: {analytics['level_up_events']}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {elapsed:.3f} seconds")

    # Small comparison to show list storage vs stream processing.
    events_list = list(game_event_stream(total_events))
    _ = sum(1 for event in events_list if event["action"] == "found treasure")
    _ = sum(
        1
        for event in filter_events(
            game_event_stream(total_events),
            lambda event: event["action"] == "found treasure",
        )
    )

    print("=== Generator Demonstration ===")
    fib_values = take_first(fibonacci_stream(), 10)
    prime_values = take_first(prime_stream(), 5)
    print(f"Fibonacci sequence (first 10): {', '.join(map(str, fib_values))}")
    print(f"Prime numbers (first 5): {', '.join(map(str, prime_values))}")


if __name__ == "__main__":
    main()
