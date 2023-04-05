import tkinter as tk

# create a new instance of tkinter window
root = tk.Tk()

# create a canvas object inside the window
canvas = tk.Canvas(root, width=500, height=500, borderwidth=0,
                   highlightthickness=0, bg="white")
canvas.grid()

# define function to create a circle on canvas


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)


# add create_circle function to the tkinter canvas
tk.Canvas.create_circle = _create_circle

# define function to create a circle arc on canvas


def _create_circle_arc(self, x, y, r, **kwargs):
    # if both start and end angles are specified
    if "start" in kwargs and "end" in kwargs:
        # calculate the extent of the arc based on start and end angles
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
        return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)


# add create_circle_arc function to the tkinter canvas
tk.Canvas.create_circle_arc = _create_circle_arc

# use the functions to create some shapes on canvas
canvas.create_circle(100, 120, 50, fill="blue", outline="#DDD", width=4)
canvas.create_circle_arc(100, 120, 48, fill="green",
                         outline="", start=45, end=140)
canvas.create_circle_arc(100, 120, 48, fill="green",
                         outline="", start=275, end=305)
canvas.create_circle_arc(100, 120, 45, style="arc",
                         outline="white", width=6, start=270-25, end=270+25)
canvas.create_circle(250, 200, 100, fill="#ffffff", width=6, outline="#47C4F1")
canvas.create_circle(250, 250, 50, fill="#ffffff", width=6, outline="#47C4F1")

# set the title of the window
root.wm_title("Circles and Arcs")

# start the main event loop of the window
root.mainloop()
