import matplotlib.pyplot as plt
import numpy as np

# creating the dataset; in dict:
data = {'C': 20, 'C++': 15, 'Java': 30, 'Python': 35}

courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(25, 10))

# creating the bar plot
plt.bar(courses, values, color='maroon',
        width=0.4)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()
