import pymem
from resolver import resolve_ptr_chain

pm = pymem.Pymem('ac_client.exe')
base = pymem.process.module_from_name(
    pm.process_handle, 'ac_client.exe'
).lpBaseOfDll

pointer_base = base + 0x0017E0A8
offset = [0xEC]

#resolver

while True:
    final_address = resolve_ptr_chain(pm, pointer_base, offset)
    value = pm.read_int(final_address)
    print('Health: ', value)
    uinp = int(input('Enter new health value: '))
    pm.write_int(final_address, uinp)