a = 15
b = 0
try:
    result = a/b
except ZeroDivisionError:
    result = 0
except TypeError:
    result = 0

print('результат деления = ' + str(result))

password = input("введите ваш пароль")
print(password)









