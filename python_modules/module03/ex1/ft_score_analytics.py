#!/usr/bin/env python3
from sys import argv

"""
=== Player Score Analytics ===
Scores processed: [1500, 2300, 1800, 2100, 1950]
Total players: 5
Total score: 9650
Average score: 1930.0
High score: 2300
Low score: 1500
Score range: 800
$> python3 ft_score_analytics.py
=== Player Score Analytics ===
No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...
"""


def ft_score_analytics():
    if len(argv) > 1:
        print("=== Player Score Analytics ===")
        print(f"Total players: {len(argv) - 1}")
        scores = []
        for i in argv[1:]:
            try:
                scores.append(int(i))
            except ValueError:
                return print("Arguments can only be scores")
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
