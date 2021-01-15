import matplotlib.pyplot as plt
import commlib as cl

iterations = 1000
sze = 1000

s = cl.binary_sequence_simulation(sze = sze, max_iterations = iterations, p1 = 0.7)
s.execute()
plt.close('all')
s.make_histogram(key = lambda x: x['ones'])
s.plot_histogram(normalize_by = sze)
plt.title('Sequenct title: %d' %sze)