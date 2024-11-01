from utils import read_video
from trackers import Tracker

def main():
    video_frames = read_video('input_videos/08fd33_4.mp4')

    # initialize Tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='stubs/track_stubs.pkl')

if __name__ == '__main__':
    main()