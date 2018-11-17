if __name__=="__main__":

    for numbers in range(1,101):
        if numbers % 15 == 0:
            print("FizzBuzz")
            continue

        if numbers % 5 == 0:
            print("Buzz")
            continue

        if numbers % 3 == 0:
            print("Fizz")
            continue

        print(numbers)