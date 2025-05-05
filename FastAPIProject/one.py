# #prog 1
# a,b=4,5
# print("sum of 4 and 5",a+b)
#
# #prog 2
# x,y=input().split()
# print(x,y)
#
# #prog 3
# l=list(map(int,input().split()))
# print(sum(l))
#
# #prog 4
# def fun1(a,b):
#     return sum(a+b)
# fun1(4,5)
#
# #prog 5
# def recursion(a,b):
#     if b==0:
#         return a
#
#     return recursion(b,a%b)
#
# print(recursion(10,20))
#
# #prog 6
# def fibonacci(n):
#     a=-1
#     b=1
#
#     for i in range(n):
#         c = a + b
#         print(c)
#         a,b=b,c
#     return c
# print(fibonacci(10))
#
# #prog 7
# a=map(int,input().split())
# b=list(a)
# print(b)
#
# #prog 8
# def generator(n):
#     for i in range(1,n+1):
#         yield i
# print(list(generator(10)))
#
# #prog 9
# n=5
# for i in range(n):
#     for j in range(n-(n-i),n+1):
#         print(j,end=" ")
#     print()
# for i in range(n):
#     for j in range(n,n-(n-i),-1):
#         print(j,end=" ")
#     print()
import random


def rock_paper_scissors():


    while True:
        user_choice = input("Rock, Paper, Scissors?:  ")
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        print("user_choice: ",user_choice, "Computer choice :", computer_choice)
        if user_choice == computer_choice:
            print("It's a draw!")
        elif user_choice == "Rock" and computer_choice == "scissors" :
            print('you win!')
        elif user_choice == "Paper" and computer_choice == "rock":
            print('you win!')
        elif user_choice == "Scissors" and computer_choice == "paper":
            print('you win!')
        else:
            print("you lose")
        print("do you want to play again?")
        choice = input("yes or no:  ")
        if choice == "no":
            print("exiting")
            break




rock_paper_scissors()
print("hello")