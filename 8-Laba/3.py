# 12. Створити клас для зберігання комплексних чисел.
# Реалізувати операції над комплексними числами: додавання, віднімання,
# множення, ділення, пару, зведення в ступінь, добування кореня.
# Передбачити можливість зміни форми запису комплексного числа: алгебраїчна форма,
# тригонометрическая форма, експоненціальна форма.
import math
class ComplexNum:
    real, i = 0, 0,
    φ, z = None, None

    def __init__(self, real: float, i: float):
        self.real = real
        self.i = i
        self.arithmetic_to_trigonometric()

    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.i + other.i)

    def __sub__(self, other):
        return ComplexNum(self.real - other.real, self.i - other.i)

    def __mul__(self, other):
        return ComplexNum((self.real * other.real - self.i * self.i), (self.real * other.i + other.real * self.i))

    def __truediv__(self, other):
        return ComplexNum((self.real * other.real + other.i * other.i) / (other.real ** 2 + other.i ** 2),
                          (other.real * self.i - self.real * other.i) / (other.real ** 2 + other.i ** 2))

    def __pow__(self, other: int):
        return ComplexNum((self.z ** other) * math.cos(other * self.φ), (self.z ** other) * math.sin(other * self.φ))

    def get_roots(self, base):
        roots = []
        for k in range(0, base + 1):
            complex_root = ComplexNum(math.sqrt(self.z) * (math.cos(self.φ + 2 * math.pi * k) / base),
                                      math.sqrt(self.z) * (math.sin(self.φ + 2 * math.pi * k) / base))
            roots.append(complex_root)
        return roots

    def arithmetic_to_trigonometric(self):
        self.φ = math.atan(self.i / self.real)
        # print(self.real ** 2)
        self.z = math.sqrt((self.real ** 2) + (self.i ** 2))
        # return self.φ, self.z

    def print_arithmetic(self):
        print(f'{self.real} + {self.i}i')

    def print_trigonometric(self):
        print(f'{self.z}*(cos{self.φ} + isin{self.φ})')

    def print_expo(self):
        print(f'|${self.z}|e^(i{self.φ})')


complexNum = ComplexNum(1, math.sqrt(3))
complexNum.print_trigonometric()