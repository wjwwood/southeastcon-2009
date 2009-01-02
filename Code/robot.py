#
#  robot.py
#  
#
#  Created by William Woodall on 12/4/08.
#  Copyright (c) 2008 Auburn University. All rights reserved.
#

# Paths #
import sys
sys.path.append("Libraries")
sys.path.append("Modules")

# Imports #
# ConfigObj
from configobj import ConfigObj
from validate import Validator
# Logging
#from logger import *  # Logging is not working yet.

# Robot #
class Robot:
	pass

# Functions #





# Handle Configurations
try:
	filename
except NameError:
	filename = "Configurations/robot.cfg"
else:
	print "Using non default config file:", filename
config = ConfigObj(filename)


print "Robot.py has been loaded."