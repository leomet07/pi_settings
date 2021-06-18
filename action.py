import os
import dotenv
dotenv.load_dotenv()

def create_wpa_supplicant_text(network_name : str, network_password : str):
	template = ""
	with open(os.path.join("templates", "wpa_supplicant_template.txt"), "r") as file:
		template = file.read()

	sensitive = (template.replace("NETWORK_NAME", network_name)).replace("NETWORK_PASSWORD", network_password)
	
	return sensitive

def create_wpa_supplicant_file(pathfile : str, sensitive : str):
	with open(pathfile, "w") as file:
		file.write(sensitive)

def create_ssh_file(bootdir):
	with open(os.path.join(bootdir, "SSH"), "w") as file:
		pass

def create_max_oc_text():
	template = ""
	with open(os.path.join("templates", "max_oc_template.txt"), "r") as file:
		template = file.read()
	
	return template 
def create_max_oc(bootdir):
	max_oc_text = create_max_oc_text()
	with open(os.path.join(bootdir, "config.txt"), "a") as file:
		file.write("\n" + max_oc_text )
	
	return max_oc_text 


if __name__ == "__main__":
	print(create_wpa_supplicant_text(os.getenv("NETWORK_NAME"), os.getenv("NETWORK_PASSWORD")))
