import random
def main():
    randomlist = []
    for i in range(10):
        randomlist.append(random.randInt(0,100))
    print(randomlist)
    evenindex(randomlist)
    evenelement(randomlist)
    x = firstandlast(randomlist)

def evenindex(listofv):
    evenidex = []
    print("These are the even indexes: ", end="")
    for i in range(len(listofv)-1):
        if i%2 == 0:
            print(listofv[i] ,end=" ")
            evenindex.append(listofv[i])


def evenelement(listofv):
    evenel = []
    print("These are the even elements: ", end="")
    for i in listofv:
        if i%2 == 0 :
            print(listofv[i], end=" ")
            evenel.append(listofv[i])


def firstandlast(listofv):
    return (listofv[0], listofv[len(listofv)-1])
