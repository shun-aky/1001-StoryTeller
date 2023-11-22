import requests

FILE_URL = "https://raw.githubusercontent.com/shun-aky/1001-StoryTeller/master/story.txt?token=GHSAT0AAAAAACC5PKVEFGLKD7HCVXAGGHIKZK6OB2Q"

class StoryTeller:
    def __init__(self) -> None:
        self.content = ""

    def get_story(self) -> None:
        try:
            # Extract the raw file URL from the GitHub repository URL
            raw_url = FILE_URL.replace("github.com", "raw.githubusercontent.com").replace("/blob", "")
            print(raw_url)
            response = requests.get(FILE_URL)
            if response.status_code == 200:
                self.content = response.text
                print("Got story successfully!")
                print(self.content)
            else:
                print("Failed to get the story. Status code: ", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Failed to get the story:", str(e))
        except:
            print("Failed to get the story.")

    # def make_mp3(self) -> None:
    #     # Rest of your code for converting text to mp3

    # def start_story(self) -> None:
    #     # Rest of your code for starting the story

st = StoryTeller()
st.get_story()
