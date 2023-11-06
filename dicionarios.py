Dict = {"key1": 1, "key2": "2", "key3": [
    3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}

release_year_dict  = {"Thriller": "1982", "Back in Black": "1980", "the dark side of the moon": "1973", "The Bodyguard": "1992",
                     "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", "Saturday Night Fever": "1977", "Rumours": "1977"} 

print(release_year_dict["Back in Black"])
print(release_year_dict.keys())

# Percorrendo elementos dicionario

for key, value in release_year_dict.items():
    print(key, value)

# Adicionando elementos ao dicionario
release_year_dict['Graduation'] = '2007'
print(release_year_dict)

# Removendo elementos do dicionario
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
print(release_year_dict)

print('The Bodyguard' in release_year_dict)