# ---------------------------------
# -- Module => Creat Your Module --
# ---------------------------------

# import sys 

# sys.path.append(r"D:\Games")
# print(sys.path)

import Diaa

Diaa.Say_How_Are_You("Diaa") 
Diaa.Say_How_Are_You("Osama") 
Diaa.Say_How_Are_You("Ahmed")

Diaa.Say_Hello("Mohamed")
Diaa.Say_Hello("Kadre")
Diaa.Say_Hello("Ali")

# Alias

import Diaa as dd

dd.Say_How_Are_You("Diaa") 
dd.Say_How_Are_You("Osama") 
dd.Say_How_Are_You("Ahmed")

dd.Say_Hello("Mohamed")
dd.Say_Hello("Kadre")
dd.Say_Hello("Ali")

from Diaa import Say_Hello as ss

ss("Adham") 
