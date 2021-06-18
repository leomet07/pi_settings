import sys
import os
import dotenv
import action
import cli_tools
dotenv.load_dotenv()

if len(sys.argv) == 1:
	print("Submit a directory please!")
	exit(1)

bootdir = sys.argv[1]

if cli_tools.get_user_boolean_input("Do you want to create a wpa_supplicant.conf?"):
	network_name = os.getenv("NETWORK_NAME")
	network_password = os.getenv("NETWORK_PASSWORD")
	sensitive = action.create_wpa_supplicant_text(os.getenv("NETWORK_NAME"), os.getenv("NETWORK_PASSWORD"))
	
	action.create_wpa_supplicant_file(os.path.join(bootdir, "wpa_supplicant.conf"), sensitive )

	print("Created a wpa_supplicant.conf in ", bootdir)
else:
	print("Did not create a wpa_supplicant.conf ")

cli_tools.seperator()

if cli_tools.get_user_boolean_input("Do you want to enable ssh access?"):
	action.create_ssh_file()
	
	print("Enabled SSH access with a blank SSH file in ", bootdir)
else:
	print("Did not enable SSH access. No file was created in", bootdir)

cli_tools.seperator()

if cli_tools.get_user_boolean_input("Do you want to overclock your raspberry pi 4 to the max?"):
	print("Overclock of:")
	the_oc = action.create_max_oc(bootdir)
	print(the_oc)
	print("has been added to the end of ", os.path.join(bootdir, "config.txt"))
	
else:
	print("Did not add an overclock")

cli_tools.seperator()