
from petroleum import *



if __name__ == '__main__':
    plot_produksjon()
    beregn_gjennomsnitt(produkt, from_year, to_year)
    finn_maks(produkt)
    print('The percentage of the products in the period', from_year,'-', to_year,'was:',
          '\nOlje:', "{:.2%}". format(beregn_areal_trapz('olje', from_year, to_year)/beregn_areal_trapz('sum', from_year, to_year)),
          '\nKondensat:', "{:.2%}". format(beregn_areal_trapz('kondensat', from_year, to_year)/beregn_areal_trapz('sum', from_year, to_year)),
          '\nNGL:', "{:.2%}". format(beregn_areal_trapz('NGL', from_year, to_year)/beregn_areal_trapz('sum', from_year, to_year)),
          '\nGas:', "{:.2%}". format(beregn_areal_trapz('gas', from_year, to_year)/beregn_areal_trapz('sum', from_year, to_year)))