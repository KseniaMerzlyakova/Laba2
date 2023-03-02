#если смешать красный и желтый, то получится оранжевый;
#если смешать синий и желтый, то получится зеленый.
#Напишите программу, которая считывает названия двух основных цветов для смешивания.
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый»,
# то программа должна вывести сообщение об ошибке. В противном случае программа должна вывести название вторичного цвета,
# который получится в результате.
a = input('введите 1 цвет ')
b = input('введите 2 цвет ')
x = ""
y = 0
if (a) != ('красный') and str(a) != ('синий') and str(a) != ('желтый'):
    print('Error')
elif str (b) != ('красный') and str(b) != ('синий') and str(b) != ('желтый'):
    print('Error')
else:
   #for i in a:
    if str(a)==('красный') or str(b)==('красный') :
        collor_num1 = 10
    else:
        collor_num1 = 0
    if str(a)==('синий') or str(b)==('синий') :
        collor_num2 = 20
    else:
        collor_num2 = 0
    if str(a)==('желтый') or str(b)==('желтый') :
        collor_num3  =  30
    else:
        collor_num3 = 0
    collor_num = collor_num1 + collor_num2 + collor_num3

    if collor_num == 30:
      x = ('фиолетовый')
    elif collor_num == 40:
      x = ('оранжевый')
    elif collor_num == 50:
      x = ('зеленый')


print(x) #+ str(collor_num)+ "  "+ str(collor_num1)+"  "+ str(collor_num2)+ "  " +str(collor_num3))