import winreg
#Connecting to keys

#Create lists of keys.  Had to make two different lists, one for HKCU and one for HLM. 
#We will just run two separate loops.
HKCU_keys_list = ["SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders"]
HKCU_keys_list += ["SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"]
HKCU_keys_list += ["Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce "]
HKCU_keys_list += ["Software\\Microsoft\\Windows\\CurrentVersion\Policies\\Explorer\\Run"]

print(f"\n[*****] First we will start with the HKEY current users keys[*****]\n")
for key in HKCU_keys_list:
    try:
        print(f"\n[+] Listing the values from key {key}...")
        access_registry = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)
        access_key = winreg.OpenKey(access_registry,key)
        #Grabbing the key

        #Determine how many keys there are total, so that we can look through them all

        num_keys = winreg.QueryInfoKey(access_key)
        length = num_keys[1]
        print(f"[+] There are {length} keys in {key}\n[+] They are: ")


        #Show the values for the actual keys. Here we can see if something is off.
        for n in range(length):
            try:
                x =winreg.EnumValue(access_key,n)
                print("\t" + x[0],x[1])
            except:
                continue
    except:
            continue

#There is probably a more pythonic way without creating an entire separate loop, but I was not able to find it due to 
#The required CONSTANT for the key type. Winreg library requies HKEY_CURRENT_USER and the like to be hard-coded here. 
HKLM_keys_list = ["SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders"]
HKLM_keys_list += ["SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders"]
HKLM_keys_list += ["System\\CurrentControlSet\\Services"]
HKLM_keys_list += ["Software\\Microsoft\\Windows\\CurrentVersion\Policies\\Explorer\\Run"]

print(f"\n\n[*****] Next we will examine with the HKEY local machine keys [*****]\n\n")

for key in HKLM_keys_list:
    try:
        print(f"\n[+] Listing the values from key {key}...")
        access_registry = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
        access_key = winreg.OpenKey(access_registry,key)
        #Grabbing the key

        #Determine how many keys there are total, so that we can look through them all

        num_keys = winreg.QueryInfoKey(access_key)
        length = num_keys[1]
        print(f"[+] There are {length} keys in {key}\n[+] They are:")


        #Show the values for the actual keys. Here we can see if something is off.
        for n in range(length):
            try:
                x =winreg.EnumValue(access_key,n)
                print("\t" + x[0],x[1])
            except:
                continue
    except:
        continue