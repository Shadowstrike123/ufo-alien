
# créer un screen
WIDTH = 500
HEIGHT = 500

# je crée un sprite ufo (unidentified flying object)
alien = Actor("ufo")
#donner une position à l'ufo (qu'on peut nommer comme on veut)
alien.pos = 40,225

# fonction d'affichage
def draw():
    screen.clear()
    screen.fill("#3B7897")
    alien.draw()

# Fonction principame de contrôle et de mise à jour
def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0
 # Fonction pour changer l'état de l'alien et jouer le son
def target_alien():
    alien.image = "ufored"
    sounds.laser.play()
    clock.schedule_unique(set_alien_normal, 1.0)

# Fonction pour remettre l'ufo jaune
def set_alien_normal():
    alien.image = "ufo"

def on_mouse_down(pos) :
    if alien .collidepoint (pos):
        target_alien()




