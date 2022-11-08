# Exercise #1
# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

def cube():
    print("Cubes!")
    c = 0
    for i in range(1, 50):
        c = i**3
        if c >= 1000:  
            break
        else:
            print(c)
cube()


# Exercise #2
# Get first prime numbers up to 100

def prime():
    print("\nPrimes:")
    for num in range(2, 101):
        count = 0
        for i in range(2, num//2 + 1):
            if num % i == 0:
                count += 1
                break

        if count == 0 and num != 1:
            print(f'{num}', end=" ")


prime()

# Exercise 3
# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors


def age_ask():
    print("\n\nAge:")
    question = "Hello there citizen! How old are you? "
    
    kids = """\nI see. You are a young one to take on the responsibility but
we need people like you nowadays. Welcome and good luck."""
    adult = """\nAha! You are indeed a full-fledged citizen. 
Don't let me disrupt your life, I'm sure you've got important work to do."""
    seniors = """\nAh! Perfect. I know you've worked long and hard
and I appreciate the contributions you've made to this society. Please. 
Rest a while and enjoy what you've wrought"""

    while True:
        
        try:
            if isinstance(age, str):
                if int(age) < 18:
                    print(kids)
                    break
                elif int(age) >= 18 and int(age) < 65:
                    print(adult)
                    break
                elif int(age) >= 65:
                    print(seniors)
                    break

        except (TypeError, ValueError):
            TypeError_retry =f"\n{age.title()}? Perhaps you misunderstood the question.  I'm looking for your age in years. "
            age = input(TypeError_retry)
            
        except (UnboundLocalError):
            age = input(question)

age_ask()