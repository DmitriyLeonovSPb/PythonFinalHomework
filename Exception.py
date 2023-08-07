class ValFormatError(Exception):
    def __str__(self):
        return f"ERROR: Нельзя сравнивать матрицы разных размеров!"