# AdROD: Public Demo and Research Companion

This repository accompanies the accepted paper **AdROD: HyperNetwork-based
Adversarially Robust Object Detection for Autonomous Driving**. It provides
selected demonstration media, paper-reported configurations, and result
summaries.

> This is **not** the executable AdROD artifact. The AdROD implementation,
> trained checkpoints, patch-generation code, and runnable training/evaluation
> pipeline are not included in this public repository.

## Why the executable implementation is not released

The AdROD technology is subject to patent-related restrictions. This repository
is therefore a public research companion only; it does not grant a license to
the unavailable implementation or to any associated patent rights. See
[`NOTICE`](NOTICE) and [`LICENSE`](LICENSE).

## Contents

- [`demo/`](demo/): selected qualitative images and GIF demonstrations.
- [`configs/paper_hyperparameters.yaml`](configs/paper_hyperparameters.yaml):
  paper-reported YOLOv5/HyperNetwork settings.
- [`configs/evaluation_protocols.yaml`](configs/evaluation_protocols.yaml):
  evaluation protocol descriptions, without evaluation data.
- [`patches/`](patches/): released adversarial-patch images and their original
  configuration metadata. They are research input assets only; no patch
  generation or AdROD evaluation code is included.
- [`evaluation_data/`](evaluation_data/): released evaluation image sequences
  and COCO-derived subsets. See [`DATASET_LICENSES.md`](DATASET_LICENSES.md)
  for provenance, attribution, and privacy information.
- [`results/reported_results.csv`](results/reported_results.csv): selected
  paper-reported ASR values.
- [`scripts/verify_release.py`](scripts/verify_release.py): a dependency-free
  check that this public release contains its required metadata and no model
  weights or executable AdROD implementation.

## Verify this public release

This check validates only the public companion's layout and metadata. It does
not run AdROD, generate patches, or reproduce the paper's experiments.

```bash
python3 scripts/verify_release.py
```

Expected output:

```text
Public AdROD companion release check passed.
```

## Demonstrations

| Vanilla detector | AdROD |
| --- | --- |
| ![Vanilla stop-sign prediction](demo/images/stopsign_yolo.png) | ![AdROD stop-sign prediction](demo/images/stopsign_adrod.png) |

The GIFs in [`demo/videos/`](demo/videos/) illustrate selected examples from
the paper, including the outdoor and laboratory settings. The corresponding
evaluation images are available in [`evaluation_data/`](evaluation_data/), but
cannot be evaluated with this repository because the executable pipeline is
not public.

## Reported configuration and results

The configuration and result files are transcriptions of the settings and
metrics reported in the accepted paper. They are supplied to make the public
claims inspectable; they are not sufficient to reconstruct the unavailable
implementation.

Please cite the accepted AdROD paper when using these materials.

## Public-release boundary

Do not interpret this repository as an offer of source code, model weights,
or permission to implement or deploy AdROD. For distribution terms covering
the material actually present here, see [`LICENSE`](LICENSE) and
[`DATASET_LICENSES.md`](DATASET_LICENSES.md).
