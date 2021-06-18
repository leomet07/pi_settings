def get_user_boolean_input(question : str):
	boolean = input(question + " Press Y if yes: ").lower() == "y"

	return boolean