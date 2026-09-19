from environment import Environment


env = Environment()

print("\n========== SENSOR TEST ==========")

print("Robot position:")
print(env.robot)

print("\n3x3 Local Observation:")

observation = env.get_local_observation()

for row in observation:
    print(row)

print("\n========== WORLD MODEL ==========")

print("\nKnown cells:")
print(env.known_cells)

print("\nKnown survivors:")
print(env.known_survivors)

print("\nKnown hazards:")
print(env.known_hazards)

print("\nKnown obstacles:")
print(env.known_obstacles)