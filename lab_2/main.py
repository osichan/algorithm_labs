def max_hamsters(S, C, hamsters):
    for number_of_hamsters in range(C, 0, -1):
        food_per_hamster = []
        food_for_hamsters = 0
        is_correct = True

        for hamster in hamsters:
            food_per_hamster.append(hamster[0] + hamster[1] * (number_of_hamsters - 1))

        food_per_hamster.sort()

        for hamster in range(number_of_hamsters):
            if food_for_hamsters + food_per_hamster[hamster] > S:
                is_correct = False
                break
            food_for_hamsters += food_per_hamster[hamster]

        if is_correct:
            return number_of_hamsters

    return 0

def s_for_all_hamsters(C,hamsters):
    all_food=0
    for hamster in hamsters:
        all_food+=hamster[0] + hamster[1] * (C - 1)

    return all_food

# Приклад 1
S1 = 32
C1 = 3
hamsters1 = [[1, 2], [3, 4], [5, 6]]
print(max_hamsters(S1, C1, hamsters1))  # Результат: 2

print(s_for_all_hamsters(3,[[1, 2], [3, 4], [5, 6]]))
