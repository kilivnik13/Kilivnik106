import matplotlib.pyplot as plt
import numpy as np
subjects = ['Математический анализ', 'Физика', 'Химия', 'Начерт']
grades = [3, 4, 4, 5]
colors = ['purple', 'green', 'blue', 'red']
fig, ax = plt.subplots()
ax.bar(subjects, grades, color=colors)
ax.set_ylim([2, 5])
ax.set_title("Оценки за первый семестр")
ax.set_xlabel("Предметы")
ax.set_ylabel("Оценка")
legend_labels = [f"{subject}: {grade}" for subject, grade in zip(subjects, grades)]
ax.legend(legend_labels, loc="upper right")
plt.show()

