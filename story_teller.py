import requests
import base64
from gtts import gTTS
import os
from mpyg321.MPyg123Player import MPyg123Player
from mpyg321.consts import PlayerStatus
import threading
import time

FILE_URL = 'https://api.github.com/repos/shun-aky/1001-StoryTeller/contents/story.txt'
STORY_PATH = "Users/shuna/University of Michigan/1001+/StoryTeller/1001-StoryTeller/story.mp3"

class StoryTeller:
    def __init__(self) -> None:
        self.content = ""
        self.player = MPyg123Player()

    def get_story(self) -> None:
        try:
            response = requests.get(FILE_URL)
            if response.status_code == 200:
                content = response.json()["content"]
                content = content.encode("utf-8")
                content = base64.b64decode(content).decode("utf-8")
                self.content = content
                print("Got story successfully!")
            else:
                print("Failed to get the story. Status code: ", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Failed to get the story:", str(e))
        except:
            print("Failed to get the story.")

    def make_mp3(self) -> None:
        print("Start creating story.mp3")
        #tts = gTTS(text=self.content, lang='en', slow=False)
        #tts.save("story.mp3")
        print("Created story.mp3 file!")

    def start_story(self) -> None:
        print("Start playing story.mp3")
        self.player.play_song("story.mp3")
        while self.is_story_running():
            True
        print("Finished playing story.mp3")

    def pause_story(self) -> None:
        self.player.pause()
        print("Story paused")

    def resume_story(self) -> None:
        self.player.resume()
        print("Story resumed")

    def stop_story(self) -> None:
        self.player.stop()
        print("Story stopped")

    def is_story_running(self) -> bool:
        return self.player.status == PlayerStatus.PLAYING

    def __del__(self) -> None:
        #os.system("rm story.mp3")
        print("story.mp3 deleted")

def test():
    st = StoryTeller()
    st.get_story()
    st.make_mp3()
    st.start_story()

if __name__ == '__main__':
    test()
