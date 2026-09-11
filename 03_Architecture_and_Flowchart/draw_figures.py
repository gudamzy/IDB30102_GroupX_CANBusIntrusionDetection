import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
plt.rcParams["font.family"] = "Liberation Sans"
DARK, LIGHT, CELL, GREY, INK = "#0B4DA2", "#39B3F2", "#EEF2EC", "#CDD5DD", "#111111"

def rbox(ax, x, y, w, h, fc, r=0.25, ec="none"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec, lw=0))

def arrow(ax, x, y1, y2):
    ax.add_patch(FancyArrowPatch((x, y1), (x, y2), arrowstyle="-|>", mutation_scale=16, lw=1.6, color="black"))

# ---------------- Figure 3.1 architecture ----------------
W, H = 11.31, 16.0
fig = plt.figure(figsize=(W / 1.4, H / 1.4))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

def layer(y, h, fc, title, sub=None, cells=(), cell_h=1.05, cell_fs=12, x0=0.45, w=10.4):
    rbox(ax, x0, y, w, h, fc, r=0.45)
    ty = y + h - 0.45
    ax.text(W / 2, ty, title, ha="center", va="center", color="white", fontsize=16, fontweight="bold")
    if sub:
        ax.text(W / 2, ty - 0.55, sub, ha="center", va="center", color="white", fontsize=13, fontweight="bold", linespacing=1.3)
    n = len(cells)
    if n:
        gap = 0.25; cw = (w - 0.6 - gap * (n - 1)) / n
        for i, c in enumerate(cells):
            cx = x0 + 0.3 + i * (cw + gap)
            rbox(ax, cx, y + 0.3, cw, cell_h, CELL, r=0.05)
            ax.text(cx + cw / 2, y + 0.3 + cell_h / 2, c, ha="center", va="center", fontsize=cell_fs, color=INK, linespacing=1.25)

layer(12.9, 2.95, DARK, "Multi-Vehicle CAN Dataset (can-train-and-test)", "4 vehicles (2 manufacturers): normal and attack CAN traffic",
      ["Vehicle A\n2011 Chevrolet\nImpala", "Vehicle B\n2011 Chevrolet\nTraverse", "Vehicle C\n2016 Chevrolet\nSilverado", "Vehicle D\n2017 Subaru\nForester"], cell_h=1.15, cell_fs=11)
arrow(ax, W / 2, 12.9, 12.55)
layer(10.35, 2.2, LIGHT, "Data Preparation and Preprocessing", None,
      ["Data cleaning", "Feature\nextraction", "Label\npreparation", "Scaling where\nrequired"], cell_h=1.1)
arrow(ax, W / 2, 10.35, 9.9)
layer(7.9, 2.0, DARK, "Selected Machine Learning Models", None, ["Random Forest", "Decision Tree", "Support Vector\nMachine"], cell_h=1.05, cell_fs=13)
arrow(ax, W / 2, 7.9, 7.45)
rbox(ax, 0.45, 5.2, 10.4, 2.25, LIGHT, r=0.45)
ax.text(W / 2, 7.0, "Evaluation Settings", ha="center", va="center", color="white", fontsize=16, fontweight="bold")
for i, (t, s) in enumerate([("Same-Vehicle Evaluation (Baseline)", "train_01 → test_01\n(same vehicle)"),
                             ("Cross-Vehicle Evaluation", "train_01 → test_02\n(different vehicle)")]):
    cx = 0.75 + i * 5.05
    rbox(ax, cx, 5.4, 4.75, 1.3, CELL, r=0.05)
    ax.text(cx + 2.375, 6.42, t, ha="center", va="center", fontsize=12.5, fontweight="bold", color=INK)
    ax.text(cx + 2.375, 5.85, s, ha="center", va="center", fontsize=11.5, color=INK, linespacing=1.25)
arrow(ax, W / 2, 5.2, 4.7)
layer(2.75, 1.95, DARK, "Performance Metrics", None, ["Accuracy", "Precision", "Recall", "F1-score", "False-positive\nrate"], cell_h=0.95, cell_fs=12)
arrow(ax, W / 2, 2.75, 2.3)
rbox(ax, 0.9, 0.35, 9.5, 1.95, LIGHT, r=0.45)
ax.text(W / 2, 1.85, "Performance Comparison and Generalisation Analysis", ha="center", va="center", color="white", fontsize=15, fontweight="bold")
ax.text(W / 2, 1.05, "Compare Random Forest, Decision Tree and Support Vector Machine,\nand analyse the performance drop from baseline to cross-vehicle testing",
        ha="center", va="center", color=INK, fontsize=12, linespacing=1.3)
fig.savefig("architecture_fixed.jpeg", dpi=220, pil_kwargs={"quality": 93})
plt.close(fig)

# ---------------- Figure 3.2 flowchart ----------------
steps = ["Obtain multi-vehicle CAN dataset\n(can-train-and-test)", "Review dataset and vehicle information", "Preprocess CAN traffic",
         "Extract features and prepare labels", "Select training and test subsets\n(train_01, test_01, test_02)",
         "Train selected ML models (Random Forest,\nDecision Tree and Support Vector Machine)",
         "Conduct same-vehicle evaluation\n(train_01 → test_01)", "Record baseline result",
         "Conduct cross-vehicle evaluation\n(train_01 → test_02)",
         "Calculate performance metrics (Accuracy, Precision,\nRecall, F1-score, False-Positive Rate)",
         "Compare model results", "Analyse cross-vehicle performance"]
fig = plt.figure(figsize=(W / 1.4, H / 1.4))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
top, bw, x0 = 15.5, 6.2, (W - 6.2) / 2
def pill(y, text):
    rbox(ax, (W - 3.8) / 2, y, 3.8, 0.8, DARK, r=0.4)
    ax.text(W / 2, y + 0.4, text, ha="center", va="center", color="white", fontsize=15, fontweight="bold")
pill(top - 0.8, "Start")
y = top - 0.8
gap, bh = 0.26, 0.66
for s in steps:
    h = bh + (0.28 if "\n" in s else 0)
    arrow(ax, W / 2, y, y - gap)
    y = y - gap - h
    rbox(ax, x0, y, bw, h, GREY, r=0.02)
    ax.text(W / 2, y + h / 2, s, ha="center", va="center", fontsize=12.5, color=INK, linespacing=1.25)
arrow(ax, W / 2, y, y - gap)
pill(y - gap - 0.8, "End")
fig.savefig("flowchart_fixed.jpeg", dpi=220, pil_kwargs={"quality": 93})
from PIL import Image
for f in ["architecture_fixed.jpeg", "flowchart_fixed.jpeg"]:
    im = Image.open(f); print(f, im.size)
