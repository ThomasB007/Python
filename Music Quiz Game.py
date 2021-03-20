import random
import time

SongNames = ["Little Bit Of Love", "Blinding Lights", "Uptown Funk", "Dynamite", "Without You", "Dance Monkey",  "Watermelon Sugar", "Calling My Phone", "Levitating", "Despacito", "Shape Of You"]
ArtistNames = ["Tom Grennan", "The Weeknd", "Mark Ronson", "BTS", "The Kid LAROI", "Tones and I", "Harry Styles", "Lil Tjay", "Dua Lipa", "Luis Fonsi", "Ed Sheeran"]
NumOfSongs = 11
MinimumAge = 13
CurrentSong = ""
CurrentArtist = ""
CurrentSongLetters = ""
Chances = 2
Score = 0

def Main():
    global SongNames, ArtistNames, NumOfSongs, MinimumAge, CurrentArtist, CurrentSong, CurrentSongLetters, Chances, Score

    print("Welcome to Music Game Quiz!")

    time.sleep(1)

    Name = input("Enter your name: ")
    Age = int(input("Hello, " + Name + "! Enter your age: "))

    if (Age < MinimumAge):
        print("You need to be at least " + MinimumAge + " to play this game.")
        time.sleep(2)
        exit()

    print("You are allowed to play this game!")
    time.sleep(1)


    def PickRandomSong():
        global CurrentArtist, CurrentSong, CurrentSongLetters
        RandomNum = random.randint(0, NumOfSongs - 1)

        CurrentSong = SongNames[RandomNum]
        CurrentArtist = ArtistNames[RandomNum]

        CurrentSongLetters = CurrentSong[0]
        for i in range(len(CurrentSong)):
            if (CurrentSong[i] == " "):
                CurrentSongLetters = CurrentSongLetters + " " + CurrentSong[i + 1]

        print("\nThe artist is: " + CurrentArtist + "\nAnd the first letters of the song name are: " + CurrentSongLetters)



    PickRandomSong()

    GameOver = False

    while GameOver == False:
        time.sleep(1)
        AttemptAnswer = input("What is the song?")

        if (AttemptAnswer == CurrentSong):
            print("Correct!")
            Score += 1
            Chances = 2
            PickRandomSong()
        else:
            print("Wrong!")
            Chances -= 1

            if (Chances <= 0):
                print("It was " + CurrentSong)
                GameOver = True
            else:
                print("You have " + str(Chances) + " chance left.")

    print("Game Over!")
    print("You scored: " + str(Score))

    Answer = input("Do you want to play again? y/n ")

    if (Answer == "y"):
        Main()

Main()

