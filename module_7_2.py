def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding= 'utf-8')
    kol = 0
    string_positions = {}
    for string in strings:
        kol += 1
        start = file.tell()
        file.write(string + '\n')
        string_positions[(kol, start)] = string
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
