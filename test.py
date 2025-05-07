import torch
import os

if __name__ == "__main__":
    # Check if CUDA is available
    if torch.cuda.is_available():
        print("CUDA is available")
    else:
        print("CUDA is not available")