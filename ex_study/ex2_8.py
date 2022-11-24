rok = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
       'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']

#kwar = [i for i in enumerate(rok) if  % 3 == 0]
poczatki_kwartalow = [x for y, x in enumerate(rok) if y % 3 == 0]

print(poczatki_kwartalow)