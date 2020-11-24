import tkinter as tk
from tkinter import filedialog


def UploadAction(event=None):
    filename = filedialog.askopenfilename(initialdir="/",
                           filetypes =(("PNG File", "*.png"),("BMP File", "*.bmp"),("JPEG File", "*.jpeg")),
                           title = "Choose a file.")
    pathTextBox.delete("1.0","end")
    pathTextBox.insert("1.0", filename)

window = tk.Tk()
window.geometry("700x700")
window.title("OCR")


uploadButton = tk.Button(window, text='Parcourir', command=UploadAction)
uploadButton.pack()

pathLabel = tk.Label(window,text = "Path:")
pathLabel.pack()

pathTextBox = tk.Text(window,height = 2)
pathTextBox.pack()

readImButton = tk.Button(window, text='Lire image')
readImButton.pack()

resultLabel = tk.Label(window,text = "Données:")
resultLabel.pack()

resultTextBox = tk.Text(window,height = 6)
resultTextBox.pack()




window.mainloop()