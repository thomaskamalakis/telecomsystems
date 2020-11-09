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