def power(number, exp):

    result = 1
    
    for _ in range(abs(exp)):
        result *= number

    if exp < 0:
        result = 1 / result

    return result


def main():
    try:
        number = float(input("Enter number: "))
    except:
        print("Invalid number input.")
        return
    try:
        exponent = int(input("Enter exponent: "))
    except:
        print("Invalid exponent input.")
        return
    
    try:
        result = power(number, exponent)
    except:
        print("Division by zero.")
        return

    print(f"Result: {result}")
    


if __name__=="__main__":
    main()