# Sample daily electricity consumption in kWh

daily_consumption = [1250, 1320, 1180, 1410, 1380, 1100, 1050]

total_consumption = sum(daily_consumption)

average_consumption = total_consumption / len(daily_consumption)

peak_consumption = max(daily_consumption)

minimum_consumption = min(daily_consumption)

print("Building Energy Analysis")
print("------------------------")
print("Total consumption:", total_consumption, "kWh")
print("Average daily consumption:", round(average_consumption, 2), "kWh")
print("Peak daily consumption:", peak_consumption, "kWh")
print("Minimum daily consumption:", minimum_consumption, "kWh")