# uxarray-asv
[![pages-build-deployment](https://github.com/UXARRAY/uxarray-asv/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/UXARRAY/uxarray-asv/actions/workflows/pages/pages-build-deployment)

Air Speed Velocity (ASV) benchmarking for the UXarray Python Package

## Quickstart

UXarray's benchmarks are stored in the package repository (not in this one), which should first be cloned. 
```
git clone https://github.com/UXARRAY/uxarray.git
```

The benchmarks and configuration files are located in the `benchmarks` directory.
```
cd benchmarks
```
Asv needs to be installed locally in order to run any benchmarks. 
```
pip install asv
```
Step 4
```
asv run --quick
```

## Profiling
```
asv profile
```

To visualuze the results, ...
```
asv profile --gui=snakeviz
```

## Local Development 

By default, asv will pull the changes from the most recent committ from whichever branch is indicated by the `"branches"` variable in the `asv.conf.json` file.

First, uxarray should be installed locally in editable mode.
```
pip install -e .
```


To run benchmarks using the local changes, we can pass through the ``-python=same`` parameter, which will use the current enviroment and not create a new one. 
```
asv run --python=same
```










