import sys
import os
import dotenv
from action import create_wpa_supplicant_text, create_wpa_supplicant_file
dotenv.load_dotenv()

if len(sys.argv) == 1:
	print("Submit a directory please!")
	exit(1)

print(sys.argv[1])

create_wpa_supplicant_file(os.path.join(sys.argv[1], "wpa_supplicant.conf"), create_wpa_supplicant_text(os.getenv("NETWORK_NAME"), os.getenv("NETWORK_PASSWORD")))