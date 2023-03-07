import string
import random

class PasswordGenerator:
    # generates a password with options for password layout
    def __init__(self, length, specialCharacters, digits, lowupcaseMix):
        self._length = length
        self._specialCharactersBool = specialCharacters
        self._digitsBool = digits
        self._lowupcaseMixBool = lowupcaseMix

    # generates a password
    def generatePassword(self):
        alphabetLow = list(string.ascii_lowercase)
        alphabetUp = list(string.ascii_uppercase)
        digits = [str(i) for i in range(10)]
        specialCharacters = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','\\',':',';','"',"'",'<',',','>','.','?','/']

        # adds relevant lists based on user input
        mashUpList = [alphabetLow]
        if self._specialCharactersBool:
            mashUpList.append(specialCharacters)
        if self._digitsBool:
            mashUpList.append(digits)
        if self._lowupcaseMixBool:
            mashUpList.append(alphabetUp)

        password = ""
        # set equal chance for each list and picks a random item from chosen list
        for i in range(self._length):
            index = random.randint(0, len(mashUpList)-1)
            chosenList = mashUpList[index]
            password += random.choice(chosenList)

        # checks that password meets criteria, if not call function again
        while self._checkPassword(password) == False:
            password = self.generatePassword()

        return password

    # checks if password meets requirements
    def _checkPassword(self, password):
        if self._digitsBool:
            digitNotFound = True
            for char in password:
                if char.isdigit():
                    digitNotFound = False
                    break
            if digitNotFound:
                return False

        if self._lowupcaseMixBool:
            lowCaseNotFound = True
            upCaseNotFound = True
            for char in password:
                if char.islower():
                    lowCaseNotFound = False
                elif char.isupper():
                    upCaseNotFound = False
            if lowCaseNotFound or upCaseNotFound:
                return False

        if self._specialCharactersBool:
            specialCharacterNotFound = True
            for char in password:
                if char.isalpha() == False and char.isdigit() == False:
                    specialCharacterNotFound = False
                    break
            if specialCharacterNotFound:
                return False

        if self._digitsBool or self._lowupcaseMixBool or self._specialCharactersBool:
            lowerNotFound = True
            for char in password:
                if char.islower():
                    lowerNotFound = False
                    break
            if lowerNotFound:
                return False

        return True
