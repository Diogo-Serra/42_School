#!/usr/bin/env python3
"""
Game Analytics Dashboard - Comprehensions Mastery
Demonstrates list, dict, and set comprehensions for data transformation
"""

# Sample gaming data
player_data = [
    {'name': 'alice', 'score': 2300, 'region': 'north', 'achievements': 5},
    {'name': 'bob', 'score': 1800, 'region': 'east', 'achievements': 3},
    {'name': 'charlie', 'score': 2150, 'region': 'central',
     'achievements': 7},
    {'name': 'diana', 'score': 2200, 'region': 'north', 'achievements': 4},
]

achievements_list = [
    ('alice', 'first_kill'),
    ('alice', 'level_10'),
    ('alice', 'boss_slayer'),
    ('bob', 'first_kill'),
    ('bob', 'level_10'),
    ('charlie', 'boss_slayer'),
    ('charlie', 'level_10'),
    ('charlie', 'first_kill'),
    ('diana', 'level_10'),
]


def main():
    """Run analytics dashboard with comprehensions"""
    print("=== Game Analytics Dashboard ===")

    # ========== LIST COMPREHENSIONS ==========
    print("=== List Comprehension Examples ===")

    # Filter: High scorers (>2000)
    high_scorers = [p['name'] for p in player_data if p['score'] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    # Transform: Double all scores
    doubled_scores = [p['score'] * 2 for p in player_data]
    print(f"Scores doubled: {doubled_scores}")

    # Filter: Players with score > 1900
    active_players = [p['name'] for p in player_data if p['score'] > 1900]
    print(f"Active players: {active_players}")

    # ========== DICT COMPREHENSIONS ==========
    print("=== Dict Comprehension Examples ===")

    # Map: player name -> score
    player_scores = {p['name']: p['score'] for p in player_data}
    print(f"Player scores: {player_scores}")

    # Categorize: Count players in score brackets
    score_brackets = {
        'high': len([p for p in player_data if p['score'] > 2100]),
        'medium': len([p for p in player_data
                       if 1900 < p['score'] <= 2100]),
        'low': len([p for p in player_data if p['score'] <= 1900]),
    }
    print(f"Score categories: {score_brackets}")

    # Count: Achievements per player
    achievement_count = {
        p['name']: sum(1 for player, _ in achievements_list
                       if player == p['name'])
        for p in player_data
    }
    print(f"Achievement counts: {achievement_count}")

    # ========== SET COMPREHENSIONS ==========
    print("=== Set Comprehension Examples ===")

    # Unique: All players
    unique_players = {p['name'] for p in player_data}
    print(f"Unique players: {unique_players}")

    # Unique: All achievements
    unique_achievements = {ach for player, ach in achievements_list}
    print(f"Unique achievements: {unique_achievements}")

    # Unique: All regions
    unique_regions = {p['region'] for p in player_data}
    print(f"Active regions: {unique_regions}")

    # ========== COMBINED ANALYSIS ==========
    print("=== Combined Analysis ===")

    # Total players
    total_players = len(player_data)
    print(f"Total players: {total_players}")

    # Count unique achievements
    total_unique_achievements = len({ach for player, ach
                                     in achievements_list})
    print(f"Total unique achievements: {total_unique_achievements}")

    # Average score
    average_score = (sum(p['score'] for p in player_data) /
                     len(player_data))
    print(f"Average score: {average_score}")

    # Top performer
    top_player = max(player_data, key=lambda p: p['score'])
    top_achievements = sum(1 for player, _ in achievements_list
                           if player == top_player['name'])
    print(f"Top performer: {top_player['name']} "
          f"({top_player['score']} points, "
          f"{top_achievements} achievements)")


if __name__ == '__main__':
    main()
