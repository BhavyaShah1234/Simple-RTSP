import cv2 as cv
import subprocess as s

video_path = 'video4.mp4'
camera = cv.VideoCapture(video_path)
stream_id = 'dummy'
ip_address = '<YOUR IP ADDRESS>'

rtsp_url = f'rtsp://{ip_address}:8554/{stream_id}'
width = 640
height = 640
fps = 30
command = [
    'ffmpeg',
    '-re',
    '-f', 'rawvideo',
    '-pix_fmt', 'bgr24',
    '-s', f'{width}x{height}', # Adjust resolution as needed
    '-r', f'{fps}',
    '-i', '-',
    '-f', 'rtsp',
    '-rtsp_transport', 'tcp',
    '-c:v', 'libx264',
    '-preset', 'ultrafast',
    '-tune', 'zerolatency',
    '-q', '5',
    '-an',
    '-x264-params', 'keyint=30:scenecut=0',
    '-g', '30',
    rtsp_url
]
ffmpeg_process = s.Popen(command, stdin=s.PIPE)

while True:
    ret, frame = camera.read()
    if not ret:
        camera = cv.VideoCapture(video_path)
        continue
    frame = cv.resize(frame, (width, height))
    try:
        ffmpeg_process.stdin.write(frame.tobytes())
        ffmpeg_process.stdin.flush()
    except Exception as e:
        print(f'ERROR: {e}')
