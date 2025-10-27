import time
import sys
import time

def type_lyric(line, char_delay=0.065):
    # time takes 😁
    for char in line:
        print(char, end="", flush=True)
        time.sleep(char_delay)
    print()

def sr_lyrics():
    #lyrics with timestamps.....
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

    delays = [
        2.0,
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

    time.sleep(1.5)

    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])
        
sr_lyrics()