def roman_to_int(roman_string):
    roman_dico = {"I": 1, "V": 5, "X": 10, "L": 50, "D": 500, "M": 1000}
    list_roman_string = list(roman_string)
    result = 0

    for index in range(len(list_roman_string)):
        for key in roman_dico:
            if list_roman_string[index] == key:
                list_roman_string[index] = roman_dico[key]
                break  # Une fois que la correspondance est trouvée, sortir de la boucle

    result = list_roman_string[0]
    for index2 in range(1, len(list_roman_string)):
        result += list_roman_string[index2]

    return result
