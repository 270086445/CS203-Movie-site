import tkinter as tk


def open_help():
    help_window = tk.Toplevel(root)
    help_window.title("Help")
    help_label = tk.Label(help_window, text="This is a simple homepage created using Tkinter.")
    help_label.pack(padx=20, pady=20)


def open_faq():
    faq_window = tk.Toplevel(root)
    faq_window.title("FAQ")
    faq_label = tk.Label(faq_window, text="This is a simple homepage created using Tkinter.")
    faq_label.pack(padx=20, pady=20)


def open_about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_label = tk.Label(about_window, text="This is a simple homepage created using Tkinter.")
    about_label.pack(padx=20, pady=20)


def open_terms():
    terms_window = tk.Toplevel(root)
    terms_window.title("Terms")
    terms_label = tk.Label(terms_window, text="This is a simple homepage created using Tkinter.")
    terms_label.pack(padx=20, pady=20)


def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_label = tk.Label(settings_window, text="This is a simple homepage created using Tkinter.")
    settings_label.pack(padx=20, pady=20)


root = tk.Tk()
root.title("Homepage")

# Create a label
label = tk.Label(root, text="Movie Maestros", font=("Helvetica", 20))
label.pack(pady=20)

# Create buttons

help_button = tk.Button(root, text="Help", command=open_help)
help_button.pack(pady=10)


faq_button = tk.Button(root, text="Terms", command=open_faq)
faq_button.pack(pady=10)


about_button = tk.Button(root, text="About", command=open_about)
about_button.pack(pady=10)


terms_button = tk.Button(root, text="Terms", command=open_terms)
terms_button.pack(pady=10)


settings_button = tk.Button(root, text="Settings", command=open_settings)
settings_button.pack(pady=10)


exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
