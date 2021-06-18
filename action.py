import os
import dotenv
dotenv.load_dotenv()

def create_wpa_supplicant_text(network_name : str, network_password : str):
	template = ""
	with open(os.path.join("templates", "wpa_supplicant_template.txt"), "r") as file:
		template = file.read()

	sensitive = (template.replace("NETWORK_NAME", network_name)).replace("NETWORK_PASSWORD", network_password)
	
	return sensitive
def create_wpa_supplicant_file(path : str, sensitive : str):
	with open(path, "w") as file:
		file.write(sensitive)
		
if __name__ == "__main__":
	print(create_wpa_supplicant_text(os.getenv("NETWORK_NAME"), os.getenv("NETWORK_PASSWORD")))
