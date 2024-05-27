plt.bar(years, population, label = "Population")
plt.bar(years, hungry_people, label = "Hungry People", color = 'r')
plt.xticks(np.arange(min(years), max(years)+1, 2.0))
plt.yticks(np.arange(1000000, 115000000, 5000000))
plt.xlabel("Year")
plt.ylabel("# of People ")
plt.legend()
plt.grid()
plt.title("Hungry People vs Population")
plt.show()