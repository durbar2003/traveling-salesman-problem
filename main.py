import itertools

def traveling_salesman(matrix):
    num_cities = len(matrix)
    
    cities = list(range(num_cities))
    
    min_distance = float('inf')
    min_path = None
    
    for permutation in itertools.permutations(cities):
        current_distance = 0
        for i in range(num_cities - 1):
            current_distance += matrix[permutation[i]][permutation[i+1]]
        
        current_distance += matrix[permutation[-1]][permutation[0]]
        
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = permutation
    
    return min_path, min_distance

num_cities = int(input("Enter the number of cities: "))

distance_matrix = []
for i in range(num_cities):
    row = []
    for j in range(num_cities):
        if i == j:
            row.append(0)
        else:
            row.append(float(input(f"Enter distance from city {i} to city {j}: ")))
    distance_matrix.append(row)

optimal_path, optimal_distance = traveling_salesman(distance_matrix)

print("Optimal TSP Path:", optimal_path)
print("Optimal TSP Distance:", optimal_distance)
