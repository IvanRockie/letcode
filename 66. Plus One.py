class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Преобразуем список цифр в число
        number = int(''.join(map(str, digits)))
        
        # Прибавляем 1
        number += 1
        
        # Преобразуем число обратно в список цифр и возвращаем
        return [int(digit) for digit in str(number)]
