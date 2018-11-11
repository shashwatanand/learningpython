# Q1 Use for, .split(), and if to create a Statement that will print out words that start with 's'

statement = "Print only the words that start with s in this sentence"

for word in statement.split() :
    if word[0] == "s" :
        print(word)


# Q2 Use range() to print all the even numbers from 0 to 10.
print(list(range(0, 11, 2)))

# Q3 Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

print([x for x in range(1, 51) if x % 3 == 0])