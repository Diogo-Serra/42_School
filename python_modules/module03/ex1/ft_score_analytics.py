#!/usr/bin/env python3
from sys import argv


def ft_score_analytics():
    if len(argv) > 1:
        scores = []
        for data in argv[1:]:
            try:
                score = int(data)
            except ValueError:
                print(f"Invalid score: '{data}'. Scores must be numbers")
                return
            scores.append(score)
        print("=== Player Score Analytics ===")
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores) - 1}")
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
