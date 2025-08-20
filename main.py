from check_odd import odd_or_even

def main():
    num = int(input("Enter the number to be check"))
    result = odd_or_even(num)
    print(f"{num} is {result}")

if __name__=="__main__":
    main()