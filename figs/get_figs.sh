#!/usr/bin/env bash
HOST='mmuetz@login.rdf.ac.uk'
DIR='um10.7_runs/postproc'
SUITE='u-al000'
DATAM="$HOST:$DIR/$SUITE/share/data/history"
DATAW="$HOST:$DIR/$SUITE/work/20000101T0000Z"

rsync -v $DATAM/suite_results/figs/atmos.profile_plot.uv_profile.png .
# rsync -v $DATAM/suite_results/figs/atmos.mass_flux_plot.z1_combined.png .
# rsync -v $DATAM/suite_results/figs/atmos.mass_flux_plot.z1_mf_weighted_comb.png .
# rsync -v $DATAM/suite_results/figs/atmos.mass_flux_spatial_scales_plot.z1_n1_combined.png .
# rsync -v $DATAM/suite_results/figs/atmos.mass_flux_spatial_scales_plot.S0.z1.all_n.hist.png .
rsync -v $DATAM/suite_results/figs/atmos.mass_flux_plot.z1_both.png .
rsync -v $DATAM/suite_results/figs/atmos.mass_flux_spatial_scales_plot.both_z1.png .
rsync -v $DATAM/suite_results/figs/atmos.profile_plot.thermodynamic_profile.png .
rsync -v $DATAM/suite_results/figs/atmos.profile_plot.mf_profile.png .
rsync -v $DATAM/suite_results/figs/atmos.precip_plot.time_index1865.png .

rsync -Rav "$DATAW/./S?_atmos/figs" .
