#!/usr/bin/env python3
import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "use",
        "release",
    ]

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        yield events.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()
    for index in range(1000):
        player, action = next(event_stream)
        print(f"Event {index}: Player {player} did action {action}")

    event_stream = gen_event()
    events_list: list[tuple[str, str]] = []
    for _ in range(10):
        events_list.append(next(event_stream))
    print(f"Built list of 10 events: {events_list}")

    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")


main()
