import cv2
#创建窗口
cv2.namedWindow('windows',cv2.WINDOW_NORMAL)
#修改窗口大小
cv2.resizeWindow('windows',800,600)
#展示名字为window的窗口
cv2.imshow('windows',0)
cv2.waitKey(0)