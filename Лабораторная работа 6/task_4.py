import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    str_ = ""
    with open(filename) as f: #Запись файла в виде строки
        for line in f:
            str_ += line
    arr = list(filter(None, str_.split("\n"))) #Разделение файла на строки и фильтрация пустых строк (запись в массив)
    for i in range(len(arr)):
        arr[i] = arr[i].split(",") #Разделение строк на слова, перезапись элементов массива
    Arr = []
    for i in range(1, len(arr)):
        dct = {}
        for j in range(len(arr[i])): #Создание словаря для каждой строки
            dct[arr[0][j]] = arr[i][j]
        Arr.append(dct)
    return Arr


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
#end
