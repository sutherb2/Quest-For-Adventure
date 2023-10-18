# Quest-For-Adventure
**Introduction:**  
This game was originally a project assigned in my CS230 class at JSU. The instructions for the assignment allowed for a great deal of creativity (aside from the title, annoyingly). All my professor really wanted was a certain number of possible win conditions and use of various structures we talked about. This is more complex than it had to be, but I wanted to prove to myself what I could do. This small text-based game is the result.

**Gameplay:** 
This game is essentially a MUD tyoe room-exploration game. While playing, you are free to walk around, pick up items, and obtain skills...until you encounter the boss. The boss is unable to detect you until you have a certain number of items in your inventory. Each item you can collect has different attack and defense values, and some even have unique attributes (like they can be used an infinite number of times).

Once you have five items in your inventory, the boss will attack you as soon as you enter the room he happens to spawn in. Once in battle, you have no choice but to fight. You may retreat, but only after your HP drops below a certain value. At that point, items can be recollected and you can try again. Keep in mind, though, that every item may only be picked up three times. After that, you don't have much choice but to fight to the death or quit the game.

If you happen to defeat the boss (it may take a couple of tries), then there is a 50% chance that a timed escape will trigger, in which case you must escape the dungeon before the time runs out, lest you ultimately lose.

**Methodology:** 
Though this game might look complex at first, it is essentially just a series of loops based on what actions are taken. Simple dictionaries hold the rooms and their relation to the surrounding rooms, as well as the items and their values. Any person who has had a little experience with Python programming should be able to easily figure out what is going on here. There is no claim that this is the best way to code a game like this, this is simply what made sense to me at the time.

**Results:**
I am pretty happy with the way this game turned out. Though it may not be all that impressive in the long run, I went from having never written code before to creating this game in just a few months, which felt very rewarding. I like developing applications that make life easier, but there's just something about being able to apply what you've learned to a "fun" thing that provides a different level of satisfaction.

**Conclusions:**
While coding this game, I learned a lot that reinforced the knowledge I gained during the class. This game provided a fun way to put everything I had learned into a single, cohesive piece of code that was actually fun to use. Creating this game also inspired me to dive into developing other simple games (like Battleship and Pong, for example).

This game can certainly be improved upon. Even I want to go back through and change some things around now that I'm no longer bound by the requirements of the assignment. A larger map, more rooms, more items, multiple bosses, and a level system would greatly improve this game.

If you were to make a single, very simple change, I would recommend adjusting the timed escape. Simply adjust the value of the list so that it is no longer a 50% chance, but rather a 100% chance to engage. It makes the game a lot more interesting. 
