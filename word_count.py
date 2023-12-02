import sys
word_phrase = input("enter any sentence \n \n")
if not word_phrase:
    sys.exit("you must enter a sentence to continue")
word_list = word_phrase.split()
print(f"this is the sentence you entered {word_phrase}")
print("")
print(f"thiis is the sentence broken into words \n {word_list}")
word_length = len(word_list)
print(f"there are {word_length} words in the sentence")
fword = word_list[0]
lword = word_list[-1]
print(f"the first and last word are {fword} and {lword}")
character = word_list[::-1]
print(character)
character1 = " ".join(character)
print(f"your sentence reversed is:")
print("")
print(character1)