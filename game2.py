from game_modules import *
ankle_status = False

def rescue(ankle_status):
	print "You're awoken in the middle of the night by a sound."
	delay(2)
	print "It's very cold, and you feel initial signs of frostbite."
	delay(2)
	print "Something is approaching!!"
	delay(5)
	print "It's getting closer!"
	delay(1)
	print "You can hear it breathing!"
	delay(1)
	print "It's too dark to see anything!"
	delay(2)
	print "'Uh'"
	delay(1)
	print"'Huh?'"
	delay(1)
	print "'Hey! Are you alright?'"
	delay(4)
	print "You're saved!"
	if ankle_status == True:
		print "You're carried to an awaiting medic."
	if ankle_status == False:
		print "You walk with the rescuer to safety!"
	delay(2)
	print "THE END"
	exit()

	
def shelter(ankle_status):
	print "You find a group of trees and create a shelter with leaves."
	print "Night is coming and you decide to rest."
	delay(5)
	rescue(ankle_status)
	
def river(ankle_status):
	print "You've made it to a river."
	delay(2)
	print "The water is cool and clean enough to drink!"
	delay(2)
	print "What would you like to do?"
	print "1. I'm hungry. I should try to catch some fish."
	print "2. I've hiked pretty far already, maybe I should find shelter."
	
	decide = decision(True) 
	if decide == '2':
		shelter(ankle_status)
	elif decide == '1':
		death("It gets late and the tempurture drops. \nYou have no shelter.")
	else:
		decision(False)
		river(ankle_status)
		
def high_ground():
	ankle_status = True
	print "You take the high ground."
	delay(2)
	print "The view is coming into focus."
	delay(5)
	print "You are in awe!"
	delay(4)
	print "'AHHH'"
	delay(1)
	print "*BOOM*"
	delay(1)
	print "*CRASH*"
	delay(1)
	print "*OUCH*"
	delay(5)
	print "Well, you were distracted by the view and fell."
	delay(2)
	print "You're okay, but you've twisted your ankle pretty badly."
	delay(2)
	print "There's a small laceration, and it's swelling fast."
	delay(2)
	print "What should you do?"
	print "1. Keep going. I'll try not to put weight on my ankle."
	print "2. I've hiked pretty far already, maybe I should find shelter."
	
	decide = decision(True) 
	if decide == '2':
		shelter(ankle_status)
	elif decide == '1':
		death("Your ankle swells and you develop a fever.")
	else:
		decision(False)
		high_ground(ankle_status)
	
	
def hike():
	print "The forest is beautiful!"
	delay(2)
	print "It's a lovely day for a hike."
	delay(2)
	print "The clouds are amazing!"
	delay(2)
	print "You hear something up ahead."
	delay(4)
	print "It sounds like running water..."
	delay(4)
	print "It is!"
	delay(2)
	print "You see a river at the bottom of the valley."
	print "What should you do?"
	print "1. Go to the river."
	print "2. Head for higher ground."
	
	decide = decision(True)
	if decide == '1':
		river(ankle_status)
	elif decide == '2':
		high_ground()
	else:
		decision(False)
		hike()

def camp():
	print "There's no great place to set up any shelter."
	delay(2)
	print "But you find some soft pine branches to lay on."
	delay(2)
	print "The sun is finally setting and it's beautiful!"
	delay(2)
	print "You're falling asleep to the smell of pine..."
	delay(5)
	death("The temperature drops. \nYou don't wake up.")
	
def go_back():
	print "Alright, you turn around and go back."
	delay(5)
	print "Ok... um..."
	delay(5)
	print "This is weird, but I think you're lost."
	delay(2)
	print "You end up back where you started in the forest."
	forest()

	
def forest():
	print "Welcome to the Forest of Bylock."
	delay(2)
	print "It's a beautiful oak forest that's over 5,000 years old."
	delay(2)
	print "Sunset is only hours away, so you'll need to act fast if want to survive."
	delay(2)
	print "What would you like to do?"
	print "1. Hike to the top of the hill."
	print "2. Lay down for the night."
	print "3. Go back!"
	
	decide = decision(True)
	if decide == '1':
		hike()
	elif decide == '2':
		camp()
	elif decide == '3':
		go_back()
	else:
		decision(False)
		forest()
		
forest()