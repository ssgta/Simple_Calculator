# A simple calculator for addition, subtraction, multiplication, and division.

def main():
    # Initialise sum as first number input
    while True:
        try:
            sum = float(input("Number: "))

        except ValueError:
            print("Please type a number.")

        else:
            break

    # Until '=' operator is sent, continue performing calculation
    while True:
        operator = input("Operator (+ - / * =): ")
        if operator == "=":
            break
        try:
            num = float(input("Number: "))

        except ValueError:
            print("Please type a number.")

        else:
            match operator:
                case "+" :
                    sum += num
                case "-" :
                    sum -= num
                case "/" :
                    sum /= num
                case "*" :
                    sum *= num
                case _:
                    print(f"Invalid operator: {operator}")
                    exit()

    # Print final sum
    print(sum)
    exit()

if __name__ == '__main__':
    main()
