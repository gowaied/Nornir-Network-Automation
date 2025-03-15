from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result
from getpass import getpass

# Gathering Credentials
username = input('Enter the username: ')
password = getpass('Enter the password: ')
secret = getpass('Enter the secret: ')

# Nornir Init
nr = InitNornir(config_file='config.yml')
nr.inventory.defaults.username = username
nr.inventory.defaults.password = password

for host in nr.inventory.hosts.values():
    host.data['secret'] = secret

# Loopback config on Routers
routers = ['R1', 'R2', 'R3', 'R4']
loopback_ip = ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4']

for router,ip in zip(routers,loopback_ip):
    commands = [
        'int lo 0',
        f'ip address {ip} 255.255.255.255',
        'no shut'
    ]

    target_rt = nr.filter(name=router)
    output = target_rt.run(task=netmiko_send_config, config_commands=commands, enable=True)
    print_result(output)
    verification = target_rt.run(task=netmiko_send_command, command_string='sh ip int br')
    print_result(verification)

input('Press Enter to start VLAN configurations......')


# Vlan config on switches
switches = ['SW','SW2']
VLANs_IDs = ['10','20','30','40']
VLAN_names = ['Engineering', 'Sales', 'HR', 'Accounting']

for switch in switches:
    for id,name in zip(VLANs_IDs,VLAN_names):
        commands = [
            f'vlan {id}',
            f'name {name}'
        ]
        target_sw = nr.filter(name=switch)
        output = target_sw.run(task=netmiko_send_config, config_commands=commands, enable=True)
        print_result(output)
    verification=target_sw.run(task=netmiko_send_command, command_string='sh vlan br')
    print_result(verification)
