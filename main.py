import random
import foo.bar




class MyClass:
    myvar = 10

    def function(self, vari):
        print("Calling constructor")
        self.myvar = vari


def randomNumbers():
    for x in range(3):
        yield random.random()


def main():
    myint = 32
    string = "Hello " + "World"
    print(string, "There are", myint, "apples in the basket")

    # print (1 + string)

    # List
    mylist = []
    mylist.append(10)
    mylist.append(20)

    # Convert to set
    set(mylist)

    for x in mylist:
        print(x)

    print(mylist[1])

    try:
        print(mylist[4])
    except IndexError:
        print("IndexError as expected")

    even_numbers = [2, 4, 6, 8]
    odd_numbers = [1, 3, 5, 7]
    all_numbers = odd_numbers + even_numbers
    all_numbers.sort()
    for x in all_numbers:
        print(x)

    name = "Adil"
    print("Hello, %s!" % name)
    print(name.count("d"), name[1:].upper(), name[::-1], name.split("A"))

    empty = []
    for x in empty:
        print(x)
    else:
        print("Nothing!")

    # cls = MyClass(29)
    # print("myvar == ", cls.myvar)

    # Imported from foo/bar.py

    foo.bar.helloBar()

    for rand in randomNumbers():
        print(rand)

    # List comprehensions
    sentence = "the quick brown fox jumps over the lazy dog"
    words = sentence.split()
    filtered_words = [word for word in words if word != "the"]
    word_lengths = [len(word) for word in filtered_words]
    print(filtered_words, word_lengths)

    # Varargs
    result = foo.bar.bar(1, 2, 3, action="sum", number="first")
    print("Result: %d" % result)


main()
