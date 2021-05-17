import csv
import matplotlib.pyplot as plt
import numpy as np
from numpy import trapz

from petroleum import csv_yearly_production

#to_read_data_from_csv
def les_prod_data(i):
    column_list = []
    with open(csv_yearly_production,) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader, None)

        for column in reader:
            tall = column[i]
            column_list.append(float(tall.replace(",",".")))
    return column_list

#visualization
def plot_produksjon():
    aar = les_prod_data(0)
    olje = les_prod_data(1)
    kondensat = les_prod_data(2)
    NGL = les_prod_data(3)
    gas = les_prod_data(4)
    sum_oljeekvivalent = les_prod_data(5)
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.set_xlabel('Year')  # Add an x-label to the axes.
    ax.set_ylabel('Millioner Sm3 Oljeekvivalenter')  # Add a y-label to the axes.
    ax.set_title("Yearly HC production")  # Add a title to the axes.
    plt.plot(aar, sum_oljeekvivalent, label="Sum oljeekvivalent")
    plt.plot(aar,olje,  label = "Olje")
    plt.plot(aar,np.array(kondensat)+np.array(olje),  label = "Kondensat")
    plt.plot(aar, np.array(NGL)+np.array(kondensat)+np.array(olje), label="NGL")
    plt.plot(aar, np.array(gas)+np.array(NGL)+np.array(kondensat)+np.array(olje), label="Gas")
    plt.xticks(rotation='vertical')
    plt.legend()
    plt.draw()
    plt.show()

#asking for user input

produkt = input('Please give me a product for which you would like to see the statistics, choose from olje - kondensat - NGL - gas')
from_year = int(input('Please give me the starting year of the statistics (1971-2020)'))
to_year = int(input('Please give me the end year of the statistics (1972-2021)'))
print('The chart shows the historical HC production on the NCS. To see statistics please close the chart')

#calculating average
def beregn_gjennomsnitt(produkt, from_year, to_year):

        aar = les_prod_data(0)
        if produkt == 'olje':
            list_produkt=les_prod_data(1)
        elif produkt == 'kondensat':
            list_produkt = les_prod_data(2)
        elif produkt == 'NGL':
            list_produkt = les_prod_data(3)
        elif produkt == 'gas':
            list_produkt = les_prod_data(4)
        fra_indeks = aar.index(from_year)
        til_indeks= aar.index(to_year)
        list_produkt_for_period = list_produkt[fra_indeks:til_indeks]

        return print( 'The average', produkt, 'production in the period', from_year, '-', to_year, 'was', round(sum(list_produkt_for_period)/len(list_produkt_for_period),1), 'Sm³ o.e.')

#calculating maximum
def finn_maks(produkt):
    aar = les_prod_data(0)
    if produkt == 'olje':
        list_produkt = les_prod_data(1)
    elif produkt == 'kondensat':
        list_produkt = les_prod_data(2)
    elif produkt == 'NGL':
        list_produkt = les_prod_data(3)
    elif produkt == 'gas':
        list_produkt = les_prod_data(4)
    max_produkt = max(list_produkt)
    index_of_max= list_produkt.index(max_produkt)
    year_of_max= aar[index_of_max]
    return print('The maximum production of', produkt, 'was', round(max_produkt,1), 'Sm³ o.e. in',int(year_of_max))

#to count area on graph
def beregn_areal_trapz(produkt, from_year,to_year):
    aar = les_prod_data(0)
    if produkt == 'olje':
        list_produkt = les_prod_data(1)
    elif produkt == 'kondensat':
        list_produkt = les_prod_data(2)
    elif produkt == 'NGL':
        list_produkt = les_prod_data(3)
    elif produkt == 'gas':
        list_produkt = les_prod_data(4)
    else:
        list_produkt = les_prod_data(5)
    fra_indeks = aar.index(from_year)
    til_indeks = aar.index(to_year)
    list_produkt_for_period = list_produkt[fra_indeks:til_indeks]
    return trapz(list_produkt_for_period,dx=1)



