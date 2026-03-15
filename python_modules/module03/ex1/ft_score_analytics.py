#!/usr/bin/env python3
from sys import argv


def ft_score_analytics():
    if len(argv) > 1:
        scores = []
        for i in argv[1:]:
            try:
                scores.append(int(i))
            except ValueError:
                return print("Arguments can only be scores")
        print("=== Player Score Analytics ===")
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(argv) - 1}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    else:
        print("=== Player Score Analytics ===")
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              "<score1> <score2> ...")


ft_score_analytics()
