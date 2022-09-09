#dictionaries are i the form key:value

nick_names={
    "Beezu":"Beatrice Anitah",
    "Maka":"Arianah",
    "Arno":"Arnold",
    "Andy":"Andrew",
    "Ellie":"Elie",
    "Bulije":"Bridget",
    "Jojo":"Ndiwanyo",
    "Essy":"Esther",
    "Yun":"Maria",
    "Karma":"Cissy"
}

print(nick_names["Jojo"])
print(nick_names.get("Maka"))
print(nick_names.get("Usher"))
print(nick_names.get("Usher", "Mukire"))
