from translate import Translator

try:
    with open('./try.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as e:
    print('Please check your file path.')