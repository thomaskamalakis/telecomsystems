import commlib as cl
import numpy as np

systems = ['2-PAM', '4-PAM', '8-PAM', '16-PSK']

for s in systems:
    sp = s.split('-')
    M = int(sp[0])
    system_type = sp[1]
    
    if system_type == 'PAM':
        c = cl.pam_constellation(M)
        c.set_SNR_range( np.arange(4, 40, 1) )
        
    elif system_type == 'PSK':
        c = cl.psk_constellation(M)
        c.set_SNR_range( np.arange(4, 30, 1) )
        
    elif system_type == 'QAM':
        c = cl.qam_constellation(M)
        c.set_SNR_range( np.arange(4, 30, 1) )
    
    c.setup_bermap()    
    
            
