# # print to see multiple fig:
# import pandas as pd
# from matplotlib import pyplot as plt
# plt.style.use('seaborn')

# ''' one figure '''
# fig, ax = plt.subplots()
# print(ax)

# ''' two plot in one figure '''
# fig, (ax1, ax2) = plt.subplots(nrows=2,ncols=1)
# print(ax1)
# print(ax2)

# # sub plot in one fig:
# import pandas as pd
# from matplotlib import pyplot as plt
# plt.style.use('seaborn')
# data = pd.read_csv('data5.csv')
# ages = data['Age']
# dev_salaries = data['All_Devs']
# py_salaries = data['Python']
# js_salaries = data['JavaScript']
# ''' sharex=True - share x-axis for both plot'''
# fig, (ax1, ax2) = plt.subplots(nrows=2,ncols=1,sharex=True)
# ax1.plot(ages, dev_salaries, color='#444444',
#         linestyle='--', label='All Devs')
# ax2.plot(ages, py_salaries, label='Python')
# ax2.plot(ages, js_salaries, label='JavaScript')

# ax1.legend()
# # ax1.set_xlabel('Ages')
# ax1.set_ylabel('Median Salary (USD)')
# ax1.set_title('Median Salary (USD) by Age')

# ax2.legend()
# ax2.set_xlabel('Ages')
# ax2.set_ylabel('Median Salary (USD)')
# # ax2.set_title('Median Salary (USD) by Age')
# plt.tight_layout()
# plt.show()

# multiple fig:
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('seaborn')
data = pd.read_csv('data5.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']
''' sharex=True - share x-axis for both fig'''
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
ax1.plot(ages, dev_salaries, color='#444444',
        linestyle='--', label='All Devs')
ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')
ax1.set_title('Median Salary (USD) by Age')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')
ax2.set_title('Median Salary (USD) by Age')
plt.tight_layout()
plt.show()

# # save fig:
# fig1.savefig('fig1.png')
# fig2.savefig('fig2.png')

