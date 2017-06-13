import os
import subprocess as sp

REL_FETCH_CMD_FMT = ("rsync -Rzav {host}:{rel_filenames} .")

HOST='mmuetz@login.rdf.ac.uk'
DIR='um10.7_runs/postproc'
SUITE='u-al000'
DATAM="{}/{}/share/data/history".format(DIR, SUITE)
DATAW="{}/{}/work/20000101T0000Z".format(DIR, SUITE)


# Remember to put a . in where you want the rel dir to start.
DATAM_FILENAMES = [
    'suite_results/figs/./atmos.profile_plot.uv_profile.png',
    'suite_results/figs/./atmos.mass_flux_plot.z1_both.png',
    'suite_results/figs/./atmos.mass_flux_spatial_scales_plot.both_z1.png',
    'suite_results/figs/./atmos.profile_plot.thermodynamic_profile.png',
    'suite_results/figs/./atmos.profile_plot.mf_profile.png',
    'suite_results/figs/./atmos.precip_plot.time_index1865.png',
    'suite_results/figs/./atmos.precip_plot.time_index1870.png',
    'suite_results/figs/./atmos.profile_plot.dz_profile.png',
]

DATAW_FILENAMES = [
    './S?_atmos/figs',
]

if __name__ == '__main__':
    remote_rel_filenames = [os.path.join(DATAM, fn) for fn in DATAM_FILENAMES]
    remote_rel_filenames.extend([os.path.join(DATAW, fn) for fn in DATAW_FILENAMES])
    cmd = REL_FETCH_CMD_FMT.format(rel_filenames=' :'.join(remote_rel_filenames),
                                   host=HOST)
    # print(cmd)
    sp.call(cmd, shell=True)