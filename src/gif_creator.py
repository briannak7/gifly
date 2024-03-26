from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


def read_images(images):
    '''
    Reads in images as pillow image object.
    '''

    for i, image in enumerate(images):

        if not isinstance(image, Image.Image):
            print('not')
            im = Image.open(image)
            images[i] = im

    return images


def img_resize(images, size):
    '''
    Resizes images to 200x200.
    '''

    for i, image in enumerate(images):
        images[i] = image.resize(size)

    return images


def img_to_png():
    pass


def create_gif(images, name, size=(200, 200), duration=300):
    '''
    Takes a list of images and returns a gif.

    Parameters:
    -----------
        images (list) : list of image file paths
        name (string) : name of the gif to be created
        size (tuple of ints): size of the images in the gif
        duration (int) : duration of each frame in the gif

    Returns:
    --------
        gif : gif of the images
    '''

    # read in images with PIL
    images = read_images(images)

    # resize images
    images = img_resize(images, size)

    gif = images[0].save(f'{name}.gif', save_all=True,
                         append_images=images[1:], duration=duration, loop=0)

    return gif


if __name__ == "__main__":

    first = 'testing/images/first.png'
    second = 'testing/images/second.png'
    img = 'testing/images/third.jpeg'

    images = [first, second, img]

    create_gif(images, 'test')
