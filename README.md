# Image Blending

This project blends two images side by side using OpenCV and a Laplacian pyramid. The image with the larger pixel area is used as the main image, and the other image is resized to match it.

## Requirements

- Python
- OpenCV (`opencv-python`)
- NumPy

Install the libraries with:

```bash
pip install opencv-python numpy
```

## Run

Place `image1.jpg` and `image2.jpg` in the project directory, then run:

```bash
python script.py
```

The script displays the source images, the resized image, the blended result, and a direct half-and-half join. It saves the results as `blended_image.jpg` and `real_image.jpg`. Press any key while an OpenCV window is focused to close the windows.
