a = input('Введите пароль: ')

is_numeric = False
is_lower = False
is_spec = False
is_upper = False

for x in a:
    if x.isnumeric():
        is_numeric = True
    elif x.islower():
        is_lower = True
    elif x.isupper():
        is_upper = True
    elif x in "@#%&":
        is_spec = True

if len(a) > 4 and is_numeric and is_upper  and is_lower and is_spec:
   print('Ок')
else:
   print('no')