import tkinter as tk
from tkinter.filedialog import askopenfilename , asksaveasfilename
window = tk.Tk()

def open_file():
    file_path = askopenfilename(filetypes = [("Text Files" , "*.txt") , ("All Files " , "*.*")])

    if not file_path:
        return
    
    txt_area.delete(1.0 , 5.0)

    with open(file_path , "r") as input_file:
        text = input_file.read()
        txt_area.insert(tk.END , text)


    window.title(f"OwaisTextEditor - {file_path}")

def save_file():
    file_path = asksaveasfilename(
        defaultextension = "txt" ,  
        filetypes = [("Text Files" , "*.txt") , ("All Files " , "*.*")])

    if not file_path:
        return
    
    
    with open(file_path , "w") as output_file:
        text = txt_area.get(1.0 , tk.END)
        output_file.write(text)

    window.title(f"OwaisTextEditor - {file_path}")


window.title("owais text editor")
window.rowconfigure(0 , minsize = 600)
window.columnconfigure(1 , minsize = 800)

txt_area = tk.Text(window)
frame_buttons = tk.Frame(window , relief=tk.SUNKEN)
btn_open = tk.Button(frame_buttons , text= "Open Files" , command = open_file)
btn_save = tk.Button(frame_buttons , text= "Save Files" ,  command = save_file)

btn_open.grid(column = 0 , row = 0 , sticky='ew' ,  padx= 5 , pady= 5)
btn_save.grid(column = 0 , row = 1 , sticky='ew' ,  padx= 5 , pady= 5)

frame_buttons.grid(column = 0 , row = 0 ,  sticky = 'nw')
txt_area.grid(column = 1 , row = 0 , sticky = "nsew" )
window.mainloop()