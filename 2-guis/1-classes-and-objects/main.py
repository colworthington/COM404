# Code to demonstrate inheritance
from Bot import Bot
from SuperBot import Superbot
from FlyingBot import Flyingbot

#from SuperBot import *
#display_name, display_age, display_energy



#bop = Bot("Bop", 30, 5, 8)
#bop.display_name()

#superbop = Superbot("SBop", 31, 6, 9, 4)
#superbop.display_name()
#superbop.display_age()
#superbop.display_energy()
#superbop.display_shield()
#superbop.display_super_power_level()

flyingbop = Flyingbot("FBop", 32, 8, 10, 6, 55)
flyingbop.display_name()
flyingbop.display_age()
flyingbop.display_energy()
flyingbop.display_shield()
flyingbop.display_super_power_level()
flyingbop.display_hover_distance()

