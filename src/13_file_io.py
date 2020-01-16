"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE


def read():
    f = open("foo.txt", "r")
    f1 = f.readlines()
    for x in f1:
        print(x)


if __name__ == "__main__":
    read()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE


def write():
    f = open("bar.txt", "w+")
    for i in range(3):
        f.write("This is line %d\r\n" % (i+1))
    f.close()
    # Open the file back up and read the contents
    f = open("bar.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        print(contents)
    f2 = f.readlines()
    for x in f2:
        print(x)


if __name__ == "__main__":
    write()
