""" Игра: угадай число """

import numpy as np

def game_core_v3(number:int=1) -> int:
    """Устанавливаем любое random число. Алгоритм нахождения:
        - Сначала сокращаем разницу между заданным и рандомным числом с шагом 10.
        - Как только разница становится меньше 10 - мы делаем шаг значением 1.
        
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    predict_number = np.random.randint(1, 101) # Предполагаемое число
    
    while number != predict_number:
        count += 1
        if number < predict_number:
            predict_number -= 10
        elif number-predict_number >= 10:
            predict_number += 10
        else:
            predict_number += 1

    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # Загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    return score
    
if __name__ == '__main__':
    # RUN
    score_game(game_core_v3)