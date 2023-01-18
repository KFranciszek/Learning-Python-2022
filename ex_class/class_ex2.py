# Potrzebujemy przeliczyć trochę waluty, czasy niepewne,
# warto mieć na uwadze swoją ulubioną walutę.
# Napisz klasę, która będzie zawierać dwie metody:

#       przeliczenie wybranej waluty z tabeli A na złotówki  <- dane wejściowe: kod waluty, ilość waluty
#       wskazanie aktualnego kursu z tabeli A <- dane wjećiowe: kod waluty

# Klasa w celu przeliczenia waluty powinna skorzystać z aktualnych kursów z Narodowego Banku Polskiego
# dokumentację API dla NBP znajdziesz pod adresem http://api.nbp.pl/

import  requests
import  json

class currency_calculator():

    def exchange_rate(self, code):
        api_url = 'http://api.nbp.pl/api/exchangerates/rates/A/'
        api_url = api_url + str(code)
        response = requests.get(api_url)


        if response.status_code == 200:
            data = response.json()
            rate = data['rates'][0]['mid']
            return rate
        else:
            print("Error")





    def convert_currency(self,code,volumen):
        api_url = 'http://api.nbp.pl/api/exchangerates/rates/A/'
        api_url = api_url + str(code)
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            rate=data['rates'][0]['mid']
            convert =rate*volumen
            return  convert
        else:
            print("Error")



nbp = currency_calculator()
ExchangeRate=nbp.exchange_rate("CHF")
ConvertCurrency=nbp.convert_currency("CHF",100)
print("Rate is ",ExchangeRate,"we will have ",ConvertCurrency,"PLN")





