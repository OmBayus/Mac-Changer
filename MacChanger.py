import subprocess
import optparse
import time
from tqdm import tqdm
import re

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help = "InterFace to Change")
    parse_object.add_option("-m","--mac",dest="mac_address",help = "Mac to Change")

    return parse_object.parse_args()



def user_inputss():
    (user_inputs,arguments) = get_user_input()
    user_interface = user_inputs.interface
    user_mac_address = user_inputs.mac_address
    return user_interface,user_mac_address

def loading():
    print("Lutfen Bekleyiniz")
    for i in tqdm(range(0,100)):
        time.sleep(0.01)

def change_mac_change(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_mac(interfacee):
	ifconfig_interface = subprocess.check_output(["ifconfig",interfacee])
	new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_interface)
	return new_mac.group(0)




print("Mac Changera Hosgeldiniz")

get_user_input()
loading()
(user_interface,user_mac_address) = user_inputss()
change_mac_change(user_interface,user_mac_address)

if control_mac(user_interface) == user_mac_address:
	print("Basariyla Mac Adresiniz Degistirildi")
else:
	print("""
		Mac Adresi degistirme islemi Basarisiz
		Dogru mac adresi dizilimi yazdiginizdan emin olun. (00:11:22:33:44:55 seklinde)
		""")