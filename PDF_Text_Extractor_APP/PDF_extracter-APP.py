import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()                                     #All the code in between both the roots

canvas = tk.Canvas(root, width=600, height=300)    #The size of the window
canvas.grid(columnspan=3, rowspan=3)                          #This attribute is basically going to split our canvas/window into 3 identical invisible columns where we can place all of our elements with a lot of precision

#logo
logo = Image.open('logo.png')                      #opening the image by using its location 
logo = ImageTk.PhotoImage(logo)                    #converting the logo image into a tkinter image
logo_label = tk.Label(image=logo)                  #place this image inside a label widget
logo_label.image = logo                            #for the above command to work nescessary
logo_label.grid(column=1, row=0)                   #placing logo inside our window object


#instructions
instructions = tk.Label(root, text = "Select a pdf file on your computer to extract all of it's text !", font='Aharoni')
instructions.grid(columnspan=3, column=0, row=1)   #as its very big chunk of text so to make it stand across all 3 of my columns we will specify columnspace, row=1 for making it underneath logo 

def open_file():
    browse_text.set('loading....')
    file = askopenfile(parent=root, mode='rb', title='Choose a file', filetype=[('Pdf file', '*.pdf')])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        #text box
        text_box = tk.Text(root, height=10, width= 50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure('center', justify='center')
        text_box.tag_add('center', 1.0, 'end')
        text_box.grid(column=1, row=3)


        browse_text.set('Browse')



#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font='Aharoni', bg='#20bebe', fg='white', height=2, width=15)
browse_text.set('Browse')
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250) 
canvas.grid(columnspan=3)  

root.mainloop()