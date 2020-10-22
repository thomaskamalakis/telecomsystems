import numpy as np
import matplotlib.pyplot as plt

# function to create the square pulse
def square(t , T):    
    f = np.logical_and( t <= T / 2.0 , t >= -T/2.0 )
    return f.astype('float')

# create time axis
def time_axis(Tmin, Tmax, N):   
    n = np.arange(-N / 2.0, N / 2.0, 1)
    Dt = (Tmax - Tmin) / N
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
def plot_signal(t, x, xlabel = 't', ylabel = 'x(t)', figure_no = None):
    if figure_no is None:
        plt.figure()
    else:
        plt.figure(figure_no)
    
    plt.plot( t, x )
    plt.xlabel( xlabel )
    plt.ylabel( ylabel )  
    
def power_density(t, x):
    T = np.max(t) - np.min(t)
    return 1.0 / T * np.abs( spectrum(t,x) ) ** 2.0