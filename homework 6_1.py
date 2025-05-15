import string

letters = input("Enter two letters separated by a dash: ")
start, end = letters.split("-")

alphabet = string.ascii_letters
start_index = alphabet.index(start)
end_index = alphabet.index(end)
if start_index > end_index:
    start_index, end_index = end_index, start_index

result = alphabet[start_index:end_index + 1]
print(result)