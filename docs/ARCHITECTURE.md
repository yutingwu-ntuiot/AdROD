# AdROD Architecture Specification

This document is a non-executable summary of the architecture described in the
accepted AdROD paper. It is provided for research understanding only. It does
not include source code, model classes, checkpoint layouts, parameter-generation
logic, or an inference API.

<p align="center">
  <img width="78%" alt="AdROD HyperNetwork architecture" src="../demo/images/hypernetwork.png" />
</p>

## Components

| Component | Public specification |
| --- | --- |
| Base detector | YOLOv5s pretrained on COCO. |
| Diverse ensemble | A low-rank HyperNetwork produces runtime detector adaptations. |
| Low-rank rank | `r = 4`. |
| Functional diversity | Each ensemble member is paired with a distinct input transformation. |
| Input resolution | 640 × 640 pixels. |
| Adapted YOLOv5 layer indices | `[0, 1, 3, 5, 7, 10, 14, 18, 21]`. |
| Training ensemble size | 3. |
| Diversity coefficient | `beta = 1.0`. |

The paper-reported training settings are also recorded in
[`../configs/paper_hyperparameters.yaml`](../configs/paper_hyperparameters.yaml).

## Serving modes

### AdROD-I: uncertainty-based recovery

AdROD-I evaluates candidate detections using the diversity-induced variation
across the detector ensemble. This variation distinguishes attack-related
suppression from benign ensemble disagreement and supports recovery of the
target detection.

### AdROD-II: on-demand recovery

AdROD-II monitors tracked detections over a consecutive image sequence. An
abrupt disappearance of the target acts as an anomaly signal that activates the
ensemble defense; the system returns to the base detector after recovery.

## Scope of this specification

The published configuration files, patch assets, and evaluation images in this
repository are inspection materials. They cannot instantiate, train, evaluate,
or deploy AdROD. The executable implementation and trained checkpoints are not
released in this repository; see [`../NOTICE`](../NOTICE).
