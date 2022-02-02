from colorsys import rgb_to_hsv
import time


def id_generator():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    return timestr


def lightness(pixel):
    # For backwards compatibility with python2
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[2] / 255.0


def hue(pixel):
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[0] / 255.0


def saturation(pixel):
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[1] / 255.0


def crop_to(image_to_crop, reference_image):
    """
    Crops image to the size of a reference image. This function assumes that the relevant image is located in the center
    and you want to crop away equal sizes on both the left and right as well on both the top and bottom.
    :param image_to_crop
    :param reference_image
    :return: image cropped to the size of the reference image
    """
    reference_size = reference_image.size
    current_size = image_to_crop.size
    dx = current_size[0] - reference_size[0]
    dy = current_size[1] - reference_size[1]
    left = dx / 2
    upper = dy / 2
    right = dx / 2 + reference_size[0]
    lower = dy / 2 + reference_size[1]
    return image_to_crop.crop(
        box=(
            int(left),
            int(upper),
            int(right),
            int(lower)))
