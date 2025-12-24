import numpy as np
from cachetools import cached, TTLCache


cache = TTLCache(maxsize=100, ttl=300)


class HashMixin:
    """
    Хэш вычисляется как сумма всех элементов, умноженная на количество строк и столбцов.
    """
    def __hash__(self):
        total_sum = np.sum(self._data)
        return hash(total_sum * self._rows * self._cols)


class Matrix(HashMixin):
    def __init__(self, data):
        if isinstance(data, list):
            if len(data) == 0 or not all(isinstance(row, list) for row in data):
                raise ValueError("Data must be a non-empty list of lists")
            if any(len(row) != len(data[0]) for row in data):
                raise ValueError("All rows must have the same length")
        elif isinstance(data, np.ndarray):
            data = data.tolist()
        else:
            raise NotImplementedError()

        self._data = data
        self._rows = len(data)
        self._cols = len(data[0])

    def __add__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if self._rows != other._rows or self._cols != other._cols:
            raise ValueError(f"Shape mismatch for add")
        result = [[] for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(self._cols):
                result[i].append(self._data[i][j] + other._data[i][j])
        return Matrix(result)

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if self._rows != other._rows or self._cols != other._cols:
            raise ValueError(f"Shape mismatch for mul")
        result = [[] for i in range(self._rows)]
        for i in range(self._rows):
            for j in range(self._cols):
                result[i].append(self._data[i][j] * other._data[i][j])
        return Matrix(result)

    @cached(cache)
    def __matmul__(self, other):
        if self._cols != other._rows:
            raise ValueError("Shape mismatch for matrix multiplication")
        result = [[0 for j in range(other._cols)] for i in range(self._rows)]
        for i in range(self._rows):
            for j in range(other._cols):
                for k in range(self._rows):
                    result[i][j] += self._data[i][k] * other._data[k][j]
        return Matrix(result)

    def save_to(self, filename):
        result = ""
        for row in self._data:
            result += ' '.join(map(str, row))
            result += '\n'
        with open(filename, 'w') as f:
            f.write(result)
