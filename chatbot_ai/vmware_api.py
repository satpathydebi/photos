# vmware_api.py

from pyVim.connect import SmartConnect, Disconnect
import ssl
import config
import atexit
import requests

def connect_to_vcenter():
    context = ssl._create_unverified_context()
    si = SmartConnect(
        host=config.VCENTER_HOST,
        user=config.VCENTER_USER,
        pwd=config.VCENTER_PASSWORD,
        port=config.VCENTER_PORT,
        sslContext=context
    )
    atexit.register(Disconnect, si)
    return si

def list_vms():
    si = connect_to_vcenter()
    content = si.RetrieveContent()
    vm_list = []
    for datacenter in content.rootFolder.childEntity:
        vm_folder = datacenter.vmFolder
        vms = vm_folder.childEntity
        for vm in vms:
            vm_list.append(vm.name)
    return vm_list

def power_on_vm(vm_name):
    si = connect_to_vcenter()
    content = si.RetrieveContent()
    for datacenter in content.rootFolder.childEntity:
        vm_folder = datacenter.vmFolder
        vms = vm_folder.childEntity
        for vm in vms:
            if vm.name == vm_name:
                if not vm.runtime.powerState == "poweredOn":
                    task = vm.PowerOn()
                    return f"Powering on {vm_name}..."
                else:
                    return f"{vm_name} is already powered on."
    return f"VM {vm_name} not found."

def power_off_vm(vm_name):
    si = connect_to_vcenter()
    content = si.RetrieveContent()
    for datacenter in content.rootFolder.childEntity:
        vm_folder = datacenter.vmFolder
        vms = vm_folder.childEntity
        for vm in vms:
            if vm.name == vm_name:
                if vm.runtime.powerState == "poweredOn":
                    task = vm.PowerOff()
                    return f"Powering off {vm_name}..."
                else:
                    return f"{vm_name} is already powered off."
    return f"VM {vm_name} not found."

def get_vm_details_from_optum(token, server="rpxx", env="prod", resource_state="all"):
    url = f"https://cloudopsapi.optum.com/api/vrops_vm_details/?server={server}&env={env}&resource_state={resource_state}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": f"Failed to fetch data. Status code: {response.status_code}, Message: {response.text}"
        }
