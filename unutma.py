
duz mantık class 
class araba: (araba class ıcıne alındı)
    marka='bmw '     (Araba markası gırıldı )
    renk='siyah'      ( renk gırıldı )
    mezıl='uzun menzil' ( menzılı girildi )

    kaanın_arabası=araba()                                               (kanın arabası olusturuluyoır )
    kaanın_arabsaı.marka='mersedes'                                       ( kaan arabasının markasını degıstırdı )
    print(kaanın_arabası.marka,kaanın_arabsı.renk,kaanın_arabası.mezil)  (markasını rengını vs yazırdı )






___class kodlaması initialzer method (ilk deger atama metodu ) ___

class araba     (arabayı class ıcıne alındı)
    sisfarı='2'     (sınıf degıskeni)
    def__init__(self,renk='siyah',marka='bmw',km='15'): 
    self.renk=renk                                                  (nesne degıskenleri)
    self.marka=marka
    self.km=km
    def arabanın_bılgılerını_goster(self): 
    print(f'''renk:{self.renk},marka:{self.marka},km:{self.km}''')
    
    durunun_arabası=araba()
    durunun_arabası.arabanın_bılgılerını_goster()

    durunun_arabası=araba('mavi','bmw','15')   (durunun arabasının rengı degıstı)
    durunun_arabası.arabanın_bılgılerını_goster()
    
    print('sisfarı saysısı',sisfarı)
    



# setter    classda sadece yonetıcının belırledıgı krıterler (alıcı belırleyemez ) vip denebilir
kullanabilr_renk=[siyah,beyaz] 
def setter_renk(self,yeni_renk):
    if yeni_renk in (class adı).kullanabilr_renk:
        self.__renk=yeni_renk
    else:
        print('bu renk kullanıma uygun degıl ')





#getter   setterın ulasılmaz seyı yazdrımak ıcınıdr (degıstırmek ıcın degıl)
def get_renk(self):
    return self.__renk
#ulasırkende get_renk olarak ulasılacak




from abc import ABC,abstractmethod
class şekil(ABC):    #soyut sınıf tanımlama
    @abstractmethod
    def alan_hesapla(self):
        pass     #alt sınıflar  bu methodu mutlaka gercekleştırmelı
# alt sınıf 
class kare(şekil):
    def __init__(self,kenar):
        self.kenar=kenar

    def alan_hesapla(self):
        return self.kenar*self.kenar

#alt sınıf2
class daire(şekil):
    def __init__(self,yarıçap):
        self.yarıçap=yarıçap

    def alan_hesapla(self):
        return 3.14*(self.yarıçap)**2

#bu fonksıyon şekil arayuzune (alan hesapla metoduna) guvenerek çalışır
def şekil_alanı_yazdır(şekil):  
    print(f'''şeklin alanı {şekil.alan_hesapla()}''')

kare=(4)
daire=(5)
şekil_alanı_yazdır(kare)
şekil_alanı_yazdır(daire)