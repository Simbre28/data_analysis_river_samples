# a program that takes three data from water samples from 10 rivers taken every month for one year (the temperature, the ph and ecoli count) and processes this data onto a graph that  shows each river and its data over the year. Can you add a feature where the program asks each data sample and then once it is complete creates the graph

import matplotlib.pyplot as plt

def get_data():
  """Gets the data from the user."""
  # Get the name of the river.
  river_name = input("Enter the name of the river: ")

  # Get the temperature data.
  temperature_data = []
  for month in range(1, 13):
    temperature = float(input("Enter the temperature for month {}: ".format(month)))
    temperature_data.append(temperature)

  # Get the pH data.
  ph_data = []
  for month in range(1, 13):
    ph = float(input("Enter the pH for month {}: ".format(month)))
    ph_data.append(ph)

  # Get the E. coli count data.
  ecoli_count_data = []
  for month in range(1, 13):
    ecoli_count = int(input("Enter the E. coli count for month {}: ".format(month)))
    ecoli_count_data.append(ecoli_count)

  return river_name, temperature_data, ph_data, ecoli_count_data

def plot_data(river_name, temperature_data, ph_data, ecoli_count_data):
  """Plots the data on a graph."""
  # Create a figure.
  fig = plt.figure()

  # Add a subplot for the temperature data.
  ax1 = fig.add_subplot(311)
  ax1.plot(range(1, 13), temperature_data)
  ax1.set_xlabel("Month")
  ax1.set_ylabel("Temperature (C)")

  # Add a subplot for the pH data.
  ax2 = fig.add_subplot(312)
  ax2.plot(range(1, 13), ph_data)
  ax2.set_xlabel("Month")
  ax2.set_ylabel("pH")

  # Add a subplot for the E. coli count data.
  ax3 = fig.add_subplot(313)
  ax3.plot(range(1, 13), ecoli_count_data)
  ax3.set_xlabel("Month")
  ax3.set_ylabel("E. coli count")

  # Show the plot.
  plt.show()

def main():
  """Gets the data and plots it on a graph."""
  # Get the data from the user.
  river_name, temperature_data, ph_data, ecoli_count_data = get_data()

  # Plot the data on a graph.
  plot_data(river_name, temperature_data, ph_data, ecoli_count_data)

if __name__ == "__main__":
  main()
