# Step 2: Fourier transform

Any signal is a sum of sine waves. The Fourier transform projects the signal onto
an orthogonal basis of sines: one dot product per frequency. The list of dot
products is the spectrum.

## Predictions (write before running)

- len(t) =
- Peaks at:
- Taller peak and ratio:
- Value at 25 Hz:

## Questions

1. Why is the 25 Hz value near zero? (Answer with orthogonality.)

2. What should `np.dot(alpha, test_10hz)` equal? (Hint: average of sin² over a cycle.)

3. What happens at 10.5 Hz? Is it still orthogonal to the 10 Hz component?

4. If alpha were a cosine, what would the sine-only detector report at 10 Hz? What's missing?

## What actually happened

## What I learned
