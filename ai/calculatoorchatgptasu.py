import tkinter as tk

def on_click(event):
    current = entry.get()
    button_text = event.widget.cget("text")
    
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry widget for the display
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create buttons and add them to the grid
row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, font=('Arial', 18), padx=20, pady=20)
    button.grid(row=row_val, column=col_val, sticky="nsew")
    
    button.bind("<Button-1>", on_click)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Make the buttons expand to fill the window when resized
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Run the main event loop
root.mainloop()