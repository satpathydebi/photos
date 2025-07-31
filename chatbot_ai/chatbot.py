# chatbot.py

import vmware_api

def chatbot():
    print("🤖 VMware Chatbot Interface")
    print("Type 'help' for commands. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("👋 Goodbye!")
            break

        elif user_input == "help":
            print("""
Available commands:
- list vms
- power on <vm_name>
- power off <vm_name>
- optum vm details <token>
""")

        elif user_input.startswith("list vms"):
            vms = vmware_api.list_vms()
            print("📋 VMs:")
            for vm in vms:
                print(f"- {vm}")

        elif user_input.startswith("power on"):
            vm_name = user_input.replace("power on", "").strip()
            if vm_name:
                print(vmware_api.power_on_vm(vm_name))
            else:
                print("⚠️ Please specify a VM name.")

        elif user_input.startswith("power off"):
            vm_name = user_input.replace("power off", "").strip()
            if vm_name:
                print(vmware_api.power_off_vm(vm_name))
            else:
                print("⚠️ Please specify a VM name.")

        elif user_input.startswith("optum vm details"):
            parts = user_input.split()
            if len(parts) >= 4:
                token = parts[3]
                response = vmware_api.get_vm_details_from_optum(token)
                print("📦 Optum VM Details:")
                print(response)
            else:
                print("⚠️ Usage: optum vm details <Bearer_Token>")

        else:
            print("❓ Unknown command. Type 'help' to see available options.")

if __name__ == "__main__":
    chatbot()
