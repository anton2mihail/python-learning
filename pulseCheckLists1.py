def main():
    x = listenter([2,5,12,7,8,0,-1,2,2,3,4])
    print(x)
#etc


def listenter(mains):
    even = []
    odd = []
    count = 0
    while count < len(mains):
        if mains[count]%2 == 0:
            even.append(mains[count])
            count+= 1
        elif mains[count]%2 != 0:
            odd.append(mains[count])
            count+=1
        else:
            raise ArithmeticError("WHY THO")
            continue
    print(sorted(even))
    print(sorted(odd))
    return min(odd)+max(even)


main()