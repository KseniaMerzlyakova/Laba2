a = int(input('Введите номер места в вагоне '))
if (a) <= 0 or a >= 55 :
 print ('неправильное место')

if (a) % 2 == 0 and a <= 36 and a > 0:
   print('Верхнее')
if int(a) % 2 != 0 and a <= 36:
   print('Нижнее')

if a > 36:
    for i in range(37, 55):
       if int(a) == i:
           print('Боковое')