Лабораторная работа №4 С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для отладки использовать не случайное заполнение, а целенаправленное. Вид матрицы А: E B C D 
Вариант 16.	Формируется матрица F следующим образом: скопировать в нее А и  если в Е максимальный элемент в нечетных столбцах больше, чем сумма чисел в нечетных строках, то поменять местами С и В симметрично, иначе В и Е поменять местами несимметрично. При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A:(-1)*A:T – K * F:(-1), иначе вычисляется выражение (A:Т +G-F:Т)*K, где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А, F и все матричные операции последовательно.
