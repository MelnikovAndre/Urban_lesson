class StepValueError(ValueError):
    pass

class Iterator:
    def __init__ (self,start,stop,step = 1):
        if step == 0:
            raise StepValueError("Шаг не может быть равен 0")
        self.start = start # Целое число, с которого начинается итерация.
        self.stop = stop # Целое число, на котором заканчивается итерация.
        self.step = step # Шаг, с которым совершается иерация.
        self.pointer = start # Указывает на текущее число в итерации (изначально start)
        self.step_sign = 1 if step > 0 else -1

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.pointer * self.step_sign > self.stop * self.step_sign:
            raise StopIteration()
        i = self.pointer
        self.pointer += self.step
        return i

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for j in iter2:
    print(j, end=' ')
print()

for j in iter3:
    print(j, end=' ')
print()

for j in iter4:
    print(j, end=' ')
print()

for j in iter5:
    print(j, end=' ')
print()