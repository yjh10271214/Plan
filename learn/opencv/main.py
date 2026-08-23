import argparse
import preprocess
import os
import logging
import numpy as np
import cv2
from preprocess import preprocess 

def parse_args():
    parser = argparse.ArgumentParser(description="Image Preprocess script")
    parser.add_argument("--input", type=str, required=True, help="Input image path")
    parser.add_argument("--size", type=int, default=640, help="Target size, default 640")
    return parser.parse_args()


def main():
    # 配置日志
    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s"
    )
    args = parse_args()
    image_path = args.input
    input_size = (args.size, args.size)

    if not os.path.exists(image_path):
        logging.info(f"input image not exist: {image_path}")
        raise SystemExit(1)

    
    logging.info(f"start process image: {image_path}")
    output = preprocess(image_path, input_size)
    logging.info(f"process successfully output shape: {output.shape}, dtype: {output.dtype}")


if __name__ == "__main__":
    main()