# See 
# atmos.surf_flux_plot.energy_flux.csv 
# ./S?/figs/atmos.936.profile_analysis.energy_loss.txt

# S0
# LHF + SHF
e_in = 150.354531079 + 17.1628587575
e_out = 204.803516563
print('S0 energy diff [W m-2]: {}'.format(e_out - e_in))

# S4
# LHF + SHF
# Yes, SHF is -ve.
e_in = 123.751533819 - 4.08887523913
e_out = 206.078934387
print('S4 energy diff [W m-2]: {}'.format(e_out - e_in))
