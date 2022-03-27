# imports
import pytube
import pytube.exceptions
import concurrent.futures
import os

# constants
SAVE_PATH = "C://Users//Ilya//Downloads"


# function block
def download_video(video_url: str) -> str:
    """
    This function downloads one video using pytube library
    :param video_url: url of the video that you want to download
    :return: response, depending on the result of the execution
    """
    # create a YouTube object
    yt = pytube.YouTube(video_url)

    # try to download the video and catch all exceptions
    try:
        yt = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

        if not os.path.exists(SAVE_PATH):
            os.makedirs(SAVE_PATH)

        yt.download(SAVE_PATH)
    except pytube.exceptions.VideoUnavailable:
        return f"The {yt.title} video is unavailable."
    except pytube.exceptions.RegexMatchError:
        return f"Regex Error occurred while parsing the URL: {yt.watch_url}"
    except pytube.exceptions.ExtractError:
        return "Extraction Error occurred while executing."

    return "Video Downloaded Successfully!"


def main():
    # multithreading
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # get the links for the videos
        with open("links.list", "r", encoding="utf-8") as file:
            data = [link[:-1] for link in file.readlines()]

        # download the videos with executor.map() function
        results = executor.map(download_video, data)

        for result in results:
            print(result)
