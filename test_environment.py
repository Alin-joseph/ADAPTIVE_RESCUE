from environment import Environment


# Create environment
env = Environment()

print("\n========== NEW EPISODE ==========")

print("Robot position:", env.robot)
print("Survivors:", env.survivors)
print("Survivor health:", env.survivor_health)
print("Hazards:", env.hazards)
print("Obstacles:", env.obstacles)
print("Battery:", env.battery)

print("\n========== RUNNING EPISODE ==========")

# Take 10 random actions
for step in range(10):

    # Random action
    action = step % 4

    print("\nStep:", step + 1)

    if action == 0:
        print("Action: UP")
    elif action == 1:
        print("Action: DOWN")
    elif action == 2:
        print("Action: LEFT")
    elif action == 3:
        print("Action: RIGHT")

    # Perform action
    state, reward, done, info = env.step(action)

    print("Robot position:", env.robot)
    print("Battery:", env.battery)
    print("Survivor health:", env.survivor_health)
    print("Reward:", reward)

    if info["hazards_spread"]:
        print("New hazards:", info["hazards_spread"])

    if info["survivors_lost"]:
        print("Survivors lost:", info["survivors_lost"])

    if done:

        print("\n========== EPISODE ENDED ==========")
        print("Reason:", info["reason"])

        break