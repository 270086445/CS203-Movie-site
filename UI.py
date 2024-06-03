import tkinter as tk


def open_about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_label = tk.Label(about_window, text="This is a simple homepage created using Tkinter.")
    about_label.pack(padx=20, pady=20)


root = tk.Tk()
root.title("Homepage")

# Create a label
label = tk.Label(root, text="Welcome to My Homepage", font=("Helvetica", 20))
label.pack(pady=20)

# Create buttons
about_button = tk.Button(root, text="About", command=open_about)
about_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
