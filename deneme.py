def hesap_makinesi():
    sayı1=int(input('Lütfen birinci sayıyı giriniz:'))
    işlem=input('Lutfen yapmak istediğiniz işlemi girin:')
    sayı2=int(input('Lutfen ikinci sayıyı giriniz:'))

    if işlem =='+':
        print(' Sonuç:',sayı1+sayı2)
        gecmis.append(f'''{sayı1}+{sayı2}={sayı1+sayı2}''')
    elif işlem=='-':
        print(' Sonuç:',sayı1-sayı2)
        gecmis.append(f'''{sayı1}-{sayı2}={sayı1-sayı2}''')
    elif işlem=='/':
        if  sayı2==0:
            print(' Sıfıra bolme yapılamaz...')
        else:
            print(' Sonuç:',sayı1/sayı2)
            gecmis.append(f'''{sayı1}/{sayı2}={sayı1/sayı2}''')
    elif işlem=='*':
        print(' Sonuç:',sayı1*sayı2)
        gecmis.append(f'''{sayı1}*{sayı2}={sayı1*sayı2}''')

gecmis=[]
while True:
    print(f'''...HESAP_MAKINESI...
    1.Hesap_makinesi
    2.Geçmiş
    3.Geçmişini sil
    4.Çıkış''')
    soru=int(input('Yapmak istediğiniz işlemi giriniz:'))
    if soru==4:
        break
    elif soru==2:
        for işlem in gecmis:
            print(işlem)
    elif soru==3:
        gecmis.clear
        print(' Geçmişinizi başarıyla sildik')

    elif soru==1:
        hesap_makinesi()
    else:
        print('Yanlış sayı girdiniz lutfen duzeltin')
    

    

         
    