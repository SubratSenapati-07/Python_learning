import time
import sys
from playsound import playsound
import threading

def type_lyric(line, char_delay=0.065):
    """Prints a line of text character by character to simulate typing."""
    for char in line:
        print(char, end="", flush=True)
        time.sleep(char_delay)
    print()

def print_kashish_lyrics_synced():
    """Defines and prints lyrics synced with song timestamps."""
    lyrics = [
        "Uski aankhon mein faila kaajal,",
        "Baaton se karti ghayal,",
        "Saanson mein uska hi hai naam,",
        "Meri neend udi hai jab se tu aa gayi jeevan mein,",
        "Roshan kar de tu mujhko aaj.",
        "Uski aankhon mein faila kaajal,",
        "Baaton se karti ghayal,",
        "Saanson mein uska hi hai naam,",
        "Meri neend udi hai jab se tu aa gayi jeevan mein,",
        "Roshan kar de tu mujhko aaj.",
    ]

    # Time delays in seconds (sync with actual song timing)
    delays = [
        2.0,  # after music intro
        1.5,
        2.0,
        4.0,
        4.0,
        2.0,
        1.5,
        2.0,
        4.0,
        5.0,
    ]

    time.sleep(1.5)  # little intro delay

    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

def play_song():
    playsound("kashish.mp3")  # apna gaana yahan dalna hai

# Run song + lyrics together using threading
song_thread = threading.Thread(target=play_song)
song_thread.start()

print_kashish_lyrics_synced()
