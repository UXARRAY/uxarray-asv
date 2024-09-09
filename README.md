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

An example of the output (on a single benchmark file) is shown below. 
```
· Creating environments
· Discovering benchmarks
· Running 4 total benchmarks (1 commits * 1 environments * 4 benchmarks)
[ 0.00%] · For uxarray commit 5410c4f0 <main>:
[ 0.00%] ·· Benchmarking virtualenv-py3.11-netcdf4-pip+pyfma-setuptools_scm-xarray
[12.50%] ··· quad_hexagon.QuadHexagon.peakmem_open_dataset                                                                                                               278M
[25.00%] ··· quad_hexagon.QuadHexagon.peakmem_open_grid                                                                                                                  275M
[37.50%] ··· quad_hexagon.QuadHexagon.time_open_dataset                                                                                                              29.8±0ms
[50.00%] ··· quad_hexagon.QuadHexagon.time_open_grid                                                                                                                 20.0±0ms
```

## Profiling
```
asv profile benchmark_file.BenchmarkClass.benchmark_method
```

For parameterized benchmarks, you can profile a single parameter using the following:

```
todo
```

To visualuze the results, ...
```
asv profile benchmark_file.BenchmarkClass.benchmark_method --gui=snakeviz
```

![image](https://github.com/user-attachments/assets/c0bfa596-7d86-413d-bf83-077f6e9d29ec)


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

## Submitting Benchmark Results

Coming soon! 














