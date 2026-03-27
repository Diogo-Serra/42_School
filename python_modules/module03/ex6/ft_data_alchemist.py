#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print(f"Initial list of players: {players}")

    capitalized_players = [player.capitalize() for player in players]
    print(
        f"New list with all names capitalized: {capitalized_players}"
    )

    already_capitalized = [player for player in players if player.istitle()]
    print(f"New list of capitalized names only: {already_capitalized}")

    score_dict = {
        player: random.randint(0, 1000) for player in capitalized_players
    }
    print(f"Score dict: {score_dict}")

    score_average = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {score_average}")

    high_scores = {
        player: score
        for player, score in score_dict.items()
        if score > score_average
    }
    print(f"High scores: {high_scores}")


main()
