import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    """
    Opens a file dialog for selecting a file to open.
    Reads the content of the file and inserts it into the text editor.
    Handles any exceptions that may occur.
    """
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                text_editor.delete(1.0, tk.END)  # Clear the text editor
                text_editor.insert(tk.END, file.read())  # Insert file content
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while opening the file: {e}")

def save_file():
    """
    Opens a file dialog for selecting a file location to save the current text.
    Writes the content of the text editor to the selected file.
    Handles any exceptions that may occur.
    """
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text_editor.get(1.0, tk.END))  # Write content to file
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

def create_text_editor(root):
    """
    Creates and configures the text editor widget.
    The text editor allows users to type and edit text.
    """
    text_editor = tk.Text(root, wrap='word')
    text_editor.grid(row=1, column=0, columnspan=2, sticky='nsew')
    return text_editor

def create_menu(root):
    """
    Creates and configures the menu bar with File options.
    The menu bar includes options for opening, saving, and exiting the application.
    """
    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)
    root.config(menu=menu_bar)

def create_buttons(root):
    """
    Creates and configures the Open and Save buttons.
    These buttons provide additional ways for users to open and save files.
    """
    open_button = tk.Button(root, text="Open", command=open_file)
    open_button.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

    save_button = tk.Button(root, text="Save", command=save_file)
    save_button.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

def main():
    """
    The main function sets up the main window, creates the text editor, menu, and buttons,
    and starts the Tkinter main loop.
    """
    root = tk.Tk()
    root.title("Simple Text Editor")
    root.geometry("800x600")
    
    # Configure row and column weights for proper resizing
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    # Create global text editor
    global text_editor
    text_editor = create_text_editor(root)
    create_menu(root)
    create_buttons(root)
    
    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
