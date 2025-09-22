# SPDX-License-Identifier: Apache-2.0

# Third Party
import torch

# First Party
from lmcache.utils import is_musa

if is_musa():
    torch.cuda.is_available = torch.musa.is_available
    torch.cuda.get_device_properties = torch.musa.get_device_properties
    torch.cuda.current_device = torch.musa.current_device
    torch.cuda.device_count = torch.musa.device_count
    torch.cuda.set_device = torch.musa.set_device
    torch.cuda.device = torch.musa.device
    torch.Tensor.cuda = torch.Tensor.musa
    torch.cuda.synchronize = torch.musa.synchronize
    torch.cuda.Event = torch.musa.Event
    torch.cuda.Stream = torch.musa.Stream
    torch.cuda.current_stream = torch.musa.current_stream
    torch.cuda.set_stream = torch.musa.set_stream
    torch.cuda.default_stream = torch.musa.default_stream
    torch.cuda.empty_cache = torch.musa.empty_cache
