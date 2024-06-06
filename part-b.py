import itertools
from collections import Counter

def calculate_sum_probabilities(die_a, die_b):
    sum_counts = Counter()
    total_combinations = len(die_a) * len(die_b)
    
    for a in die_a:
        for b in die_b:
            sum_counts[a + b] += 1
    
    probabilities = {sum_value: count / total_combinations for sum_value, count in sum_counts.items()}
    return probabilities

def transform_dice(die_a, die_b):
    original_probabilities = calculate_sum_probabilities(die_a, die_b)
    
    possible_die_a_faces = [1, 2, 3, 4]
    possible_die_a_configurations = list(itertools.product(possible_die_a_faces, repeat=6))
    
    for new_die_a in possible_die_a_configurations:
        remaining_values = []
        
        for original_sum, prob in original_probabilities.items():
            for a in new_die_a:
                b_value = original_sum - a
                if b_value > 0:
                    remaining_values.append(b_value)
        
        remaining_values_counter = Counter(remaining_values)
        most_common_values = remaining_values_counter.most_common(6)
        
        if len(most_common_values) == 6:
            new_die_b = [value for value, count in most_common_values]
            new_probabilities = calculate_sum_probabilities(new_die_a, new_die_b)
            
            if new_probabilities == original_probabilities:
                return list(new_die_a), list(new_die_b)
    
    return new_die_a, new_die_b

die_a = [1, 2, 3, 4, 5, 6]
die_b = [1, 2, 3, 4, 5, 6]

new_die_a, new_die_b = transform_dice(die_a, die_b)

print(f"New Die A: {new_die_a}")
print(f"New Die B: {new_die_b}")
