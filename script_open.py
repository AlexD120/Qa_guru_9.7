with open('hello', 'w') as file: # - w перезаписывает файл
    file.write('Hello Word')

with open('hello2', 'a') as file: # - a добавляет текст в конце
    file.write('Hello Word\n')