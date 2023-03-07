from tkinter import ttk
from tkinter.tix import *
from PIL import Image, ImageTk
from passwordGenerator import PasswordGenerator
import pyperclip

class GeneratorGUI:
    # GUI for a password generator
    def __init__(self, master):
        self._master = master
        self._master.geometry("450x250")
        self._master.title("Password generator")
        font = ("Helvetica", 10)

        self._specialCharactersVar = BooleanVar()
        specialCharactersCheck = Checkbutton(self._master, variable=self._specialCharactersVar, text="Special characters",
                                             onvalue=True, offvalue=False, command=self._setPasswordLenComboRange, font=font)
        specialCharactersCheck.grid(row=1, column=0, sticky="w", pady=2, columnspan=2)
        self._specialCharactersVar.set(True)

        self._digitsVar = BooleanVar()
        digitsCheck = Checkbutton(self._master, variable=self._digitsVar, text="Include digits?",
                                  onvalue=True, offvalue=False, command=self._setPasswordLenComboRange, font=font)
        digitsCheck.grid(row=2, column=0, sticky="w", pady=2, columnspan=2)
        self._digitsVar.set(True)

        self._caseMixVar = BooleanVar()
        caseMixCheck = Checkbutton(self._master, variable=self._caseMixVar, text="Up- and lowcase mix?",
                                   onvalue=True, offvalue=False, command=self._setPasswordLenComboRange, font=font)
        caseMixCheck.grid(row=3, column=0, sticky="w", pady=2, columnspan=2)
        self._caseMixVar.set(True)

        self._passwordLenVar = IntVar()
        self._passwordLenCombo = ttk.Combobox(self._master, width=4, textvariable=self._passwordLenVar, font=font)
        self._passwordLenCombo.grid(row=4, column=0, sticky="w", pady=5)

        passwordLengthLabel = Label(self._master, text="Length of password", font=font)
        passwordLengthLabel.grid(row=4, column=1, sticky="w", pady=5)

        self._startUp = True
        self._setPasswordLenComboRange()

        generateButton = Button(self._master, text="Generate", bg="springgreen", font=font, command=self._getPassword)
        generateButton.grid(row=5, column=1, pady=2)

        suggestLabel = Label(self._master, text="Suggested password", font=font)
        suggestLabel.grid(row=6, column=0, sticky="w", columnspan=2)

        self._suggestedVar = StringVar()
        self._suggestionEntry = Entry(self._master, textvariable=self._suggestedVar, state="disabled", font=font, width=35)
        self._suggestionEntry.place(x=130, y=155)

        rawPhoto = Image.open(r"C:\AibelProgs\Code\tkinter\passwordGenerator\copy.png")
        resizedPhoto = rawPhoto.resize((20, 20))
        self._copyPhoto = ImageTk.PhotoImage(resizedPhoto)

        copyButton = Button(self._master, image=self._copyPhoto, command=self._copyToClipboard)
        copyButton.place(x=380, y=152)

        # tooltip for copy button
        tooltip = Balloon(self._master)
        tooltip.bind_widget(copyButton, balloonmsg="Copy password to clipboard")

    # sets selection of password length
    def _setPasswordLenComboRange(self):
        currentSelection = int(self._passwordLenCombo.get())
        numRange = self._getValidRange()
        self._passwordLenCombo['values'] = numRange
        # keep length in combobox if possible
        if currentSelection in numRange:
            index = numRange.index(currentSelection)
        else:
            # set length to 10 when starting app
            if self._startUp:
                self._startUp = False
                index = numRange.index(10)
            else:
                index = 0
        self._passwordLenCombo.current(index)

    # gets the range of possible password lengths
    def _getValidRange(self):
        count = 1
        if self._specialCharactersVar.get():
            count += 1
        if self._digitsVar.get():
            count += 1
        if self._caseMixVar.get():
            count += 1

        return list(range(count, 31))

    # copies suggested password to clipboard
    def _copyToClipboard(self):
        password = self._suggestedVar.get()
        pyperclip.copy(password)

    # gets a suggested password
    def _getPassword(self):
        passwordLength = self._passwordLenVar.get()
        specialCharacters = self._specialCharactersVar.get()
        digits = self._digitsVar.get()
        lowUpCaseMix = self._caseMixVar.get()
        generator = PasswordGenerator(passwordLength, specialCharacters, digits, lowUpCaseMix)
        password = generator.generatePassword()

        self._setPasswordEntry(password)

    # sets the password entry
    def _setPasswordEntry(self, password):
        self._suggestedVar.set(password)

master = Tk()
gui = GeneratorGUI(master)
master.mainloop()