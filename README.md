# ML for Drift Chamber Signal Processing

## 0. Setup 

### Navigating s3df 

Request [ATLAS membership](https://atlas.slac.stanford.edu/user-computer-account/request-atlas-membership-s3df) on S3DF. 

Navigate to your disk areas with good quota to clone the code; for ex. `/sdf/data/atlas/u/<username>` has 200 GB.

Read more [HERE](https://usatlas.readthedocs.io/projects/af-docs/en/latest/sshlogin/ssh2SLAC/)

### Conda env

First source the central installation: 
`source /sdf/group/atlas/sw/conda/etc/profile.d/conda.sh` 

Then put the following lines in your `~/.condarc`: 
```
unsatisfiable_hints: true
envs_dirs:
 - /sdf/data/atlas/u/<username>/conda/envs
pkgs_dirs:
 - /sdf/data/atlas/u/<username>/conda/pkgs
```


And these lines in your `.bashrc`:
```
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/sdf/group/atlas/sw/conda/' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
# export PATH="/sdf/group/atlas/sw/conda/bin:$PATH"  # commented out by conda initialize
fi
export TMPDIR="${SCRATCH}"
unset __conda_setup
```

Start a fresh shell, and now you're ready to create a conda environment for all local packages: 

```
conda create -n myenv torch tqdm tensorboard scikit-learn numpy matplotlib ot torchmetrics
conda init
conda activate myenv
conda install -c conda-forge root
conda install -c conda-forge pot
```

On each subsequent login, you only need to do `source /sdf/group/atlas/sw/conda/etc/profile.d/conda.sh` and `conda activate myenv`.

## 1. Peak Finding for Drift Chamber Cluster Counting
* "Peak finding algorithm for cluster counting with domain adaptation", [2402.16270](https://arxiv.org/abs/2402.16270) (11 Apr 2024)

### 1a. Input

Download `source_test.root` from [CERNBox](https://cernbox.cern.ch/s/PP68mQPxbdvxuou) and put in local directory 

### 1b. Evaluate 

Run `python predict.py` (it will take a while) and inspect the outputs in the `results/` directory. You can use imgcat to view pngs in the terminal (`pip install imgcat`).
TODO JULIA: 
- [ ] Reduce # eval events by default

## 2. Cluster Counting Algorithm for the CEPC Drift Chamber using LSTM and DGCNN
* "Cluster Counting Algorithm for the CEPC Drift Chamber using LSTM and DGCNN", [2402.16493](https://arxiv.org/pdf/2402.16493) (13 May 2025)
* Jupyter on s3df: [SLACjupyter](https://usatlas.readthedocs.io/projects/af-docs/en/latest/jupyter/SLACjupyter/)

### 2a. Run

`cd alt_CEPC/`
Test `processor.ipynb`  and `clustercount.ipynb`.

 
## 3. Synthesize (hls4ml) 
* hls4ml [README](https://github.com/fastmachinelearning/hls4ml)

### FastX (Be comfortable with [[Vim Commands]]) runs on [[RDSRV]]

From Alex:
1. go to https://fastx.slac.stanford.edu:3300/
2. open desktop session
3. enter password
4. open terminal
	(Or ssh <username>@fastx3)
1. ssh rdsrv409
2. enter password
3. cd into ML_FPGAonPixel/HLS/setup
4. conda activate hls4ml-env
5. source setup.sh
6. vitis\_hls 
	^ To enter AMD Vitis HLS program



## References 
