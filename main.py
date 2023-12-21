import pygame
import random

# Initialisation de Pygame
pygame.init()

# Paramètres du jeu
largeur, hauteur = 800, 600
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu du Pendu")

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
marron = (128, 0, 0)
rouge = (255, 0, 0)
gris_fonce = (169, 169, 169)

# Police
police = pygame.font.Font("Kids Draw.otf", 36)

# Chargement des mots depuis le fichier
with open("mots.txt", "r") as fichier:
    mots = fichier.readlines()

# Stockage du mot saisi par l'utilisateur
texte_saisi_c = ""
saisie_active = False

# Fonction pour choisir un mot aléatoire
def choisir_mot():
    return random.choice(mots).strip().lower()

# Fonction pour afficher le mot avec les lettres découvertes
def afficher_mot(mot, lettres_trouvees):
    affichage = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            affichage += lettre + " "
        else:
            affichage += "_ "
    return affichage.strip()

# Fonction pour dessiner le pendu
def dessiner_pendu(essais_restants):
    pygame.draw.line(ecran, marron, (50, 300), (150, 300), 5)  # Base du pendu (bas)
    pygame.draw.line(ecran, marron, (100, 100), (200, 100), 5)  # Base du pendu (partie 2)
    pygame.draw.line(ecran, marron, (200, 100), (200, 150), 5)  # Base du pendu (partie 3)
    pygame.draw.line(ecran, marron, (120, 100), (100, 130), 5)  # Base du pendu (partie 4)
    pygame.draw.line(ecran, marron, (100, 100), (100, 300), 5)  # Poteau
    if essais_restants == 5:
        pygame.draw.circle(ecran, blanc, (200, 170), 20, 3)  # Tête
    if essais_restants == 4:
        pygame.draw.circle(ecran, blanc, (200, 170), 20, 3)  # Tête
        pygame.draw.line(ecran, blanc, (200, 190), (200, 250), 3)  # Corps
    if essais_restants == 3:
        pygame.draw.circle(ecran, blanc, (200, 170), 20, 3)  # Tête
        pygame.draw.line(ecran, blanc, (200, 190), (200, 250), 3)  # Corps
        pygame.draw.line(ecran, blanc, (200, 200), (185, 230), 3)  # Bras gauche
    if essais_restants == 2:
        pygame.draw.circle(ecran, blanc, (200, 170), 20, 3)  # Tête
        pygame.draw.line(ecran, blanc, (200, 190), (200, 250), 3)  # Corps
        pygame.draw.line(ecran, blanc, (200, 200), (185, 230), 3)  # Bras gauche
        pygame.draw.line(ecran, blanc, (200, 200), (215, 230), 3)  # Bras droit
    if essais_restants == 1:
        pygame.draw.circle(ecran, blanc, (200, 170), 20, 3)  # Tête
        pygame.draw.line(ecran, blanc, (200, 190), (200, 250), 3)  # Corps
        pygame.draw.line(ecran, blanc, (200, 200), (185, 230), 3)  # Bras gauche
        pygame.draw.line(ecran, blanc, (200, 200), (215, 230), 3)  # Bras droit
        pygame.draw.line(ecran, blanc, (200, 250), (185, 280), 3)  # Jambe gauche
    if essais_restants == 0:
        pygame.draw.circle(ecran, blanc, (200, 170), 20, 3)  # Tête
        pygame.draw.line(ecran, blanc, (200, 190), (200, 250), 3)  # Corps
        pygame.draw.line(ecran, blanc, (200, 200), (185, 230), 3)  # Bras gauche
        pygame.draw.line(ecran, blanc, (200, 200), (215, 230), 3)  # Bras droit
        pygame.draw.line(ecran, blanc, (200, 250), (185, 280), 3)  # Jambe gauche
        pygame.draw.line(ecran, blanc, (200, 250), (215, 280), 3)  # Jambe droite

