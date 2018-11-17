def FizzBuzz_convert(number):
    if number % 15 == 0:
        return "FizzBuzz"

    if number % 5 == 0:
        return "Buzz"

    if number % 3 == 0:
        return "Fizz"

    return str(number)


if __name__ == "__main__":

    for numbers in range(1, 101):
        print(FizzBuzz_convert(numbers))
