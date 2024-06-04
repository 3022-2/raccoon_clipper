# raccoon crypto clipper written in python

![Documentation](https://img.shields.io/badge/documentation-yes-brightgreen)
![Maintenance](https://img.shields.io/maintenance/yes/2025)
![GitHub issues](https://img.shields.io/github/issues/3022-2/raccoon_clipper)
![GitHub stars](https://img.shields.io/github/stars/3022-2/raccoon_clipper)
![GitHub release](https://img.shields.io/github/v/release/3022-2/raccoon_clipper)


## A GUI based builder for making custom crypto stealing malware that bypasses most antiviruses including windows defender
## GUI AND MALWARE DESIGNED FOR WINDOWS COMPUTERS - ANY OTHER SYSTEM WONT RUN
# features
gui features
- written with [customtkinter](https://github.com/TomSchimansky/CustomTkinter), [CTkToolTip](https://github.com/Akascape/CTkToolTip), [CTkMessagebox](https://github.com/Akascape/CTkMessagebox) and [hPyT](https://github.com/Zingzy/hPyT)
- uses [pyarmor](https://github.com/dashingsoft/pyarmor) for obfuscating malware and [pyinstaller](https://github.com/pyinstaller/pyinstaller) for compiling to .exe
- allows setting custom icons to the malware .exe
- allows setting custom name for the malware .exe
- has documentation built into the GUI under the documentation tab

malware features
- undetected by majority of anti virus softwares including windows defender
- supports Bitcoin, Ethereum, Litecoin and monero at the same time
- three different types of the same malware but using different methods. subprocess, ctypes and pyperclip  
    - subprocess uses powershell commands to read and set clipboard - uses python standard libary so no need for the target to install anything
    - ctypes uses ctypes to read clipboard and powerhsell to set clipboard - uses python standard libary so no need for the target to install anything
    - pyperclip uses the pyperclip module to read and set clipboard - requires the target the run the command pip install pyperclip
- duplicates and adds itself to startup apps for persistence
- has single use method
- allows discord webhook (whenever a address is detected you get a discord notification which says the computer name and that the address has been changed), doesnt need any installs as uses http.client rather than requests to send POST requests to webhook 
- option to ping @everyone
- malware saved as .pyw and then compiled to .exe meaning that the malware runs in the background silently

features i will likely add in the future
- file extention spoofer
- file size pumper
# pictures
![Screenshot 2024-06-03 232449](https://github.com/3022-2/crypto_clipper_builder/assets/82278708/97864c80-a368-4855-b93f-13b15b58b065)
![Screenshot 2024-06-03 232529](https://github.com/3022-2/crypto_clipper_builder/assets/82278708/de08a1e4-5d0d-411c-b042-2fadab67f5a8)  
if discord is being used  
![Screenshot 2024-06-03 233516](https://github.com/3022-2/crypto_clipper_builder/assets/82278708/b0111946-3bed-425c-a871-ebf63b9d33f1)
# installation
```console
git clone https://github.com/3022-2/crypto_clipper_builder.git

cd crypto_clipper_builder-main

pip install -r requirements.txt

python main.pyw or double click main.pyw
```
# how to uninstall malware
1. kill the process in task manager and delete .exe
2. run uninstaller.py in uninstaller folder - if there is an error removing registry entry (cant find path) this is fine it means it isnt in startup anyway

you can also manual uninstall
1. kill the process in task manager and delete .exe
2. goto %appdata%
3. delete storage0 folder and CLPPTH folder
4. goto Software\Microsoft\Windows\CurrentVersion\Run in registry editor
5. delete entry named CLPPTH

# legal
DISCLAIMER: The code provided in this repository is intended for educational and malware analysis purposes only. Any use of this code for illegal or unethical activities is strictly prohibited. The author of this code shall not be held responsible for any misuse or damage resulting from its use. Users are solely responsible for ensuring compliance with applicable laws and ethical standards.  
WARNING: THIS IS MAKES MALWARE DESIGNED FOR STEALING CRYPTOCURRENCY. USE UNINSTALL GUIDE IF UNINSTALL CODE FAILS. (not found error doesn't necessarily mean didnt uninstall)

# contact
discord: cumsock0  
