#!/usr/bin/python3
number = 7
guess = -1
print("guess the number!")
while guess != number:
	guess = int(input("is it ..."))

	if guess == number:
		print("hooray! you guessed it right!")
	elif guess < number:
		print("it'a bigger...")
	elif guess > number:
		print("it's not so big.")