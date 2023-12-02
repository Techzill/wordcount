import sys
playagain = True
while playagain:
    max_num = int(input("Enter the last number of the range you want to genereate: \n"))
    number = 1
    numbers = []
    while number <= max_num:
        numbers.append(number)
        number += 1
    print(f"the numbers between 1 and {max_num} are: \n {numbers} \n")
    playagain = input("Do you want to play again? \n y for yes or \n Enter to quit \n")
    if playagain.lower() == "y":
        continue
    else: 
        print("thanks for playing")
        playagain = False
sys.exit("Bye for now!👍")