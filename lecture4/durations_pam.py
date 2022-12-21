import numpy as np

samples = 10
ak = np.array([-1, 1, 3, 5])
tinitial = 0
TS = 3
tguard = 6

t0 = tinitial - tguard
Dt = TS/samples
Nguard = np.round( tguard / Dt )
Ntot = 2 * Nguard + samples * ak.size
T = Ntot * Dt