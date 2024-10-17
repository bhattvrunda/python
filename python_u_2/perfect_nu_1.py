#Find the  perfect numbers.(A number is perfect if the sum of its proper divisors equals itself.EG:28=1+2+4+7+14)
#This is Perfect number
def is_perfect_number(n):
    # Calculate the sum of proper divisors
    proper_divisors = [i for i in range(1, n) if n % i == 0]
    sum_of_divisors = sum(proper_divisors)

    # Check if the sum of proper divisors is equal to the number
    if sum_of_divisors == n:
        return proper_divisors
    else:
        return None

def main():
    number = 28# You can change this to any number you want to check
    divisors = is_perfect_number(number)

    if divisors is not None:
        divisors_string = '+'.join(map(str, divisors))
        print(f"{number} = {divisors_string}")
    else:
        print(f"{number} is not a perfect number.")

if __name__ == "__main__":
    main()

#This program is from user input values.
#def is_perfect_number(n):
    # Calculate the sum of proper divisors
    #proper_divisors = [i for i in range(1, n) if n % i == 0]
    #sum_of_divisors = sum(proper_divisors)

    # Check if the sum of proper divisors is equal to the number
    #if sum_of_divisors == n:
        #return proper_divisors
    #else:
        #return None

#def main():
    #try:
        #number = int(input("Enter a positive integer: "))
        #if number <= 0:
            #print("Please enter a positive integer.")
            #return

        #divisors = is_perfect_number(number)

        #if divisors is not None:
            #divisors_string = '+'.join(map(str, divisors))
            
            #print(f"{number} = {divisors_string}")
        #else:
            #print(f"{number} is not a perfect number.")
    #except ValueError:
        #print("Invalid input. Please enter a valid positive integer.")

#if __name__ == "__main__":
    #main()
