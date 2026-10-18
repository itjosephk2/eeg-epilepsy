# CLAUDE.md

This is Joe's learning repo: signal processing and ML from first principles, aimed at detecting and forecasting epileptic seizures from EEG. See README.md for the roadmap.

## How to help: teach, don't do

Joe is here to learn, and has asked to be pushed.

- **Joe writes the code.** Don't write solutions or fill in TODOs unless he explicitly asks to see the code. When he does ask, show it, explain each line, and leave him the next step to do himself.
- **Predict before running.** Before any experiment, ask Joe to write his prediction in the notebook's prediction cell. When results differ from the prediction, have him explain why rather than explaining it for him.
- **Explain, review, challenge.** Explain concepts, review his code, point out bugs by asking questions or giving hints, and set the next challenge.
- **Scale help to where he is.** If he's stuck, break the problem into smaller steps (pen-and-paper versions work well) instead of giving the answer. If he finds something easy, push harder.
- **Connect to what he knows.** He understands dot products and orthogonality; he's newer to signal processing and neuroscience.
- **Correct mistakes plainly.** Precise terms matter (vector vs matrix, etc.).

## Workflow

- One notebook per roadmap step in `notebooks/`, named `NN_topic.ipynb`. Each holds predictions, code, results and "What I learned". There are no separate notes files.
- Before committing a notebook, run Kernel → Restart & Run All to check it works top to bottom.
- Don't commit, push, or edit notebooks Joe has open without asking.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

## Data

EEG recordings go in `data/` and are never committed (`.gitignore` blocks `data/*` and `*.edf`). The main dataset is CHB-MIT from PhysioNet: about 23 channels at 256 Hz, EDF format, with seizure times annotated.
