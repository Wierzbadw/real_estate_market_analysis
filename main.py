import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

location = r"C:\Users\User\PycharmProjects\nieruchomosci\ceny_mieszkan.xlsx"


def divideList(list1, list2):
    result = []

    for str1, str2 in zip(list1, list2):
        number1 = int(str1)
        number2 = int(str2)

        r = number1 / number2
        result.append(r)

    return result


def cityLineChart():
    excel_data_p = pd.read_excel(location, sheet_name="Rynek pierwotny")
    cities_list = excel_data_p.columns.tolist()
    time_list = excel_data_p[cities_list[0]].tolist()
    cities_list.pop(0)

    for i, city in enumerate(cities_list):
        print(i, city)

    city = int(input("Which city would you like to analyze?"))
    price_list_p = excel_data_p[cities_list[city]].tolist()

    excel_data_s = pd.read_excel(location, sheet_name="Rynek wtórny")
    price_list_s = excel_data_s[cities_list[city]].tolist()

    price_list_ratio = divideList(price_list_p, price_list_s)

    fig, axs = plt.subplots(2, 2)
    major_locator = MultipleLocator(4)

    axs[0, 0].plot(time_list, price_list_p, 'tab:blue')
    axs[0, 0].set_title('Prices of square meter in ' + cities_list[city] + ' on the primary market')

    axs[0, 1].plot(time_list, price_list_s, 'tab:orange')
    axs[0, 1].set_title('Prices of square meter in ' + cities_list[city] + ' on the secondary market')

    axs[1, 0].plot(time_list, price_list_p, 'tab:blue')
    axs[1, 0].plot(time_list, price_list_s, 'tab:orange')
    axs[1, 0].set_title('Prices of square meter in ' + cities_list[city] + ' on the primary and secondary market')
    axs[1, 0].legend(["Primary market", "Secondary market"], loc='lower right')

    axs[1, 1].plot(time_list, price_list_ratio, 'tab:red')
    axs[1, 1].set_title('Price ratio of square meter in ' + cities_list[city] + ' on the primary to secondary market')

    for ax in axs[0, 0], axs[0, 1], axs[1, 0], axs[1, 1]:
        ax.grid(True)
        ax.set_xticks(range(len(time_list)))
        ax.set_xticklabels(time_list, rotation=45, ha='right')
        ax.xaxis.set_major_locator(major_locator)

    for ax in axs[0, 0], axs[0, 1], axs[1, 0]:
        ax.set_ylabel('Price for square meter in PLN')
        ax.set_xlabel('Time ')

    axs[1, 1].set_ylabel('Price ratio')
    axs[1, 1].set_xlabel('Time ')

    print("To continue, close the chart window")
    plt.show()


def allCitiesBarChart():
    excel_data_p = pd.read_excel(location, sheet_name="Rynek pierwotny")
    time_list = excel_data_p["Kwartał"].tolist()

    for i, quarter in enumerate(time_list):
        print(i, "-->", quarter)

    quarter = int(input("Which quarter would you like to analyze?"))

    price_list = excel_data_p.loc[quarter].tolist()
    price_list.pop(0)

    for i in range(0, len(price_list)):
        price_list[i] = int(price_list[i])

    cities_list = excel_data_p.columns.tolist()
    cities_list.pop(0)

    fig, ax = plt.subplots()
    ax.grid(True)
    bar_colors = ['tab:red', 'tab:blue', 'tab:cyan', 'tab:orange', 'tab:green', 'tab:purple', 'tab:olive', 'tab:pink',
                  'tab:brown',
                  'tab:red', 'tab:blue', 'tab:cyan', 'tab:orange', 'tab:green', 'tab:purple', 'tab:olive', 'tab:pink',
                  'tab:brown']
    ax.bar(cities_list, price_list, color=bar_colors)

    ax.set_ylabel('Price for square meter in PLN')
    ax.set_xlabel('Cities')
    ax.set_title('Price for square meter on thr primary market in largest cities in Poland in ' + time_list[quarter])

    ax.grid(True)
    ax.label_outer()

    for i, price in enumerate(price_list):
        plt.text(i, price + 0.1, str(price), ha='center', va='bottom')

    for label in ax.get_xticklabels(which='major'):
        label.set(rotation=30, horizontalalignment='right')

    print("To continue, close the chart window")
    plt.show()


