# 1-Сформувати список з 30 випадкових цілих чисел від -100 до + 100.
# Знайти максимальний елемент списку і його порядковий номер. Отримати
# інший список, що складається тільки з непарних чисел вихідного списку
# або повідомити, що таких чисел немає. Отриманий список вивести в
# порядку зменшення елементів.

#Подключаю библиотеку для рандомных чисел
import random
#Создаю лист с наборм 30-ти рандомных чисел
random_list = [random.randrange(-100,100) for i in range(30)]
#Вывожу итог в консоль
print("\nСлучайный список чисел от -100 до 100: ", random_list)
#проходит поиск макс. значения в списке
max_element = max(random_list)
#поиск индекса макс. значения в списке
position = random_list.index(max_element)
# вывод индекса элемента
print("\nМаксимальное значение из списка: ", max_element, "\nна позиции: ", position + 1)
#создаю новый лист
new_list=[]
# обращаемся к элементам старого списка и говорим, если элемент является нечётным, то мы добавляем элемент этот в конец нового списка
for element in random_list:
    if (element % 2) == 1:
        new_list.append(element)
# если в список не заносится никакое число, то выскакивает надпись, что нет никаких нечётных чисел
if len(new_list) == 0:
  print("\nнет ни одного нечетного числа")
# если длина меняется, то те находящиеся числа сортируются по убыванию и выводится новый список
else:
  new_list.sort(reverse=True)
  print("\nНовый список: ", new_list)
#Извиняюсь что не выполнил задачу в git но я его не понимаю и он мне противен
