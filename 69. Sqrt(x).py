class Solution:
    def mySqrt(self, x: int) -> int:
        # Если x меньше 2, корень от x равен самому x (0 и 1).
        if x < 2:
            return x
        
        # Инициализация диапазона для бинарного поиска.
        left, right = 2, x // 2
        
        while left <= right:
            mid = (left + right) // 2
            # Проверка, является ли mid квадратным корнем
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        # Когда цикл заканчивается, правый указатель указывает на наибольшее значение,
        # которое при возведении в квадрат не превышает x.
        return right
