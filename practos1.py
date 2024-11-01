import random
 
# Определение уровней игры как словарь  
levels = {  
    1: {  
        "name": "Темный лес",  
        "description": (  
            "Ты попал(а) в темный лес. Тебе нужно выбраться из него, "  
            "но не заблудившись. Стоит плотная тишина, изредка раздаётся скрип ветвей."  
        ),  
        "puzzle": (  
            "Перед тобой три пути: налево, направо и прямо. "  
            "Выбери один из них, доверяясь своей интуиции."  
        ),  
        "correct_path": "налево",  
        "items": ["Древесина волшебной ивы"],  
        "actions": {  
            "налево": lambda: "Ты выбрал(а) путь налево, следуя за сломанными веточками. Молодец!",  
            "направо": lambda: "Ты наткнулся(лась) на гнездо дракона. Конец игры.",  
            "прямо": lambda: "Ты попадаешь в болото и тонешь. Конец игры.",  
        }  
    },  
    2: {  
        "name": "Глубокая пещера",  
        "description": (  
            "Ты находишься в глубокой пещере. Здесь темно, "  
            "и слышны страшные звуки, напоминающие рычание чудовищ."  
        ),  
        "puzzle": (  
            "Ты нащупал(а) три каменных таблички с надписями: 'север', 'юг', и 'восток'. "  
            "Куда ты решишь пойти в этой тьме?"  
        ),  
        "correct_path": "север",  
        "items": ["Волшебный светящийся камень"],  
        "actions": {  
            "север": lambda: "Ты освещаешь путь светящимся камнем и продвигаешься дальше, чувствуя себя увереннее.",  
            "юг": lambda: "Ты наткнулся на стену. Путь закрыт. Здесь нужно искать другой путь.",  
            "восток": lambda: "Ты слышишь странный шорох и убегаешь в страхе.",  
        }  
    },  
    3: {  
        "name": "Замок злого колдуна",  
        "description": (  
            "Ты добрался(ась) до замка злого колдуна. "  
            "Здесь очень мрачно, и ты чувствуешь его присутствие не только в воздухе, но и за углами замка."  
        ),  
        "puzzle": (  
            "На троне лежит волшебная палочка колдуна. "  
            "Используй все свои собранные вещи, чтобы победить колдуна и завершить это приключение."  
        ),  
        "correct_path": "атаковать",  
        "required_items": ["Древесина волшебной ивы", "Волшебный светящийся камень"],  
        "items": ["Волшебная палочка"],   
        "actions": {  
            "использовать предметы": lambda: "Ты собрал все предметы и создаёшь артефакт для победы над колдуном!",  
            "осмотреться": lambda: "В комнате стало тише, и напряжение окутывает тебя с каждой секундой.",  
            "атаковать": lambda: "Ты нападаешь на колдуна с помощью волшебной палочки и найденных ранее предметов и побеждаешь его!",  
        }  
    }  
} 

inventory = set() 
player_name = "" 
current_level = 1 
previous_levels = []  # Список для отслеживания предыдущих уровней 

# Начало игры 
def start_game(): 
    global inventory, current_level, player_name, previous_levels #здесь хранится состояние игры
    inventory.clear() 
    current_level = 1 
    previous_levels.clear()  # Очистка списка уровней 
    player_name = input("Введите ваше имя: ").strip() 
    print(f"Добро пожаловать в игру, {player_name}!") 
    play_game()  # Запуск основной игровой функции

# Отображения информации о текущем уровне
def show_level_info(level): 
    print(level["description"]) 
    print(level["puzzle"]) 
    print("Возможные действия:") 
    for action in level["actions"]: 
        print(f" - {action}") 
    print("") 

# Обработка действий 
def handle_action(level, user_input): 
    if user_input in level["actions"]: 
        action_function = level["actions"][user_input] 
        result = action_function() 
        print(result)  # Вывод результата действия
        return user_input == level["correct_path"]  # Проверяет, является ли путь правильным 
    else: 
        print("Некорректное действие. Попробуй еще раз.") 
        return False 

# Обновление инвентаря 
def update_inventory(level): 
    global inventory 
    items = level.get("items", []) 
    for item in items: 
        inventory.add(item) 
        print(f"Ты получил(а) новый предмет: {item}!") 

# Основная игровая функция 
def play_game():
    global current_level, previous_levels
    while True:
        level = levels[current_level]
        show_level_info(level)

        action = input("Выбери действие: ").strip().lower()
        if handle_action(level, action):
            update_inventory(level)
            previous_levels.append(current_level)  # Сохраняем предыдущий уровень
            if current_level < len(levels):  # Переход к следующему уровню
                current_level += 1
            else:  # Конец игры
                print(f"Поздравляю, {player_name}! Ты завершил игру!")
                break
        else:
            print("Попытайся снова.")

# Запуск игры
start_game()