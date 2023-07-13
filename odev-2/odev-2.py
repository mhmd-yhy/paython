#SORU-1
def solution(lst):
    # Listeyi sıralamak
    b = sorted(lst)
    print(b)
    for x in b:
        if not b.__contains__(x + 1):
            return (x + 1)

#a = [0,-1,-2,-3,-4]
#a = [1,2,3,5,7,8,9]
a = [1,7,10,5,-1,8,9,0]
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