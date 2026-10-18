"""
Exercise 1: Make a fake brain

Build a fake EEG signal from two pure sine waves, then plot it.

Formula for a sine wave:  A * sin(2 * pi * f * t)
  A = amplitude, f = frequency in Hz, t = time in seconds

Before you run anything, write your prediction for len(t) in notes/02-fourier.md.
"""

import numpy as np
import matplotlib.pyplot as plt

FS = 256          # sampling rate in Hz
DURATION = 2      # seconds

# TODO 1: time array, 2 seconds at 256 Hz (hint: np.arange with step 1/FS)
t = None

# TODO 2: 10 Hz alpha wave, amplitude 1
alpha = None

# TODO 3: 2 Hz delta wave, amplitude 3
delta = None

# TODO 4: add them together
signal = None

# TODO 5: plot alpha, delta and signal on three stacked subplots
#         label the axes (time in s, amplitude) and give each a title


if __name__ == "__main__":
    print("len(t) =", None if t is None else len(t))
