import random

# Для теста test_wrong_user_id
wrong_user_id = [
    0,
    'hulk9999',
    ',',
    '.6',
    ',7',
    '2,',
    '@#$^&',
    random.randint(13, 999),
]

# Для теста test_wrong_user_id и test_wrong_user_id
ids_wrong_user_id = [
    '0',
    'Буквы и цифры',
    'Запятая',
    'Точка с цифрой',
    'Запятая с цифрой',
    'Цифра с запятой',
    'Спец. символы',
    'Рандомное число от 13 до 999',
]

# Для теста test_create_user и test_update
valid_data_user = [{
    'name': 'morpheus',
    'job': 'leader',
},
    {
    'name': 'Keanu Charles Reeves',
    'job': 'the chosen one.',
},
    {
    'name': 'Keanu, Charles, Reeves',
    'job': 'the, chosen, one.',
},
    {
    'name': 1,
    'job': 1,
},
    {
    'name': -1,
    'job': -1,
},
    {
    'name': 0,
    'job': 0,
},
    {
    'name': '!..,,',
    'job': '.,@$%^^!',
},
]

# Для теста test_create_user и test_update
ids_valid_data_user = [
    'Валидные значения из документации',
    'Валидные значения из нескольких слов',
    'Валидные значения из нескольких слов с запятыми',
    'Валидные значения из положительных чисел',
    'Валидные значения из отрицательных чисел',
    'Валидные значения из нулей',
    'Валидные значения из спец. символов',
]

# Для теста test_create_with_wrong_payload и test_update_with_wrong_payload
not_valid_data_user = [
    {
        123: 'morpheus',
        1223: 'leader',
    },
    {
        'name': True,
        'job': False,
    },
    {
        'name': 'morpheus',
        'job': 'leader',
        'names': 'morpheus',
        'jobs': 'leader',
    },
    {},
    {
        ' name': 'morpheus',
        ' job': 'leader',
    },
    {
        'na me': 'morpheus',
        'jo b': 'leader',
    },
    {
        'name ': 'morpheus',
        'job ': 'leader',
    },
]

# Для теста test_create_with_wrong_payload и test_update_with_wrong_payload
ids_not_valid_data_user = [
    'Ключи из цифр',
    'Значения bool',
    'Дополнительные ключи',
    'Пустое тело',
    'В ключах пробелы в начале слова',
    'В ключах пробелы в середине слова',
    'В ключах пробелы в конце слова',
]

# Для теста test_register_successful и test_login_successful
valid_data_register = [{
    "email": "eve.holt@reqres.in",
    "password": "pistol",
},
    {
    "email": "eve.holt@reqres.in",
    "password": "pistol123",
},
    {
    "email": "eve.holt@reqres.in",
    "password": "@$%^pistol123!!,.234",
},
    {
    "email": "eve.holt@reqres.in",
    "password": " pistol123!! 234 ",
},
]

# Для теста test_register_successful и test_login_successful
ids_valid_data_register = [
    'Валидные значения из документации',
    'Пароль с цифрами',
    'Пароль со спец. симолами',
    'Пароль с пробелами',
]

# Для теста test_register_with_wrong_payload и test_login_successful_with_wrong_payload
not_valid_data_register = [{
    "email": "eve!,23423holt@gmail.com",
    "password": "pistol123",
},
    {
    "email": "eve!,23423holt@yandex.ru",
    "password": "pistol123!! 234",
},
    {
    "email": "t@mail.com",
    "password": " pistol123!! 234 ",
},
    {
    " em ail ": "t@mail.com",
    " pass word ": " pistol123!! 234 ",
},
    {
    "email": "t@mail.com",
    "password": " pistol123!! 234 ",
    "emaill": "t@mail.com",
    "passwordd": " pistol123!! 234 ",
},
    {
    "email": "eve.holt@reqres.in",
},
    {
    "password": "pistol",
},
]

# Для теста test_register_with_wrong_payload и test_login_successful_with_wrong_payload
ids_not_valid_data_register = [
    'Значение Email отличается от документации',
    'Значение Email отличается от документации',
    'короткий email',
    'Пробелы в ключах',
    'Дополнительные ключи',
    'В теле только email',
    'В теле только пароль',
]
