from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import customtkinter as ctk

import matplotlib.pyplot as plt

# Generate random values for the pie chart
labels = ['A', 'B', 'C', 'D']
sizes = [random.randint(10, 50) for _ in labels]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Create the main window
root=ctk.CTk()
root.title("Pie Chart in CustomTkinter")

# Create a canvas to display the pie chart
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()