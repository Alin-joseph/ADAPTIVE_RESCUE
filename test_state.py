from environment import Environment

from state_encoder import create_state


env = Environment()

# Get current sensor
observation = env.get_local_observation()

# Choose one known survivor if available
if env.known_survivors:

    target_survivor = min(
        env.known_survivors,
        key=env.known_survivors.get
    )

    target_health = env.known_survivors[
        target_survivor
    ]

else:

    target_survivor = None
    target_health = 0


# Create RL state
state = create_state(
    robot=env.robot,
    local_observation=observation,
    target_survivor=target_survivor,
    target_health=target_health,
    battery=env.battery
)


print("\n========== STATE TEST ==========")

print("Robot:")
print(env.robot)

print("\n3x3 Sensor:")
for row in observation:
    print(row)

print("\nTarget survivor:")
print(target_survivor)

print("\nTarget health:")
print(target_health)

print("\nBattery:")
print(env.battery)

print("\nFinal RL state:")
print(state)