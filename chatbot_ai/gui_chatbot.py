# gui_chatbot.py

import tkinter as tk
from tkinter import messagebox
from vmware_api import list_vms, power_on_vm, power_off_vm, get_vm_details_from_optum

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
        elif cmd.startswith("optum vm details"):
            parts = cmd.split()
            if len(parts) >= 4:
                token = parts[3]
                data = get_vm_details_from_optum(token)
                output.insert(tk.END, f"📦 Optum VM Details:\n{data}")
            else:
                output.insert(tk.END, "⚠️ Usage: optum vm details <Bearer_Token>")
        else:
            output.insert(tk.END, "❓ Unknown command. Try 'list vms', 'power on <vm>', 'power off <vm>', or 'optum vm details <token>'.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("🖥️ VMware Chatbot")

title_label = tk.Label(root, text="VMware Chatbot Interface", font=("Arial", 14))
title_label.pack(pady=10)

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=5)

send_button = tk.Button(root, text="Send Command", command=handle_command, font=("Arial", 12))
send_button.pack(pady=5)

output = tk.Text(root, height=15, width=60, font=("Courier", 10))
output.pack(pady=10)

root.mainloop()
