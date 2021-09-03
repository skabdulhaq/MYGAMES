import random
import os

import requests.exceptions


def clear():
    os.system("cls")


def compare(score_human, score_coumputer):
    if score_human < 22:
        if score_coumputer < 22:
            if score_human == score_coumputer:
                return "Game is draw"
            elif score_human > score_coumputer:
                return "You win"
            else:
                return "You lose"
        else:
            return "You win"
    else:
        return "You lose"


def printerfinal(list_human, score_human, list_coumputer , score_coumputer):
    print(f"Your cards are {list_human} , your final score = {score_human} ")
    print(f"coumputers cards are {list_coumputer}, coumputer's final score = {sum(list_coumputer)}")


def printer(list_human, score_human, list_coumputer):
    print(f"Your cards are {list_human} , your current score = {score_human} ")
    print(f"coumputers card is {list_coumputer}")


def dealer(number):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choices(cards, k=int(number))


def comcardchange(score_coumputer, list_coumputer):
    if score_coumputer < 17:
        list_coumputer = list_coumputer+dealer(1)
        return list_coumputer
    else:
        return list_coumputer


def elevenorone(lidt_coumputer_up, list_human):
    if 11 in lidt_coumputer_up and sum(lidt_coumputer_up) > 21:
        lidt_coumputer_up.remove(11)
        lidt_coumputer_up.append(1)
    if 11 in list_human and sum(list_human) > 21:
        list_human.remove(11)
        list_human.append(1)


def black(list_human, score_human, list_coumputer, score_coumputer):
    printer(list_human, score_human, list_coumputer)
    asking = input("Press 'y' to get an other card, 'n' to hold : ").lower()
    if asking == "y":
        lidt_coumputer_up = comcardchange(score_coumputer, list_coumputer)
        list_human = list_human+dealer(1)
        if 11 in lidt_coumputer_up and sum(lidt_coumputer_up)>21:
            lidt_coumputer_up.remove(11)
            lidt_coumputer_up.append(1)
        if 11 in list_human and sum(list_human)>21:
            list_human.remove(11)
            list_human.append(1)
        score_coumputer_final = sum(lidt_coumputer_up)
        score_human = sum(list_human)
        final = compare(score_human, score_coumputer_final)
        if final == "You lose":
            printerfinal(list_human, score_human, comcardchange(score_coumputer_final, lidt_coumputer_up),score_coumputer_final)
            print(final)
            return
        black(list_human, score_human, list_coumputer, score_coumputer_final)
    elif asking == "n":
        lidt_coumputer_up = comcardchange(score_coumputer, list_coumputer)
        list_coumputer = lidt_coumputer_up
        if 11 in lidt_coumputer_up and sum(lidt_coumputer_up)>21:
            lidt_coumputer_up.remove(11)
            lidt_coumputer_up.append(1)
        if 11 in list_human and sum(list_human)>21:
            list_human.remove(11)
            list_human.append(1)
        score_coumputer_final = sum(lidt_coumputer_up)
        score_human = sum(list_human)
        final = compare(score_human, score_coumputer_final)
        if final == "You lose":
            printerfinal(list_human, score_human, comcardchange(score_coumputer_final, list_coumputer), score_coumputer_final)
            print(final)
            return
        else:
            lidt_coumputer_up = comcardchange(score_coumputer, list_coumputer)
            if 11 in lidt_coumputer_up and sum(lidt_coumputer_up) > 21:
                lidt_coumputer_up.remove(11)
                lidt_coumputer_up.append(1)
            if 11 in list_human and sum(list_human) > 21:
                list_human.remove(11)
                list_human.append(1)
            score_coumputer_final = sum(lidt_coumputer_up)
            printerfinal(list_human, score_human, lidt_coumputer_up, score_coumputer_final)
            print("You win")
end = False

while not end:
    clear()
    list_human = dealer(2)
    score_human = sum(list_human)
    list_coumputer = dealer(1)
    score_coumputer = sum(list_coumputer)
    black(list_human, score_human, list_coumputer,score_coumputer)
    ends = input("To play Black jack press 'y', To exit Press 'n': ").lower()
    if ends == "n":
        end = True
    else:
        end = False
