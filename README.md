# crypto clipper builder

## A GUI based builder for making custom crypto stealing malware supporting btc, eth, ltc, xmr

gui features
- written with [customtkinter](https://github.com/TomSchimansky/CustomTkinter), [CTkToolTip](https://github.com/Akascape/CTkToolTip), [CTkMessagebox](https://github.com/Akascape/CTkMessagebox) and [hPyT](https://github.com/Zingzy/hPyT)
- uses pyarmor for obfuscating malware and pyinstaller for compiling to .exe
- allows setting custom icons to the malware .exe
- allows setting custom name for the malware .exe
- has documentation built into the GUI under the documentation tab

malware features
- supports Bitcoin, Ethereum, Litecoin and monero at the same time
- three different types of the same malware but using different methods. subprocess, ctypes and pyperclip
- duplicates and adds itself to startup apps for persistence
- has single use method
- allows discord webhook (whenever a address is detected you get a discord notification which says the computer name and that the address has been changed)
