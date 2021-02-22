 #!/usr/bin/python

import requests, json, sys, socket, collections
 
# Ignore SSL Errors
#requests.packages.urllib3.disable_warnings()

from ansible.module_utils.basic import AnsibleModule
from netmiko import ConnectHandler
from datetime import datetime

# def CONFIGURE_JUN(jun_server,jun_username,jun_password,list_IP):
def CONFIGURE_JUN(jun_server,jun_username,jun_password):	

 list_IP = ['100.6.6.6', '100.7.7.7', '100.8.8.8', '100.9.9.9']
 listi = ["untrust","unstrust-ISP2"]
 output = []
 i = 0
	
 device = ConnectHandler(device_type='juniper', host = '192.168.72.200',username ='root',password ='Ertyui1',port = '22')
 print('connex ok')
# config_commands = ['configure'] 
# temp = device.send_config_set(config_commands, exit_config_mode=False)
# output.insert(i,temp)
# i = i+1 

 for var_int in listi: 
    
    config_commands = ['edit security zones security-zone ' + var_int + ' address-book'] 
    temp = device.send_config_set(config_commands, exit_config_mode=False)
    output.insert(i,temp)
    i = i+1 

    for var_ip in list_IP:
       
       cmd = "set address IP_" + var_ip + " " + var_ip
       temp = device.send_config_set(cmd, exit_config_mode=False) 
       output.insert(i,temp)
       i = i+1
                	
    temp = device.send_config_set("edit address-set IP_Blocked",exit_config_mode=False)       
    output.insert(i,temp)   
    i = i+1 

    for var2_ip  in list_IP:

       cmd = "set address IP_" + var2_ip
       temp = device.send_config_set(cmd, exit_config_mode=False)
       output.insert(i,temp)
       i = i+1
 
    exit_commands = [ 'exit','exit']	
    temp = device.send_config_set(exit_commands,exit_config_mode=False)
    output.insert(i,temp)          
    i = i+ 1
 
 temp = device.commit()
 output.insert(i,temp)

 for varout in output:     
  print (varout)
	
def main():

	module_args = dict(
		jun_server=dict(type="str", required=False),
		username=dict(type="str", required=False),
		password=dict(type="str",no_log=True, required=False)
#		list_ip=dict(type="list", required=False)
	)
	
#	module = AnsibleModule(argument_spec=module_args)

#	A_jun_server = module.params["jun_server"]
	A_jun_server = "192.168.72.200"    
#	A_username = module.params["username"]
	A_username = "root"
#	A_password = module.params["password"]
	A_password ="Ertyui1"
#	A_list_ip = module.params["list_ip"]


#       result=CONFIGURE_JUN(A_jun_server,A_username,A_password,A_list_ip)
	result=CONFIGURE_JUN(A_jun_server,A_username,A_password)

#	module.exit_json(changed=True, result=result)
	
if __name__ == '__main__':
	main()
