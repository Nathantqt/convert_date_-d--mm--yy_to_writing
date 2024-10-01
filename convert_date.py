# Chaîne d'entrée
input_string = "2-Oct-25"

# Dictionnaire pour convertir les mois abrégés en mois complets
months = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December',
}

# Séparer le jour, le mois et l'année
day, month_abbr, year = input_string.split('-')

# Convertir l'année à 4 chiffres
year = '20' + year  # Cela suppose que les années sont entre 2000 et 2099

# Obtenir le mois complet
month_full = months[month_abbr[:3]]  # Prendre les trois premières lettres

# Construire la nouvelle chaîne
output_string = f"{day} {month_full} {year}"

print(output_string)
