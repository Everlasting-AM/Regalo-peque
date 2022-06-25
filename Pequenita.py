import random
import os
from pygame import mixer

cola = False
menu = False
pausa = False
bucle = False
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


def reproducir(song):
    in_bucle = False
    limpiar_pantalla()
    global menu
    global pausa
    global bucle
    pausa = False
    mixer.init()
    cancion = str(song) + ".mp3"
    mixer.music.load("./src/" + cancion)
    mixer.music.set_volume(0.3)
    if bucle:
        bucle = False
        mixer.music.play(-1)
    else:
        mixer.music.play()
    print("Estás escuchando", song, " en modo bucle")
    print("Pulsa p para detener la canción.")
    print("Pulsa r para reanudar la canción.")
    print("Pulsa a para reproducir otra la canción aleatoria.")
    print("Pulsa e para elegir otra la canción.")
    print("Pulsa b para reproducir en bucle")
    if cola:
        print("Pulsa c para saltar a la siguiente canción de la cola.")
    print("Pulsa s para salir al menú.")
    while mixer.music.get_busy() or pausa or in_bucle:
        if not mixer.music.get_busy() and not pausa:
            mixer.music.play()
        opcion_song = input(">>")
        if opcion_song == "p":
            mixer.music.pause()
            pausa = True
        elif opcion_song == "r":
            mixer.music.unpause()
        elif opcion_song == "s":
            mixer.music.stop()
            menu = True
            return False
        elif opcion_song == "e":
            mixer.music.stop()
            reproducir_unica()
            return False
        elif opcion_song == "a":
            mixer.music.stop()
            reproducir_aleatoria()
            break
        elif cola and opcion_song == "c":
            mixer.music.stop()
            break
        elif opcion_song == "b":
            print("La canción se va a reproductir en modo bucle en modo bucle")
            bucle = True
            return reproducir(song)
        else:
            print("Ey! Esa letra no tiene opciones asignadas, introduce una p, r, s o e.")
    if not pausa:
        print("La canción ha terminado")
    return True


def listar_canciones():
    print("Te puedo ofrecer las siguientes opciones de un autor que quizas conozcas:")
    print("=============================================================")
    for i in range(0, canciones.__len__()):
        print(str(i) + ".", canciones[i])
    print("=============================================================")


def reproducir_aleatoria():
    print("A continuación vamos a reproducir una canción aleatoria:")
    a = random.randint(1, canciones.__len__())
    reproducir(canciones[a])


def reproducir_cola():
    global cola
    global menu
    menu = False
    cola = True
    print("Introduce a continuación los números de las canciones que quieres escuchar separada por espacios.")
    print("Introduce una l si necesitar que te liste las canciones disponibles(en caso contrario, nada).")
    listar = input(">>")
    if listar == "l":
        listar_canciones()
    entrada = (input(">>"))
    print("A continuación se van a reproducir las canciones en el orden que has indicado.")
    for cancion in entrada.split():
        if int(cancion) and canciones.__len__() >= int(cancion) > 0:
            if not reproducir(canciones[int(cancion)]):
                if menu:
                    break
    print("La cola de canciones ya ha terminado, regresando al menú...")
    return True


def reproducir_unica():
    print("Si quieres ver la lista de canciones pon una l, y si ya sabes el número de la canción solo escríbelo.")
    while True:
        opcion = input(">>")
        if not opcion.isalpha() and canciones.__len__() >= int(opcion) > 0:
            if not reproducir(canciones[int(opcion)]):
                break
            else:
                print("Introduce la siguiente canción mi vida.")
        elif opcion == "l":
            listar_canciones()
        else:
            print("Ese número no era válido vida mía, mete otro.")


def limpiar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def listar_opciones_main():
    print("¿Que te gustaría hacer cariño?")
    print("Presiona l para listar la lista de canciones.")
    print("Presiona a para reproducir una canción aleatoria")
    print("Presiona c para reproducir una cola de canciones.")
    print("Presiona u para reproducir una única canción.")
    print("Presiona s para salir.")


if __name__ == '__main__':
    cola = False
    limpiar_pantalla()
    print("****************************************************************************************************")
    print("***                                                                                              ***")
    print("***  ESTE ES EL REPRODUCTOR PERSONAL DE LA COSITA MÁS DULCE DEL MUNDO, MÍRIAM ZAMBUDIO MARTÍNEZ  ***")
    print("***                                                                                              ***")
    print("***    Espero que te guste este regalo mi amor, ha sido creado especialmente para ti, mi vida    ***")
    print("***                                                                                              ***")
    print("****************************************************************************************************")
    print("Recuerda, debes introducir número de las canciones, no el nombre (el que aparece en la lista)\n")
    listar_opciones_main()
    while True:
        main_option = input(">>")
        if main_option == "l":
            limpiar_pantalla()
            listar_canciones()
            listar_opciones_main()
        elif main_option == "a":
            limpiar_pantalla()
            reproducir_aleatoria()
            limpiar_pantalla()
            print("Estás en el menú de inicio")
            listar_opciones_main()
        elif main_option == "c":
            limpiar_pantalla()
            reproducir_cola()
            limpiar_pantalla()
            print("Estás en el menú de inicio")
            listar_opciones_main()
        elif main_option == "u":
            limpiar_pantalla()
            reproducir_unica()
            limpiar_pantalla()
            listar_opciones_main()
            print("Estás en el menú de inicio")
        elif main_option == "s":
            break
        else:
            print("La letra introducida no es una opción, vuelvelo a intentar :)")
    print("\nCiao bella mía.")
