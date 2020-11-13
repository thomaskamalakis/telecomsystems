import numpy as np
import matplotlib.pyplot as plt

DEFAULT_PLOT_SETTINGS = {
    'plot_type' : '-o', 
    'xlabelt' : 't', 
    'ylabelt' : 'x(t)',
    'xlabelf' : 'f', 
    'ylabelf' : 'X(f)',    
    'xlimt' : None,
    'ylimt' : None,
    'xlimf' : None,
    'ylimf' : None,    
    'show_gridt' : False,
    'show_gridf' : False,    
    'titlet' : None,
    'titlef' : None    
}

def array_to_str(a):
    astr = [ str(x) for x in a ]
    return ''.join(astr)

def str_to_array(s):
    return np.array( [ int(x) for x in s ] )

# function to create the square pulse
def square(t , T):    
    f = np.logical_and( t < T / 2.0 , t >= -T/2.0 )
    return f.astype('float')

# Calculate a simple cosine sinal
def cos_signal(A, f0, t, phi = 0.0 ):
    return A * np.cos ( 2.0 * np.pi * f0 * t + phi )

# create time axis
def time_axis(Tmin, Tmax, N):   
    return np.linspace(Tmin, Tmax, N, endpoint = False)

# Plot signal
def plot_signal(t, x, plot_type = 'o', close_all = False,
                      xlabel = 't', ylabel = 'x(t)', figure_no = None,
                      xlim = None, ylim = None, show_grid = False, title = None):
    
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
        
    if title is not None:
        plt.title(title)

# random_bits : generation of random bits with equal probability
def random_bits(Nbits):
    return np.random.randint(0, high = 2, size = Nbits, dtype = int)


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

def str_to_bitsarray( bits_str ):    
    bits = np.zeros( len(bits_str) )
    for i, bit in enumerate(bits_str):
        bits[i] = int( bit )
    
    return bits

class signal:
    
    def __init__(self, t = None, samples = None, signal_callable = None):
        self.t = t               
        if self.t is not None:
            self.Dt = t[1] - t[0]
            self.N = t.size
            
        if samples is not None:
           self.samples = samples
        elif signal_callable is not None:
           self.signal = signal_callable(t)
          
        self.set_default_plot_properties()
        
    def set_time_axis(self, Tmin, Tmax, N):
        self.t = np.linspace(Tmin, Tmax, N, endpoint = False)
        self.N = N
        self.Dt = self.t[1] - self.t[0]
        
    def set_frequency_axis(self):
        n = np.arange(-self.N / 2.0, self.N / 2.0, 1)
        self.Df = 1.0 / ( self.N * self.Dt)
        self.f = n * self.Df
        
    def calc_spectrum(self):
        self.set_frequency_axis()
        self.spec = self.Dt * np.fft.fftshift( 
                              np.fft.fft( np.fft.fftshift( self.samples ) ) ) 
        
    def calc_invspectrum(self):
        self.samples = self.N * self.Df * np.fft.fftshift(
                              np.fft.ifft( np.fft.fftshift( self.spec ) ) )
        
    def energy(self):
        return np.trapz( np.abs( self.samples ) ** 2.0, self.t)
            
    def average_power(self):
        ta = np.min(self.t)
        tb = np.max(self.t)
        return self.energy() / ( tb - ta )

    def power_density(self):
        T = np.max(self.t) - np.min(self.t)
        
        if hasattr( self, 'spec' ):
            self.calc_spectrum()
            
        return 1.0 / T * np.abs( self.spec ) ** 2.0

    def set_default_plot_properties( self ):
        
        for key in DEFAULT_PLOT_SETTINGS:
            setattr( self, key, DEFAULT_PLOT_SETTINGS[key] )
        
    def plot(self, close_all = False, figure_no = None, what = 'time'):
        
        if what == 'time':
           plot_signal(self.t, self.samples, plot_type = self.plot_type, 
                       close_all = close_all, xlabel = self.xlabelt, 
                       ylabel = self.ylabelt, figure_no = figure_no,
                       xlim = self.xlimt, ylim = self.ylimt, 
                       show_grid = self.show_gridt, title = self.titlet)
        
        elif what == 'spec':
           plot_signal(self.f, self.spec, plot_type = self.plot_type, 
                       close_all = close_all, xlabel = self.xlabelf, 
                       ylabel = self.ylabelf, figure_no = figure_no,
                       xlim = self.xlimf, ylim = self.ylimf, 
                       show_grid = self.show_gridt, title = self.titlef)
    
    def windowed(self, ta, tb):
                
        j = np.where( np.logical_and(self.t >= ta, self.t <= tb ) )
        y = np.zeros( self.N )
        y[j] = self.samples[j]
        
        return signal(t = self.t, samples = y)    
      
