"""Root package info."""
import logging as __logging
import os

from torchmetrics.__about__ import *  # noqa: F401 F403

_logger = __logging.getLogger("torchmetrics")
_logger.addHandler(__logging.StreamHandler())
_logger.setLevel(__logging.INFO)

_PACKAGE_ROOT = os.path.dirname(__file__)
_PROJECT_ROOT = os.path.dirname(_PACKAGE_ROOT)

from torchmetrics.audio import SI_SDR, SI_SNR, SNR  # noqa: F401 E402
from torchmetrics.average import AverageMeter  # noqa: F401 E402
from torchmetrics.classification import (  # noqa: F401 E402
    AUC,
    AUROC,
    F1,
    ROC,
    Accuracy,
    AveragePrecision,
    BinnedAveragePrecision,
    BinnedPrecisionRecallCurve,
    BinnedRecallAtFixedPrecision,
    CohenKappa,
    ConfusionMatrix,
    FBeta,
    HammingDistance,
    Hinge,
    IoU,
    KLDivergence,
    MatthewsCorrcoef,
    Precision,
    PrecisionRecallCurve,
    Recall,
    Specificity,
    StatScores,
)
from torchmetrics.collections import MetricCollection  # noqa: F401 E402
from torchmetrics.image import FID, IS, KID, PSNR, SSIM  # noqa: F401 E402
from torchmetrics.metric import Metric  # noqa: F401 E402
from torchmetrics.regression import (  # noqa: F401 E402
    CosineSimilarity,
    ExplainedVariance,
    MeanAbsoluteError,
    MeanAbsolutePercentageError,
    MeanSquaredError,
    MeanSquaredLogError,
    PearsonCorrcoef,
    R2Score,
    SpearmanCorrcoef,
    SymmetricMeanAbsolutePercentageError,
)
from torchmetrics.retrieval import (  # noqa: F401 E402
    RetrievalFallOut,
    RetrievalMAP,
    RetrievalMRR,
    RetrievalNormalizedDCG,
    RetrievalPrecision,
    RetrievalRecall,
)
from torchmetrics.wrappers import BootStrapper  # noqa: F401 E402
