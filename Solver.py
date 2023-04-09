import tkinter as tk
import cmath
import math

# Define a function to solve the quadratic equation


def solve_quadratic(a, b, c):
    d = (b**2) - (4*a*c)

# find two solutions
    root1 = (-b-math.sqrt(d))/(2*a)
    root2 = (-b+math.sqrt(d))/(2*a)
    return root1, root2

# Define a function to handle button clicks


def on_button_click():
    # Get the values from the input fields
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())

    # recalculate discriminant
    d = (b**2) - (4*a*c)

    # Call the solve_quadratic function
    if d > 0:

        # Call the solve_quadratic function
        roots = solve_quadratic(a, b, c)
        sroot = str(roots)

        suroot = f"Roots : Real"
        roots_label.config(text=(sroot), font=("Consolas", 14))

    elif d < 0:
        # find two solutions

        def solve_complex_quadratic(a, b, c):
            d = (b**2) - (4*a*c)
            root1 = (-b-cmath.sqrt(d))/(2*a)
            root2 = (-b+cmath.sqrt(d))/(2*a)
            return root1, root2

        complexquad = solve_complex_quadratic(a, b, c)
        sroot = str(complexquad)

        suroot = f"Roots : Non-Real"

        roots_label.config(text=(sroot), font=("Consolas", 14))

    # Display the type of roots in the label widget
    roots_labelal.config(text=(suroot), font=("Consolas", 14))


# Create the GUI
root = tk.Tk()
root.geometry("600x300")
root.title("Quadratic Equation Solver")

heading = tk.Label(root, text='Quadratic Equation',
                   font=("Consolas", 16, "bold"))


# Create a frame for the input fields
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

# Create the input fields
entry_width = 60
a_label = tk.Label(input_frame, text="A", font=("Consolas"))
a_label.grid(row=0, column=0)
a_entry = tk.Entry(input_frame, width=entry_width, font=("Consolas"))
a_entry.grid(row=0, column=1, padx=10)

b_label = tk.Label(input_frame, text="B", font=("Consolas"))
b_label.grid(row=1, column=0)
b_entry = tk.Entry(input_frame, width=entry_width, font=("Consolas"))
b_entry.grid(row=1, column=1, padx=10, pady=10)

c_label = tk.Label(input_frame, text="C", font=("Consolas"))
c_label.grid(row=2, column=0)
c_entry = tk.Entry(input_frame, width=entry_width, font=("Consolas"))
c_entry.grid(row=2, column=1, padx=10)

# Create the solve button
solve_button = tk.Button(
    root, text="Solve", command=on_button_click, width=40, font=("Consolas"))
solve_button.pack(pady=10)

# Create a label frame for the type of roots
roots_frame = tk.LabelFrame(
    root, text="Type Of Roots", font=("Consolas"), labelanchor="n")
roots_frame.pack(padx=10, pady=10)

# Create the label widget for displaying the roots
roots_labelal = tk.Label(roots_frame, text="", width=100)
roots_labelal.pack()

# Create a label frame for the output label
output_frame = tk.LabelFrame(
    root, text="Roots Of The Equation", font=("Consolas"), labelanchor="n")
output_frame.pack(padx=10, pady=10)

# Create the label widget for displaying the roots
roots_label = tk.Label(output_frame, text="", width=100)
roots_label.pack()

# Start the GUI
root.mainloop()
