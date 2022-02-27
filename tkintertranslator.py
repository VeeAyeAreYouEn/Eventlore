# -*- coding: utf-8 -*-
# Import libs
from tkinter import *
import tkinter as tk
import wget
from zipfile import ZipFile
import os
from tkPDFViewer import tkPDFViewer as pdf
import pdfplumber
from deep_translator import GoogleTranslator

# Create tk object
root = Tk()

# test file for program
filename = wget.download("https://ncert.nic.in/textbook/pdf/aemh1dd.zip")

options = [
    "বাংলা",
    "हिंदी",
    "ગુજરાતી",
    "ಕನ್ನಡ",
    "മലയാളം",
    "मराठी",
    "ਪੰਜਾਬੀ",
    "தமிழ்",
    "తెలుగు",
]

# Adjust size
root.geometry("600x600")

root.title("Language Selection")

# datatype of menu text
lang_select = StringVar()

# initial menu text
lang_select.set("Select Language")

# Create Dropdown menu
drop = OptionMenu(root, lang_select, *options)
drop.pack()

# func to get language
def get_lang_selected():
    global lang_selected
    if lang_select.get() == "বাংলা":
        lang_selected = "bn"
    elif lang_select.get() == "हिंदी":
        lang_selected = "hi"
    elif lang_select.get() == "ગુજરાતી":
        lang_selected = "gu"
    elif lang_select.get() == "ಕನ್ನಡ":
        lang_selected = "kn"
    elif lang_select.get() == "മലയാളം":
        lang_selected = "ml"
    elif lang_select.get() == "मराठी":
        lang_selected = "mr"
    elif lang_select.get() == "ਪੰਜਾਬੀ":
        lang_selected = "pa"
    elif lang_select.get() == "தமிழ்":
        lang_selected = "ta"
    elif lang_select.get() == "తెలుగు":
        lang_selected = "te"
    openNewWindowForInputs1()


# func to get path of zip file which has been downloaded
def openNewWindowForInputs1():
    global pathinput
    global translated_submit
    # Toplevel object which will be treated as a new window
    inputwindow1 = Toplevel(root)
    # sets the title of the
    # Toplevel widget
    inputwindow1.title(
        GoogleTranslator(source="en", target=lang_selected).translate(
            text="Input Window 1"
        )
    )
    # sets the geometry of toplevel
    inputwindow1.geometry("600x600")
    translated_path_input = GoogleTranslator(
        source="en", target=lang_selected
    ).translate(text="Enter path of zip file")
    label_path_input = Label(inputwindow1, text=translated_path_input)
    label_path_input.grid(row=0, column=0, padx=5, pady=10)
    pathinput = Entry(inputwindow1, width=20)
    pathinput.grid(row=0, column=1)

    # Button Creation
    translated_submit = GoogleTranslator(source="en", target=lang_selected).translate(
        text="Submit"
    )
    submitbutton = tk.Button(inputwindow1, text=translated_submit, command=zipunzip)
    submitbutton.grid(row=3, column=1)


# unzip zip
def zipunzip():
    with ZipFile(pathinput.get(), "r") as zip_ref:
        zip_ref.extractall()
        os.remove(pathinput.get())
    openNewWindowForInputs2()


# path for chapter downloaded
def openNewWindowForInputs2():
    global inputwindow2
    global chap_input
    # Toplevel object which will be treated as a new window
    inputwindow2 = Toplevel(root)
    # sets the title of the
    # Toplevel widget
    inputwindow2.title(
        GoogleTranslator(source="en", target=lang_selected).translate(
            text="Input Window 2"
        )
    )
    # sets the geometry of toplevel
    inputwindow2.geometry("600x600")

    translated_chap_input = GoogleTranslator(
        source="en", target=lang_selected
    ).translate(text="Enter path of desired chapter:")
    label_chap_input = Label(inputwindow2, text=translated_chap_input)
    label_chap_input.grid(row=0, column=0, padx=5, pady=10)
    chap_input = Entry(inputwindow2, width=20)
    chap_input.grid(row=0, column=1)
    # Button Creation
    submitbutton = tk.Button(
        inputwindow2, text=translated_submit, command=openNewWindowToDisplay
    )
    submitbutton.grid(row=3, column=1)


# display pdf
def openNewWindowToDisplay():
    display = Toplevel(root)
    # sets the title of the
    # Toplevel widget
    display.title(
        GoogleTranslator(source="en", target=lang_selected).translate(text="Display")
    )
    # sets the geometry of toplevel
    pdf_file = pdf.ShowPdf()
    pdf_file_display = pdf_file.pdf_view(
        display, pdf_location=chap_input.get(), width=100, height=100
    )
    pdf_file_display.pack()
    pdftext()


# parse
def pdftext():
    global final
    with pdfplumber.open(chap_input.get()) as pdf:
        num = len(pdf.pages)
        final = ""
        for page in range(num):
            data = pdf.pages[page].extract_text()
            final = final + "\n" + data
    translator()


# display translation
def translator():
    translationwin = Toplevel(root)
    translationwin.title(
        GoogleTranslator(source="en", target=lang_selected).translate(text="Translated")
    )
    translated = GoogleTranslator(source="en", target=lang_selected).translate(
        text=final
    )
    label_translated = Label(translationwin, text=translated)
    label_translated.grid(row=0, column=0, padx=5, pady=10)


submitbutton = tk.Button(root, text="Submit", command=get_lang_selected)
submitbutton.pack()
# Execute tkinter
root.mainloop()
