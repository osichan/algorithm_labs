def zigzag_mn(n:int, m:int):
    result =[]

    for i in range(n):
        result.append([])
        for f in range(m):
            result[i].append(0)

    def left_bottom(number_to_add,x,y):
        result[x][y] = number_to_add
        if x == n - 1 and y == m - 1:
            return result
        if x == n-1:
            return right_top(number_to_add+1,x,y+1)
        elif y==0:
            return right_top(number_to_add+1,x+1,y)
        else:
            return left_bottom(number_to_add+1,x+1,y-1)


    def right_top(number_to_add,x,y):
        result[x][y]=number_to_add
        if x>=n-1 and y>=m-1:
            return result
        if y==m-1:
            return left_bottom(number_to_add+1,x+1,y)
        elif x==0:
            return left_bottom(number_to_add+1,x,y+1)
        else:
            return right_top(number_to_add+1,x-1,y+1)

    return right_top(1,0,0)


def  zigzag_array(array):
    n = array.__len__()
    m = array[0].__len__()
    result=[]

    def left_bottom(position_of_number, x, y):
        result.append(array[x][y])
        if x == n - 1 and y == m - 1:
            return result
        if x == n-1:
            return right_top(position_of_number + 1, x, y + 1)
        elif y==0:
            return right_top(position_of_number + 1, x + 1, y)
        else:
            return left_bottom(position_of_number + 1, x + 1, y - 1)


    def right_top(position_of_number, x, y):
        result.append(array[x][y])
        if x>=n-1 and y>=m-1:
            return result
        if y==m-1:
            return left_bottom(position_of_number + 1, x + 1, y)
        elif x==0:
            return left_bottom(position_of_number + 1, x, y + 1)
        else:
            return right_top(position_of_number + 1, x - 1, y + 1)

    return right_top(0,0,0)

if __name__ == "__main__":
    result_mn = zigzag_mn(3,6)
    print(result_mn)
    print("-----------------------------")

    result_array = zigzag_array([[1, 2, 6, 7, 12, 13], [3, 5, 8, 11, 14, 17], [4, 9, 10, 15, 16, 18]])
    print(result_array)