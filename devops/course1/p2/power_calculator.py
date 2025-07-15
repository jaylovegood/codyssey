def power(number, exp):

    result = 1
    
    for _ in range(exp):
        result *= number

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
    
    result = power(number, exponent)
    print(f"Result: {result}")
    


if __name__=="__main__":
    main()