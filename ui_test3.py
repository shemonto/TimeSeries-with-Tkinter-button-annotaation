'''This is the one that
works according to requirement'''



import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np

# Define your label options
label_options = ['Option 1', 'Option 2', 'Option 3']

# Define a function to add labels to the plot
def add_label(x, y, label):
    ax[0].annotate(label, xy=(x, y), xytext=(0, 10), textcoords='offset points',
                ha='center', va='bottom', fontsize=12, color='red')
    canvas.draw()

# Create your tkinter root window
root = tk.Tk()
root.title('Matplotlib Figure with Label Widget')

label_var = tk.StringVar(value=label_options[0])
label_widget = tk.OptionMenu(root, label_var, *label_options)
label_widget.pack()

# Create your figure
fig, ax = plt.subplots(1,2,figsize=(6, 4))

# Add your plot
x = np.array([0, 1, 2]) 
y = np.array([1, 2, 3])
scatter = ax[0].scatter(x,y,picker=True)

# Add a Matplotlib canvas to display the figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Define a function to handle button click events
def on_button_click():
    global x_coord, y_coord
    label = label_var.get()
    print(label)
    #add_label(x_coord, y_coord, label)

# Define a function to handle mouse button press events
def on_press(event):
    global x_coord, y_coord
    ind = event.ind

    x_coord = x[ind][0]
    y_coord = y[ind][0]
    print(x_coord,y_coord)
    # Add a tkinter button widget
    button_widget = tk.Button(root, text='Add Label', command=on_button_click)
    button_widget.pack()

    # Add a Matplotlib navigation toolbar
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Bind the button press event to the figure
cid = fig.canvas.mpl_connect('pick_event', on_press)

# Start the tkinter mainloop
tk.mainloop()
