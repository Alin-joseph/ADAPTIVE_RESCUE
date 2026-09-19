def calculate_reward(
    moved,
    hit_obstacle,
    entered_hazard,
    discovered_survivor,
    rescued_survivor,
    survivor_lost,
    battery_empty,
    mission_complete
):

    reward = 0

    # Normal movement
    if moved:
        reward -= 1

    # Tried to move into an obstacle or outside the grid
    if hit_obstacle:
        reward -= 5

    # Robot entered a hazard
    if entered_hazard:
        reward -= 20

    # Robot discovered a survivor
    if discovered_survivor:
        reward += 10

    # Robot rescued a survivor
    if rescued_survivor:
        reward += 50

    # A survivor was lost
    if survivor_lost:
        reward -= 50

    # Battery became empty
    if battery_empty:
        reward -= 30

    # All survivors rescued
    if mission_complete:
        reward += 100

    return reward