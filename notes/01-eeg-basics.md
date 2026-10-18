# Step 1: EEG basics

1. **EEG** is voltage from big groups of neurons, recorded as an array of `(channels, samples)`.
2. **Sampling rate** is samples per second; you can only see frequencies up to half of it (the Nyquist limit).
3. **Brain activity** is a mix of waves at different speeds, grouped into bands: delta, theta, alpha, beta, gamma.
4. **Seizures** look rhythmic, large and spreading. ML either detects them (ictal) or forecasts them (preictal vs interictal).

## Seizure states

| State | Meaning |
| --- | --- |
| Preictal | Window before a seizure |
| Ictal | During the seizure |
| Postictal | Recovery afterwards |
| Interictal | Baseline between seizures |

## Check questions

- 1 hour, 23 channels, 256 Hz → shape `(23, 921600)`. Sampling rate is not an axis; it sets how many samples a second becomes. Windowed into 1 s chunks → `(3600, 23, 256)`.
- 256 Hz can't see 200 Hz: you need 2 samples per cycle, so the ceiling is 128 Hz. A 200 Hz wave would alias to a fake 56 Hz.
- 30-minute-ahead prediction → preictal vs interictal.
