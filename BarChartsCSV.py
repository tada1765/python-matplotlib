# # Counter:
# from collections import Counter
# li = Counter(['Python', 'JavaScript'])
# print(li) '''=Counter({'Python': 1, 'JavaScript': 1})'''
# li.update(['C++', 'Python'])
# print(li) '''=Counter({'Python': 2, 'JavaScript': 1, 'C++': 1})'''
# li.update(['C++', 'Python'])
# print(li) '''=Counter({'Python': 3, 'C++': 2, 'JavaScript': 1})'''

# # print 1st row obverse return data
# import csv
# import numpy as np
# from matplotlib import pyplot as plt
# # print(plt.style.available) # display style available
# plt.style.use('fivethirtyeight')# fivethirtyeight 

# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     row = next(csv_reader)
#     print(row['LanguagesWorkedWith'].split(';'))

# # bar graph:
# import csv
# import numpy as np
# from collections import Counter
# from matplotlib import pyplot as plt
# # print(plt.style.available) # display style available
# plt.style.use('fivethirtyeight')# fivethirtyeight 

# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     language_counter = Counter()

#     for row in csv_reader:
#         language_counter.update(row['LanguagesWorkedWith'].split(';'))
# # print(language_counter) ''' get all '''
# # print(language_counter.most_common(15)) ''' get 15 most '''
# languages = []
# popularity = []   
# for item in language_counter.most_common(15):
#     languages.append(item[0])
#     popularity.append(item[1])
# # print(languages)
# # print(popularity)
# languages.reverse()
# popularity.reverse()

# plt.barh(languages,popularity) #bar to barh
# plt.title("Most Popular Languages")
# # plt.ylabel("Programming Languages")
# plt.xlabel("Number of People Who Use")
# plt.tight_layout()
# plt.show()

# bar graph with pandas:
import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ids =data['Responder_id'] # from data.csv
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for respones in lang_responses:
    language_counter.update(respones.split(';'))

languages = []
popularity = []   
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages,popularity) #bar to barh
plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")
plt.tight_layout()
plt.show()