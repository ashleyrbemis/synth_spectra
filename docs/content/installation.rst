.. _installationS:

Installation
========================

Step 1: Create a new environment
--------------------------------

We recommend that users create a new ``conda`` virtual environment:

.. code-block:: bash 

    conda create -n synth_spectra python=3.10

Set up the environment

.. code-block:: bash    

    conda activate synth_spectra
    conda install numpy scipy matplotlib

Step 2: Install
----------------------

``synth_spectra`` can be installed via ``pip`` or from source by cloning the `GitHub <https://github.com/ashleyrbemis/synth_spectra>`_ repo.

To install via ``pip``:

.. code-block:: bash 

    pip install synth_spectra

To install from GitHub:

.. code-block:: bash 

    git clone https://github.com/ashleyrbemis/synth_spectra.git
    cd synth_spectra
    pip install -e .


Step 3: Test installation
-------------------------

.. code-block:: python    

    import synth_spectra
    import matplotlib.pyplot as plt
    spec   = synth_spectra.generate_synthetic_spectrum()
    fig,ax = synth_spectra.plot_spectrum(spec)
    plt.show()

This will generate a sample spectrum and show you a plot.