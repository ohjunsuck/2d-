# -*- coding: utf-8 -*-
import urllib.request
from urllib.parse  import quote
import xml.etree.ElementTree as etree


class Data:
    CONTINENT =1
    CONTRYNAME =2
    CONTRYENAME =3
    def __init__(self):
        self.basic = '0'
        self.targetDt = None
        self.conti=None
        self.name=None
        self.ename=None
        self.test='ERALdzlI%2FkiXZqCCA3LW1n7E3Mv7uY5uR52OlH5KGT7gJNXQA2wQOJoKYTGcL5w9%2Fce7EpSuU%2F%2FDb7kiGehAZg%3D%3D&numOfRows=999'
    def parse(self):
        self.url = " http://apis.data.go.kr/1262000/CountryBasicService/getCountryBasicList?ServiceKey=%s" % (self.test)
        data = urllib.request.urlopen(self.url).read()
        self.filename = "kkk" + ".xml"
        f = open(self.filename, "wb")
        f.write(data)
        f.close()
        self.tree = etree.parse(self.filename)
        self.root = self.tree.getroot()

    def printInfo(self,menu):
        self.select_menu=menu
        if self.select_menu == self.CONTINENT:
            for response in self.root.iter("response"):
                for item in response.iter("item"):
                    print('대륙\t: '+item.findtext('continent'))
        elif self.select_menu == self.CONTRYNAME:
            for response in self.root.iter("response"):
                for item in response.iter("item"):
                    print('나라이름\t: '+item.findtext('countryEnName'))
        elif self.select_menu == self.CONTRYENAME:
            for response in self.root.iter("response"):
                for item in response.iter("item"):
                    print('영어이름\t: '+item.findtext('countryEnName'))
                    #print('기본정보\t: '+item.findtext('basic'))

def main():

    data = Data()


    while(1):
        menu = 0
        name=None
        conti=None
        ename = None
        print("------------메뉴-------------")
        print("1. 대륙별")
        print("2. 국가별")
        print("3. 영문 국가별")
        print("------------------------------")

        while(menu < 1 or menu > 3):
            menu = int(input("메뉴를 선택하세요:  "))
            print('\n\n')
            data.parse()
        if menu == data.CONTINENT:
            data.printInfo(menu)

        elif menu == data.CONTRYNAME:
            data.printInfo(menu)

        elif menu == data.CONTRYENAME:
            data.printInfo(menu)




if __name__ == "__main__":
    main()

