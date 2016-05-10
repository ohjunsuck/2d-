import os
arr = [[0 for i in range(0, 10)]]

def find():
    pass
def pricesort():
    pass
def tastesort():
    pass
def distantsort():
    pass
def pirintAll():
    pass


def open(a,b):
    if(b=='1'):
        f1= open('삼겹살.txt')
        arr = f1.read().split()
        print(arr)
        os.system('cls')
    elif(b=='2'):
        f2= open('짜장면.txt')
        arr = f2.readline()
        print(arr)
        os.system('cls')
    elif(b=='3'):
        f3= open('치킨.txt')
        arr = f3.readline()
        print(arr)
        os.system('cls')



while(1):

    b = input("1.삼겹살 2.짜장면 3.치킨 : ")
    a = input("1.검색 2.가격순정렬 3.맛순정렬 4.거리순정렬 5.전체출력 : ")

    open(a, b)


