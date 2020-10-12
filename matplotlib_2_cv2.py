import matplotlib.pyplot as plt
import numpy as np
import cv2
 
 
def fig2data(fig):
    """
    fig = plt.figure()
    image = fig2data(fig)
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    import PIL.Image as Image
    # draw the renderer
    fig.canvas.draw()
 
    # Get the RGBA buffer from the figure
    w, h = fig.canvas.get_width_height()
    buf = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint8)
    buf.shape = (w, h, 4)
 
    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = np.roll(buf, 3, axis=2)
    image = Image.frombytes("RGBA", (w, h), buf.tostring())
    image = np.asarray(image)
    print(image.shape)
    return image
 
 
if __name__ == "__main__":
    # Generate a figure with matplotlib</font>
    figure = plt.figure()
    plot = figure.add_subplot(111)
 
    # draw a cardinal sine plot
    x = np.arange(1, 100, 0.1)
    y = np.sin(x) / x
    plot.plot(x, y)
    # plt.show()
    ##
    image = fig2data(figure)
    cv2.imshow("image", image)
    cv2.waitKey()
    cv2.destroyAllWindows()