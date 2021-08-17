def greet (name):
    print("hello " + name)

greet("Katherine")

def countwords():
    filename=input("Enter your file name- ")
    numberofwords=0
    file=open(filename,'r')
    for i in file:
        words=i.split()
        numberofwords+=len(words)
    print(numberofwords)

countwords()
