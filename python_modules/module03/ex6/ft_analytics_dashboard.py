#!/usr/bin/env python3

# Player records:
player_data = [
    {
        'name': 'alice',
        'score': 2300,
        'status': 'active',
        'region': 'north',
        'achievements': 5
    },
    {
        'name': 'bob',
        'score': 1800,
        'status': 'inactive',
        'region': 'east',
        'achievements': 3
    },
    {
        'name': 'charlie',
        'score': 2150,
        'status': 'active',
        'region': 'central',
        'achievements': 7
    },
    {
        'name': 'diana',
        'score': 2200,
        'status': 'active',
        'region': 'north',
        'achievements': 4
    },
    {
        'name': 'eve',
        'score': 1900,
        'status': 'active',
        'region': 'east',
        'achievements': 2
    },
]

# Achievements list for each player
achievements_data = [
    ('alice', 'first_kill'),
    ('alice', 'level_10'),
    ('alice', 'boss_slayer'),
    ('bob', 'first_kill'),
    ('bob', 'level_10'),
    ('charlie', 'boss_slayer'),
    ('charlie', 'level_10'),
    ('charlie', 'first_kill'),
    ('diana', 'level_10'),
    ('eve', 'first_kill'),
]


# ============================================================================
# LIST COMPREHENSIONS
# ============================================================================

