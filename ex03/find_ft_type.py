def all_thing_is_obj(object: any) -> int:
	typeof = type(object)
	if typeof == int:
		print("Type not found")
	elif typeof == str and (object == "Brian" or object == "Toto"):
		print(f"{object} is in the kitchen : {typeof}")
	elif typeof == list:
		print(f"List : {typeof}")
	elif typeof == set:
		print(f"Set : {typeof}")
	elif typeof == dict:
		print(f"Dict : {typeof}")
	elif typeof == tuple:
		print(f"Tuple : {typeof}")	
	return 42

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
