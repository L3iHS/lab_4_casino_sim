class Chip:
    def __init__(self, value: int) -> None:
        self.value = max(1, int(value))  # значение фишки должно быть >=1
    
    def __repr__(self) -> str:
        return f'Chip(value={self.value})'
    
    def __add__(self, other: 'Chip') -> 'Chip':  # суммирование фишек
        if not isinstance(other, Chip):
            return NotImplemented
        
        return Chip(self.value + other.value)
    
    def __radd__(self, other: 'Chip') -> 'Chip':
        '''
        нужен если левый операнд не поддерживает сложение (__add__),
        то вызовется __radd__ правого операнда
        например при sum(), когда первый элемент 0 (int)
        '''
        if other == 0:
            return self
        
        if isinstance(other, Chip):
            return self.__add__(other)

        # дальше питон попробует другие варианты и если нужно, выдаст ошибку
        return NotImplemented