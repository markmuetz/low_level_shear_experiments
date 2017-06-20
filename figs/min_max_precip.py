import numpy as np

mp = np.genfromtxt('atmos.precip_plot.max_precip.csv', delimiter=',', dtype=object)[1:]

for expt in ['S0', 'S1', 'S2', 'S3', 'S4']:
    min_max = mp[mp[:, 1] == expt][:, 2].astype(float).min(), mp[mp[:, 1] == expt][:, 2].astype(float).max()
    print('{} min/max [mm/hr]: {}, {}'.format(expt, *min_max))
