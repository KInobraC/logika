books = {
    'Кінг': 'Воно',
    'Лондон': 'Біле ікло ',
    'Керролл': 'Аліса в країні чудес ',
    'Ліндгрен': 'Карлсон, який живе на даху '}

# Додай два найменування
# Видали одне найменування
books['Дефо'] = "Пригоди Робінзона Крузо"
books['Дюма'] = 'Граф Монте-Крісто'
del books['Кінг']
if 'Дефо' in books and 'Дюма' in books:
     print ('База оновлена!')
if ('Кінг' in books) == False:
     print ('Переваги оновлені')

#1. Додай в books нові популярні книги:
#- Дефо: Пригоди Робінзона Крузо,
#- Дюма: Граф Монте-Крісто.

#2. Видалити книгу:
#- Кінг: Воно.