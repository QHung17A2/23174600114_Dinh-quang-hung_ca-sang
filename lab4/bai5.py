
so = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

n = input("Nhập một số: ")

# In ra số bằng chữ tiếng Anh
english_words = [so[digit] for digit in n]
english_number = ' '.join(english_words)
print("Số bạn nhập bằng chữ tiếng Anh là:", english_number)