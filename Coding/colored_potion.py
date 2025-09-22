#pip install colorama
import random
import os
from colorama import init, Fore, Style

# Цвета активируем
init(autoreset=True)

# Начальные ингредиенты
avaliable = ['чешуя дракона', 'корень мандрагоры', 'перо совы', 'сердце дриады',
             'палец огра', 'хвост хамелеона', 'носик комара', 'крыло летучей мыши',
             'мех вендиго', 'мед', 'горсть цветов', 'слеза единорога']

# Рецепты: 
recipes = {
    tuple(sorted(['мед', 'горсть цветов'])): 'зелье здоровья',
    tuple(sorted(['чешуя дракона', 'палец огра'])): 'зелье силы',
    tuple(sorted(['слеза единорога', 'перо совы'])): 'зелье левитации',
    tuple(sorted(['сердце дриады', 'корень мандрагоры'])): 'зелье буйного роста',
    tuple(sorted(['чешуя дракона', 'корень мандрагоры'])): 'зелье защиты',
    tuple(sorted(['крыло летучей мыши', 'носик комара'])): 'зелье вампиризма',
    tuple(sorted(['горсть цветов', 'сердце дриады'])): 'зелье вечного цветения',
    tuple(sorted(['хвост хамелеона', 'перо совы'])): 'зелье невидимости',
    tuple(sorted(['мех вендиго', 'перо совы'])): 'зелье теплоты'
}

def load_custom_recipes():
    if not os.path.exists('recipes.txt'):
        return
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(' = ')
            if len(parts) == 2:
                ing_list, potion_name = parts
                ing1, ing2 = [x.strip().lower() for x in ing_list.split(', ')]
                key = tuple(sorted([ing1, ing2]))
                recipes[key] = potion_name.strip()
                for ing in key:
                    if ing not in avaliable:
                        avaliable.append(ing)

def save_recipe_to_file(ing1, ing2, name):
    key = tuple(sorted([ing1, ing2]))
    with open('recipes.txt', 'a', encoding='utf-8') as f:
        f.write(f'{key[0]}, {key[1]} = {name.strip()}\n')

def show_ingredients():
    print(Fore.YELLOW + '\n📦 Доступные ингредиенты:')
    for i, item in enumerate(avaliable, 1):
        print(Fore.YELLOW + f'{i}. {item}')
    print('')

def add_custom_recipe():
    add = input(Fore.CYAN + 'Хочешь добавить свой рецепт в книгу зелий? (да/нет): ').strip().lower()
    if add == 'да':
        ing1 = input('Введи первый ингредиент: ').strip().lower()
        ing2 = input('Введи второй ингредиент: ').strip().lower()

        if ing1 == ing2:
            print(Fore.RED + '⚠️ Рецепт должен содержать два разных ингредиента.')
            return

        name = input('Как будет называться зелье?: ').strip()

        key = tuple(sorted([ing1, ing2]))

        if key in recipes:
            print(Fore.LIGHTBLACK_EX + 'Такой рецепт уже существует!\n')
            return

        recipes[key] = name

        for ing in key:
            if ing not in avaliable:
                avaliable.append(ing)

        save_recipe_to_file(ing1, ing2, name)
        print(Fore.GREEN + f'✅ Записано: {key[0]} + {key[1]} = {name}\n')

def magic_potion(ing1, ing2):
    color_names = ['радужный', 'огненный', 'чёрный', 'зелёный', 'алый', 'синий', 'белый', 'сияющий', 'золотой']
    potion_color = random.choice(color_names)
    key = tuple(sorted([ing1.strip().lower(), ing2.strip().lower()]))

    if key in recipes:
        return Fore.MAGENTA + f'✨ Твоё зелье окрасилось в {potion_color} цвет. Ты создала {recipes[key]}!'
    else:
        return Fore.RED + f'💀 Хм... Твоё зелье из {ing1} и {ing2} стало болотного цвета... Лучше не пробовать!'

def brew_loop():
    while True:
        print(Fore.BLUE + '\n🔮 --- Новый виток варева ---')
        ing1 = input('Добавь первый ингредиент в котёл (или "очистить"): ').strip().lower()
        if ing1 == 'очистить':
            print(Fore.LIGHTBLACK_EX + 'Ты выливаешь содержимое котла... Он снова чист.')
            continue

        ing2 = input('Теперь второй ингредиент (или "очистить"): ').strip().lower()
        if ing2 == 'очистить':
            print(Fore.LIGHTBLACK_EX + 'Ты передумала. Варево не завершено.')
            continue

        if ing1 == ing2:
            print(Fore.RED + '⚠️ Нельзя использовать два одинаковых ингредиента!')
            continue

        print(magic_potion(ing1, ing2))

        again = input(Fore.CYAN + '\nСварить ещё одно зелье? (да/нет): ').strip().lower()
        if again != 'да':
            print(Fore.LIGHTBLUE_EX + 'Ты тушишь огонь под котлом... Лаборатория уходит в тень.')
            break

def rpg_menu():
    while True:
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + '''
╔════════════════════════════════╗
║   🧪 Школа Магии: Алхимия RPG  ║
╠════════════════════════════════╣
║ 1. Посмотреть ингредиенты     ║
║ 2. Сварить зелье              ║
║ 3. Добавить новый рецепт      ║
║ 4. Выйти                      ║
╚════════════════════════════════╝
''')

        choice = input(Fore.CYAN + 'Выбери действие (1-4): ').strip()

        if choice == '1':
            show_ingredients()
        elif choice == '2':
            brew_loop()
        elif choice == '3':
            add_custom_recipe()
        elif choice == '4':
            print(Fore.GREEN + '🧳 До новых встреч, юная ведьма!')
            break
        else:
            print(Fore.RED + '🚫 Неверный выбор. Попробуй ещё раз.')

# Запуск
load_custom_recipes()
rpg_menu()
