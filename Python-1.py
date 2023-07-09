def solution(inp):
    buyuk = []
    for x in range(len(inp)-1):
        carpma = inp[x]*inp[x+1]
        buyuk.append(carpma)
        print(carpma)
    print("en büyük çarpma :")
    return max(buyuk)

inp = [5,6,9,2,7,5]
print(solution(inp))