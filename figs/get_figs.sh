#!/usr/bin/env bash
HOST='mmuetz@login.rdf.ac.uk'
DIR='um10.7_runs/postproc'
SUITE='u-al000'
URL="$HOST:$DIR/$SUITE/share/data/history"

rsync $URL/suite_results/figs/profile_plot.uv_profile.png .
