items = ["Mic", "Phone", 456, 987.4, "Justin", "Bag", 54, "Aspandiyar"]

def parse_list(some_list):
	str_list_items = []
	int_list_items = []
	for i in some_list:
		if isinstance(i, int) or isinstance(i, float):
			int_list_items.append(i)
		elif isinstance(i, str):
			str_list_items.append(i)
		else:
			pass
	return int_list_items, str_list_items			

print(parse_list(items))	