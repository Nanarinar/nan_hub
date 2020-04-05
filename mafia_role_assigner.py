from random import shuffle
import numpy as np
import pandas as pd

n = int(input("Enter number of players :"))
special_roles = input("Enter special roles separated by comma: ").replace(" ", "").split(",")

mafia_count = np.floor(n/3).astype(int)
player_number = np.linspace(1,n,num = n,dtype = int)
roles = mafia_count*['Mafia']+special_roles+(n-len(special_roles)-mafia_count)*['Citizen']
shuffle(roles)
id = int(input("Enter your player number: "))
print ("Your role is", roles[id-1])

#roles_dict= dict(zip(player_number, roles))
#for player, role in zip(player_number,roles):
#   print("Player", player, "gets role", role )
