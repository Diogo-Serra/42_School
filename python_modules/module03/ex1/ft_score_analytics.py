#!/usr/bin/env python3
from sys import argv


def ft_score_analytics() -> None:

    if len(argv) > 1:
        scores: list[int] = []
        print("=== Player Score Analytics ===")

        for data in argv[1:]:
            try:
                score: int = int(data)
                scores.append(score)
            except ValueError:
                print(f"Invalid parameter: '{data}'")

        if not scores:
            return

        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    else:
        print("=== Player Score Analytics ===")
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")


ft_score_analytics()
