# Evaluation Data: Provenance, Attribution, and Privacy

## Included data

| Data | Location | Provenance and release basis |
| --- | --- | --- |
| COCO stop-sign subset | `evaluation_data/nonconsecutive_data/coco_stopsign` | 256 images drawn from COCO 2017 validation data. COCO is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); retain COCO attribution when redistributing these images. |
| COCO person subset | `evaluation_data/nonconsecutive_data/coco_person` | 426 images drawn from COCO 2017 validation data, under CC BY 4.0. |
| Outdoor road sequences | `evaluation_data/consecutive_data/road_clean`, `road_noisy` | Author-collected on a restricted private road for the physical stop-sign experiments in the accepted paper. |
| Indoor laboratory sequence | `evaluation_data/consecutive_data/lab_noisy` | Author-collected controlled indoor experiment data. |

## Release boundary

The author-collected road and laboratory sequences are released as research
assets only. The authors state that they hold the required release rights for
these sequences. They exclude third-party vehicle-challenge recordings and
OpenCDA assets mentioned elsewhere in the paper.

No executable detector, patch-generation code, model weights, annotations, or
evaluation pipeline is included in this repository. The public repository is
therefore not a runnable benchmark or a reproduction package.

## Privacy

Before publishing this repository, perform a final check that the author-
collected sequences contain no identifiable persons, vehicle registration
numbers, GPS metadata, or other personal data. Redact or remove any affected
frame before publication. If an issue is identified after publication, please
contact the authors through the paper's listed correspondence channel.
