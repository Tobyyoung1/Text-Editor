# Text Editor
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath= askopenfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    
    text_edit.delete(1.0,tk.END)
    with open(filepath, "r") as f:
        content= f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")
    
    
    
def save_file(window, text_edit):
    filepath= asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    # Ensure file has a .txt extension
    if not filepath.endswith(".txt"):
        filepath += ".txt"
    
    with open(filepath, "w") as f:
        content= text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File: {filepath}")

def main():
    window= tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    
    text_edit= tk.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=1)
    
    frame= tk.Frame(window, relief=tk.RAISED, bd=2) #arg1: which window, #arg2: 3D appearance, #arg3 border of 2 pixels
    save_button= tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button= tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))
    
    save_button.grid(row=0, column=0, padx=5, pady=5, sticky= "ew")
    open_button.grid(row=1, column=0, padx=5, sticky= "ew")
    frame.grid(row=0, column=0, sticky="ns") #Sticky sticks the frame to the north or south side of the frame
    
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))
    
    window.mainloop() #runs the window until the user quits

main()