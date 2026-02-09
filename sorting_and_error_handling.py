students_list = ["John", "Lisa", "Mary", "Chris", "Linda", "Matt"]
test_performance_dictionary = {"John": 87, "Lisa": 90, "Mary": 75, "Chris": 100, "Linda": 100, "Matt": 70}

scores = [] #initialized an empty list

for value in test_performance_dictionary.values():
    scores.append(value)
print(f"Students scores:", scores) #checking the scores list

""" sorting scores in ascending order: 2 ways

def bubble_sort(scores): #modern efficient sort
  scores.sort()
  return scores """

def bubble_sort(scores): #classic bubble sort
    n = len(scores)
    for i in range(n):
        for j in range(0, n - i - 1):
            if scores[j] > scores[j + 1]:
                aux = scores[j]
                scores[j] = scores[j + 1]
                scores[j + 1] = aux
    return scores

sorted_scores = bubble_sort(scores)
print(f"Sorted students scores:", sorted_scores) #checking the new sorted list

#calculate the highest and lowest scores
highest_score = sorted_scores[len(sorted_scores)-1]
lowest_score = sorted_scores[0]

print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")

#calculate the class average score, excluding the error from an empty list
def average_class_score(students_list, scores):
    try:
        return sum(scores)/(len(scores))
    except ZeroDivisionError:
        print("Error: the list is empty")
    
average_score = average_class_score(students_list, scores) 
print(f"Average Score: {average_score}") #checking the avg. score

#checking the case of an empty class with the same function and different lists
empty_class = []
empty_scores = []
error_average = average_class_score(empty_class, empty_scores)
