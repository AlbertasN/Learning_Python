import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(x):
    x=x.lower()
    if x in data:
        return data[x]
    elif x.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[x.title()]
    elif x.upper() in data: #in case user enters words like USA or NATO
        return data[x.upper()]
    elif len(get_close_matches(x, data.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(x, data.keys())[0]} instead. If you meant this word press Y(yes) if not N(no)")
        if yn == "Y":
            return data[get_close_matches(x, data.keys())[0]]
        elif yn == "N":
            return "Please try again, your word cen't be found"
        else:
            return "We can't understand the answer"
    else:
        return "The word doesnt exist."

word=input("Enter a word: ")

output = (translate(word))

if type(output)==list:
    for item in output:
        print(item)

else:
    print(output)
