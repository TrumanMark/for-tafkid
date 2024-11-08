# Функция для вычисления детерминанта матрицы
def calculate_determinant(matrix):
   
    if len(matrix) == 1:
        return matrix[0][0]
    
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0

    for f in range(len(matrix)):
        
        minor = [row[:f] + row[f+1:] for row in matrix[1:]]
        
        det += ((-1) ** f) * matrix[0][f] * calculate_determinant(minor)
    
    return det

n = int(input("Введите размер матрицы n: "))

matrix = []
print("Введите элементы матрицы:")

for i in range(n):
    row = list(map(float, input(f"Введите элементы {i+1}-й строки через пробел: ").split()))
    matrix.append(row)

det = calculate_determinant(matrix)

print(f"Детерминант матрицы равен: {det:.2f}")
