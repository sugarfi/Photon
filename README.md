# Photon
Photon is an esolang. In it, each command takes the same format. Here it is, expressed in regex: \[[#:].,[#:].>.\]. Basically, it goes like this:<br/>
[(a # or a :)(a character),(a # or a :)(a character)>(a character)]<br/>
To run Photon, do the following:<br/>
<ul>
  <li>Run main.py. You should see a list of files.</li>
  <li>Type a filename or type "help".</li>
  <li>Watch.</li>
 </ul>
The following is just the contents of the help guide. If, at the prompt, you type "help", you will get the same thing.
<pre>
PHOTON ESOTERIC LANGAGE - HELP
o=================o
1. Introduction
All commands in Photon take the form of two arguments passed to a function, enclosed in square brackets. For example:
[#5,#7>+]
Arguments can have one of two prefixes - ":" or "#".
If an argment is prefixed with "#", it is interpreted as a single digit value, ie. 5.
If it is prefixed with ":", it is taken from the variable list. (We'll get to that in a minute.) Example: :7.
The two arguments are comma seperated, and a ">" is between them and the function, which is always one character, ie. +.
2. The Variable List
The variable list is where photon variables are stored.
Variables begin with ":" and end with a single digit.
There are two exceptions to this rule: $ and -.
$ is where the result of an arithmetic operation is stored.
- is a null value, passed to functions that need less than two arguments.
To set a variable in Photon, you use the = function.
For example, to set the variable :1 to 5, you would do:
[:1,#5>=]
3. Maths
To do arithmetic in Photon is simple. You just use the +, -, /, and * functions. Examples:
[#5,#7>+]
[#2,#9>*]
[#6,#3>/]
[#8,#5>-]
As well as values, variables can be used for math. To add 5 to the variable :1, you would use:
[#5,:1>+]
The result of any math operation is stored in the (read-only) variable $.
To store it in a variable, you would assign $ to the variable after performing the maths. Example:
[#5,#7>+]
[:1,:$>=]
The variable :1 now has the value 12.
4. Reference
[:(a),#/:(b)>=] - Set the variable a equal to b.
[#/:(a),#/:(b)>+] - Addition.
[#/:(a),#/:(b)>-] - Subtraction.
[#/:(a),#/:(b)>*] - Multiplication.
[#/:(a),#/:(b)>/] - Division.
[:-,:->.] - Clear all variables and set $ to 0.
[#/:(a),:->_] - Print the value of a.
[#/:(a),:->_] - Print the ascii char of a.
[:-,:->~] - Print a newline.
[:(a),:->?] - Read keyboard input, and assign the first character as an integer to variable a.
[#/:(a),:->^] - Goto line a (0 = first line).
[#/:(a).#/:(b)>{] - If a is not zero, go to line b.
5. Notes
DO NOT PUT ANY SPACES!
The interpreter will ignore the line they are on. The following (probably) will not run:
[ #5 , #6 > + ]
ALL COMMANDS MUST BE ENCLOSED IN BRACKETS!
The interpreter will ignore instructions outside of them. The following will not run:
#5,#6>+
INVALID INPUT WILL BE IGNORED!
Input not matching the regex \[[#:].,[#:].>.\] will be ignored and not run.
This is how you would comment things. No // or #. Just type them, like so:
[#5,#6>+]
Assign the result to variable 1:
[:1,:$>=]
o=================o
Photon not © or ™ or ® 2019 by sugarfi
</pre>
