"""These are the modules for game.py"""
import time

def delay(sleep_time):
	"""Delays time where 'sleep_time' is in seconds."""
	print ".........."
	time.sleep(sleep_time)
	return
	
def decision(valid):
	"""Takes an input and returns invalid or returns the input, as decided by the caller."""
	if valid == True:
		choice = raw_input("Which one? > ")
		print "Sounds like a good idea."
		delay(2)
		return choice
	elif valid == False:
		print "Wait."
		delay(2)
		print "That's not an option, try again."
		print "-----------"
	
	else:
		return ValueError

def death(reason):
	"""End of game where 'reason' is the cause of death."""
	delay(5)
	print reason, "\nDeath. \nBetter luck next time."	
	exit()
