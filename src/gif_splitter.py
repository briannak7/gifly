import os
from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


def get_gif_images(gif_path, save_gif_imgs=False):
    '''
    Splits a gif into its frames and returns a list of pillow image objects.

    Parameters:
    -----------
        gif_path : str, path to the gif
        save (bool) : if True, the frames are saved as pngs

    Returns:
    --------
        images : list of pillow image objects
    '''

    gif = Image.open(gif_path)

    images = []
    for frame in range(gif.n_frames):

        # Extract each frame from the GIF
        gif.seek(frame)
        # Save the frame as a PNG file (temporary step)
        gif.save('frame{:02d}.png'.format(frame))
        # Open and append the PNG frame to the list
        images.append(Image.open('frame{:02d}.png'.format(frame)))

        # delete the created images
        if not save_gif_imgs:
            os.remove('frame{:02d}.png'.format(frame))

    return images


if __name__ == "__main__":

    gif = 'test.gif'

    images = get_gif_images(gif)
    print(images)
