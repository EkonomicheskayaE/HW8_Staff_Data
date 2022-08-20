import pandas as pd
from data_staff import data_staff

def data_staff():
    # print('Первоначальная база сотрудников: ')
    data = data_staff()
    data.to_csv('data_staff_first.csv', index=False)
    return data

# просмотр базы данных сотрудников

def print_data():
    print('База сотрудников:\n')
    # df = pd.read_csv('data_staff_first.csv')
    df = pd.read_csv('data_staff.csv')
    return df

# добавление сотрудника в базу данных

def data_add():
    data_add = pd.read_csv('data_staff.csv')
    print('Перед вами представлен текущий список сотрудников нашей организации:\n')
    print(data_add)
    print('\nКакую ещё информацию вы хотели в него бы внести?\n')
    new_row = {'Фамилия': input('Введите фамилию: '), 'Имя': input('Введите имя: '), 'Должность': input('Введите должность: '), 'Телефон': input('Введите номер телефона: '), 'Адрес': input('Введите адрес: ')}
    data_add = data_add.append(new_row, ignore_index=True)
    data_add.to_csv('data_staff.csv', index=False)
    print('\nДанные успешно сохранены!')
    return data_add

# удаление сотрудников

def data_del():
    data_del = pd.read_csv('data_staff.csv')
    print('Перед вами представлен весь список сотрудников нашей организации:\n')
    print(data_del,'\n')
    data_del = data_del.loc[data_del['Фамилия'] != input('Введите фамилию сотрудника, которого хотите удалить из списка: ')]
    data_del.to_csv('data_staff.csv', index=False)
    print('\nДанные успешно сохранены!')
    return data_del

# поиск сотрудников

def search_data():
    data = pd.read_csv('data_staff.csv')
    print('\nПеред вами представлены фамилии сотрудников, которые работают в нашей организации:\n')
    print(data['Фамилия'],'\n')
    print('Выберите id сотрудника, чтобы просмотреть его данные:\n')
    index = int(input('Какой индекс вы выберете: '))
    if index > 6:
        print('\nПросим прощения, но данные по этому сотруднику отсутствуют или его нет в списке!\n')
        print('Посмотрите ещё раз внимательнее на список:\n')
        print(data['Фамилия'],'\n')
        index = int(input('Какой индекс вы выберете: '))
    if index == 0:
        new0 = data.loc[0]
        print(new0)
    if index == 1:
        new1 = data.loc[1]
        print(new1)  
    if index == 2:
        new2 = data.loc[2]
        print(new2)
    if index == 3:
        new3 = data.loc[3]
        print(new3)
    if index == 4:
        new4 = data.loc[4]
        print(new4)
    if index == 5:
        new5 = data.loc[5]
        print(new5)
    if index == 6:
        new6 = data.loc[6]
        print(new6) 
                  
    

