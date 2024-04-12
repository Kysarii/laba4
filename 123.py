import numpy as np
import matplotlib.pyplot as plt

K = int(input('Введите K: '))
while True:
    N = int(input('Введите N: '))
    if N % 2 ==0 and N >= 6:
        break
    else:
        print('Матрица должна быть четной и больше 6', '\n')

A = np.random.randint(-10, 11, (N, N))
E = A[:N//2, :N//2]
B = A[:N//2, N//2:]
D = A[N//2:, :N//2]
C = A[N//2:, N//2:]

F = np.copy(A)
print("Матрица A:\n", A, '\n')
max_E = -100
for i in range(len(E)):
    for j in range(len(E)):
        if j % 2 != 0:
            max_E = max(max_E, E[i][j])
print("Максимальный элемент:", max_E, '\n')

sum_E = 0
for i in range(len(E)):
    for j in range(len(E)):
        if i % 2 != 0:
            sum_E += E[i][j]
print("Сумма элементов:", sum_E, '\n')

if max_E > sum_E:
    F[:N // 2, :N // 2], F[N // 2:, N // 2:] = F[N // 2:, N // 2:], F[:N // 2, :N // 2]
else:
    F[:N//2, N//2:], F[N//2:, :N//2] = F[N//2:, :N//2], F[:N//2, N//2:]

det_A = np.linalg.det(A)
print("Определитель матрицы A: ", det_A, '\n')
sum_diag_F = np.sum(np.diag(F))
print("Сумма диагоналей матрицы F: ", sum_diag_F, '\n')
G = np.tril(A)
print("Нижняя треугольная матрица G:\n", G, '\n')
if det_A > sum_diag_F:
    result = (np.linalg.inv(A) * np.transpose(A)) - (K * np.linalg.inv(F))
else:
    result = (np.transpose(A) + G - np.transpose(F))*K #answer = ((np.linalg.inv(a) + g) - np.transpose(f) * k)
print("Результат вычислений:\n", result, '\n')

for i in range(N):
    plt.plot(F[i], label=f'Row {i + 1}')
plt.legend()
plt.title('Графики данных из матрицы F')
plt.xlabel('Столбцы')
plt.ylabel('Значения')
plt.show()


plt.title("Cоответсвие номера и квадрата элемента из первой строки ")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(range(0,N),F[0],linestyle="-",color="g")
plt.show()


plt.plot(sum_diag_F, marker='s')
plt.title("График суммы диагональных элементов матрицы F")
plt.grid(True)
plt.show()