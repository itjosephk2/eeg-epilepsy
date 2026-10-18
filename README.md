# EEG Epilepsy Lab

Learning signal processing and machine learning from first principles, pointed at one problem: detecting and forecasting epileptic seizures from EEG.

Everything here is written by hand first, then checked against library implementations.

## Why

I have epilepsy. I don't want to only be a patient; I want to contribute to the research. This repo is the start of that.

## Roadmap

1. **Signal basics:** EEG, channels, sampling rate, Nyquist, frequency bands
2. **Fourier transform:** built from dot products, then checked against `np.fft`
3. **Real EEG:** load CHB-MIT recordings, plot them, compute spectra
4. **Features:** band power per channel and window
5. **Seizure detection:** classify ictal vs non-ictal windows
6. **Seizure forecasting:** preictal vs interictal (the hard, open problem)
7. **From scratch in C:** reimplement the pipeline with no libraries

## Structure

```
exercises/   one notebook per step (my code)
notes/       predictions, answers, and what I learned
data/        datasets (not committed; see data/README.md)
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Log

| Date | Step | What I did |
| --- | --- | --- |
| 2026-10-18 | 1 | EEG basics: channels, sampling, Nyquist, bands, seizure states |
