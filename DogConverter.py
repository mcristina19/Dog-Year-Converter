# dog years converter
# input dog years
# output human years


def dog_year_converter(years):
	years = int(years)
	if years < 0:
		return 'Value must be larger than 0'
	return years*7

human_years = input('Enter your dogs age:')

print(dog_year_converter(human_years), 'Years old')





