class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        lowercase_letters = list(string.ascii_lowercase)
        result = []
        shift_array = [0] * (len(s) + 1) # Сумируем сдвиги для каждого shifts
        for i,j,k in shifts:
            k = 1 if k == 1 else -1
            shift_array[i] += k
            shift_array[j + 1] -= k
        shift_array = accumulate(shift_array)
        for i, [char,shift] in enumerate(zip(s,shift_array)):
            current_index = lowercase_letters.index(char)  # Найти индекс текущей буквы
            # Для каждого символа из shifts берем соответствующий сдвиг
            count_char = ord(char) - 97
            new_index = count_char + shift
            result.append(lowercase_letters[new_index % 26]) # Новый символ в результат 
        return ''.join(result) 
