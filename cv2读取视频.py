#! /usr/bin/env python
# -*- coding: utf-8 -*-


def read_video(video_path):
    import cv2
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
            
if __name__ == '__main__':
    video_path=''
    read_video(video_path)
