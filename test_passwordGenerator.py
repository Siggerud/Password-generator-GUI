from passwordGenerator import PasswordGenerator
from random import randint

# testing PasswordGenerator class
def test_generatePassword():
    # different argument combinations that can be input for class
    combinations = [[True, True, True], [True, False, True], [True, False, False], [True, True, False],
    [False, True, True], [False, True, False], [False, False, True], [False, False, False]]
    for combination in combinations:
        specialArg = combination[0]
        digitsArg = combination[1]
        caseMixArg = combination[2]
        lenPassword = randint(5, 30) # make length of password random

        generator = PasswordGenerator(lenPassword, specialArg, digitsArg, caseMixArg)
        password = generator.generatePassword()

        # checking if password generated matches input arguments
        lowerFound = False
        upperFound = False
        specialFound = False
        digitFound = False
        for char in password:
            if char.islower():
                lowerFound = True
            elif char.isupper():
                upperFound = True
            elif char.isdigit():
                digitFound = True
            elif char.isalpha() == False and char.isdigit() == False:
                specialFound = True

        assert len(password) == lenPassword
        assert lowerFound == True # should always be True
        assert upperFound == caseMixArg
        assert specialFound == specialArg
        assert digitFound == digitsArg

test_generatePassword()