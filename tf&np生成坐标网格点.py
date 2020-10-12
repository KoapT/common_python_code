#! /usr/bin/env python
# -*- coding: utf-8 -*-


# 3. 根据图的h,w 产生坐标点
def gen_coord(h, w):
    import tensorflow as tf
    tf.enable_eager_execution()
    x = tf.constant(list(range(w)), dtype=tf.float32)[:, tf.newaxis]
    y = tf.constant(list(range(h)), dtype=tf.float32)[:, tf.newaxis]
    tile_x = tf.tile(x, [tf.shape(y)[0], 1])
    tile_y = tf.tile(y, [1, tf.shape(x)[0]])
    # grid_x = tf.reshape(tile_x, [-1, tf.shape(x)[0]])   # 类似np.meshgrid的网格
    # grid_y = tile_y
    tile_y = tf.reshape(tile_y, [-1, 1])
    coord = tf.concat([tile_x, tile_y], axis=1)  # 从左到右，从上到下 每个坐标点的坐标
    return coord#, grid_x, grid_y

# 参考np.meshgrid
def meshgrid(h, w):
    import numpy as np
    x1 = np.arange(w)
    x2 = np.arange(h)
    x, y = np.meshgrid(x1, x2)
    # print(x)
    # print(y)
    xy_coord = np.concatenate([x[:,:,None],y[:,:,None]],axis=-1)
    print(xy_coord)


if __name__ == '__main__':
    h=5
    w=6
    print(gen_coord(h,w))
    meshgrid(h,w)