class square_pulse(signal):
    
    def __init__(self, t, T1, tcenter = 0.0):
        samples = square(t - tcenter, T1)
        super().__init__( t = t, samples = samples )        

class carrier(signal):
    
    def __init__(self, t, f0, A = 1, phi = 0.0):
        samples = cos_signal(A, f0, t, phi = phi )
        super().__init__( t = t, samples = samples )


class constellation:
    
    def __init__(self, title = None):
       self.bit_map = {}
       self.bits = []
       self.bits_str = []
       self.symbols = []
       self.title = title
              
    def plot(self, figure_no = None, plot_type = 'o'):
    
        if figure_no is None:
            plt.figure()
        else:
            plt.figure(figure_no)
        
        cr = np.real(self.symbols)
        ci = np.imag(self.symbols)
        plt.plot(cr, ci, plot_type)
        plt.xlabel('Real')
        plt.ylabel('Imag')
        
        if self.title is not None:
            plt.title(self.title)
    
    def plot_map( self, figure_no = None, disp_x = 0.0, disp_y = 0.0,
                  rotation = 90, plot_type = 'bo'):
    
        for i, bits in enumerate(self.bits_str):
            symbol = self.symbols[i]
            bits_str = self.bits_str[i]
            plt.plot( np.real(symbol), np.imag(symbol), plot_type )
            plt.text( np.real(symbol) + disp_x, np.imag(symbol) + disp_y, bits_str, 
                      rotation = rotation)
        
        if self.title is not None:
            plt.title(self.title)
            
    def set_symbols( self, symbols ):
        self.symbols = symbols
        
    def set_gray_bits( self, m ):
        g = gray_code( m )
        self.bits = []
        self.bits_str = []
        self.map = {}
        self.m = m
        
        for i, cw in enumerate(g):
            self.bits_str.append(cw)
            self.bits.append( str_to_bitsarray( cw ) )
            self.map[ cw ] = self.symbols[ i ]
            
    def bits_to_symbols( self, bits, return_groups = False ):
        symbols = []
        bitgroups = []
        i = 0
        j = 0

        if not isinstance(bits, str):
            bits = array_to_str(bits)
                        
        while i < len(bits):

            key = bits[ i : i + self.m ]
            bitgroups.append( key )
            symbols.append( self.map[ key ] )
            i += self.m
            j += 1

        if not return_groups:    
            return np.array(symbols)    
        else:
            return np.array(symbols), bitgroups
    
                
class pam_constellation(constellation):
    
    def __init__(self, M, beta = 1, title = None):
        super().__init__(title = title)
        
        self.M = M
        self.m = np.log2(M).astype(int)
        
        symbols = np.zeros( M )
        for i in range( M ):
            symbols [ i ] = 2 * i - M + 1
            
        self.set_symbols( symbols )
        self.set_gray_bits( self.m )              
    
class digital_signal(signal):
    
    def __init__(self, TS = 1e-6, samples_per_symbol = 10, 
                 tinitial = 0, tguard = 0.0, constellation = None):
    
        super().__init__()
        self.TS = TS
        self.samples_per_symbol = samples_per_symbol
        self.tinitial = tinitial
        self.tguard = tguard
        self.constellation =  constellation
        
    def set_constellation(self, constellation):
        self.constellation = constellation
        
    def set_input_bits(self, bits):
        self.input_bits = bits
        
        
    def modulate_from_symbols( self, symbols ):
        
        self.Tmin = self.tinitial - self.tguard
        self.Tmax = self.Tmin + symbols.size * self.TS + 2 * self.tguard
        self.Dt = self.TS / self.samples_per_symbol
        self.t = np.arange(self.Tmin, self.Tmax, self.Dt)
        self.samples = np.zeros( self.t.size )
        self.symbols = symbols
        
        i = np.floor( (self.t - self.tinitial) / self.TS).astype(int)
        j = np.where( np.logical_and(i >= 0, i < symbols.size ) )

        self.samples[j] = symbols[ i[j] ]
        
    def modulate_from_bits( self, bits, constellation = None):
        
        if constellation is not None:
            self.set_constellation(constellation)
        
        self.set_input_bits( bits )
        samples = self.constellation.bits_to_symbols( bits )
        self.modulate_from_symbols( samples )
        
        
        

    
        
        
        

       
       
          
    
            
