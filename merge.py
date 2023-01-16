import cv2
resim = cv2.LoadImage('1.jpg')
capture = cv2.CaptureFromFile('vid.mp4')
while(1):
    frame = cv2.QueryFrame(capture)
    cv2.SetImageROI(frame,(100,100,resim.width,resim.height))
    cv2.Add(frame,resim,frame)
    cv2.ResetImageROI(frame)
    cv2.ShowImage('frame',frame)
    if cv2.WaitKey(33)==27:
        break