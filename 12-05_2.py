file = open('text_3.txt', 'r', encoding='utf-8')
content = file.readlines()
print(f'Количество строк в файле - {len(content)}')
file = open('text_3.txt', 'r', encoding='utf-8')
content = file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
_file = open('text_3.txt', 'r', encoding='utf-8')
content = file.read()
content = file.readfiles()
print(f'Общее количество слов - {len(content)}')
file.close()