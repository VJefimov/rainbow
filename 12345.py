def sort_values (valjund):
    rida=input("Введите цифры и буквы в произвольном порядкеx через запятую:" )
    '''fuktsioon mis sorteerib tähed ja numbrid'''
    uusrida=rida.replace(",","")
    print(uusrida)
    uusrida=sorted(uusrida)
    i=1
    for i in uusrida:
        print(i, end="")
    return valjund
print(sort_values("valjund"))
























        
        
        



 
