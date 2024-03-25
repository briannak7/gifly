from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


def read_images(images=[]):
    '''
    Reads in images as pillow image object.
    '''

    for i, image in enumerate(images):
        im = Image.open(image)

        # TODO: test if this works with a non-PNG image
        if image.format == "PNG":
            im = im.convert("RGB")

        images[i] = im

    return images


def img_resize(images=[]):
    '''
    Resizes images to 200x200.
    '''

    for i, image in enumerate(images):
        images[i] = image.resize((200, 200))

    return images


def img_to_png():
    pass


def create_gif(images=[]):
    '''
    Takes a list of images and returns a gif.

    Parameters:
    -----------
        images: list of image file paths

    Returns:
    --------
        gif : gif of the images
    '''
    # TODO: add paramerter 'duration' to change the speed of the gif

    # read in images with PIL
    images = read_images(images)

    # resize images
    images = img_resize(images)

    gif = images[0].save('test.gif', save_all=True,
                         append_images=images[1:], duration=300, loop=0)

    return gif


if __name__ == "__main__":

    first = 'testing/images/first.png'
    second = 'testing/images/second.png'

    images = [first, second]

    create_gif(images)
