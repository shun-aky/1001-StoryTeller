import requests
import base64
from gtts import gTTS
import os

FILE_URL = 'https://api.github.com/repos/shun-aky/1001-StoryTeller/contents/story.txt'

class StoryTeller:
    def __init__(self) -> None:
        self.content = ""

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
        tts = gTTS(text=self.content, lang='en', slow=False)
        tts.save("story.mp3")
        print("Created story.mp3 file!")

    def start_story(self) -> None:
        print("Start playing story.mp3")
        os.system("mpg123 story.mp3")
        print("Finished playing story.mp3")

    def __del__(self) -> None:
        os.system("rm story.mp3")
        print("story.mp3 deleted")

st = StoryTeller()
st.get_story()
st.make_mp3()
st.start_story()
