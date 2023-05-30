from tkinter import *
from tkinter import ttk

def show_main_program():
    welcome_screen.destroy()  # Close the welcome screen
    root.deiconify()  # Show the main program window

def show_welcome_screen():
    global welcome_screen
    welcome_screen = Toplevel(root)
    welcome_screen.title("Welcome to Julie's Party Hire")
    welcome_screen.geometry("300x200")

    label = Label(welcome_screen, text="Welcome to Julie's Party Hire!")
    label.pack(pady=20)

    continue_button = ttk.Button(welcome_screen, text="Continue", command=show_main_program)
    continue_button.pack()

def process_input():
    name = entry.get()
    receipt = entry2.get()
    item = entry3.get()
    quantity = entry4.get()

    # Insert the input data into the TreeView widget
    tree.insert("", "end", values=(name, receipt, item, quantity))

    # Display the outcome (You can customize this as per your requirements)
    outcome_label.config(text=f"Thank you, {name}! Your order has been processed.")

    # Clear the input fields
    entry.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)

# Hide the main program window initially
root = Tk()
root.withdraw()

entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)
entry3 = ttk.Entry(root, width=30)
entry4 = ttk.Entry(root, width=30)

entry.insert(0, '')
entry2.insert(0, '')
entry3.insert(0, '')
entry4.insert(0, '')

button = ttk.Button(root, text='Enter', command=process_input)

lbltitle = ttk.Label(text='Julie\'s Party Hire', font=(('Arial'), 30))
lblname = ttk.Label(text='Your Name:')
lblreceipt = ttk.Label(text='Receipt Number:')
lblitem = ttk.Label(text='Item Hired:')
lblhowmany = ttk.Label(text='How Many Items Have You Hired:')

lbltitle.grid(row=0, column=0)
lblname.grid(row=1, column=0)
lblreceipt.grid(row=2, column=0)
lblitem.grid(row=3, column=0)
lblhowmany.grid(row=4, column=0)

entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
entry3.grid(row=3, column=1)
entry4.grid(row=4, column=1)
button.grid(row=5, column=1)

# Create a TreeView widget
tree = ttk.Treeview(root)
tree["columns"] = ("Name", "Receipt", "Item", "Quantity")

# Format columns
tree.column("#0", width=0, stretch=NO)
tree.column("Name", width=100)
tree.column("Receipt", width=100)
tree.column("Item", width=100)
tree.column("Quantity", width=100)

# Define column headings
tree.heading("#0", text="", anchor=W)
tree.heading("Name", text="Name", anchor=W)
tree.heading("Receipt", text="Receipt", anchor=W)
tree.heading("Item", text="Item", anchor=W)
tree.heading("Quantity", text="Quantity", anchor=W)

tree.grid(row=8, column=0, columnspan=2, pady=7)

# Outcome label
outcome_label = ttk.Label(root, text="")
outcome_label.grid(row=7, columnspan=2, pady=10)

# Show the welcome screen
show_welcome_screen()

root.geometry('600x500')
root.mainloop()

