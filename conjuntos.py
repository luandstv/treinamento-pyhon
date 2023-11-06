# set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
# print(set1)

# music_genres = set(["pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco", "progressive rock", "soft rock", "soft rock", "folk rock", "glam rock", "rock"])
# print(music_genres)

# A = set(["Thriller", "Back in Black", "AC/DC"])
# print(A)

# A.add("NSYNC")
# print(A)

# A.remove("NSYNC")
# print(A)

# print("AC/DC" in A)

album_set1 = set(["Thriller", "AC/DC", "Back in Black"])
album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])

intersection = album_set1 & album_set2
print(intersection)
print("interseção:",album_set1.intersection(album_set2))

print("diferença: ",album_set2.difference(album_set1))

print("união:", album_set1.union(album_set2))

# verificando se é super ou sub conjunto

print(set(album_set1).issuperset(album_set2))
print(set(album_set2).issubset(album_set1))