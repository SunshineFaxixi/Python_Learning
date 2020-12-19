def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            print("It's a prime number")
            break
    else:
        print("It is not a prime number")


def prime_checker_1(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number")
    else:
        print("It is not a prime number")


n = int(input("Check this number: "))
prime_checker_1(number = n)