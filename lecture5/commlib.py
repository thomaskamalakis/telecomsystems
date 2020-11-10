import numpy as np
import matplotlib.pyplot as plt

# function to create the square pulse
def square(t , T):    
    f = np.logical_and( t < T / 2.0 , t >= -T/2.0 )
    return f.astype('float')

# create time axis
def time_axis(Tmax, N):   
    n = np.arange(-N / 2.0, N / 2.0, 1)
    Dt = 2*Tmax / N
    return n * Dt

# create frequency axis
def frequency_axis(t):
    N = t.size
    Dt = t[1] - t[0]
    n = np.arange(-N / 2.0, N / 2.0, 1)
    Df = 1.0 / ( N * Dt)
    return n * Df

# Calculate spectrum of x using FFT
def spectrum(t, x):
    Dt = t[1] - t[0]
    return Dt*np.fft.fftshift(np.fft.fft(np.fft.fftshift(x)))

# Inverse fourier transform 
def inv_spectrum(f, X):
    Df = f[1] - f[0]
    N = f.size
    return N * Df * np.fft.fftshift(np.fft.ifft(np.fft.fftshift(X)))

# Square filter
def square_filter(f , Fmax):
    return square(f, Fmax)

# System action    
def system_action(t, x, Hcallable):
    f = frequency_axis(t)
    Hf = Hcallable(f)
    X = spectrum(t, x)
    Y = X * Hf
    return inv_spectrum(f, Y)
    
# Calculate energy
def energy(t, x):
    return np.trapz( np.abs(x) ** 2.0, t)

# Calculate average power
def average_power(t, x):
    ta = np.min(t)
    tb = np.max(t)
    return energy( t , x ) / ( tb - ta )

# Calculate a simple cosine sinal
def cos_signal(A, f0, t, phi = 0.0 ):
    return A * np.cos ( 2.0 * np.pi * f0 * t + phi )

# plot signal
def plot_signal(t, x, plot_type = 'o', close_all = False,
                      xlabel = 't', ylabel = 'x(t)', figure_no = None,
                      xlim = None, ylim = None, show_grid = False):
    
    if close_all:
        plt.close('all')
        
    if figure_no is None:
        plt.figure()
    else:
        plt.figure(figure_no)
    
    plt.plot( t, x, plot_type )
    plt.xlabel( xlabel )
    plt.ylabel( ylabel ) 
    
    if xlim is not None:
        plt.xlim(xlim)
    
    if ylim is not None:
        plt.ylim(ylim)
    
    if show_grid:
        plt.grid()
    
# power spectral density    
def power_density(t, x):
    T = np.max(t) - np.min(t)
    return 1.0 / T * np.abs( spectrum(t,x) ) ** 2.0

def default_pulse(t, TS):
    return square(t - TS/2.0, TS)
    
# pulse amplitude modulation waveform : slow version    
def pam_waveform1(ak, TS, p_callable = default_pulse, 
                 samples = 10, tinitial = 0, tguard = 0.0):
    
    Dt = TS / samples                                # sampling period    
    Nguard = np.round(tguard / Dt)                   # guard points                         
    Ntot = 2 * Nguard + samples * ak.size            # total number of points   
    
    x = np.zeros( Ntot.astype(int) )
    t = np.arange( tinitial, tinitial + Ntot * Dt, Dt )
        
    for k, a in enumerate(ak):        
        x += a * p_callable( t - k * TS, TS )
        
    return t, x

# pulse amplitude modulation : fast version
def pam_waveform2(ak, TS,  
                 samples = 10, tinitial = 0, tguard = 0.0):
    
    Dt = TS / samples                                # sampling period    
    Nguard = np.round(tguard / Dt)                   # guard points                         
    Ntot = 2 * Nguard + samples * ak.size            # total number of points   
    
    x = np.zeros( Ntot.astype(int) )
    t = np.arange( tinitial, tinitial + Ntot * Dt, Dt )

    i = np.floor( (t - tinitial) / TS).astype(int)
    j = np.where( np.logical_and(i >= 0, i < ak.size ) )

    x[j] = ak[ i[j] ]
    return t, x

# windowed version of a signal
def window(t, x, ta, tb):
    
    j = np.where( np.logical_and(t >= ta, t <= tb ) )
    y = np.zeros( x.size )
    y[j] = x[j]
    return y

# PAM symbol constellation
def pam_constellation(M, beta = 1):
    m = np.arange(1, M + 1).astype(int)
    return (2 * m - M - 1) * beta
    
# Plot symbol constellation
def plot_constellation(c, figure_no = None, title = None):
    
    if figure_no is None:
        plt.figure()
    else:
        plt.figure(figure_no)
        
    cr = np.real(c)
    ci = np.imag(c)
    plt.plot(cr, ci, 'o')
    plt.xlabel('Real')
    plt.ylabel('Imag')
    
    if title is not None:
        plt.title(title)
        
# gray coding        
def gray_code(m):

    if m==1:
        g = ['0','1']

    elif m>1:
        gs = gray_code(m-1)
        gsr = gs[::-1]
        gs0 = ['0' + x for x in gs]
        gs1 = ['1' + x for x in gsr]
        g= gs0 + gs1
    return g 

def pam_gray_map(M, beta = 1):
    
    gc = gray_code( np.log2(M) )
    Am = pam_constellation(M, beta = beta)
    pam_map = []
    
    for i, cw in enumerate(gc):
        
        pam_map.append([ i, gc[i], Am[i] ])
        
    return pam_map

def plot_map( smap, figure_no = None, disp_x = 0.0, disp_y = 0.0 ):
    
    for i, bits, symbol in smap:
        plt.plot( np.real(symbol), np.imag(symbol), 'o' )
        plt.text( np.real(symbol) + disp_x, np.imag(symbol) + disp_y, bits, rotation=90)

# build a dictionary like map for faster encoding        
def pam_gray_forward_map(M, beta = 1):

    pam_map = pam_gray_map(M, beta = beta)
    symbols = [x[2] for x in pam_map]
    bits = [x[1] for x in pam_map]
    forward_map = {}
    
    for i, symbol in enumerate(symbols):
        key = bits[i]
        forward_map[ key ] = symbol
        
    return forward_map

def array_to_str(a):
    astr = [str(x) for x in a]
    return ''.join(astr)

# bits to symbols
def bits_to_symbols(bits, fmap, return_bits = False):
    
    M = len( fmap )
    m = np.log2( M ).astype( int )
    Nbits = bits.size
    
    symbols = []
    bitgroupsψο = []
    i = 0
    j = 0
    
    while i < Nbits:
        key = array_to_str(bits[ i : i+m ])
        bitgroups.append( key )
        symbols.append( fmap[ key ] )
        i += m
        j += 1
    if not return_bits:    
        return np.array(symbols)    
    else:
        return np.array(symbols), bitgroups

# random bit series
def random_bits(Nbits):
    return np.random.randint(0, high = 2, size = Nbits, dtype = int)
        
            
