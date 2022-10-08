# CRUD магазина на функциях 
# C - CREATE
# R - READ
# U - UPDATE
# D - DELETE


import datetime
data = [
    {
        'id': 1,
        'name': 'product1',
        'price': 100,
        'created_at': '2022, 10, 4',
        'is_active': True
    },
    {
        'id': 2,
        'name': 'product1',
        'price': 100,
        'created_at': '2022, 10, 4',
        'is_active': True
    },
    {
        'id': 3,
        'name': 'product1',
        'price': 100,
        'created_at': '2022, 10, 4',
        'is_active': True
    },
    {
        'id': 4,
        'name': 'product1',
        'price': 100,
        'created_at': '2022, 10, 4',
        'is_active': True
    }
]

def get_products():
    return data
def get_one_product(id):
    product = [i for i in data if id == i['id']]
    if product:
        return product[0]
    return 'нет такого товара!!!'

def post_product():
    max_id =max([i ['id'] for i in data ])
    new_data = {
        'id': max_id + 1,
        'name': input('введите имя товара: '),
        'price':int(input('введите цену: ')),
        'created_at': datetime.datetime.now(),
        'is_active' : True
    }
    data.append(new_data)
    return f'вы добавили новый товар:\n {new_data}'

def delete_product(id):
    delete_product = [i for i in data if i['id'] == id] #[{ }]
    if delete_product:
   
        data.remove(delete_product[0])
        return ' успешно удален!'
    return ' нет такого продукта! '

def update_product(id):
    update_product = [i for i in data if  i['id'] == id]
    if update_product:
        index_item = data.index(update_product[0])

        if input('хотите обновить имя: ') == 'да':
            data[index_item]['name'] == input('введите новое имя: ')
        if input('хотите обновить цену: ') == 'да':
            data[index_item]['price'] = int(input('введите новую цену: '))
            return 'удачно обновили!'
    return 'нет такого товара!'

def filter_odd_price():
    filter_price = [ i for i in data if i['price']<100]
    filter_price2 = [ i for i in data if i['price'] >=100]
    if input('хотите посмотреть товары ниже 100$?: ')=='да':
        return filter_price
    elif input('хотите посмотреть товары выше 100$ ?: ') == 'да':
        return filter_price2
    else:
        return 'удачного вам дня'

def filter_statuss():
    filter_status = [i for i in data if i['is_active']==True]
    filter_status2 = [i for i in data if i['is_active']==False]
    if input('хотите получить товар который продается?: ') == 'да':
        return filter_status
    elif input('хотите получить список товаров которых нет в наличии?: ') == 'да':
        return filter_status2
    else:
        return 'удачного вам дня!!'

def page():
    count = 0
    for i in data:
        count += 1
    x = int(input("Введите сколько элементов хотите посмотреть?\n"))
    if x > count:
        print('Ошибка!')
    else:
        for i in range(0, x):
            print(data[i])



def main():
    print('привет вот функционал:\n 1 - получить все товары\n 2 - получить определенный товар\n 3 - создать товар\n 4 - удалить товар\n 5 - обновить товар \n6- фильтрация по цене \n7 - фильтрация по статусу \n8 - пагинация')
    method = input(' введите число: ')
    if method == '1':
        print(get_products)
    elif method == '2':
        id = int(input(' введи id товаров'))
        print(get_one_product(id))
    elif method == '3':
        print(post_product)
    elif method == '4':
        id = int(input('введите id который хотите удалить: '))
        print(delete_product(id))
    elif method == '5':
        id = int(input('введите id товара который хотите обновить: '))
        print(update_product(id))
    elif method == '6':
        print(filter_odd_price())
    elif method == '7':
        print(filter_statuss())
    elif method == '8':
        print(page())
    else:
        print('нет такого функционала')



if __name__ == '__main__':
    main() 
