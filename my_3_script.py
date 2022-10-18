 #!/usr/bin/env python3
import sys

# the typed number could be an integer when you write the argument in this way. If you don't put int then it will require a string as input (' ') 
fish = int(sys.argv[1])
if fish > 28:
	message = "too much"
	print (fish, message)
elif fish < 28:
	message = "too little"
	print (fish, message)
else:
	message = "is great temperature for the fish!"
	print (fish, message)

