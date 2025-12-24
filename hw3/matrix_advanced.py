import numpy as np
from dataclasses import dataclass

from matrix import Matrix


@dataclass
class MatrixAdvanced(np.lib.mixins.NDArrayOperatorsMixin):
    _data: list

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

    _HANDLED_TYPES_ = (Matrix, np.ndarray, list)

    def __hash__(self):
        return hash(super())

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES_ + (MatrixAdvanced, )):
                raise NotImplementedError()
        converted_inputs = []
        for inp in inputs:
            if isinstance(inp, (Matrix, MatrixAdvanced)):
                converted_inputs.append(inp.data)
            else:
                converted_inputs.append(inp)
        result = getattr(ufunc, method)(*converted_inputs, **kwargs)
        return type(self)(result)

    @property
    def shape(self):
        return (self._rows, self._cols)

    @property
    def size(self):
        return self._rows * self._cols
    
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
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

    def __str__(self):
        return f"Matrix:\n{self.data}\nShape: {self.shape}"

    def save_to(self, filename):
        result = ""
        for row in self._data:
            result += ' '.join(map(str, row))
            result += '\n'
        with open(filename, 'w') as f:
            f.write(result)