def demonstrate_list_comprehensions():
    """List comprehensions: elegant one-liners for filtering and
    transforming"""
    print("\n=== List Comprehension Examples ===")
    # 1. Filter: Get high scorers (score > 2000)
    high_scorers = [player['name'] for player in player_data
                    if player['score'] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    # 2. Transform: Double all scores (with transformation)
    doubled_scores = [player['score'] * 2 for player in player_data]
    print(f"Scores doubled: {doubled_scores}")
    # 3. Filter + Transform: Get active player names
    active_players = [p['name'] for p in player_data
                      if p['status'] == 'active']
    print(f"Active players: {active_players}")
    # 4. Nested: Create a list of (player, score) tuples
    high_performer_tuples = [(p['name'], p['score']) for p in player_data
                             if p['score'] > 2100]
    print(f"High performers (tuples): {high_performer_tuples}")
    # 5. Conditional expression: Categorize players
    player_categories = [f"{p['name']}: "
                         f"{'strong' if p['score'] > 2000 else 'learning'}"
                         for p in player_data]
    print(f"Player categories: {player_categories}")


# ============================================================================
# DICT COMPREHENSIONS
# ============================================================================

def demonstrate_dict_comprehensions():
    """Dict comprehensions: powerful for creating key-value mappings"""
    print("\n=== Dict Comprehension Examples ===")
    # 1. Create a mapping: player name -> score
    player_scores = {player['name']: player['score']
                     for player in player_data}
    print(f"Player scores: {player_scores}")
    # 2. Filter + Create mapping: only active players
    active_player_scores = {p['name']: p['score'] for p in player_data
                            if p['status'] == 'active'}
    print(f"Active player scores: {active_player_scores}")
    # 3. Transform keys and values: score -> region mapping
    player_regions = {player['name']: player['region']
                      for player in player_data}
    print(f"Player regions: {player_regions}")
    # 4. Grouping by category: Categorize scores into brackets
    score_categories = {}
    for player in player_data:
        if player['score'] > 2100:
            category = 'high'
        elif player['score'] > 1900:
            category = 'medium'
        else:
            category = 'low'
        score_categories[player['name']] = category
    # Better: using dict comprehension with conditional
    score_brackets = {
        p['name']: ('high' if p['score'] > 2100
                    else 'medium' if p['score'] > 1900
                    else 'low')
        for p in player_data
    }
    print(f"Score brackets: {score_brackets}")
    # 5. Count occurrences: How many achievements per player
    achievement_count = {}
    for player, achievement in achievements_data:
        achievement_count[player] = (achievement_count.get(player, 0)
                                     + 1)
    print(f"Achievement counts: {achievement_count}")
    # 6. Score distribution
    score_distribution = {
        'high': len([p for p in player_data if p['score'] > 2100]),
        'medium': len([p for p in player_data
                       if 1900 < p['score'] <= 2100]),
        'low': len([p for p in player_data if p['score'] <= 1900]),
    }
    print(f"Score distribution: {score_distribution}")
    # 7. Invert mapping: score -> list of players with that score
    score_to_players = {}
    for player in player_data:
        score = player['score']
        if score not in score_to_players:
            score_to_players[score] = []
        score_to_players[score].append(player['name'])
    print(f"Scores to players: {score_to_players}")


# ============================================================================
# SET COMPREHENSIONS
# ============================================================================

def demonstrate_set_comprehensions():
    """Set comprehensions: perfect for finding unique values"""
    print("\n=== Set Comprehension Examples ===")
    # 1. Get unique players
    unique_players = {player['name'] for player in player_data}
    print(f"Unique players: {unique_players}")
    # 2. Get unique achievements
    unique_achievements = {achievement for player, achievement
                           in achievements_data}
    print(f"Unique achievements: {unique_achievements}")
    # 3. Get unique regions
    unique_regions = {player['region'] for player in player_data}
    print(f"Active regions: {unique_regions}")
    # 4. Filter unique: active player regions only
    active_regions = {p['region'] for p in player_data
                      if p['status'] == 'active'}
    print(f"Regions with active players: {active_regions}")
    # 5. Unique achievements per player (filter + unique)
    alice_achievements = {ach for player, ach in achievements_data
                          if player == 'alice'}
    print(f"Alice's achievements: {alice_achievements}")
    # 6. Find players with achievements
    players_with_achievements = {player for player, achievement
                                 in achievements_data}
    print(f"Players with achievements: {players_with_achievements}")
    # 7. Performance levels (unique categories)
    performance_levels = {'high' if p['score'] > 2100
                          else 'medium' if p['score'] > 1900
                          else 'low' for p in player_data}
    print(f"Unique performance levels in dataset: "
          f"{performance_levels}")


# ============================================================================
# COMBINED ANALYSIS
# ============================================================================

def demonstrate_combined_analysis():
    """Combining all comprehension types for powerful analytics"""
    print("\n=== Combined Analysis ===")
    # Count: Total players
    total_players = len(player_data)
    print(f"Total players: {total_players}")
    # Count: Total unique achievements
    all_achievements = {ach for player, ach in achievements_data}
    print(f"Unique achievements available: {len(all_achievements)}")
    print(f"  Achievements: {all_achievements}")
    # Average: Calculate average score
    average_score = (sum(p['score'] for p in player_data) /
                     len(player_data))
    print(f"Average score: {average_score:.1f}")
    # Top performer:
    top_player = max(player_data, key=lambda p: p['score'])
    top_achievement_count = sum(1 for player, ach in achievements_data
                                if player == top_player['name'])
    print(f"Top performer: {top_player['name']} "
          f"({top_player['score']} points, "
          f"{top_achievement_count} achievements)")
    # Comprehensive player report
    print("\n--- Player Report ---")
    # Create player stats using dict comprehension
    player_stats = {
        p['name']: {
            'score': p['score'],
            'status': p['status'],
            'achievements': sum(1 for player, ach in achievements_data
                                if player == p['name']),
            'performance': ('high' if p['score'] > 2100
                            else 'medium' if p['score'] > 1900
                            else 'low')
        }
        for p in player_data
    }
    # Print each player's stats
    for name, stats in player_stats.items():
        print(f"  {name}: {stats['score']} pts | "
              f"{stats['status']} | {stats['achievements']} achievements | "
              f"Performance: {stats['performance']}")
    # Sort by region (using set comprehension to group)
    print("\n--- Players by Region ---")
    regions = {p['region'] for p in player_data}
    for region in sorted(regions):
        players_in_region = [p['name'] for p in player_data
                             if p['region'] == region]
        print(f"  {region.capitalize()}: {', '.join(players_in_region)}")
    # Active vs Inactive breakdown
    print("\n--- Activity Status ---")
    active_count = len([p for p in player_data
                        if p['status'] == 'active'])
    inactive_count = len([p for p in player_data
                          if p['status'] == 'inactive'])
    print(f"  Active: {active_count} | Inactive: {inactive_count}")


# ============================================================================
# BONUS:
# ============================================================================

def bonus_comprehensions_vs_loops():
    """
    Demonstrate why comprehensions are essential for data engineering
    """
    print("\n=== Why Comprehensions Matter ===")
    print("\n1. READABILITY: Clear intent at a glance")
    print("   Comprehension: high_scores = [p['score'] for p in players "
          "if p['score'] > 2000]")
    print("   vs Loop: 5 lines of code doing the same thing")
    print("\n2. PERFORMANCE: Comprehensions are faster than loops")
    print("   - Optimized bytecode generation")
    print("   - Less overhead than manual loops")
    print("\n3. PYTHONIC: Following Python's philosophy of elegance")
    print("   - 'There should be one way to do it'")
    print("   - Comprehensions are the standard for transformations")
    print("\n4. DATA ENGINEERING WORKFLOW:")
    print("   Extract → Filter → Transform → Load")
    print("   Comprehensions handle Extract, Filter, and Transform "
          "elegantly")
    print("\n5. COMPOSABILITY: Easy to chain and combine")
    power_users = {
        p['name']: len([ach for player, ach in achievements_data
                        if player == p['name']])
        for p in player_data
        if p['score'] > 2000 and p['status'] == 'active'
    }
    print(f"   Power users achievements: {power_users}")


def main():
    """Run all demonstrations"""
    print("=" * 70)
    print("       GAME ANALYTICS DASHBOARD - Comprehensions Mastery")
    print("=" * 70)
    demonstrate_list_comprehensions()
    demonstrate_dict_comprehensions()
    demonstrate_set_comprehensions()
    demonstrate_combined_analysis()
    bonus_comprehensions_vs_loops()
    print("\n" + "=" * 70)
    print("  Comprehensions are Python's magic wand for data "
          "transformation!")
    print("=" * 70)


if __name__ == '__main__':
    main()
