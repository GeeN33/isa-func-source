import re
"""
Сервис, который “повторяет” функционал командной строки линукса для обработки файлов.
"""

def loading_file():
    """
    Загрузка данных для дальнейшей работы
    """
    with open('data\\apache_logs.txt') as f:
        arr = []
        while True:
            try:
                #line = next(f)
                line = re.split("- -",next(f))
            except StopIteration:
                break
            arr.append(line)

    return arr

def search_true(x:list,strs:str):
    pattern = re.compile(strs)
    if 0 < len(pattern.findall(x[1])):
        return True
    else:
        return False

def filters(arr:list, strs:str):
    """
    Команда filter принимает в качестве аргумента строку, по которой нужно будет фильтровать
    """
    print(f'filter {strs}')
    arrs = list(filter(lambda x: search_true(x,strs), arr))
    for a in arrs:
        print(' '.join(a))
    return arrs

def maps(arr:list, col:int):
    """
    команду map <col> - этой командой мы изменяем формат исходных данных
    """
    print(f'map {col}')
    for a in arr:
        if len(a) > col:
            print(a[col])
        else:
            print(a[0])

def limit(arr:list,lim:int):
    """
    Команда limit выводит только необходимое количество строки из запроса
    """
    print(f'limit {lim}')
    count = lim if lim < len(arr) else len(arr)
    arrs = []
    for i in range(count):
         print(' '.join(arr[i]))
         arrs.append(arr[i])
    return arrs

def uniques(arr:list):
    """
    unique она оставляет только уникальные значения
    """
    print(f'unique -')
    arrs = []
    arrs2 = []
    for a in arr:
        if a[0] not in arrs:
            print(a[0])
            arrs.append(a[0])
            arrs2.append(a)
    return arrs2

def sorteds(arr:list, asc_desc:bool):
    """
    Команда sort сортирует данные в алфавитном порядке или в обратном алфавитном порядке
    """
    print(f'sorted {asc_desc}')
    dicts = {}
    arrs = []
    for i in range(len(arr)):
        dicts[i]= arr[i]
    dicts = sorted(dicts.values(), reverse=asc_desc)
    for d in  dicts:
        s = ' '.join(d)
        arrs.append(s)
        print(s)
    return arrs

def main():
    arr = loading_file()
    # 'filter POST | limit 3 | map 0  | unique'
    while True:
       commands = input('Введите команду(ы)\n')
       command_list = commands.split(' | ')
       if len(command_list) > 0:
           break
       else:
           print('Не верный формат')
    print(command_list)
    for c in command_list:
        com = c.split(' ')
        if com[0] == 'filter':
             arr = filters(arr, com[1])
        elif com[0] == 'limit':
            arr = limit(arr, int(com[1]))
        elif com[0] == 'unique':
            arr = uniques(arr)
        elif com[0] == 'sorted':
             arr =  sorteds(arr,bool(com[1]))
        elif com[0] == 'map':
             maps(arr,int(com[1]))
        else:
             print('Команда не наедена')

main()
