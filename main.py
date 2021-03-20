


def predict(txt=None, wordList=None):
    if not txt or not wordList:
        return "Missing arguments"

    txtOrg = txt

    if txtOrg in wordList:
        return f"\n\n-------------\nWordlist:\n{wordList}\n-------------\nYour input:\n{txtOrg}\n-------------\nMy predictions:\n{txt}"

    detectLen = len(txt) // 2 + len(txt) // 4
    matchingCmds = []
    commands_count = 0
    txt = f";{txt}"
    for word in wordList:
        if txt[1:len(txt)] == word[0:len(txt)]:
            matchingCmds.append(word)
        detection2 = detectLen + 1
        if txt[1:detection2].lower() == word[0:detectLen].lower() or txt[detection2:len(txt)].lower() == word[detectLen:len(txt)].lower():
            if commands_count > 4:
                break
            else:
                matchingCmds.append(word)
                commands_count += 1
    if not matchingCmds:

        detectLen = len(txt) // 3
        commands_count = 0
        for word in wordList:
            detection2 = detectLen + 1
            if txt[1:detection2].lower() == word[0:detectLen].lower() or txt[detection2:len(txt)].lower() == word[detectLen:len(txt)].lower():
                if commands_count > 4:
                    break
                else:
                    matchingCmds.append(word)
                    commands_count += 1
        if not matchingCmds:
            return f"\n\n-------------\nWordlist:\n{wordList}\n-------------\nYour input:\n{txtOrg}\n-------------\nMy predictions:\nCould not find any words to match this word!"
        else:
            string = ""
            for word in matchingCmds:
                string = f"{string}\n{word}"
            return f"\n\n-------------\nWordlist:\n{wordList}\n-------------\nYour input:\n{txtOrg}\n-------------\nMy predictions:\n{string}"

    else:
        string = ""
        for word in matchingCmds:
            string = f"{string}\n{word}"
        return f"\n\n-------------\nWordlist:\n{wordList}\n-------------\nYour input:\n{txtOrg}\n-------------\nMy predictions:\n{string}"

default_list = ['ambivert', 'calcspar', 'deaness', 'entrete', 'gades', 'monkeydom', 'outclimbed', 'outdared', 'pistoleers', 'redbugs', 'snake-line', 'subrules', 'subtrends', 'torenia', 'unhides']
default_list = ["dog", "cat", "house", "home", "cat", "child", "python", "food", "apple", "kid", "adult", "school", "fun"]

string = ""
for word in default_list:
    string = f"{word}, {string}"


print(f"-------------------------\nHello, this is an algorithm that will predict your words!\nPlease misspell one of "
      f"the following words:\n\n{string}\n")

userInput = input("Please misspell one of the words above: ")

print(predict(userInput, default_list))
