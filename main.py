import sys
import os
import dotenv
from action import create_wpa_supplicant_text, create_wpa_supplicant_file
import cli_tools
dotenv.load_dotenv()

if len(sys.argv) == 1:
	print("Submit a directory please!")
	exit(1)

bootdir = sys.argv[1]

if cli_tools.get_user_boolean_input("Do you want to create a wpa_supplicant.conf?"):
	network_name = os.getenv("NETWORK_NAME")
	network_password = os.getenv("NETWORK_PASSWORD")
	sensitive = create_wpa_supplicant_text(os.getenv("NETWORK_NAME"), os.getenv("NETWORK_PASSWORD"))
	
	create_wpa_supplicant_file(os.path.join(bootdir, "wpa_supplicant.conf"), sensitive )

	print("Created a wpa_supplicant.conf in ", bootdir)
else:
	print("Did not create a wpa_supplicant.conf ")

if cli_tools.get_user_boolean_input("Do you want to enable ssh access?"):
	with open(os.path.join(bootdir, "SSH"), "w") as file:
		pass
	print("Enabled SSH access with a blank SSH file in ", bootdir)

