import torch
import os

import logging

logger = logging.getLogger(__name__)


def enable_cuda(device=0):
    """This function will set the default device to CUDA if possible. Call before declaring any variables!"""
    if torch.cuda.is_available():
        os.environ["TORCH_DEVICE"] = "cuda:" + str(device)
        logger.info("__pyTorch VERSION:" + str(torch.version))
        logger.info("__CUDNN VERSION:" + str(torch.backends.cudnn.version()))
        logger.info("__Number CUDA Devices:" + str(torch.cuda.device_count()))
        logger.info("Active CUDA Device: GPU" + str(torch.cuda.current_device()))
        logger.info("Setting default tensor type to Float32")
        torch.set_default_tensor_type(torch.cuda.FloatTensor)
    else:
        logger.warn(
            "Error enabling CUDA. cuda.is_available() returned False. CPU will be used."
        )

