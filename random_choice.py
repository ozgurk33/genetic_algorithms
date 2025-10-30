import numpy as np
import random

def random_choice(array, size):
    array_len = len(array)
    if size > array_len:
        raise ValueError("Seçilecek eleman sayısı dizinin toplam eleman sayısından fazla olamaz!")
    counter = 0
    selected_numbers = []
    while counter != size:
        selected = array[random.randint(0,array_len-1)]
        if selected not in selected_numbers:
            selected_numbers.append(selected)
            counter += 1
    return selected_numbers

if __name__ == "__main__":
    np_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(random_choice(np_array, int(input("How many elements do you want to choose randomly on that array?: "))))


