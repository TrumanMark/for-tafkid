#
def quick_sort(mass):
    
    if len(mass) <= 1:
        return mass
    
    pivot = mass[len(mass) // 2]
    
    left = [x for x in mass if x < pivot]
    middle = [x for x in mass if x == pivot]
    right = [x for x in mass if x > pivot]
    
    
    return quick_sort(left) + middle + quick_sort(right)

def fill_mass():
    array = []  
    while True:
        element = input("Enter an array element (or press Enter to finish)): ")
        if element == "":  
            break
        array.append(element)  
    return array

def find_min_or_max(array, find_max=True):
    if not array:
        return None  
    
    result = array[0]
    
    for element in array:
        if find_max and element > result:
            result = element
        elif not find_max and element < result:
            result = element

    return result

def print_mass(array):
    for i in range(len(array)):
        print(f"{array[i]} ", end="")
    return array

def fill_matrix(n, m):
    matrix = []
    
    print(f"Enter the elements for the matrix {n}x{m}:")
    
    for i in range(n):
        row = []
        for j in range(m):
            element = float(input(f"Enter the elements [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    
    return matrix
