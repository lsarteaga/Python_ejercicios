"""
1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high,
Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
"""
    
text = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, \
         Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
text2 = ""
aux = ""
count = 0
for i in text:
	if i.isupper() and i != "I":
		if i != aux and aux != '':
			if count > 4:
				count = 1
			if count == 1:
				print(text2)
			elif count == 2:
				print('    ' + text2)
			elif count > 2:
				print('        ' + text2)
			text2 = ''
		aux = i
		text2 += i
		count += 1
	else:
		text2 += i
print('    ' + text2)
		