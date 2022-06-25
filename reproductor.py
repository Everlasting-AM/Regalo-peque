import random
from pygame import mixer
import pygame
from configuracion import resource_path

siguiente=""

class datos:
    def __init__(self) -> None:
        self.cancion_actual = ""
        self.siguiente = ""
        self.next = ""
        self.parado = True
        

misd = datos()     
CADENA_REPRODUCIENDO = "Reproduciendo: "
MUSIC_END = pygame.USEREVENT+1
PESTANA_COLA_OFF = pygame.USEREVENT+2



canciones = ["15", "1996", "Angel With The Scabbed Wings", "Antichrist Superstar",
             "Are You The Rabbit", "Arma-goddamn-motherfuckin-geddon",
             "Astonishing Panorama of the Endtimes", "Better Of Two Evils",
             "Birds of Hell Awaiting", "Blank and White", "Blood Honey",
             "Born Again", "Born Villain", "Breaking the Same Old Ground",
             "Broken Needle", "Burning Flag", "Cake And Sodomy",
             "Children of Cain", "Coma White",
             "Count To Six And Die The Vacuum Of Infinite Space Encompassing",
             "Cryptorchid", "Cupid Carries a Gun", "Cyclops",
             "Deep Six", "Deformography", "Devour", "Disassociative",
             "Disposable Teens", "Dogma", "DollDagga BuzzBuzz ZiggetyZag",
             "Don't Chase the Dead", "Dope Hat", "Down In The Park",
             "Dried Up Tied And Dead To The World", "EAT ME DRINK ME",
             "Evidence", "Four Rusted Horses", "Fundamentally Loathsome",
             "Get Your Gunn", "Godeatgod", "Great Big White World",
             "Half-Way & One Step Forward", "Heart-Shaped Glasses (When the Heart Guides the Hand)",
             "Heaven Upside Down", "Hey Cruel World",
             "I Don't Like the Drugs (But the Drugs Like Me)", "I Have to Look Up Just to See Hell",
             "I Want To Disappear", "I Want To Kill You Like They Do In the Movies",
             "If I Was Your Vampire", "Infinite Darkness", "Into the Fire",
             "Irresponsible Hate Anthem", "JE$U$ CRI$I$", "Just A Car Crash Away",
             "KaBoom KaBoom", "Keep My Head Together", "Kill4Me",
             "Killing Strangers", "Kinderfeld", "King Kill 33", "Lamb Of God",
             "Lay Down Your Goddamn Arms", "Leave A Scar", "Little Horn",
             "Long Hard Road Out of Hell", "Lunchbox", "Man That You Fear",
             "Marilyn Manson  The Speed Of Pain", "May Cause Discoloration Of The Urine Or Feces",
             "Mechanical Animals", "Minute Of Decay", "Misery Machine",
             "Mister Superstar", "mOBSCENE", "Murderers Are Getting Prettier Every Day",
             "Mutilation Is The Most Sincere Form Of Flattery", "My Monkey",
             "New Model No 15", "No Reflection", "Odds of Even",
             "Organ Grinder", "Overneath the Path of Misery", "Paint You With My Love",
             "Para-noir", "Perfume", "Personal Jesus", "Pistol Whipped",
             "Posthuman", "Pretty as a ($)", "Putting Holes in Happiness",
             "Red, Black And Blue", "Rock is Dead", "Rock N Roll Nigger",
             "Running to the Edge of the World", "(s)AINT",
             "Saturnalia", "SAY10", "Shitty Chicken Gang Bang",
             "Slave Only Dreams To Be King", "Slo-Mo-Tion", "Slutgarden",
             "Snake Eyes And Sissies", "Solve Coagula",
             "Sweet Dreams(Are Made of This)", "Sweet Tooth", "Tainted Love",
             "Tattooed In Reverse", "The Beautiful People",
             "The Bright Young Things", "The Death Song", "The Devil Beneath My Feet",
             "The Dope Show", "The Fall Of Adam", "The Fight Song",
             "The Flowers of Evil", "The Gardener", "The Golden Age Of Grotesque",
             "The Horrible People", "The Last Day On Earth", "The Love Song",
             "The Mephistopheles of los Angeles", "The Nobodies",
             "The Red Carpet Grave", "The Reflecting God",
             "They Said That Hell's Not Hot", "Third Day of a Seven Day Binge",
             "This Is the New Shit", "Threats of Romance", "Tourniquet",
             "Track 16", "Unkillable Monster", "Use Your Fist And Not Your Mouth",
             "User Friendly", "Valentines Day", "Vodevil",
             "Warship My Wreck", "We Are Chaos", "WE KNOW WHERE YOU FUCKING LIVE",
             "We're from America", "Wight Spider", "Wormboy", "WOW",
             "Wrapped In Plastic", "You and Me and the Devil Makes 3"]

def reproducirSiguiente():
    if misd.siguiente=="Bucle":
        reproducir(misd.cancion_actual)
    elif misd.siguiente=="Aleatorio":
        reproducir_aleatoria()
    else:
        pos = canciones.index(misd.cancion_actual)
        if(len(canciones)-1 == pos):
            reproducir(canciones[0])
        else:
            reproducir(canciones[pos+1])

    

def setVolume(nuevo_volumen):
    mixer.music.set_volume(nuevo_volumen)

def returnFormatedSong(song):
    cancion = str(song) + ".mp3"
    return resource_path("./src/" + cancion)

def iniciarReproductor():
    pygame.init()
    mixer.music.set_endevent(MUSIC_END)

def reproducir_aleatoria():
    a = random.randint(0, len(canciones)-1)
    reproducir(canciones[a])

def reproducir(song):
    misd.cancion_actual = song
    mixer.music.load(returnFormatedSong(song))
    mixer.music.play()

def pararCancion():
    mixer.music.pause()

def reanudarCancion():
    mixer.music.unpause()

