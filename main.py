import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
classes_per_week = 3
print(classes_per_week, type(classes_per_week))
cost_per_class = cost_per_week / classes_per_week
print(cost_per_class, type(cost_per_class))
print(f"Your cost per class is : {cost_per_class}. How expensive!")
print("Cost per week:", cost_per_week)


#Part B
my_list = [3, 6, 8, 9, 12]
output = random.choice(my_list)
print(output)
