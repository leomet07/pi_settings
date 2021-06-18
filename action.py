import os
import dotenv
dotenv.load_dotenv()

def create_wpa_supplicant(network_name : str, network_password : str):
	template = ""
	with open(os.path.join("templates", "wpa_supplicant_template.txt")) as file:
		template = file.read()

	sensitive = (template.replace("NETWORK_NAME", network_name)).replace("NETWORK_PASSWORD", network_password)
	
	print(sensitive)
		
if __name__ == "__main__":
	create_wpa_supplicant(os.getenv("NETWORK_NAME"), os.getenv("NETWORK_PASSWORD"))
