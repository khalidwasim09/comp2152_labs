"""
Author: Khalid Wasim
Assignment: #1
"""
gym_member = "Alex Alliton"  


preferred_weight_kg = 20.5  


highest_reps = 25  

membership_active = True  


workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (25, 50, 30),
    "Taylor": (40, 35, 25)
}

updated_workout_stats = {}

for friend, minutes in workout_stats.items():
    total_minutes = sum(minutes)
    updated_workout_stats[f"{friend}_Total"] = total_minutes


workout_stats.update(updated_workout_stats)

workout_list = [list(minutes) for minutes in workout_stats.values() if isinstance(minutes, tuple)]

yoga_running = [row[:2] for row in workout_list]
print("Yoga & Running Minutes:", yoga_running)


weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting (Last Two Friends):", weightlifting_last_two)


for friend, total in workout_stats.items():
    if isinstance(total, int) and total >= 120:
        print(f"Great job staying active, {friend.replace('_Total', '')}!")
        
friend_name = input("Enter a friend's name: ")

if friend_name in workout_stats:
    minutes = workout_stats[friend_name]
    print(f"{friend_name}'s Workout Stats - Yoga: {minutes[0]}, Running: {minutes[1]}, Weightlifting: {minutes[2]}")
    print(f"Total Workout Minutes: {workout_stats.get(friend_name + '_Total', 'N/A')}")
else:
    print(f"Friend {friend_name} not found in the records.")


total_minutes = {k: v for k, v in workout_stats.items() if isinstance(v, int)}
max_friend = max(total_minutes, key=total_minutes.get).replace("_Total", "")
min_friend = min(total_minutes, key=total_minutes.get).replace("_Total", "")

print(f"Friend with Highest Workout Minutes: {max_friend}")
print(f"Friend with Lowest Workout Minutes: {min_friend}")
