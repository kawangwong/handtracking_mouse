

def vidset(video, cv2):
  video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
  width = 1920
  height = 1080
  video.set(cv2.CAP_PROP_FRAME_WIDTH, width)
  video.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
  video.set(cv2.CAP_PROP_FPS, 30)

