#create Function to change full name to abbreviation

def abbreviation(text):
    name = ""
    for i in text:
        if i.isupper():
            name +=i
    return print(name)


abbreviation("Codex Alimentarius Commission")
