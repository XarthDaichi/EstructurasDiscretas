class Number:
    """
    >>> n = Number(-4.1)
    >>> print(n.value)
    -4.1
    """
    def __init__(self, value):
        """Uses property setter."""
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class Integer(Number):
    """
    >>> i = Integer(-4.1)
    >>> print(i.value)
    -4
    """
    @property
    def value(self):
        return super().value

    @value.setter
    def value(self, new_value):
        _value = int(new_value)
        super(Integer, type(self)).value.fset(self, _value)
