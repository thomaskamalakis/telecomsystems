import commlib as cl

M = 16
Am = cl.pam_constellation( M )
cl.plot_constellation( Am, title = 'PAM, M = ' + str(M))