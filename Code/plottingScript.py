import pandas as pd  # Read CSV data into a table.
import matplotlib.pyplot as plt  # Make the plot.

INPUT_FILE = "power_per_hour_20250724_20250730_sum.csv"  # File to plot.

df = pd.read_csv(INPUT_FILE)  # Load the CSV file.
df["hour"] = df["time"].str.slice(0, 2).astype(int)  # Pull hour from the HH:MM time string.

for day in df["date"].unique():  # Loop once per day.
    day_data = df[df["date"] == day]  # Only rows for this day.
    plt.plot(day_data["hour"], day_data["power_db"], label=day)  # Plot this day's line.

plt.xticks(range(24))  # Show hours 0 to 23 on the x axis.
plt.xlabel("Hour of day")  # Label the x axis.
plt.ylabel("Power (dB)")  # Label the y axis.
plt.title("Sum of power per hour for each day (dB)")  # Title of the plot.
plt.grid(alpha=0.3)  # Light grid for readability.
plt.legend()  # Show the legend with each day.
plt.show()  # Display the plot window.
