import numpy as np

mp = np.genfromtxt('atmos.mass_flux_plot.mf_linregress.csv', delimiter=',', dtype=object)
headers = mp[0]
data = mp[1:]

for expt in ['S0', 'S1', 'S2', 'S3', 'S4']:
    m, c, rval, pval, stderr = [float(v) for v in data[(data[:, 0] == '1') & (data[:, 1] == expt)][0][2:]]
    x = -c/m
    print('expt {}, x-intercept = {}, r^2 = {}'.format(expt, x, rval**2))
