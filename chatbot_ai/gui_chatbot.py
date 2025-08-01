# gui_chatbot.py

import tkinter as tk
from tkinter import messagebox
from vmware_api import list_vms, power_on_vm, power_off_vm, get_vm_details_from_optum
import json

# 🔐 Hardcoded Bearer Token
OPTUM_BEARER_TOKEN = "your_actual_bearer_token_here"  # <-- Replace with real token

def handle_command():
    cmd = entry.get().strip().lower()
    output.delete(1.0, tk.END)

    try:
        if cmd == "list vms":
            vms = list_vms()
            if vms:
                output.insert(tk.END, "📋 VMs:\n" + "\n".join(vms))
            else:
                output.insert(tk.END, "No VMs found.")

        elif cmd.startswith("power on"):
            vm_name = cmd.replace("power on", "").strip()
            if vm_name:
                result = power_on_vm(vm_name)
                output.insert(tk.END, result)
            else:
                output.insert(tk.END, "⚠️ Please specify a VM name.")

        elif cmd.startswith("power off"):
            vm_name = cmd.replace("power off", "").strip()
            if vm_name:
                result = power_off_vm(vm_name)
                output.insert(tk.END, result)
            else:
                output.insert(tk.END, "⚠️ Please specify a VM name.")

        elif cmd.startswith("vm "):
            server = cmd.replace("vm", "").strip()
            if server:
                data = get_vm_details_from_optum(OPTUM_BEARER_TOKEN, server=server)
                pretty = json.dumps(data, indent=2)
                output.insert(tk.END, f"📦 VM details for '{server}':\n{pretty}")
            else:
                output.insert(tk.END, "⚠️ Please specify a server name after 'vm'")

        else:
            output.insert(tk.END, "❓ Unknown command. Try:\n- list vms\n- power on <vm>\n- power off <vm>\n- vm <server>")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("🖥️ VMware Chatbot")

# Title label
title_label = tk.Label(root, text="VMware Chatbot Interface", font=("Arial", 14))
title_label.pack(pady=10)

# Entry box
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=5)

# Send button
send_button = tk.Button(root, text="Send Command", command=handle_command, font=("Arial", 12))
send_button.pack(pady=5)

# Output area
output = tk.Text(root, height=20, width=80, font=("Courier", 10), wrap=tk.WORD)
output.pack(pady=10)

# Start GUI loop
root.mainloop()
