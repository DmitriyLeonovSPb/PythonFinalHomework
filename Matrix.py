#Добавьте к ним логирование ошибок и полезной информации. 
#Также реализуйте возможность запуска из командной строки с передачей параметров.
#В качестве примера - сравнение, умножение и сложение двух матриц
import logging
from random import randint
from Exception import ValFormatError
logging.basicConfig(filename='Loging.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} FUNCTION "{funcName}()" STRING {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
class Matrix:
    def __init__(self, matr):
        self._matr = matr
    def get_matrix(self):
        return self._matr
    def __add__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            logger.error(f'ERROR! Невозможно сложить матрицы, матрицы несовместимы!:  [{len(self._matr)}][{len(self._matr[0])}] !=  [{len(other._matr)}][{len(other._matr[0])}] ')
        else:
            new_matr = Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in range(len(self._matr))])
            logger.info(f' СЛОЖЕНИЕ:  {self._matr} + {other._matr} = {new_matr}  ')
            return new_matr
    def __mul__(self, other):
        if len(self._matr[0]) != len(other._matr):
            logger.error(f'ERROR! Невозможно перемножить матрицы, матрицы несовместимы!: [{len(self._matr)}][{len(self._matr[0])}] !=  [{len(other._matr)}][{len(other._matr[0])}]')
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in self._matr]
            logger.info(f' УМНОЖЕНИЕ:  {self._matr} * {other._matr} = {new_matr}  ')
            return Matrix(new_matr)
    def __eq__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            raise ValFormatError
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        return False
            logger.info(f' РАВЕНСТВО:  {self._matr} = {other._matr} ')
            return True
    def __repr__(self):
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i])
        return s
if __name__ == '__main__':
    matrix1 = [[0, 9, 8],
              [7, 6, 5],
              [4, 3, 2],
              [1, 1, 1]]
    matrix2 = [[0, 10, 7],
              [8, 9,  0],
              [4, 5,  6],
              [-10, 22, -6]]
    matrix3 = [[6, 5, 4, 3, 8],
              [8, 8, 4, 3],
              [1, 1, 8, 0]]
    matrix4 = [[7, 7, 8, 9, 1],
              [5, 6, 7, 8, 1],
              [2, 3, 4, -5, 90]]
    print ("Cложение матриц:")
    print(Matrix(matrix1) + Matrix(matrix2))
    print(Matrix(matrix3) + Matrix(matrix1))
    print("Cравнение матриц:")
    print(Matrix(matrix1) == Matrix(matrix1))
    print("Умножение матриц:")
    print(Matrix(matrix1) * Matrix(matrix3))
    print(Matrix(matrix1) * Matrix(matrix2))