def compareCitiesLineChart():
    excel_data_p = pd.read_excel(location, sheet_name="Rynek pierwotny")
    cities_list = excel_data_p.columns.tolist()
    time_list = excel_data_p[cities_list[0]].tolist()
    cities_list.pop(0)

    for i, city in enumerate(cities_list):
        print(i, city)

    city_1 = int(input("Choose first city to compare: "))
    city_2 = int(input("Choose second city to compare: "))

    price_list_p_1 = excel_data_p[cities_list[city_1]].tolist()
    price_list_p_2 = excel_data_p[cities_list[city_2]].tolist()

    excel_data_s = pd.read_excel(location, sheet_name="Rynek wtórny")
    price_list_s_1 = excel_data_s[cities_list[city_1]].tolist()
    price_list_s_2 = excel_data_s[cities_list[city_2]].tolist()

    price_list_compare_p = divideList(price_list_p_1, price_list_p_2)
    price_list_compare_s = divideList(price_list_s_1, price_list_s_2)

    fig, axs = plt.subplots(2, 2)
    major_locator = MultipleLocator(4)

    axs[0, 0].plot(time_list, price_list_p_1, 'tab:blue')
    axs[0, 0].plot(time_list, price_list_p_2, 'tab:orange')
    axs[0, 0].set_title(
        'Prices of square meter on primary market in ' + cities_list[city_1] + ' and ' + cities_list[city_2])
    axs[0, 0].legend([cities_list[city_1], cities_list[city_2]], loc='lower right')

    axs[0, 1].plot(time_list, price_list_s_1, 'tab:blue')
    axs[0, 1].plot(time_list, price_list_s_2, 'tab:orange')
    axs[0, 1].set_title(
        'Prices of square meter on secondary market in ' + cities_list[city_1] + ' and ' + cities_list[city_2])
    axs[0, 1].legend([cities_list[city_1], cities_list[city_2]], loc='lower right')

    axs[1, 0].plot(time_list, price_list_compare_p, 'tab:red')
    axs[1, 0].set_title('Price ratio on the primary market in ' + cities_list[city_1] + ' and ' + cities_list[city_2])

    axs[1, 1].plot(time_list, price_list_compare_s, 'tab:green')
    axs[1, 1].set_title('Price ratio on the secondary market in ' + cities_list[city_1] + ' and ' + cities_list[city_2])

    for ax in axs[0, 0], axs[0, 1], axs[1, 0], axs[1, 1]:
        ax.grid(True)
        ax.set_xticks(range(len(time_list)))
        ax.set_xticklabels(time_list, rotation=45, ha='right')
        ax.xaxis.set_major_locator(major_locator)

    for ax in axs[0, 0], axs[0, 1]:
        ax.set_ylabel('Price for square meter in PLN')
        ax.set_xlabel('Time ')

    for ax in axs[1, 0], axs[1, 1]:
        ax.set_ylabel('Price ratio')
        ax.set_xlabel('Time ')

    print("To continue, close the chart window")
    plt.show()


def executeChoice(choice):
    if choice == "1":
        cityLineChart()
    elif choice == "2":
        allCitiesBarChart()
    elif choice == "3":
        compareCitiesLineChart()
    elif choice == "4":
        print("Thank you!")
    else:
        print("Wrong choice, try again")


choice = 0
print("This is a program for analysis of data about real estate in Poland.\n")
while (choice != '4'):
    print("Which chart would you like to create? \n")
    print("[1] - Show line charts of prices over time in a specific city")
    print("[2] - Show bar chart of prices in the biggest polish cities in a given quarter")
    print("[3] - Show line charts comparing prices over time in two selected cities")
    print("[4] - End\n")

    choice = input("Type number:")
    executeChoice(choice)
