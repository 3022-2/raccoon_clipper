import shutil
import winreg
import time
import sys
import os

def remove_files():
    try:        
        roaming_path = os.path.join(os.getenv('APPDATA'))
        folders_to_delete = ['Storage0', 'CLPPTH']
        for folder_name in folders_to_delete:
            folder_path = os.path.join(roaming_path, folder_name)
            shutil.rmtree(folder_path, ignore_errors=True)
    except Exception as e:
        print(f"Error while removing files: {e}")

def remove_registry_entry():
    try:
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key = winreg.HKEY_CURRENT_USER
        with winreg.OpenKey(key, key_path, 0, winreg.KEY_ALL_ACCESS) as reg_key:
            winreg.DeleteValue(reg_key, "CLPPTH")
    except Exception as e:
        print(f"Error while removing registry entry: {e}")

def main():
    remove_files()
    remove_registry_entry()
    print("Uninstallation completed.")
    time.sleep(0.5)

if __name__ == "__main__":
    choice = input("do you want to uninstall the malware from pc? y/n: ").strip().lower()
    if choice == "y":
        main()
    elif choice == "n":
        sys.exit()
    else:
        print(f"{choice} isnt an  option - quitting")
        sys.exit()
