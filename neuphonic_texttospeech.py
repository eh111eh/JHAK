from pyneuphonic import Neuphonic, AudioPlayer, TTSConfig
import time


def neuphonic_tts(input_text):
    client = Neuphonic(api_key="f2928a1cb3315ffc6117ade6280443ca5143039518b3f31ccf948ab24c0ea61d.dc2f172a-968a-445a-80d4-b57e7f184dfa")

    sse = client.tts.SSEClient()

    tts_config = TTSConfig(
        speed=1.0, model="neu_hq", voice="e564ba7e-aa8d-46a2-96a8-8dffedade48f"
    )

    with AudioPlayer() as player:
        response = sse.send(input_text, tts_config=tts_config)

        for item in response:
            player.play(item.data.audio)

        time.sleep(0.1)


if __name__ == "__main__":
    text = "Welcome to the Edinburgh Hackathon with Neuphonic, where we're going to build innovative new technology to enhance Conversational Experiences!"
    neuphonic_tts(text)
