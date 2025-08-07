# run_generation.py
import matplotlib.pyplot as plt
import config
from spectrum_utils import generate_synthetic_spectrum

def plot_spectrum(spectrum_data):
    """
    A reusable function to plot spectrum data.

    Parameters
    ----------
    spectrum_data : dict 
        Dictionary containing the spectral arrays.

    Returns
    ----------
    matplotlib plot
    """
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(spectrum_data['x'], spectrum_data['y_observed'], label='Observed')
    ax.plot(spectrum_data['x'], spectrum_data['y_true'], label='True', linestyle='--')
    ax.set_title("Synthetic Spectrum")
    ax.set_xlabel("Wavelength / Velocity")
    ax.set_ylabel("Intensity")
    ax.legend()
    ax.grid(True)
    plt.show()

# The "main" execution block
if __name__ == '__main__':
    print("Running Spectrum Generation Script")
    example_components = [{'amplitude': 0.035, 'mean': 1450.0, 'sigma': 25.0}]
    data = generate_synthetic_spectrum(
        x_range=(config.DATA_X_MIN, config.DATA_X_MAX),
        num_channels=config.NUM_CHANNELS,
        components=example_components,
        rms_noise_level=config.RMS_NOISE_MIN
    )
    print("Plotting")
    plot_spectrum(data)