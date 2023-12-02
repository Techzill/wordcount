name = input("what is your name \n")
rname = name.split()
#print(rname)
reversed_name = rname[::-1]
rname1 = "".join(reversed_name)
print(f"the name you entered is {name} \n your name reversed is {rname1}")
