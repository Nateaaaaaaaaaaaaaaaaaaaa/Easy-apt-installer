import os
dpkg = input('What would you like to download today?')
aptin = "apt install "
aptind = aptin + dpkg
os.system(aptind)
