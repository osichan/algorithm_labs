def recursive_count_ways(matrix, w, h):
    def recursive(current_w, current_h):
        current_number_of_ways = 0
        current_symbol = matrix[current_h][current_w]
        if current_w == w - 1:
            if current_h == 0 or current_h == h - 1:
                return 1
            return 0

        current_number_of_ways += recursive(current_w + 1, current_h)

        for width in range(current_w + 1, w):
            for height in range(h):
                if (
                        not (height == current_h and width == current_w + 1)
                        and current_symbol == matrix[height][width]
                ):
                    current_number_of_ways += recursive(width, height)

        return current_number_of_ways

    number_of_ways = 0

    for start_symbol_height in range(h):
        number_of_ways += recursive(0, start_symbol_height)

    return number_of_ways


def dynamic_count_ways(matrix, w, h):
    result = 0
    iteration = 0
    results_array = [[0 for _ in range(w)] for _ in range(h)]
    results_array[0][w - 1] = 1
    results_array[h - 1][w - 1] = 1
    symbol_results_array = [{} for _ in range(w)]
    if matrix[0][w - 1] == matrix[h - 1][w - 1]:
        symbol_results_array[w - 1][matrix[0][w - 1]] = 2
    else:
        symbol_results_array[w - 1][matrix[0][w - 1]] = 1
        symbol_results_array[w - 1][matrix[h - 1][w - 1]] = 1

    for width_position in reversed(range(w - 1)):
        for height_position in range(h):

            if matrix[height_position][width_position] not in symbol_results_array[width_position]:
                symbol_results_array[width_position][matrix[height_position][width_position]] = 0

            if matrix[height_position][width_position] != matrix[height_position][width_position + 1]:
                if matrix[height_position][width_position + 1] not in symbol_results_array[width_position + 1]:
                    pass
                else:
                    symbol_results_array[width_position][matrix[height_position][width_position]] += \
                        results_array[height_position][width_position + 1]

                    results_array[height_position][width_position] = \
                        results_array[height_position][width_position + 1]

            for width in range(width_position + 1, w):
                iteration += 1
                if matrix[height_position][width_position] not in symbol_results_array[width]:
                    pass
                else:
                    results_array[height_position][width_position] += \
                        symbol_results_array[width][matrix[height_position][width_position]]
                    symbol_results_array[width_position][matrix[height_position][width_position]] += \
                        symbol_results_array[width][matrix[height_position][width_position]]

    print(iteration)
    print(symbol_results_array)
    for i in results_array:
        print(i)

    for i in symbol_results_array[0].keys():
        result += symbol_results_array[0][i]

    return result



def main(in_file, out_file):
    with open(in_file, "r") as file:
        w, h = map(int, file.readline().split())
        matrix = [file.readline().strip() for _ in range(h)]

    result = dynamic_count_ways(matrix, w, h)
    print(result)

    with open(out_file, "w") as file_out:
        file_out.write(str(result))


if __name__ == "__main__":
    main("ijones.in", "ijones.out")
