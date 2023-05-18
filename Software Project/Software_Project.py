import os
import numpy as np
import pygame

# Adding audio files path
audio_directory = "/home/mayank/music"

pygame.mixer.init()

# Main program infinite while loop
while True:
    # Making a list of all mp3 files
    audio_files = [os.path.join(audio_directory, f) for f in os.listdir(audio_directory) if f.endswith(".mp3")]

    # Shuffle the list of audio files using numpy
    np.random.shuffle(audio_files)

    paused = False

    # Loop through the shuffled list of audio files and play them
    for audio_file in audio_files:
        # Load the audio file into Pygame mixer
        pygame.mixer.music.load(audio_file)

        # Extract the file name
        song_name = os.path.basename(audio_file)

        # Play the audio file
        pygame.mixer.music.play()

        # Displaying the name of the currently playing song
        print("Now playing:", song_name)

        # Taking commands or wait for the audio file to finish.
        while pygame.mixer.music.get_busy() or paused:
            command = input("Enter command (p: pause, r: resume, n: next, q: quit): ")

            if command == "p":           # Adding Pause Command
                pygame.mixer.music.pause()
                paused = True
            elif command == "r":         # Adding Play command
                pygame.mixer.music.unpause()
                paused = False           # Adding next command  
            elif command == "n":
                pygame.mixer.music.stop()
                break
            elif command == "q":         # Adding quit command
                pygame.mixer.music.stop()
                pygame.quit()
                quit()

    # After playing the entire playlist, reshuffle and continue the loop
    np.random.shuffle(audio_files)


