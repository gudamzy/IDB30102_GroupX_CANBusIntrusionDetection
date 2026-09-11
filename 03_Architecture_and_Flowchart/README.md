# 03_Architecture_and_Flowchart

The same figures as Chapter 3 of the proposal. If a figure changes in the proposal, replace the file here in the same commit.

| File | Proposal figure |
|---|---|
| `architecture.jpeg` | Figure 3.1 Proposed Research Architecture |
| `flowchart.jpeg` | Figure 3.2 Proposed Research Flowchart |
| `gantt_chart.png` | Figure 3.3 Proposed Gantt Chart |
| `draw_figures.py` | Script that draws Figures 3.1 and 3.2 (matplotlib) |

## Data flow

1. **Dataset** – can-train-and-test, four vehicles from two manufacturers; each sub-dataset has `train_01`, `test_01` (same vehicle) and `test_02` (different vehicle).
2. **Preprocessing** – load each capture, convert IDs and data bytes, keep per-message labels, compute time since the previous frame with the same ID.
3. **Models** – Random Forest, Decision Tree and linear SVM trained on the same 500,000-frame stratified sample of `train_01`.
4. **Evaluation** – same-vehicle (`test_01`, baseline) and cross-vehicle (`test_02`).
5. **Metrics** – accuracy, precision, recall, F1-score, false-positive rate, F1 retention.
6. **Comparison** – which model keeps its performance best when the vehicle changes.

Code for each stage is in `04_Source_Code/`.
