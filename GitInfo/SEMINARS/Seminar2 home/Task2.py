# Задача 2: Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def factorial(num):   
    result = 1
    for i in range(num):       
        result *= i+1
        print(result)
          

factorial(10)