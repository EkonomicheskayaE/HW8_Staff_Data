from logger import data_staff, print_data, data_add, data_del, search_data

def interface():
    print('Что вам нужно сделать?\n'
          '1. Просмотреть всю базу сотрудников, в том числе первоначальную\n'
          '2. Добавить сотрудника\n'
          '3. Удалить сотрудника\n'
          '4. Найти сотрудника\n')
    command = int(input("Введите номер операции: "))

    while command < 1 or command > 4:
        print('Номер операции введен некорректно!')
        command = int(input("Введите номер операции: "))

    if command == 1:
        # print(data_staff())
        print(print_data())
    elif command == 2:
        print(data_add())
    elif command == 3:
        print(data_del())
    elif command == 4:
        print(search_data())
    else:
        print('Что-то пошло не так!')

