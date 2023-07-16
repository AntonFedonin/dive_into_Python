# Напишите функцию для транспонирования матрицы

def trans_matrix(mtr):
    trans_mtr = [[0 for j in range(len(mtr))] for i in range(len(mtr[0]))]
    for i in range(len(mtr)):
        for j in range(len(mtr[0])):
            trans_mtr[j][i] = mtr[i][j]

    return trans_mtr


matrix = [[1, 3], [9, 4], [5, 2]]

result_matrix = trans_matrix(matrix)
print(matrix)
print(result_matrix)
