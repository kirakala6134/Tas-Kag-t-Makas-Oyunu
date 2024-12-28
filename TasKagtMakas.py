import random
User_Point=0
Computer_Point=0
print('Taş Kağıt Makas oyununa hoş geldiniz!')
for x in range(3):
          User_input=input('taşı seçmek istiyorsanız (taş) kağıtı seçmek istiyorsanız(kağıt) makası seçecekseniz(makas) yazınız:')
          computer=['Taş','Kağıt','Makas']
          computer_choice=random.choice(computer)
          if User_input=='taş' and computer_choice=='Taş':
                    print('sizin seçtiğiniz >',User_input, '\nbilgisayarın seçtiği >',computer_choice,'\n |durum berabere!|')
                    User_Point=User_Point+1 
                    Computer_Point=Computer_Point+1
                    print('sizin puanınız >',User_Point,'\nbilgisayarın puanı >',Computer_Point)
          elif User_input=='taş' and computer_choice=='Kağıt':
                    print('sizin seçtiğiniz >',User_input,'\nbilgisayarın seçtiği >',computer_choice,'\n |bilgisayar kazandı!|')
                    Computer_Point=Computer_Point+3
                    print('sizin puanınız >',User_Point,'\nbilgisayarın puanı >',Computer_Point)
          elif User_input=='taş' and computer_choice=='Makas':
                    print('sizin seçtiğiniz >',User_input,'\nbilgisayarın seçtiği >',computer_choice,'\n |tebrikler siz kazandınız!|')
                    User_Point=User_Point+3
                    print('sizin puanınız >',User_Point,'\nbilgisayarın puanı >',Computer_Point)
          elif User_input=='kağıt' and computer_choice=='Taş':
                    print('sizin seçtiğiniz >',User_input,'\nbilgisayarın seçtiği >',computer_choice,'\n |tebrikler siz kazandınız!|')
                    User_Point=User_Point+3
                    print('sizin puanınız >',User_Point,'\nbilgisayarın puanı >',Computer_Point)
          elif User_input=='kağıt' and computer_choice=='Kağıt':
                    print('sizin seçtiğiniz >',User_input,'\nbilgisayarın seçtiği >',computer_choice,'\n |durum berabere!|')
                    User_Point=User_Point+1 
                    Computer_Point=Computer_Point+1
                    print('sizin puanınız >',User_Point,'\nbilgisayarın puanı >',Computer_Point)
          elif User_input=='kağıt' and computer_choice=='Makas':
                    print('sizin seçtiğiniz >',User_input,'\nbilgisayarın seçtiği >',computer_choice,'\n |bilgisayar kazandı!|')
                    Computer_Point=Computer_Point+3
                    print('sizin puanınız >',User_Point,'\nbilgisayarın puanı >',Computer_Point)
          elif User_input=='makas' and computer_choice=='Taş':
                    print('sizin seçtiğiniz >',User_input,'\nbilgisayarın seçtiği >',computer_choice,'\n |bilgisayar kazandı!|')
                    Computer_Point=Computer_Point+3
                    print('sizin puanınız >',User_Point,'\nbilgisayarın puanı >',Computer_Point)
          elif User_input=='makas' and computer_choice=='Kağıt':
                    print('sizin seçtiğiniz >',User_input,'\nbilgisayarın seçtiği >',computer_choice,'\n |tebrikler siz kazandınız!|')
                    User_Point=User_Point+3
                    print('sizin puanınız >',User_Point,'\nbilgisayarın puanı >',Computer_Point)
          elif User_input=='makas' and computer_choice=='makas':
                    print('sizin seçtiğiniz >',User_input,'\nbilgisayarın seçtiği >',computer_choice,'\n |durum berabere|')
                    User_Point=User_Point+1 
                    Computer_Point=Computer_Point+1
                    print('sizin puanınız >',User_Point,'\nbilgisayarın puanı >',Computer_Point)
          else:
                  print('lütfen doğru kelimeyi giriniz!')
                  exit()
if User_Point>Computer_Point:
        print('|OYUN BİTTİ! SİZ KAZANDINIZ!| \nsiz toplamda',User_Point,'kadar puan topladınız! \n Bilgisayar ise toplamda',Computer_Point,'kadar puan topladı')       
elif User_Point==Computer_Point:
        print('|OYUN BİTTİ! BERABERE!| \nsiz toplamda',User_Point,'kadar puan topladınız! \n Bilgisayar ise toplamda',Computer_Point,'kadar puan topladı')
else:
        print('|OYUN BİTTİ! KAYBETTİNİZ!| \nsiz toplamda',User_Point,'kadar puan topladınız! \n Bilgisayar ise toplamda',Computer_Point,'kadar puan topladı')
