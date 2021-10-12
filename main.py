import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

from pandas.core.tools.datetimes import to_datetime

details = pd.read_csv('desafio_details.csv')
prices = pd.read_csv('desafio_priceav.csv')


#Ordenando bairros por ordem crescente de id no dataFrame details.
details = details.sort_values(by=['suburb','airbnb_listing_id'])
#print(details)

#Faturamento médio por id (anúncio)
fat_medio_id = prices[prices['occupied']==1].groupby('airbnb_listing_id').price_string.agg('mean')
#print(fat_medio_id)

#Como a informação dos bairros está em details, vou primeiro adicionar o faturamento médio por id em details, para depois ordenar 
#os bairros por faturamento médio dos listings.
details = pd.merge(fat_medio_id, details, on='airbnb_listing_id').sort_values(by=['suburb', 'price_string'])
#print(details)

#Podemos também ver o faturamento médio por bairro:
#details = details.groupby('suburb').price_string.agg('mean').sort_values(ascending=False)
#print(details)

#Análise de correlações - Faturamento x Característica
#print(details[['star_rating','price_string']].dropna().corr())
#print(details[['number_of_bedrooms','price_string']].dropna().corr())
#print(details[['number_of_bathrooms','price_string']].dropna().corr())
#print(details[['is_superhost','price_string']].dropna().corr())
#print(details[['number_of_reviews','price_string']].dropna().corr())

#Gráficos comparativos
#plt.scatter(details['star_rating'],details['price_string'])
#plt.suptitle('Star rating x Average billing', fontsize=20)
#plt.xlabel('Star rating [-]', fontsize=16)
#plt.ylabel('Average billing [R$]', fontsize=16)
#plt.show()
#plt.savefig('star_rating_x_faturamento.png')

#plt.scatter(details['number_of_bedrooms'],details['price_string'])
#plt.suptitle('Number of bedrooms x Average billing', fontsize=20)
#plt.xlabel('Number of bedrooms [-]', fontsize=16)
#plt.ylabel('Average billing [R$]', fontsize=16)
#plt.show()
#plt.savefig('number_of_bedrooms_x_faturamento.png')

#plt.scatter(details['number_of_bathrooms'],details['price_string'])
#plt.suptitle('Number of bathrooms x Average billing', fontsize=20)
#plt.xlabel('Number of bathrooms [-]', fontsize=16)
#plt.ylabel('Average billing [R$]', fontsize=16)
#plt.show()
#plt.savefig('number_of_bathrooms_x_faturamento.png')

#plt.scatter(details['is_superhost'],details['price_string'])
#plt.suptitle('Is superhost x Average billing', fontsize=20)
#plt.xlabel('Is superhost [-]', fontsize=16)
#plt.ylabel('Average billing [R$]', fontsize=16)
#plt.show()
#plt.savefig('is_superhost_x_faturamento.png')

#plt.scatter(details['number_of_reviews'],details['price_string'])
#plt.suptitle('Number of reviews x Average billing', fontsize=20)
#plt.xlabel('Number of reviews [-]', fontsize=16)
#plt.ylabel('Average billing [R$]', fontsize=16)
#plt.show()
#plt.savefig('number_of_reviews_x_faturamento.png')

#Média de antecedência das reservas
print((pd.to_datetime(prices[prices['booked_on']!='blank']['date'])-pd.to_datetime(prices[prices['booked_on']!='blank']['booked_on'])).mean())

#Média de antecedência das reservas nos fins de semana
datas_alugadas = pd.to_datetime(prices[prices['booked_on']!='blank']['date'])
datas_reservas = pd.to_datetime(prices[prices['booked_on']!='blank']['booked_on'])
print((datas_alugadas[datas_alugadas.dt.dayofweek>4]-datas_reservas[datas_alugadas.dt.dayofweek>4]).mean())

