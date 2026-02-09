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

print(f"Sorted students scores:", bubble_sort(scores))
