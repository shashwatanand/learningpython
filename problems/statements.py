# Q1 Use for, .split(), and if to create a Statement that will print out words that start with 's'

statement = "Print only the words that start with s in this sentence"

for word in statement.split() :
    if word[0] == "s" :
        print(word)

print("###############################################################################################")
# Q2 Use range() to print all the even numbers from 0 to 10.
print(list(range(0, 11, 2)))

print("###############################################################################################")
# Q3 Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

print([x for x in range(1, 51) if x % 3 == 0])

print("###############################################################################################")

# Q4 Write a program that prints the integers from 1 to 100. But for multiples of 
# three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".


for num in range(1, 101) :
    if num % 3 == 0 and num % 5 == 0 :
        print("FizzBuzz")
    elif num % 3 == 0 :
        print("Fizz")
    elif num % 5 == 0 :
        print("Buzz")
    else :
        print(num)


print("###############################################################################################")
#@Q5 Write a function that capitalizes the first and fourth letters of a name

def capFirstAnadFourthLetter(name) :
    if (len(name) > 3) :
        return name[:3].capitalize() + name[4:].capitalize()
    else :
        return "Input is too short"

print(capFirstAnadFourthLetter("shashwatanand"))

print("###############################################################################################")

#Q6 Given a sentence, return a sentence with the words reversed

def reverse_sentance(sentence) :
    return " ".join(sentence.split()[::-1])

print(reverse_sentance("I am good person"))

print("###############################################################################################")

#Q7 Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(input) :
    for index in range(0, len(input) - 1) :
        if input[index:index+2] == [3, 3] :
            return True
    return False


print(has_33([1, 3, 1, 3]))
print(has_33([1, 3, 3]))
