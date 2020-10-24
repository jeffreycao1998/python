import json
from difflib import get_close_matches

data = json.load(open('data.json'))
words = data.keys()

def lookup(word):
  word = word.lower()

  if word in data:
    return data[word]
  elif word.title() in data:
    return data[word.title()]
  elif word.upper() in data:
    return data[word.upper()]
  elif len(get_close_matches(word, data.keys())) > 0:
    close_matches = get_close_matches(word, data.keys())
    close_match = close_matches[0]
    answer = input(f"Did you mean {close_match} instead? Enter Y if yes, or N if no: ").lower()
    if answer == 'y':
      return data[close_match]
    elif answer == 'n':
      return "Sorry, we didn't understand that."
    else:
      return lookup(data[close_match])
  else:
    return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = lookup(word)

if type(output) == list:
  for definition in output:
    print(definition)
else:
  print(output)