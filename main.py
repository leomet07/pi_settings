import sys
import os
import dotenv
from action import create_wpa_supplicant_text, create_wpa_supplicant_file
dotenv.load_dotenv()

if len(sys.argv) == 1:
	print("Submit a directory please!")
	exit(1)

bootdir = sys.argv[1]

if input("Do you want to create a wpa_supplicant.conf? Press Y if yes: ").lower() == "y":
	network_name = os.getenv("NETWORK_NAME")
	network_password = os.getenv("NETWORK_PASSWORD")
	sensitive = create_wpa_supplicant_text(os.getenv("NETWORK_NAME"), os.getenv("NETWORK_PASSWORD"))

	filepath = os.path.join(bootdir, "wpa_supplicant.conf")
	
	create_wpa_supplicant_file(filepath, sensitive )
	print("Created a wpa_supplicant.conf in ", bootdir)
else:
	print("Did not create a wpa_supplicant.conf ")