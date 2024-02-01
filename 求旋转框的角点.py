import numpy as np

def box2corners_2d(box):
    # box -> corners
    # x, y, theta, l, w = box
    x, y, l, w, theta = box
    sin_s = np.sin(theta)
    cos_s = np.cos(theta)
    tmp = np.array([[-l / 2, -w / 2],
                    [l / 2, -w / 2],
                    [l / 2, w / 2],
                    [-l / 2, w / 2]]).T
    Rmat = np.array([[cos_s, -sin_s], [sin_s, cos_s]])
    corners = np.array([[x], [y]]) + np.dot(Rmat, tmp)
    corners = corners.T
    return corners