def capitalize_line(sentences):
  converted = sentences.split(',') #aggiungo una conversione da stringa a lista, 
  #così che ogni stringa funzioni con questo metodo
  return [i.upper() for i in converted] #così fa lo spelling in caps, 
  #però se inserisci una lista di parole te le torna maiuscolate

sentences = input('frase da maiuscolare:')
maiuscolata = capitalize_line(sentences)

print(maiuscolata)