# Fonction pour afficher le texte dans la fenêtre
def afficher_message(message):
    text = police.render(message, True, blanc)
    ecran.blit(text, (largeur // 2 - text.get_width() // 2, hauteur // 2 - text.get_height() // 2 + 100))
saisie_active = False

# Fonction pour afficher le menu
def afficher_menu(survol_jouer, survol_nouveau_mot):
    global texte_saisi_c, saisie_active

    ecran.fill(noir)

    # Titre du jeu
    titre = police.render("JEU DU PENDU", True, blanc)
    rect_titre = titre.get_rect(center=(largeur // 2, hauteur // 4))
    ecran.blit(titre, rect_titre)

    # Couleur du texte
    couleur_jouer = gris_fonce if survol_jouer else blanc
    couleur_nouveau_mot = gris_fonce if survol_nouveau_mot else blanc

    text_jouer = police.render("Jouer", True, couleur_jouer)
    rect_jouer = text_jouer.get_rect(center=(largeur // 2, hauteur // 2 - 50))
    ecran.blit(text_jouer, rect_jouer)

    pygame.draw.rect(ecran, noir, (250, 325, 300, 50))
    text_nouveau_mot = police.render("Insérer un nouveau mot", True, couleur_nouveau_mot)
    rect_nouveau_mot = text_nouveau_mot.get_rect(center=(largeur // 2, hauteur // 2 + 50))
    ecran.blit(text_nouveau_mot, rect_nouveau_mot)

    # Dessin du rectangle et affichage du texte saisi
    pygame.draw.rect(ecran, blanc if saisie_active else noir, (250, 450, 300, 30), 2)

    pygame.display.flip()

    return rect_jouer, rect_nouveau_mot

pygame.display.flip()

# Fonction pour insérer un mot
def inserer_mot_page():
    global texte_saisi_c, saisie_active

    ecran.fill(noir)

    # Titre de la page d'insertion de mot
    titre = police.render("INSERER UN MOT", True, blanc)
    rect_titre = titre.get_rect(center=(largeur // 2, hauteur // 4))
    ecran.blit(titre, rect_titre)

    # Texte d'instruction
    instruction = police.render("Veuillez insérer un mot :", True, blanc)
    rect_instruction = instruction.get_rect(center=(largeur // 2, hauteur // 2 - 50))
    ecran.blit(instruction, rect_instruction)

    # Zone de texte
    pygame.draw.rect(ecran, blanc, (250, 300, 300, 50))

    mot_ajoute = False
    texte_saisi_c=""

    while not mot_ajoute:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mot_ajoute = True
                elif event.key == pygame.K_BACKSPACE:
                    texte_saisi_c = texte_saisi_c[:-1]
                elif event.unicode.isalpha():
                    texte_saisi_c += event.unicode
        text_saisi = police.render(texte_saisi_c, True, rouge)
        ecran.blit(text_saisi, (320, 300))

        pygame.display.flip()

    maj_text_saisi = texte_saisi_c.upper()
    with open("mots.txt", "a") as fichier:
        fichier.write(maj_text_saisi.strip() + "\n")

# Fonction principale du jeu
def jouer():
    global texte_saisi_c, saisie_active
    survol_jouer = False
    survol_nouveau_mot = False
    inserer_mot = False

    while True:
        if inserer_mot == True:
            inserer_mot_page()
        else:
            rect_jouer,rect_nouveau_mot = afficher_menu(survol_jouer, survol_nouveau_mot)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect_jouer.collidepoint(event.pos):
                    jouer_partie()
                elif rect_nouveau_mot.collidepoint(event.pos):
                    inserer_mot = True
                elif 250 <= event.pos[0] <= 550 and 450 <= event.pos[1] <= 480:
                    saisie_active = not saisie_active
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                survol_jouer = rect_jouer.collidepoint(x, y)
                survol_nouveau_mot = rect_nouveau_mot.collidepoint(x, y)
                pygame.mouse.set_cursor(*pygame.cursors.arrow if not (survol_jouer or survol_nouveau_mot) else pygame.cursors.diamond)
        
        pygame.display.flip()

def jouer_partie():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = set()
    essais_restants = 6 

    while True:
        ecran.fill(gris_fonce)

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha() and event.unicode.islower():
                    lettre = event.unicode.lower()
                    if lettre not in lettres_trouvees:
                        lettres_trouvees.add(lettre)
                        if lettre not in mot_a_deviner:
                            essais_restants -= 1
        
        dessiner_pendu(essais_restants)

        # Affichage du mot
        mot_affiche = afficher_mot(mot_a_deviner, lettres_trouvees)
        text = police.render(mot_affiche, True, blanc)
        ecran.blit(text, (largeur // 2 - text.get_width() // 2, hauteur // 2 - text.get_height() // 2))

        pygame.display.flip()

        # Vérification de la fin de partie
        if essais_restants == 0:
            afficher_message("Vous avez perdu. Le mot était : {}".format(mot_a_deviner))
            break
        elif "_" not in mot_affiche:
            afficher_message("Félicitations ! Vous avez deviné le mot : {}".format(mot_a_deviner))
            break

        pygame.display.flip()

    # Attendre que l'utilisateur appuie sur une touche pour fermer la fenêtre
    attente = True
    while attente:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                attente = False
        pygame.display.flip()

    pygame.quit()

jouer()