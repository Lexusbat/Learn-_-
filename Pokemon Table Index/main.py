from prettytable import PrettyTable # Imported a PrettyTable Class from this Module installed 

#Object = class
table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)