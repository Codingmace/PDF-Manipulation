from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import filedialog
from tkinter import ttk
from tkinter import *

def open_file():
  file = filedialog.askopenfilename(initialdir = "~",
                                    title = "Choose PDF File",
                                    filetypes = [("PDF Files", "*.pdf")])
  if file != "":
    input['text'] = file
    total_pages = PdfFileReader(open(file, "rb"), strict=False).numPages
    pages = [ i  for i in range(1, total_pages+1) ]
    left_combo.config(values=pages)
    right_combo.config(values=pages)
    left_combo.current(0)
    right_combo.current(0)

def save_file():
  min = left_combo.get()
  max = right_combo.get()
  if (min != "..."):
    min = int(min) - 1
    max = int(max)
    if (min <= max):
      file = filedialog.asksaveasfile(initialdir = "~", 
                                      title = "Save File", 
                                      filetypes = [("PDF", "*.pdf")],
                                      defaultextension=".pdf")
      pdf_reader = PdfFileReader(open(input['text'], "rb"), strict=False)
      pdf_writer = PdfFileWriter()
      for page in range(min, max):
        pdf_writer.addPage(pdf_reader.getPage(page))
      with open(file.name, 'wb') as f:
        pdf_writer.write(f)


if __name__ == '__main__':

  root = Tk()
  root.title("PDF Splitter")
  root.resizable(width=False, height=False)

  # Create entry + buttons
  open_file = Button(root, text="Open File", command=open_file)
  save_file = Button(root, text="Save File", command=save_file)
  input = Label(root, relief=GROOVE, text="No Input Yet")
  to = Label(root, text="-")
  left_combo = ttk.Combobox(root, state="readonly", values=["..."], width=10)
  right_combo = ttk.Combobox(root, state="readonly", values=["..."], width=10)

  left_combo.current(0)
  right_combo.current(0)

  # Position entry + buttons
  open_file.grid(row=0, column=0, columnspan=3, padx=15, pady=(15, 0), sticky=W+E+N+S)
  input.grid(row=1, column=0, columnspan=3, padx=15, pady=(15, 15), sticky=W+E+N+S)
  left_combo.grid(row=2, column=0, padx=15, sticky=W+E+N+S)
  to.grid(row=2, column=1, padx=15, sticky=W+E+N+S)
  right_combo.grid(row=2, column=2, padx=15, sticky=W+E+N+S)
  save_file.grid(row=3, column=0, padx=15, pady=(15, 15), columnspan=3, sticky=W+E+N+S)

  # Center window
  root.eval('tk::PlaceWindow . center')

  root.mainloop()
