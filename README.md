# Simple-RTSP
This a very simple script to run a RTSP streamer and RTSP subscriber and stream videos using RTSP.

# How to run streamer and subscriber
1) Clone this repository using `git clone https://github.com/BhavyaShah1234/Simple-RTSP && cd Simple-RTSP`.
2) Download the latest `mediamtx` server from `Releases`---->`Assets` of [https://github.com/bluenviron/mediamtx](this) repository corresponding to your operating system.
3) Unzip the downloaded `.zip` or `.tar` file and run `./mediamtx`.
4) Edit IP address of the streamer machine in `rtsp.py`.
5) Run `python3 rtsp.py` to run streamer/publisher and stream the video.
6) To view the video and verify the stream run `ffplay -rtsp_transport tcp rtsp://<streamer_ip_address_that_you_put_in_rtsp.py>:8554/dummy`

# Note: Streamer and Subscriber should be in the same network.
