from gtts import gTTS
import os

FILE_PATH = "story.txt"



class StoryTeller:
    def __init__(self) -> None:
        self.content = ""

    def get_story(self) -> None:
        # Open the file in read mode
        try:
            with open(file_path, "r") as file:
                # Read the contents of the file
                self.content = file.read()

            if self.content != "":
                print("Got story successfully!")
            else:
                print("Opened the file successfully but it's empty.")

            # convert text to mp3 file
        except:
            print("Failed to get the story.")

    def make_mp3(self) -> None:
        myobj = gTTS(text = self.content, lang = "en", slow = False)
        myobj.save("story.mp3")

    def start_story(self):

