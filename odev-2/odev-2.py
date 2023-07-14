#SORU-1
#SORU-1
def solution(lst):
    # Listeyi sıralamak
    b = sorted(lst)
    num = []
    print(f"b = {b}")
    for x in b:
         if not b.__contains__(x + 1) and x+1 < 0:
             num.append((x + 1)*-1)
         elif not b.__contains__(x + 1) and x+1 > 0:
             num.append(x+1)
    print(f"num = {num}")
    return min(num)

#a = [0,1,-7,-1,-2,-3,-4]
#a = [1,2,3,5,7,8,9]
a = [1,2,10,5,-7,-1,8,9,0]
birinci_soru_cevab = solution(a)

"""____________________________________________________________________________________________"""
#SORU-2
def tekrar_eden_karakter(txt):
    harflar = [*txt]
    harf_sayi = []
    for x in harflar:
        harf_sayi.append(harflar.count(x))
    for x in harflar:
        if harflar.count(x) == max(harf_sayi):
            return(x*max(harf_sayi))

#txt="helloooworlddd"
txt="abbcccddddeeeee"
ikinci_soru_cevab = tekrar_eden_karakter(txt)
