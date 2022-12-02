from __def__ import *
import time, math
import sys

clearscreen()
logo()

target_set = input('[+] Enter the target/s (Slpit Targets Range with , ): ')
target_set.strip(' ')

clearscreen()
logo()
print('Target/s: %s' %target_set)

target_ip_range = input('[+] Enter port/s (Slpit Port Range with - ): ')
target_ip_range.strip(' ')

clearscreen()
logo()
print('Target/s: %s' %target_set)
print('Timeout value set on %s' %target_ip_range)

while True:
    target_ip_timeout = ''
    target_ip_timeout = input('[+] Set Timeout (Default=0.5): ')
    target_ip_timeout.strip(' ')
    try:
        if target_ip_timeout.isdigit() or type(target_ip_timeout) == str:
            target_ip_timeout = float(target_ip_timeout)
            break
        elif target_ip_timeout == '':
            target_ip_timeout = 0.5
            break
    except:
        print('Unverified input!')

clearscreen()
logo()
print('Target/s: %s' %target_set)
print('Port Range: %s' %target_ip_range)
print('Timeout: %s' %target_ip_timeout)

while True:
    verbosemode = input('[+] do you want to activate Verbose mode (Y/n): ')
    verbosemode.strip(' ')
    if verbosemode == 'y' or verbosemode == 'Y' or verbosemode == '':
        verbosemode = 'Active'
        break
    elif verbosemode == 'N' or verbosemode == 'n':
         verbosemode = 'Deactive'
         break

clearscreen()
logo()
print('Target/s: %s' %target_set)
print('Timeout: %s' %target_ip_timeout)
print('Port Range: %s' %target_ip_range)
print('verbose mode: %s' %verbosemode)


start_time = time.time()

if '-' in target_ip_range:
    target_ip_range_start = int(target_ip_range.split('-')[0])
    target_ip_range_end = int(target_ip_range.split('-')[1])+1
else:
    target_ip_range_start = int(target_ip_range)
    target_ip_range_end = int(target_ip_range)+1

resualt = ''
if ',' in target_set:
    for target_set_single in target_set.split(','):
        print(f'\nscanning {target_set_single} ...')
        resualt += port_scanner(target_set_single,target_ip_range_start,\
            target_ip_range_end,target_ip_timeout,verbosemode)

else:
    print(f'\nscanning {target_set} ...')
    resualt = port_scanner(target_set,target_ip_range_start,target_ip_range_end,\
        target_ip_timeout,verbosemode)

end_time = time.time()
end_time = format(end_time-start_time)

clearscreen()
logo()
print('Target/s: %s' %target_set)
print('Timeout: %s' %target_ip_timeout)
print('Port Range: %s' %target_ip_range)
print('verbose mode: %s' %verbosemode)

print(resualt)
print(f"It took {round(float(end_time),1)} seconds to test ports")
