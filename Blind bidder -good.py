dictionary = {

}
import os
def clear():
    os.system("cls")
def maxbid(dictionary):
    Bid = []
    for names in dictionary:
        Bid.append(dictionary[names])
    result = max(Bid)
    dictionary_of_winners = {}
    for namees in dictionary:
        if dictionary[namees] == result:
            dictionary_of_winners[namees] = result
    nub = len(dictionary_of_winners)
    for final in dictionary_of_winners:
        namme = final
        result = dictionary_of_winners[namme]
        print(f"{namme} won the Bid,His bid is {result} rupees")
        if nub > 1:
            print("Try Again")

yes = True
clear()
while yes==True :
    keys = input("Enter your name => ")
    values = int(input("Enter your bid => "))
    end = input("Do you have others to bid (Yes/No) ?\n").lower()
    dictionary[keys] = values
    if end == "no":
        clear()
        yes = False
        maxbid(dictionary)
    elif end == "yes":
        clear()
