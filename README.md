# my_first_game
A simple text based game written in python using a custom module

game2.py is a texted-based adventure game inspired by working through Learn Python The Hard Way (one of Zed Shaw's 'The Hard Way' books).

The part of the code that I'm most excited about is in the game_modules.py file, where I've created custom modules to solve simple repetitive tasks. They're by no means rocket science, (however, they are computer science...), but I challanged myself to write all of the code without searching for how others solved similar problems, and is the most elegant solution that my current technical abilities can muster. The ultimate goal for the entire game_modules.py module is to create a simple and clear format for expanding and adapting the game.

The decision function is my favorite because it creates a very intuitive format for expanding and adapting the game users' choices. By loading most of the decision making into the module, the game script simply has to call the function with True or False parameters, and let it return user input or an invalid statement. Likewise, from a design perspective, I liked creating the delay function to add to the user experience.

Finally, the ankle_injury paramerter was exciting to add because it allowed me to discover another way to branch the code.

#To Play:
Add game2.py and game_modules.py to the same directory, and run game2.py from your favorite commandline terminal. 

I hope you enjoy!
