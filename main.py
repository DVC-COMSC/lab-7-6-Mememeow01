
def getInput():
    """
    Prompt the user to enter multiple values in a single line,
    split these values, convert them into a list of integers, and return it.
    """
    user_input = input("Enter multiple values separated by spaces: ")
    return list(map(int, user_input.split()))

def makeReverse(numbers):
    """
    Takes a list of numbers as input and returns a new list with the numbers in reverse order.
    """
    reversed_numbers = []
    while numbers:
        reversed_numbers.append(numbers.pop())
    return reversed_numbers

def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')

if __name__ == '__main__':
    main()
