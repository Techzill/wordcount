word_phrase = input("enter any sentence \n \n")
word_list = word_phrase.split()
print(f"this is the sentence you entered {word_phrase}")
print("")

for word in word_list:
    print(word)

word_length = len(word_list)
print(f"there are {word_length} words in the sentence")
fword = word_list[0]
lword = word_list[-1]
print(f"the first and last word are {fword} and {lword}")