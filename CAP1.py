# References
# https://www.w3schools.com/python/python_ref_string.asp
# https://www.geeksforgeeks.org/python-program-for-linear-search/
# https://www.geeksforgeeks.org/python-program-for-binary-search/
# https://www.geeksforgeeks.org/python-program-for-insertion-sort/
# https://www.geeksforgeeks.org/python-program-for-bubble-sort/
# https://www.geeksforgeeks.org/reading-writing-text-files-python/
# https://k4y0x13.github.io/CSF101-Programming-Methodology/unit4/0-intro-u4.html
# https://www.youtube.com/watch?v=Uh2ebFW8OYM&t=923s




# Read the file
with open('02230292.txt', 'r') as file:
    content = file.read()

# Split the data into lines
lines = content.splitlines()

# Initialize lists to hold names and scores
names = []
scores = []

# Process each line
for line in lines:
    name, score = line.split(',')
    names.append(name)
    scores.append(int(score))

# Calculate the average score
average_score = sum(scores) / len(scores) if scores else 0

# Find the lowest and highest scores with corresponding students
lowest_score = min(scores)
highest_score = max(scores)
lowest_students = [names[i] for i in range(len(scores)) if scores[i] == lowest_score]
highest_students = [names[i] for i in range(len(scores)) if scores[i] == highest_score]

# Find students scoring above and below average
above_average_students = [names[i] for i in range(len(scores)) if scores[i] > average_score]
below_average_students = [names[i] for i in range(len(scores)) if scores[i] < average_score]

# Sort using Bubble Sort
def bubble_sort(names, scores):
    n = len(scores)
    for i in range(n):
        for j in range(0, n - i - 1):
            if scores[j] > scores[j + 1]:
                scores[j], scores[j + 1] = scores[j + 1], scores[j]
                names[j], names[j + 1] = names[j + 1], names[j]
    return names, scores

# Sort using Insertion Sort
def insertion_sort(names, scores):
    n = len(scores)
    for i in range(1, n):
        key_score = scores[i]
        key_name = names[i]
        j = i - 1
        while j >= 0 and key_score < scores[j]:
            scores[j + 1] = scores[j]
            names[j + 1] = names[j]
            j -= 1
        scores[j + 1] = key_score
        names[j + 1] = key_name
    return names, scores

# Sort the lists
bubble_sorted_names, bubble_sorted_scores = bubble_sort(names[:], scores[:])
insertion_sorted_names, insertion_sorted_scores = insertion_sort(names[:], scores[:])

# Prepare for searches using sorted lists (for binary search)
def linear_search(target_score):
    found = [(names[i], scores[i]) for i in range(len(scores)) if scores[i] == target_score]
    return found if found else None

def binary_search(target_score):
    low, high = 0, len(bubble_sorted_scores) - 1  # Use bubble sorted scores
    found = []

    while low <= high:
        mid = (low + high) // 2
        if bubble_sorted_scores[mid] == target_score:
            found.append((bubble_sorted_names[mid], bubble_sorted_scores[mid]))
            left, right = mid - 1, mid + 1
            while left >= 0 and bubble_sorted_scores[left] == target_score:
                found.append((bubble_sorted_names[left], bubble_sorted_scores[left]))
                left -= 1
            while right < len(bubble_sorted_scores) and bubble_sorted_scores[right] == target_score:
                found.append((bubble_sorted_names[right], bubble_sorted_scores[right]))
                right += 1
            break
        elif bubble_sorted_scores[mid] < target_score:
            low = mid + 1
        else:
            high = mid - 1

    return found if found else None

# Accept user input for the target score
target_score = int(input("Enter the score to search for: "))

# Perform searches
linear_result = linear_search(target_score)
binary_result = binary_search(target_score)

# Store results in a dictionary
results_dict = {
    "linear search": linear_result,
    "binary search": binary_result
}

# Prepare output content for output.txt
output_content = f"Average Score: {average_score:.2f}\n\n"
output_content += "Bubble Sorted Students by Scores:\n"
output_content += f"{'Name':<20} {'Score':<5}\n"
output_content += "-" * 25 + "\n"
for name, score in zip(bubble_sorted_names, bubble_sorted_scores):
    output_content += f"{name:<20} {score:<5}\n"

output_content += "\nInsertion Sorted Students by Scores:\n"
output_content += f"{'Name':<20} {'Score':<5}\n"
output_content += "-" * 25 + "\n"
for name, score in zip(insertion_sorted_names, insertion_sorted_scores):
    output_content += f"{name:<20} {score:<5}\n"

# Students scoring above average
output_content += "\nStudents Scoring Above Average:\n"
output_content += f"{'Name':<20} {'Score':<5}\n"
output_content += "-" * 25 + "\n"
for name in above_average_students:
    score = scores[names.index(name)]
    output_content += f"{name:<20} {score:<5}\n"

# Students scoring below average
output_content += "\nStudents Scoring Below Average:\n"
output_content += f"{'Name':<20} {'Score':<5}\n"
output_content += "-" * 25 + "\n"
for name in below_average_students:
    score = scores[names.index(name)]
    output_content += f"{name:<20} {score:<5}\n"

# Results for the searched score
output_content += f"\nResults for score {target_score}:\n"
for search_type, result in results_dict.items():
    if result:
        for name, score in result:
            output_content += f"{search_type:<15} {name:<20} {score:<5}\n"
    else:
        output_content += f"{search_type:<15} No results found\n"

# Lowest and highest scores in table format
output_content += "\nLowest Score:\n"
output_content += f"{'Name':<20} {'Score':<5}\n"
output_content += "-" * 25 + "\n"
for student in lowest_students:
    output_content += f"{student:<20} {lowest_score:<5}\n"

output_content += "\nHighest Score:\n"
output_content += f"{'Name':<20} {'Score':<5}\n"
output_content += "-" * 25 + "\n"
for student in highest_students:
    output_content += f"{student:<20} {highest_score:<5}\n"

# Write the results to output.txt
with open('output.txt', 'w') as output_file:
    output_file.write(output_content)

# Optional: Print the output for verification
print("Results have been written to output.txt.")
