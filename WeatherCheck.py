print("")
humidity = int(input("Enter the humidity percentage: "))
print(" ")
temp = int(input("Enter the temprature (in Celsius): "))
print(" ")
	
is_sunny = input("Is the weather sunny? True or false? ")

while is_sunny.lower() == "true":
	is_sunny = True
if is_sunny.lower() == "false":
	is_sunny = False
else:
	print("Answer with true or false")
	
print(" ")

if humidity >= 60 and temp >= 25 and is_sunny:
	print("The weather is hot and humid 🥵")
	print("The sun is shining fiercefully ☀️")
elif humidity >= 60 and temp >= 25 and not is_sunny:
	print("The weather is hot and moist 🥵")
	print("The sun is hidden behind the clouds 🌥️️")
elif humidity >= 60 and 24 > temp > 10 and is_sunny:
	print("The weather is warm and humid 🌫️")
	print("The sun is shining brightly ☀️️")
elif humidity >= 60 and 24 > temp > 10 and not is_sunny:
	print("The weather is warm and humid 🌫️")
	print("The sun is hidden behind the clouds 🌥️")
elif humidity >= 60 and temp <= 9  and is_sunny:
	print("The weather is cold and humid 🌫️")
	print("The sun is glowing through the fog ☀️️")				
elif humidity >= 60 and temp <= 9  and not is_sunny:
	print("The weather is cold and humid 🌫️")
	print("The sun is hidden behind the clouds 🌥️")	
														
elif 59 > humidity > 30 and 24 > temp > 10 and is_sunny:
	print("The weather is warm and a bit dank ✨")
	print("The sun is shining brightly ☀️")
elif 59 > humidity > 30 and 24 > temp > 10 and not is_sunny:
	print("The weather is warm and a bit dank ✨")
	print("Clouds are everywhere 🌥️")
elif 59 > humidity > 30 and temp >= 25 and is_sunny:
	print("The weather is hot and a bit dank 🥵")
	print("The sun is shining brightly ☀️")
elif 59 > humidity > 30 and temp >= 25 and not is_sunny:
	print("The weather is hot and a bit dank 🥵")
	print("The sun is hidden behind the clouds 🌥️")
elif 59 > humidity > 30 and temp <= 9 and is_sunny:
	print("The weather is cold and a bit dank 🌫️")
	print("The sun is lighting the sky 🌤️") 
elif 59 > humidity > 30 and temp <= 9 and not is_sunny:
	print("The weather is cold and a bit dank 🌫️")
	print("The sun is hiding from the vision 🌤️")

elif 30 > humidity >= 0 and temp >= 25 and is_sunny:
	print("The weather is hot and dry 🥵")
	print("The sun is shining scorching hot ☀️")
elif 30 > humidity >= 0 and temp >= 25 and not is_sunny:
	print("The weather is hot and dry 🥵")
	print("Clouds are protacting us ☁️") 	
elif 30 > humidity >= 0 and 24 > temp > 10 and is_sunny:
	print("The weather is warm and dry ⭐️")
	print("The sun is shining brightly ☀️")
elif 30 > humidity >= 0 and 24 > temp > 10 and not is_sunny:
	print("The weather is freezing and arid 🌬️")
	print("Clouds are everywhere ☁️")
elif 30 > humidity >= 0 and temp <= 9 and is_sunny:
	print("The weather is freezing and arid 🌬️")
	print("The sun is shining brightly ☀️")
elif 30 > humidity >= 0 and temp <= 9 and not is_sunny:
	print("The weather is freezing and arid 🌬️")
	print("Clouds are ruling the sky ☁️")

