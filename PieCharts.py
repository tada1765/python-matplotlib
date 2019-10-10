# from matplotlib import pyplot as plt

# slices = [60,40]
# plt.pie(slices)

# plt.style.use("fivethirtyeight")

# plt.title("My Pie Chart")
# plt.tight_layout()
# plt.show()

# # add more pie:
# from matplotlib import pyplot as plt

# slices = [120,80,30,20]
# labels = ['Sixty', 'Forty', 'Extral', 'Extral2']
# colors = ['blue', 'red', 'yellow', 'green']

# plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor':'black'})

# plt.style.use("fivethirtyeight")

# plt.title("My Pie Chart")
# plt.tight_layout()
# plt.show()

# # use color code replace words:
# # Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow= #e5ae37
# Green = #6d904f

# from matplotlib import pyplot as plt

# slices = [120,80,30,20]
# labels = ['Sixty', 'Forty', 'Extral', 'Extral2']
# colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

# plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor':'black'})

# plt.style.use("fivethirtyeight")

# plt.title("My Pie Chart")
# plt.tight_layout()
# plt.show()

# take slice of pie out:
from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")
slices = [59219,55466,47544,36443,35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.1,0]

plt.pie(slices, labels=labels, explode=explode, shadow=True,
        startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor':'black'})

plt.title("My Pie Chart")
plt.tight_layout()
plt.show()