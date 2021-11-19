def CHECK(UNI, PWI, usernameArray, PasswordArray):
    for UN in usernameArray:
        if UN == UNI:
            for PW in PasswordArray:
                if PW == PWI:
                    if usernameArray.index(UNI) == PasswordArray.index(PWI):
                        return True
            
def login(correctMessage, inCorrectMessage, usernameInputPrompt, passwordInputPrompt, usernameArray, PasswordArray):
    if CHECK(input(usernameInputPrompt), input(passwordInputPrompt), usernameArray, PasswordArray):
        print(correctMessage)
        return True
    else:
        print(inCorrectMessage)