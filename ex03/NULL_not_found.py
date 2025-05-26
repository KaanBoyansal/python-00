def NULL_not_found(object: any) -> int:
	typeof = type(object)
	flag = 1
	print_str = ""
	if object == None:
		flag = 0
		print_str += "Nothing"
	elif typeof == str and not object:
		flag = 0
		print_str += "Empty"
	elif typeof == bool and object == 0:
		flag = 0
		print_str += "Fake"
	elif typeof == int and object == 0:
		flag = 0
		print_str += "Zero"
	elif isinstance(object, float) and object != object:
		flag = 0
		print_str += "Cheese"
	elif isinstance(object, (list, tuple, dict, set)) and len(object) == 0:
		flag = 0
	if flag == 0:
		print_str += f": {object} {typeof}"
		print(print_str)
	elif flag:
		print("Type not Found")
	return flag

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
