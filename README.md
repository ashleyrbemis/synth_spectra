# Synthetic Spectra Generator

This is a simple tool for generating synthetic astronomical spectra. You can use it to create test data with multiple Gaussian components and control the amount of noise.

### How It's Organized

* `config.py`: Contains all the settings you might want to tweak, like the spectral range and noise levels.
* `spectrum_utils.py`: The core library with functions that do the actual work of building a spectrum.
* `run_generation.py`: The main script you execute to see an example plot.

### Getting Started

1.  **Clone the repo:**
    ```bash
    git clone https://github.com/ashleyrbemis/synth_spectra.git
    cd synth_spectra
    ```

2.  **Set up the environment:**
    This project uses Conda. Make sure your `codeastro` environment is active and has the necessary packages.
    ```bash
    conda activate codeastro
    conda install numpy scipy matplotlib
    ```

3.  **Run the script:**
    ```bash
    python run_generation.py
    ```
    This will generate a sample spectrum and show you a plot.