from __def__ import *
import time, math

target_set = input('[+] Enter the target/s (Slpit Targets Range with , ): ')
target_set.strip(' ')
target_ip_range = input('[+] Enter port/s (Slpit Port Range with - ): ')
target_ip_range.strip(' ')

start_time = time.time()

if '-' in target_ip_range:
    target_ip_range_start = int(target_ip_range.split('-')[0])
    target_ip_range_end = int(target_ip_range.split('-')[1])+1
else:
    target_ip_range_start = int(target_ip_range)
    target_ip_range_end = int(target_ip_range)+1

# print(port_scanner(ip_finder(target_set),target_ip_range_start,target_ip_range_end))
resualt = ''
if ',' in target_set:
    for target_set_single in target_set.split(','):
        print(f'\nstarting with {target_set_single} ...')
        resualt += port_scanner(target_set_single,target_ip_range_start,target_ip_range_end)

else:
    print(f'\nstarting with {target_set} ...')
    resualt = port_scanner(target_set,target_ip_range_start,target_ip_range_end)

end_time = time.time()
end_time = format(end_time-start_time)

print(resualt)
print(f"It took {round(float(end_time),1)} seconds to test ports")
