from PIL import Image
from PIL import ImageFile
import gif_splitter
import gif_creator

# ImageFile.LOAD_TRUNCATED_IMAGES = True


def add_frames(gif, new_images):
    '''
    Adds frames to images.

    Parameters:
    -----------
        images : initial gif's list of pillow image objects
        frames : new images to add

    Returns:
    --------
        images : list of pillow image objects
    '''

    # split the gif into its frames as PIL images
    images = gif_splitter.get_gif_images(gif)

    # add the new images to the list of images
    for image in new_images:
        images.append(image)

    gif = gif_creator.create_gif(images)
    return gif


if __name__ == "__main__":

    new_img = 'testing/images/third.png'

    gif = 'test.gif'

    images = [new_img, new_img]

    add_frames(gif, images)
