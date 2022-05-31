'''Домашняя работа 12'''

import pandas as pd
import matplotlib.pyplot as plt

course = pd.read_csv('coursera_data.csv', delimiter=',', index_col='id')
sort = course.sort_values(by='course_organization').head(10)
table = pd.DataFrame(sort)
kol_courses = course['course_organization'].value_counts().head(10)
print(kol_courses)
kol_courses = course['course_organization'].value_counts().head(10)  # количество курсов
kol_courses = pd.DataFrame({'title': kol_courses.index, 'amount': kol_courses.values})
plt.bar(kol_courses['title'], kol_courses['amount'])
plt.savefig('ages.png')
plt.show()
mn = course['course_rating'].min()  #нахождение минимального рейтинга
print(mn)
row = course.sort_values('course_rating').head(n=1)
print(row.to_string())
avg = course['course_rating'].mean()  #нахожденияе среднего рейтинга
print(avg)
mx = course['course_rating'].max()  #нахождение максимального рейтинга
print(mx)
row1 = course.sort_values('course_rating',ascending=False).head(n=1)
print(row1.to_string())
plt.bar(row['course_organization'], row['course_rating'])
plt.bar("Среднее", course['course_rating'].mean())
plt.bar(row1['course_organization'], row1['course_rating'])
plt.savefig('ages1.png')
plt.show()
