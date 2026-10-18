"""
Exercise 2: Build your own frequency detector

Rules: np.sin and np.dot only. No np.fft.

Idea: sine waves at different whole-number frequencies are orthogonal over
whole cycles. Dot the signal against a test sine at each frequency; only the
matching frequencies should survive.

Write your answers to the four questions in notes/02-fourier.md BEFORE running.
"""

import numpy as np
import matplotlib.pyplot as plt

# TODO 1: rebuild t and signal exactly as in ex01
#         (or import them: from ex01_fake_brain import t, signal)

# TODO 2: frequencies to test, 0 to 40 Hz in steps of 1
freqs = None

# TODO 3: for each frequency, build a test sine on t and dot it with signal
scores = []

# TODO 4: plot frequency (x) against dot product (y)

# TODO 5 (question 3): try a test frequency of 10.5 Hz. What do you get, and why?

# TODO 6 (question 4): replace the alpha sine with np.cos(...) and rerun.
#         What does the detector say at 10 Hz? What is it missing?
