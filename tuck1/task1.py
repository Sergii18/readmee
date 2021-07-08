# Створити програму, яка на вхід приймає рядок, та виділяє з нього всі
# числа в окремий масив, після чого програма друкує рядок без чисел. і
# масив чисел. Змінити цей рядок таким чином, щоб кожне слово в ньому,
# починалось і закінчувалось великою літерою. Знайти максимальне
# значення в масиві чисел, а всі інші числа піднести до степеню по їх
# індексу, та записати в інший масив.



import re
row=input("\nВведите свою строку: ")
print("\nВаша строка: ", row)
extract_letter=" ".join(re.split("[0-9]+", row))
extract_number="".join(re.split("[a-zA-Z]+", row))
extract_com_let=", ".join(extract_letter.split())
extract_com_num=", ".join(extract_number.split())
print("\nВсе номера: ", str(extract_com_num))
print("\nВсе слова между цифрами: ", str(extract_com_let))
for let in extract_letter.split():
    print("\nЗаглавные первые и последние буквы каждого слова: ", let[0].upper() + let[1:-1].lower() + let[-1].upper(),end="\n") 
new_num_max=list(map(int, extract_number.split()))
max_num=max(new_num_max)
print("\nМаксимальный элемент из чисел: ", max_num)
for element in new_num_max:
    if element != max_num:
        element=element**new_num_max.index(element)
        print("\nстепень числа к его индексу: ", element)
    else:
        continue
