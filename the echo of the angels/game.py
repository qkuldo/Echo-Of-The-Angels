import pygame
import sys
import classes
from random import randint
from random import choice
import json
import os
import copy
#---------------------
pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
pygame.display.set_caption("The Echo of The Angels")
sprites = {
           "title bg":pygame.transform.scale(pygame.image.load("assets/title.png"), (600,600)).convert(),
           "player left":pygame.transform.scale(pygame.image.load("assets/player/player_idle.png"), (50,50)).convert_alpha(),
           "player right":pygame.transform.scale(pygame.image.load("assets/player/player_right.png"), (50,50)).convert_alpha(),
           "player down":pygame.transform.scale(pygame.image.load("assets/player/player_down.png"), (50,50)).convert_alpha(),
           "player up":pygame.transform.scale(pygame.image.load("assets/player/player_up.png"), (50,50)).convert_alpha(),
           "wall":(pygame.transform.scale(pygame.image.load("assets/wall.png"), (30, 230)).convert_alpha(), pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/wall.png"), (30, 500)), 90).convert_alpha()),
           "cursor":pygame.transform.scale(pygame.image.load("assets/cursor.png"), (40,40)).convert_alpha(),
           "sword swing":{
                          "down":pygame.transform.scale(pygame.image.load("assets/sword_swing.png"), (40,40)).convert_alpha(),
                          "up":pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/sword_swing.png"), (40,40)), 180).convert_alpha(),
                          "right":pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/sword_swing.png"), (40,40)), -90).convert_alpha(),
                          "left":pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/sword_swing.png"), (40,40)), 270).convert_alpha(),
                         },
           "hud bg":pygame.transform.scale(pygame.image.load("assets/hud/hud_bg.png"), (600, 90)).convert_alpha(),
           "coin icon":pygame.transform.scale(pygame.image.load("assets/hud/coin_icon.png"), (30, 30)).convert_alpha(),
           "footstep":pygame.transform.scale(pygame.image.load("assets/particle/footstep_particle.png"), (8, 8)).convert_alpha(),
           "dash":pygame.transform.scale(pygame.image.load("assets/particle/dash_particle.png"), (10,10)).convert_alpha(),
           "slime":pygame.transform.scale(pygame.image.load("assets/enemy/slime/slime.png"), (50,50)).convert_alpha(),
           "slimeball":pygame.transform.scale(pygame.image.load("assets/enemy/slime/slimeball.png"), (30, 30)).convert_alpha(),
           "invincible slime":pygame.transform.scale(pygame.image.load("assets/enemy/slime/slime_inv.png"), (50,50)).convert_alpha(),
           "door":pygame.transform.scale(pygame.image.load("assets/door.png"), (30,30)).convert_alpha(),
           "floor":pygame.transform.scale(pygame.image.load("assets/floor.png"), (450, 250)).convert_alpha(),
           "player rest":pygame.transform.scale(pygame.image.load("assets/player/player_rest.png"), (50,50)).convert_alpha(),
           "small wall":pygame.transform.scale(pygame.image.load("assets/small_wall.png"), (30,30)).convert_alpha(),
           "slime 2":pygame.transform.scale(pygame.image.load("assets/enemy/slime/slime_2.png"), (50,50)).convert_alpha(),
           "sword swing2":{
                          "up":pygame.transform.scale(pygame.image.load("assets/sword_swing2.png"), (40,40)).convert_alpha(),
                          "down":pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/sword_swing2.png"), (40,40)), 180).convert_alpha(),
                          "right":pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/sword_swing2.png"), (40,40)), 270).convert_alpha(),
                          "left":pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/sword_swing2.png"), (40,40)), 90).convert_alpha(),
                         },
           "enemy death":{
                          1:pygame.transform.scale(pygame.image.load("assets/particle/enemy_death1.png"), (40,40)).convert_alpha(),
                          2:pygame.transform.scale(pygame.image.load("assets/particle/enemy_death2.png"), (40,40)).convert_alpha(),
                          3:pygame.transform.scale(pygame.image.load("assets/particle/enemy_death3.png"), (40,40)).convert_alpha()
                         },
           "player left invincible":pygame.transform.scale(pygame.image.load("assets/player/player_idle_inv.png"), (50,50)).convert_alpha(),
           "player right invincible":pygame.transform.scale(pygame.image.load("assets/player/player_right_inv.png"), (50,50)).convert_alpha(),
           "player down invincible":pygame.transform.scale(pygame.image.load("assets/player/player_down_inv.png"), (50,50)).convert_alpha(),
           "player up invincible":pygame.transform.scale(pygame.image.load("assets/player/player_up_inv.png"), (50,50)).convert_alpha(),
           "corrupted golem 1":pygame.transform.scale(pygame.image.load("assets/enemy/corrupted_golem/corrupted_golem1.png"), (64,64)).convert_alpha(),
           "corrupted golem 2":pygame.transform.scale(pygame.image.load("assets/enemy/corrupted_golem/corrupted_golem2.png"), (64,64)).convert_alpha(),
           "invincible corrupted golem":pygame.transform.scale(pygame.image.load("assets/enemy/corrupted_golem/corrupted_golem_inv.png"), (64,64)).convert_alpha(),
           "stomp":pygame.transform.scale(pygame.image.load("assets/enemy/corrupted_golem/stomp_attack.png"), (50, 50)).convert_alpha(),
           "slime corpse":pygame.transform.scale(pygame.image.load("assets/enemy/slime/slime_corpse.png"), (30,30)).convert_alpha(),
           "corrupted golem corpse":pygame.transform.scale(pygame.image.load("assets/enemy/corrupted_golem/corrupted_golem_corpse.png"), (60,60)).convert_alpha(),
           "flame particle 1":pygame.transform.scale(pygame.image.load("assets/particle/flame_particle1.png"), (5,5)).convert_alpha(),
           "flame particle 2":pygame.transform.scale(pygame.image.load("assets/particle/flame_particle2.png"), (5,5)).convert_alpha(),
           "torch":(pygame.transform.scale(pygame.image.load("assets/torch.png"), (30, 30)),pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/torch.png"), (30, 30)), 180),pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/torch.png"), (30, 30)), 270),pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/torch.png"), (30, 30)), 90),),
           "title bg 2":pygame.transform.scale(pygame.image.load("assets/title2.png"), (600,600)).convert(),
           "torch 2":(pygame.transform.scale(pygame.image.load("assets/torch2.png"), (30, 30)),pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/torch2.png"), (30, 30)), 180),pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/torch2.png"), (30, 30)), 270),pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/torch2.png"), (30, 30)), 90),),
           "gameover 1":pygame.transform.scale(pygame.image.load("assets/ripbozo_dead.png"), (600,600)).convert(),
           "gameover 2":pygame.transform.scale(pygame.image.load("assets/ripbozo_dead2.png"), (600,600)).convert(),
           "key icon":pygame.transform.scale(pygame.image.load("assets/hud/key_icon.png"), (30, 30)).convert_alpha(),
           "locked door":pygame.transform.scale(pygame.image.load("assets/locked_door.png"), (30,30)).convert_alpha(),
           "pot":pygame.transform.scale(pygame.image.load("assets/pot.png"),(40,40)).convert_alpha(),
           "alert":pygame.transform.scale(pygame.image.load("assets/alert.png"),(20,20)).convert_alpha(),
           "damage particle":pygame.transform.scale(pygame.image.load("assets/particle/damage_particle.png"),(30,30)).convert_alpha()
          }
sprites["player left"].set_colorkey((255,255,255))
sprites["player right"].set_colorkey((255,255,255))
sprites["player down"].set_colorkey((255,255,255))
sprites["player up"].set_colorkey((255,255,255))
sprites["cursor"].set_colorkey((255,255,255))
sprites["sword swing"]["up"].set_colorkey((255,255,255))
sprites["sword swing"]["down"].set_colorkey((255,255,255))
sprites["sword swing"]["left"].set_colorkey((255,255,255))
sprites["sword swing"]["right"].set_colorkey((255,255,255))
sprites["coin icon"].set_colorkey((255,255,255))
sprites["slime"].set_colorkey((255,255,255))
sprites["slimeball"].set_colorkey((255,255,255))
sprites["invincible slime"].set_colorkey((255,255,255))
sprites["player rest"].set_colorkey((255,255,255))
sprites["slime 2"].set_colorkey((255,255,255))
sprites["sword swing2"]["up"].set_colorkey((255,255,255))
sprites["sword swing2"]["down"].set_colorkey((255,255,255))
sprites["sword swing2"]["left"].set_colorkey((255,255,255))
sprites["sword swing2"]["right"].set_colorkey((255,255,255))
sprites["enemy death"][1].set_colorkey((255,255,255))
sprites["enemy death"][2].set_colorkey((255,255,255))
sprites["enemy death"][3].set_colorkey((255,255,255))
sprites["player left invincible"].set_colorkey((255,255,255))
sprites["player right invincible"].set_colorkey((255,255,255))
sprites["player down invincible"].set_colorkey((255,255,255))
sprites["player up invincible"].set_colorkey((255,255,255))
sprites["corrupted golem 1"].set_colorkey((255,255,255))
sprites["corrupted golem 2"].set_colorkey((255,255,255))
sprites["invincible corrupted golem"].set_colorkey((255,255,255))
sprites["stomp"].set_colorkey((255,255,255))
sprites["slime corpse"].set_colorkey((255,255,255))
sprites["corrupted golem corpse"].set_colorkey((255,255,255))
sprites["flame particle 1"].set_colorkey((255,255,255))
sprites["flame particle 2"].set_colorkey((255,255,255))
sprites["torch"][0].set_colorkey((255,255,255))
sprites["torch"][1].set_colorkey((255,255,255))
sprites["torch"][2].set_colorkey((255,255,255))
sprites["torch"][3].set_colorkey((255,255,255))
sprites["torch 2"][0].set_colorkey((255,255,255))
sprites["torch 2"][1].set_colorkey((255,255,255))
sprites["torch 2"][2].set_colorkey((255,255,255))
sprites["torch 2"][3].set_colorkey((255,255,255))
sprites["key icon"].set_colorkey((255,255,255))
sprites["pot"].set_colorkey((255,255,255))
sprites["alert"].set_colorkey((255,255,255))
sprites["damage particle"].set_colorkey((255,255,255))
sprites["dash"].set_colorkey((255,255,255))
pygame.display.set_icon(sprites["player down"])
cursor_rect = sprites["cursor"].get_rect()
sound_effects = {
                 "swing sword":pygame.mixer.Sound("sounds/sword_swing.wav"),
                 "defeat enemy":pygame.mixer.Sound("sounds/defeat_enemy.wav")
                }
pygame.mixer.music.set_volume(0.7)
music = [
         "sounds/Echoes_From_The_Deep.wav",
         "sounds/Start_Anew.wav",
         "sounds/Dark_Room.wav",
         "sounds/Voices_Of_Many.wav",
         "sounds/Angels_Choir.wav"
        ]
def play_music(music, infinite=True):
    pygame.mixer.music.load(music)
    if (infinite):
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.play()
def save(to_save):
    file = open("saves/data.json", "w")
    json.dump(to_save, file, indent=4)
    file.close()

#---------------------
def title():
    global cursor_rect
    play_music(music[1])
    button_font = pygame.font.Font("fonts/Pixeltype.ttf", 60)
    title_font = pygame.font.Font("fonts/Pixeltype.ttf", 80)
    title_surf = title_font.render("The Echo of The Angels", True, (178, 157, 157))
    start_surf = button_font.render("-Load Game-", True, (127,98,98))
    new_surf = button_font.render("-New Game-", True, (127,98,98))
    start_rect = start_surf.get_rect()
    title_rect = title_surf.get_rect()
    new_rect = new_surf.get_rect()
    title_rect.midtop = (600/2, 50)
    start_rect.midtop = (150, 200)
    new_rect.midtop = (150, 300)
    anim_frames = (sprites["title bg"],sprites["title bg 2"],)
    anim_index = 0
    anim_pause = 500
    current_bg = anim_frames[anim_index]
    while True:
        cursor_rect.center = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and start_rect.colliderect(cursor_rect)):
                return
            elif (event.type == pygame.MOUSEBUTTONDOWN and new_rect.colliderect(cursor_rect)):
                save({"pos":{"x":300, "y":300}, "room":"spawn room", "stats": {"hp": 100, "max hp": 100, "gold": 0, "inventory": [], "max inventory capacity": 20, "current weapon":"sword", "weapons":["sword"],"keys":0,"speed":5,"attack":1,"key enemies":[True],"locked rooms":[True]}, "respawn timer":{}})
                return
            anim_pause -= clock.get_time()
            if (anim_pause <= 0):
                anim_index += 1
                anim_pause = 500
            if (anim_index > 1):
                anim_index = 0
            current_bg = anim_frames[anim_index]
            screen.blit(current_bg, (0,0))
            if (start_rect.colliderect(cursor_rect)):
                start_surf = button_font.render("[Load Game]", True, (178, 157, 157))
            else:
                start_surf = button_font.render("-Load Game-", True, (127,98,98))
            if (new_rect.colliderect(cursor_rect)):
                new_surf = button_font.render("[New Game]", True, (178, 157, 157))
            else:
                new_surf = button_font.render("-New Game-", True, (127,98,98))
            start_rect = start_surf.get_rect(midtop=(150, 200))
            new_rect = new_surf.get_rect(midtop=(150, 300))
            screen.blit(title_surf, title_rect)
            screen.blit(start_surf, start_rect)
            screen.blit(new_surf, new_rect)
            if (pygame.mouse.get_focused()):
                screen.blit(sprites["cursor"], cursor_rect)
            pygame.display.update()
            clock.tick(60)
#--------------------
def checkfor_collision_dir(wall, player_x, player_y):
    if (player_x > wall.pos[0]):
        return "left"
    elif (player_x < wall.pos[0]):
        return "right"
    elif (player_y > wall.pos[1]):
        return "up"
    elif (player_y < wall.pos[1]):
        return "down"
#--------------------
def gameover(coins, died_msg):
    current_bg = sprites["gameover 1"]
    anim_timer = 500
    break_while = False
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and back_to_game_rect.colliderect(cursor_rect)):
                game()
            elif (event.type == pygame.MOUSEBUTTONDOWN and back_to_title_rect.colliderect(cursor_rect)):
                break_while = True
        if (break_while):
            break
        anim_timer -= clock.get_time()
        if (anim_timer <= 0):
            if (current_bg == sprites["gameover 1"]):
                current_bg = sprites["gameover 2"]
            elif (current_bg == sprites["gameover 2"]):
                current_bg = sprites["gameover 1"]
            anim_timer = 500
        cursor_rect.center = pygame.mouse.get_pos()
        screen.blit(current_bg, (0,0))
        gameover_font = pygame.font.Font("fonts/Pixeltype.ttf", 100)
        stats_font = pygame.font.Font("fonts/Pixeltype.ttf", 40)
        button_font = pygame.font.Font("fonts/Pixeltype.ttf", 40)
        back_to_title_surf = button_font.render("-Return To Title Screen-", True, (127,98,98))
        back_to_game_surf = button_font.render("-Return To Last Save-", True, (127,98,98))
        back_to_title_rect = back_to_title_surf.get_rect(midtop=(300, 200))
        back_to_game_rect = back_to_title_surf.get_rect(midtop=(300, 260))
        if (back_to_title_rect.colliderect(cursor_rect)):
            back_to_title_surf = button_font.render("[Return To Title Screen]", True, (178, 157, 157))
        else:
            back_to_title_surf = button_font.render("-Return To Title Screen-", True, (127,98,98))
        if (back_to_game_rect.colliderect(cursor_rect)):
            back_to_game_surf = button_font.render("[Return To Last Save]", True, (178, 157, 157))
        else:
            back_to_game_surf = button_font.render("-Return To Last Save-", True, (127,98,98))
        back_to_title_rect = back_to_title_surf.get_rect(midtop=(300, 200))
        back_to_game_rect = back_to_title_surf.get_rect(midtop=(300, 300))
        gameover_surf = gameover_font.render("Game Over", True, (127,98,98))
        gameover_rect = gameover_surf.get_rect(midtop=(300, 100))
        coins_surf = stats_font.render("Gold:"+str(coins), True, (127,98,98))
        coin_rect = coins_surf.get_rect(midtop=(300, 360))
        death_msg = stats_font.render(died_msg, True, (127,98,98))
        death_rect = death_msg.get_rect(midtop=(300,400))
        screen.blit(gameover_surf, gameover_rect)
        screen.blit(coins_surf, coin_rect)
        screen.blit(death_msg, death_rect)
        screen.blit(back_to_title_surf, back_to_title_rect)
        screen.blit(back_to_game_surf, back_to_game_rect)
        if (pygame.mouse.get_focused()):
            screen.blit(sprites["cursor"], cursor_rect)
        clock.tick(60)
        pygame.display.update()
#--------------------
def glowsurf(glow, radius, layers=25, color=255, main_color="n"):
    surf = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
    glow = pygame.math.clamp(glow, 0, color)
    for i in range(layers):
        k = i*glow
        k = pygame.math.clamp(k,0,color)
        if (main_color == "n"):
            circle_color = (k,k,k,)
        if (main_color == "r"):
            circle_color = (color,k,k,)
        if (main_color == "g"):
            circle_color = (k,color,k,)
        if (main_color == "b"):
            circle_color = (k,k,color,)
        if (main_color == "y"):
            circle_color = (color,color,k,)
        pygame.draw.circle(surf, circle_color, surf.get_rect().center, radius-i*3)
    return surf
#--------------------
def pause(save_options):
    global cursor_rect
    button_font = pygame.font.Font("fonts/Pixeltype.ttf", 60)
    pause_font = pygame.font.Font("fonts/Pixeltype.ttf", 100)
    pause_txt = pause_font.render("Paused", True, (127,98,98))
    pause_rect = pause_txt.get_rect(midtop=(300,100))
    resume_txt = button_font.render("-Resume-", True, (127,98,98))
    resume_rect = resume_txt.get_rect(midtop=(300,200))
    save_txt = button_font.render("-Save And Quit-", True, (127,98,98))
    save_rect = save_txt.get_rect(midtop=(300,300))
    while_break = False
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN and resume_rect.colliderect(cursor_rect)):
                while_break = True
            if (event.type == pygame.MOUSEBUTTONDOWN and save_rect.colliderect(cursor_rect)):
                save(save_options)
                return True
        cursor_rect.center = pygame.mouse.get_pos()
        if(while_break):
            break
        screen.fill("black")
        if (resume_rect.colliderect(cursor_rect)):
            resume_txt = button_font.render("[Resume]", True, (178, 157, 157))
        else:
            resume_txt = button_font.render("-Resume-", True, (127,98,98))
        if (save_rect.colliderect(cursor_rect)):
            save_txt = button_font.render("[Save And Quit]", True, (178, 157, 157))
        else:
            save_txt = button_font.render("-Save And Quit-", True, (127,98,98))
        resume_rect = resume_txt.get_rect(midtop=(300,200))
        save_rect = save_txt.get_rect(midtop=(300,300))
        screen.blit(pause_txt, pause_rect)
        screen.blit(resume_txt, resume_rect)
        screen.blit(save_txt, save_rect)
        screen.blit(sprites["cursor"], cursor_rect)
        clock.tick(60)
        pygame.display.update()
    return False
#--------------------
def screenshake():
    buffersurf = screen.copy()
    screen.fill("black")
    screen.blit(buffersurf, (randint(-10,10),randint(-10,10)))
#--------------------
def game():
    global cursor_rect
    file = open("saves/data.json")
    data = json.load(file)
    player_x = data["pos"]["x"]
    player_y = data["pos"]["y"]
    player_stats = data["stats"]
    main_dir = sprites["player down"]
    sword_cooldown = 470
    sword_pause = False
    sword_pause_timer = 0
    hud_font = pygame.font.Font("fonts/Pixeltype.ttf", 40)
    coin_surf = hud_font.render("x"+str(player_stats["gold"]), True, (255,255,255))
    hp_surf = hud_font.render("HP:", True, (255,255,255))
    hp_rect = pygame.Rect(150, 30, player_stats["hp"]*2, 30)
    max_hp_rect = pygame.Rect(150, 30, player_stats["max hp"]*2, 30)
    player_hitbox = main_dir.get_rect(x=player_x,y=player_y)
    footsteps = classes.particle.ParticleGroup(sprites["footstep"], [player_hitbox.midbottom[0], player_hitbox.midbottom[1]-20], randint(-3, 3), randint(-3,3), 100)
    dash_particle = classes.particle.ParticleGroup(sprites["dash"], [player_hitbox.midbottom[0], player_hitbox.midbottom[1]-20], randint(-3, 3), 0, 300)
    flame_particle_1 = classes.particle.ParticleGroup(sprites["flame particle 1"], [0,0], 0, -1, 500)
    flame_particle_2 = classes.particle.ParticleGroup(sprites["flame particle 2"], [0,0], 0, -1, 500)
    damage_particle = classes.particle.ParticleGroup(sprites["damage particle"], [0,0], 0, 1, 500)
    increment_x = 0
    increment_y = 0
    dash_pause = 0
    dash = False
    enemies = []
    enemy_projectiles = []
    invincibility_frames = 0
    sword_usage = 0
    room_dict = {
                 "spawn room":classes.room.Room([classes.room.Spawner(classes.enemy.enemy_ids["slime"], [250, 300])], ["dungeon room 2", None, None, "dungeon room 3"]),
                 "dungeon room 2":classes.room.Room([classes.room.Spawner(classes.enemy.enemy_ids["slime"], [250, 300]), classes.room.Spawner(classes.enemy.enemy_ids["corrupted golem"], [390, 300])], [None, "spawn room", None, "dungeon room 4"]),
                 "dungeon room 4":classes.room.Room([classes.room.Spawner(classes.enemy.enemy_ids["slime"], [250, 300])], [classes.room.Lock("dungeon room 6"), "dungeon room 3", "dungeon room 2", "dungeon room 5"], [classes.room.Wall([350, 290], sprites["small wall"]), classes.room.Wall([200, 300], sprites["small wall"])]),
                 "dungeon room 3":classes.room.Room([], ["dungeon room 4", None, "spawn room", None], [classes.room.Wall([250, 290], sprites["small wall"]), classes.room.Wall([350, 300], sprites["small wall"])]),
                 "dungeon room 5":classes.room.Room([classes.room.Spawner(classes.enemy.enemy_ids["slime"], [300, 350], key_item="key"),classes.room.Spawner(classes.enemy.enemy_ids["slime"], [200, 350])], [None, None, "dungeon room 4", None], [classes.room.Wall([340, 250], sprites["small wall"]), classes.room.Wall([240, 300], sprites["small wall"])]),
                 "dungeon room 6":classes.room.Room([], [None, "dungeon room 4", None, None], pots=[classes.room.Pot([100, 350],texture=sprites["pot"]),classes.room.Pot([240,300],texture=sprites["pot"])])
                }
    if (player_stats["locked rooms"][0] == False):
        room_dict["dungeon room 4"].exits[0] = "dungeon room 6"
    wall_list = []
    pot_list = []
    current_room = data["room"]
    respawn_timer = data["respawn timer"]
    if (current_room in respawn_timer):
        room_dict[current_room].load_room(enemies, sprites, wall_list, pot_list, False, False)
    else:
        room_dict[current_room].load_room(enemies, sprites, wall_list, pot_list)
    room_cooldown = 0
    resting = False
    player_gothit = pygame.USEREVENT + 1
    player_death = pygame.USEREVENT + 2
    play_music(music[0], False)
    current_music = music[0]
    rest_cooldown = 0
    time_till_wakeup = 0
    notification_font = pygame.font.Font("fonts/Pixeltype.ttf", 20)
    dialogue_font = pygame.font.Font("fonts/Pixeltype.ttf", 50)
    current_notification = None
    notification_rect = None
    wall_move = [True, True, True, True]
    roomwall_rects = []
    for i in wall_list:
        roomwall_rects.append(i.hitbox)
    died_to = "Null"
    animations = []
    footstep_cooldown = 0
    player_blitscreen = main_dir
    spin_walk_cooldown = 0
    dark_surf = pygame.Surface((600, 600))
    dark_surf.fill("black")
    dark_surf.set_alpha(45)
    combat_text_font = pygame.font.Font("fonts/Pixeltype.ttf", 25)
    combat_text = []
    current_torch = sprites["torch"]
    torch_timer = 500
    while_break = False
    player_effects = []
    screenshake_duration = 0
    moved = True
    dash_duration = 0
    transition = True
    while True:
        dark_surf.fill("black")
        dark_surf.set_alpha(45)
        coin_surf = hud_font.render("x"+str(player_stats["gold"]), True, (255,255,255))
        key_surf = hud_font.render("x"+str(player_stats["keys"]), True, (255,255,255))
        updated_x = 0
        possible_attack_dist = pygame.Rect(player_x, player_y, 100, 100)
        torch_timer -= clock.get_time()
        if (screenshake_duration > 0):
            screenshake_duration -= clock.get_time()
        if (torch_timer <= 0):
            if (current_torch == sprites["torch"]):
                current_torch = sprites["torch 2"]
            elif (current_torch == sprites["torch 2"]):
                current_torch = sprites["torch"]
            torch_timer = 500
        if (dash_duration > 0):
            dash_duration -= clock.get_time()
            if ((main_dir == sprites["player left"] or main_dir == sprites["player left invincible"]) and not player_hitbox.colliderect(wall_r_rect)):
                player_x -= player_stats["speed"]*2
            if ((main_dir == sprites["player right"] or main_dir == sprites["player right invincible"]) and not player_hitbox.colliderect(wall_l_rect)):
                player_x += player_stats["speed"]*2
            if ((main_dir == sprites["player up"] or main_dir == sprites["player up invincible"]) and not player_hitbox.colliderect(wall_n_rect)):
                player_y -= player_stats["speed"]*2
            if ((main_dir == sprites["player down"] or main_dir == sprites["player down invincible"]) and not player_hitbox.colliderect(wall_s_rect)):
                player_y += player_stats["speed"]*2
        if (invincibility_frames > 0):
            invincibility_frames -= 1
        if (room_cooldown > 0):
            room_cooldown -= clock.get_time()
        if (spin_walk_cooldown > 0):
            spin_walk_cooldown -= clock.get_time()
        if (rest_cooldown > 0):
            rest_cooldown -= clock.get_time()
        if (time_till_wakeup > 0):
            time_till_wakeup -= clock.get_time()
        if (footstep_cooldown > 0):
            footstep_cooldown -= clock.get_time()
        cursor_rect.center = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            elif (event.type == player_gothit):
                knockback = choice([-15,15])
                if (knockback == -15 and not wall_r_rect.colliderect(player_hitbox)):
                    player_x += knockback
                if (knockback == 15 and not wall_l_rect.colliderect(player_hitbox)):
                    player_x += knockback
                knockback = choice([-15,15])
                if (knockback == -15 and not wall_n_rect.colliderect(player_hitbox)):
                    player_y += knockback
                if (knockback == 15 and not wall_s_rect.colliderect(player_hitbox)):
                    player_y += knockback
                current_notification = notification_font.render("You were hit!", True, (127, 98, 98))
                notification_rect = current_notification.get_rect(midtop=(200, 450))
            elif (event.type == player_death):
                fade()
                gameover(player_stats["gold"], died_to)
                while_break = True
            del event
        if (while_break):
            break
        hp_rect = pygame.Rect(150, 30, player_stats["hp"]*2, 30)
        max_hp_rect = pygame.Rect(150, 30, player_stats["max hp"]*2, 30)
        player_hitbox = player_blitscreen.get_rect(x=player_x,y=player_y)
        keys = pygame.key.get_pressed()
        wall_n_rect = sprites["wall"][1].get_rect(x=50,y=200)
        wall_s_rect = sprites["wall"][1].get_rect(x=50,y=400)
        wall_r_rect = sprites["wall"][0].get_rect(x=50, y=230)
        wall_l_rect = sprites["wall"][0].get_rect(x=520, y=230)
        exits = [wall_n_rect.midbottom, wall_s_rect.midtop, [wall_l_rect.midleft[0], wall_l_rect.midleft[1]-40], [wall_r_rect.midright[0], wall_r_rect.midright[1]-40]]
        exit_rects = [pygame.Rect(wall_n_rect.midbottom[0],wall_n_rect.midbottom[1]+2,30,30), pygame.Rect(wall_s_rect.midtop[0],wall_s_rect.midtop[1]-30,30,30), pygame.Rect(wall_l_rect.midleft[0]-30,wall_l_rect.midleft[1]-40,30,30), pygame.Rect(wall_r_rect.midright[0],wall_r_rect.midright[1]-40,30,30)]
        dash_pause -= clock.get_time()
        if (dash_pause <= 0):
            dash = True
            dash_pause = 1000
        old_x = copy.deepcopy(player_x)
        old_y = copy.deepcopy(player_y)
        if (keys[pygame.K_UP] and not wall_n_rect.colliderect(player_hitbox) and (not sword_pause) and (not resting) and (wall_move[0]) and (not dash_duration > 0)):
            if ((keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]) and dash):
                screenshake_duration = 100
                player_y -= player_stats["speed"]*2
                dash = False
                invincibility_frames = 20
                dash_duration = 200
                for i in range(1, 10):
                    dash_particle.pos = [player_x+randint(-10,10), player_y+randint(-30,30)]
                    dash_particle.spawn_particle()
                    dash_particle.particlelist[-1].velocity_y = 2
                    dash_particle.particlelist[-1].velocity_x = 0
            else:
                player_y -= player_stats["speed"]
            main_dir = sprites["player up"]
            if (randint(1,3) == 2):
                 footsteps.spawn_particle()
            moved = True
        elif (keys[pygame.K_DOWN] and not wall_s_rect.colliderect(player_hitbox) and (not sword_pause) and (not resting) and (wall_move[1]) and (not dash_duration > 0)):
            if ((keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]) and dash):
                screenshake_duration = 100
                player_y += player_stats["speed"]*2
                dash = False
                invincibility_frames = 20
                dash_duration = 200
                for i in range(1, 10):
                    dash_particle.pos = [player_x+randint(-10,10), player_y+randint(-30,30)]
                    dash_particle.spawn_particle()
                    dash_particle.particlelist[-1].velocity_y = -2
                    dash_particle.particlelist[-1].velocity_x = 0
            else:
                player_y += player_stats["speed"]
            main_dir = sprites["player down"]
            if (randint(1,3) == 2):
                 footsteps.spawn_particle()
            moved = True
        if (keys[pygame.K_RIGHT]and not wall_l_rect.colliderect(player_hitbox) and (not sword_pause) and (not resting) and (wall_move[2]) and (not dash_duration > 0)):
            updated_x = 1
            if ((keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]) and dash):
                screenshake_duration = 100
                player_x += player_stats["speed"]*2
                dash = not dash
                invincibility_frames = 20
                dash_duration = 200
                for i in range(1, 10):
                    dash_particle.pos = [player_x+randint(-30,30), player_y+randint(-10,10)]
                    dash_particle.spawn_particle()
                    dash_particle.particlelist[-1].velocity_x = -1
                    dash_particle.particlelist[-1].velocity_y = 0
            else:
                player_x += player_stats["speed"]
            main_dir = sprites["player right"]
            if (randint(1,3) == 2):
                 footsteps.spawn_particle()
            moved = True
        elif (keys[pygame.K_LEFT] and not wall_r_rect.colliderect(player_hitbox) and (not sword_pause) and (not resting) and (wall_move[3] == True) and (not dash_duration > 0)):
            updated_x = 2
            if ((keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]) and dash):
                player_x -= player_stats["speed"]*2
                dash = not dash
                invincibility_frames = 100
                screenshake_duration = 100
                dash_duration = 200
                for i in range(1, 10):
                    dash_particle.pos = [player_x+randint(-30,30), player_y+randint(0,10)]
                    dash_particle.spawn_particle()
                    dash_particle.particlelist[-1].velocity_x = 1
                    dash_particle.particlelist[-1].velocity_y = 0
            else:
                player_x -= player_stats["speed"]
            main_dir = sprites["player left"]
            if (randint(1,3) == 2):
                 footsteps.spawn_particle()
            moved = True
        if (keys[pygame.K_e] and room_cooldown <= 0 and not resting):
            for i in exits:
                """
                   I took so much time trying to figure out how to code something that delays coin farming.
                   if only players were dumb.
                """
                if (player_hitbox.collidelist(exit_rects) != -1 and player_hitbox.collidelist(exit_rects) == exits.index(i)):
                    if ((not current_room in respawn_timer)):
                        respawn_timer[current_room] = 10
                    direction = exits.index(i)
                    if (room_dict[current_room].exits[direction] != None and type(room_dict[current_room].exits[direction]) != classes.room.Lock):
                        current_room = room_dict[current_room].exits[direction]
                        enemies = []
                        enemy_projectiles = []
                        wall_list = []
                        pot_list = []
                        roomwall_rects = []
                        animations = []
                        if ((not current_room in respawn_timer) or (respawn_timer[current_room] == 0) or (current_room == "dungeon room 5" and player_stats["key enemies"][0] == True)):
                            room_dict[current_room].load_room(enemies, sprites, wall_list, pot_list)
                            if (current_room in respawn_timer and respawn_timer[current_room] == 0):
                                respawn_timer.pop(current_room)
                        else:
                            room_dict[current_room].load_room(enemies, sprites, wall_list, pot_list, False, False)
                            respawn_timer[current_room] -= 1
                        for i in wall_list:
                            roomwall_rects.append(i.hitbox)
                        if (direction == 0):
                            player_x = wall_s_rect.midtop[0]-5
                            player_y = wall_s_rect.midtop[1]-40
                        elif (direction == 1):
                            player_x = exit_rects[0].x
                            player_y = exit_rects[0].y
                        elif (direction == 2):
                            player_x = exit_rects[3].x
                            player_y = exit_rects[3].y
                        elif (direction == 3):
                            player_x = exit_rects[2].x
                            player_y = exit_rects[2].y
                        save({"pos":{"x":player_x, "y":player_y}, "room":current_room, "stats":player_stats, "respawn timer":respawn_timer})
                        room_cooldown = 1000
                        fade()
                        transition = True
                    elif (type(room_dict[current_room].exits[direction]) == classes.room.Lock and player_stats["keys"] == 0):
                        current_notification = notification_font.render("This door is locked.",True, (127,98,98))
                        notification_rect = current_notification.get_rect(midtop=(200, 450))
                    elif (type(room_dict[current_room].exits[direction]) == classes.room.Lock and player_stats["keys"] > 0):
                        current_notification = notification_font.render("You unlock the door.",True, (127,98,98))
                        notification_rect = current_notification.get_rect(midtop=(200, 450))
                        pygame.time.delay(300)
                        if (current_room == "dungeon room 4"):
                            room_dict["dungeon room 4"].exits[0] = "dungeon room 6"
                            player_stats["locked rooms"][0] = False
                        player_stats["keys"] -= 1
        if (keys[pygame.K_r] and rest_cooldown <= 0):
            if (len(enemies) == 0):
                 resting = not resting
                 rest_cooldown = 10000
                 time_till_wakeup = 1000
                 current_notification = notification_font.render("You rest for a bit.",True, (127,98,98))
                 notification_rect = current_notification.get_rect(midtop=(200, 450))
                 if (player_stats["hp"] < 100):
                      player_stats["hp"] += 2
                 main_dir = sprites["player rest"]
                 player_blitscreen = pygame.transform.rotate(main_dir, randint(-5,5))
                 player_blitscreen.set_colorkey((255, 255, 255))
            else:
                current_notification = notification_font.render("You tried to sleep, but the noises of the monsters distract you.",True, (127,98,98))
                notification_rect = current_notification.get_rect(midtop=(200, 450))
        if (keys[pygame.K_s]):
            save({"pos":{"x":player_x, "y":player_y}, "room":current_room, "stats":player_stats, "respawn timer":respawn_timer})
            current_notification = notification_font.render("Game saved!",True, (127,98,98))
            notification_rect = current_notification.get_rect(midtop=(200, 450))
        if (keys[pygame.K_ESCAPE]):
            while_break = pause({"pos":{"x":player_x, "y":player_y}, "room":current_room, "stats":player_stats, "respawn timer":respawn_timer})
        if (resting and time_till_wakeup <= 0):
            resting = not resting
            main_dir = sprites["player down"]
        if (invincibility_frames > 0):
            if (main_dir == sprites["player up"]):
                main_dir = sprites["player up invincible"]
            if (main_dir == sprites["player down"]):
                main_dir = sprites["player down invincible"]
            if (main_dir == sprites["player left"]):
                main_dir = sprites["player left invincible"]
            if (main_dir == sprites["player right"]):
                main_dir = sprites["player right invincible"]
            if (spin_walk_cooldown <= 0):
                player_blitscreen = pygame.transform.rotate(main_dir, randint(-5, 5))
                player_blitscreen.set_colorkey((255, 255, 255))
                spin_walk_cooldown = 100
        else:
            if (main_dir == sprites["player up invincible"]):
                main_dir = sprites["player up"]
            if (main_dir == sprites["player down invincible"]):
                main_dir = sprites["player down"]
            if (main_dir == sprites["player left invincible"]):
                main_dir = sprites["player left"]
            if (main_dir == sprites["player right invincible"]):
                main_dir = sprites["player right"]
            if (spin_walk_cooldown <= 0 and moved):
                player_blitscreen = pygame.transform.rotate(main_dir, randint(-5, 5))
                player_blitscreen.set_colorkey((255, 255, 255))
                spin_walk_cooldown = 100
        if (player_stats["hp"] > 100):
            player_stats["hp"] = 100
        footsteps.pos = [player_hitbox.midbottom[0], player_hitbox.midbottom[1]-20]
        dash_particle.pos = [player_hitbox.midbottom[0], player_hitbox.midbottom[1]-20]
        screen.fill("black")
        if (not current_notification == None):
             screen.blit(current_notification, notification_rect)
        sword_cooldown += clock.get_time()
        screen.blit(sprites["hud bg"], (0, 0))
        screen.blit(sprites["coin icon"], (30, 30))
        screen.blit(sprites["key icon"], (400, 30))
        screen.blit(coin_surf, (56, 35))
        screen.blit(hp_surf, (115, 35))
        screen.blit(key_surf, (420,35))
        pygame.draw.rect(screen, (219, 182,182), max_hp_rect)
        pygame.draw.rect(screen, (142, 98, 98), hp_rect)
        screen.blit(sprites["floor"], (50, 200))
        for i in wall_list:
            wall_glow = glowsurf(20, 25, 20, 70,main_color="r")
            wall_glowpos = [i.pos[0] - 10, i.pos[1] - 10]
            screen.blit(wall_glow, wall_glowpos)
        for i in animations:
            i.update(clock)
            i.draw(screen)
            if (i.lifetime <= 0):
                animations.remove(i)
        screen.blit(player_blitscreen, (player_x,player_y))
        screen.blit(sprites["wall"][1], (50,200))
        screen.blit(sprites["wall"][1], (50,400))
        screen.blit(sprites["wall"][0], (50,200))
        screen.blit(sprites["wall"][0], (520,200))
        screen.blit(glowsurf(20, 15, 30), (250, 200), special_flags=pygame.BLEND_RGB_ADD)
        screen.blit(current_torch[0], (250, 200))
        screen.blit(glowsurf(20, 15, 30), (376, 200), special_flags=pygame.BLEND_RGB_ADD)
        screen.blit(current_torch[0], (376, 200))
        screen.blit(glowsurf(20, 15, 30), (250, 400), special_flags=pygame.BLEND_RGB_ADD)
        screen.blit(current_torch[1], (250, 400))
        screen.blit(glowsurf(20, 15, 30), (376, 400), special_flags=pygame.BLEND_RGB_ADD)
        screen.blit(current_torch[1], (376, 400))
        screen.blit(glowsurf(20, 15, 30), (50,240), special_flags=pygame.BLEND_RGB_ADD)
        screen.blit(current_torch[3], (50, 240))
        screen.blit(glowsurf(20, 15, 30), (50, 368), special_flags=pygame.BLEND_RGB_ADD)
        screen.blit(current_torch[3], (50, 368))
        screen.blit(glowsurf(20, 15, 30), (527,240), special_flags=pygame.BLEND_RGB_ADD)
        screen.blit(current_torch[2], (527, 240))
        screen.blit(glowsurf(20, 15, 30), (526, 368), special_flags=pygame.BLEND_RGB_ADD)
        screen.blit(current_torch[2], (526, 368))
        if (randint(0,20) == 15):
                flame_particle_1.pos[0] = choice([250, 376, 50,50,527,526])
                flame_particle_1.pos[1] = choice([200, 200,263,368, 263,368])
                flame_particle_2.pos[0] = choice([250, 376, 50,50,527,526])
                flame_particle_2.pos[1] = choice([200, 200,263,368, 263,368])
                if (randint(0,1) == 1):
                    flame_particle_1.spawn_particle()
                elif (randint(0,1) == 0):
                    flame_particle_2.spawn_particle()
        if (sword_pause):
            sword_pause_timer += clock.get_time()
            if (sword_pause_timer >= 100):
                sword_pause_timer = 0
                sword_pause = False
        for i in dash_particle.particlelist:
            if (60 < i.lifetime <= 90):
                i.texture.set_alpha(40)
            elif (30 < i.lifetime <= 60):
                i.texture.set_alpha(30)
            elif (i.lifetime <= 30):
                i.texture.set_alpha(20)
        footsteps.setup(screen,clock)
        dash_particle.setup(screen,clock)
        for i in enemies:
            i.hitbox = i.texture.get_rect(x=i.pos[0], y=i.pos[1])
            if (i.cooldown > 0):
                i.cooldown -= clock.get_time()
            if (i.inv_frames > 0):
                i.inv_frames -= 1
                if (i.ID == [0,1]):
                    i.texture = sprites["invincible slime"]
                elif (i.ID == [0,2]):
                    i.texture = sprites["invincible corrupted golem"]
                i.texture = pygame.transform.rotate(i.texture, randint(-5, 5))
                i.texture.set_colorkey((255,255,255))
            else:
                i.update(clock)
            if (i.ID == [0,2]):
                i.state = "chase"
            i.draw(screen)
            coord_list = [player_x, player_y]
            i.old_pos = copy.deepcopy(i.pos)
            if (i.state == "patrol" and i.direction == 2):
                i.pos[1] += i.speed
                if (i.pos[1] >= 360):
                  i.direction = 0
                if (i.line_of_sight.colliderect(player_hitbox)):
                    i.state = "chase"
                    combat_text.append([sprites["alert"],[i.pos[0],i.pos[1]], 200])
            elif (i.state == "patrol" and i.direction == 0):
                i.pos[1] -= i.speed
                if (i.pos[1] <= 210):
                  i.direction = 2
                if (i.line_of_sight.colliderect(player_hitbox)):
                    i.state = "chase"
                    combat_text.append([sprites["alert"],[i.pos[0],i.pos[1]], 200])
            elif (i.state == "chase"):
                if (i.pos[0] > player_x and not i.hitbox.colliderect(wall_r_rect)):
                    i.pos[0] -= i.speed
                    i.direction = 0
                if (i.pos[0] < player_x and not i.hitbox.colliderect(wall_l_rect)):
                    i.pos[0] += i.speed
                    i.direction = 2
                if (i.pos[1] > player_y and not i.hitbox.colliderect(wall_n_rect)):
                    i.pos[1] -= i.speed
                    i.direction = 1
                if (i.pos[1] < player_x and not i.hitbox.colliderect(wall_s_rect)):
                    i.pos[1] += i.speed
                    i.direction = 3
            if (i.cooldown <= 0 and i.state == "chase" and i.ID == [0,2] and not i.inv_frames > 0):
                i.cooldown = 1500
                enemy_attack = True
                enemy_projectiles.append(classes.enemy.Projectile(sprites["stomp"], 0, 0, i.dmg, 100, [i.hitbox.bottomleft[0], i.hitbox.bottomleft[1]-30]))
            if (i.cooldown <= 0 and i.state == "chase" and i.ID == [0,1] and not i.inv_frames > 0):
                i.cooldown = 1000
                enemy_attack = True
                if (i.direction == 0):
                    enemy_projectiles.append(classes.enemy.Projectile(sprites["slimeball"], 0, -5, i.dmg, 5000, [i.pos[0], i.pos[1]]))
                elif (i.direction == 1):
                    enemy_projectiles.append(classes.enemy.Projectile(sprites["slimeball"], -5, 0, i.dmg, 5000, [i.pos[0], i.pos[1]]))
                elif (i.direction == 2):
                    enemy_projectiles.append(classes.enemy.Projectile(sprites["slimeball"], 0, 5, i.dmg, 5000, [i.pos[0], i.pos[1]]))
                elif (i.direction == 3):
                    enemy_projectiles.append(classes.enemy.Projectile(sprites["slimeball"], 5, 0, i.dmg, 5000, [i.pos[0], i.pos[1]]))
            if (sword_pause):
                if (i.hitbox.colliderect(sword_rect) and i.inv_frames <= 0):
                    screenshake_duration = 100
                    if (not i.state == "chase"):
                        i.state = "chase"
                    if (randint(0, 10) == 10):
                        damage = player_stats["attack"]*2 
                        i.hp -= damage
                        combat_text.append([combat_text_font.render("Critical Hit!", True, (255, 15, 15)),[i.pos[0],i.pos[1]], 500])
                    else:
                        damage = player_stats["attack"]
                        i.hp -= damage
                        combat_text.append([combat_text_font.render(f"-{damage} HP", True, (255, 15, 15)),[i.pos[0],i.pos[1]], 500])
                    i.inv_frames = 15
                    current_notification = notification_font.render("You damaged an enemy",True, (127,98,98))
                    notification_rect = current_notification.get_rect(midtop=(200, 450))
                    if ((main_dir == sprites["player left"] or main_dir == sprites["player left invincible"]) and not i.hitbox.colliderect(wall_r_rect)):
                        i.pos[0] -= 15
                        i.direction = 0
                    if ((main_dir == sprites["player right"] or main_dir == sprites["player right invincible"]) and not i.hitbox.colliderect(wall_l_rect)):
                        i.pos[0] += 15
                        i.direction = 2
                    if ((main_dir == sprites["player up"] or main_dir == sprites["player up invincible"]) and not i.hitbox.colliderect(wall_n_rect)):
                        i.pos[1] -= 15
                        i.direction = 1
                    if ((main_dir == sprites["player down"] or main_dir == sprites["player down invincible"]) and not i.hitbox.colliderect(wall_s_rect)):
                        i.pos[1] += 15
                        i.direction = 3
                    for j in range(damage):
                        damage_particle.pos = [i.hitbox.center[0]+randint(-20,20), i.hitbox.center[1]+randint(-20,20)]
                        damage_particle.spawn_particle()
                    if (i.hp <= 0):
                        combat_text.pop()
                        sound_effects["defeat enemy"].play()
                        player_stats["gold"] += i.point_drop
                        pygame.time.delay(300)
                        combat_text.append([combat_text_font.render(f"+{i.point_drop} coins", True, (255, 196, 0)),[i.pos[0],i.pos[1]], 500])
                        animations.append(classes.animation_effect.Effect((sprites["enemy death"][1], sprites["enemy death"][2], sprites["enemy death"][3]), 500, (i.pos[0], i.pos[1])))
                        if (i.key_item == "key"):
                            combat_text.append([combat_text_font.render("+1 Key", True, (255, 196, 0)),[i.pos[0],i.pos[1]], 500])
                            if (current_room == "dungeon room 5" and player_stats["key enemies"][0]==True):
                                player_stats["keys"] += 1
                                player_stats["key enemies"][0] = False
                        animations.append(classes.animation_effect.Effect((sprites[i.corpse],), 2000, (i.pos[0], i.pos[1])))
                        enemies.remove(i)
                        current_notification = notification_font.render("You defeated an enemy",True, (127,98,98))
                        notification_rect = current_notification.get_rect(midtop=(200, 450))
        if (keys[pygame.K_SPACE] and sword_cooldown >= 470 and player_stats["current weapon"] == "sword" or sword_pause):
            if (not sword_pause):
                sound_effects["swing sword"].play()
            if (main_dir == sprites["player up"] or main_dir == sprites["player up invincible"]):
                sword_dir = sprites["sword swing"]["up"]
                if (sword_pause_timer >= 80):
                    sword_dir = sprites["sword swing2"]["up"]
                sword_coords = (player_hitbox.topleft[0], player_hitbox.topleft[1]-20)
                sword_rect = sword_dir.get_rect(x=sword_coords[0], y=sword_coords[1])
            elif (main_dir == sprites["player down"] or main_dir == sprites["player down invincible"]):
                sword_dir = sprites["sword swing"]["down"]
                if (sword_pause_timer >= 80):
                    sword_dir = sprites["sword swing2"]["down"]
                sword_coords = player_hitbox.bottomleft
                sword_rect = sword_dir.get_rect(x=sword_coords[0], y=sword_coords[1])
            elif (main_dir == sprites["player left"] or main_dir == sprites["player left invincible"]):
                sword_dir = sprites["sword swing"]["left"]
                if (sword_pause_timer >= 80):
                    sword_dir = sprites["sword swing2"]["left"]
                sword_coords = (player_hitbox.midleft[0]-20, player_hitbox.midleft[1]-20)
                sword_rect = sword_dir.get_rect(x=sword_coords[0], y=sword_coords[1])
            elif (main_dir == sprites["player right"] or main_dir == sprites["player right invincible"]):
                sword_dir = sprites["sword swing"]["right"]
                if (sword_pause_timer >= 80):
                    sword_dir = sprites["sword swing2"]["right"]
                sword_coords = (player_hitbox.midright[0]-20, player_hitbox.midright[1]-20)
                sword_rect = sword_dir.get_rect(x=sword_coords[0], y=sword_coords[1])
            sword_dir = pygame.transform.rotate(sword_dir, randint(-5,5))
            sword_dir.set_colorkey((255,255,255))
            screen.blit(sword_dir, sword_coords)
            sword_cooldown = 0
            sword_pause = True
        for i in enemy_projectiles:
            i.draw(screen)
            i.lifetime -= clock.get_time()
            i.pos[0] += i.velocity_x
            i.pos[1] += i.velocity_y
            if (i.lifetime <= 0):
                enemy_projectiles.remove(i)
            elif ((player_hitbox.colliderect(i.hitbox) or i.hitbox.colliderect(player_hitbox) or player_hitbox.contains(i.hitbox)) and invincibility_frames <= 0):
                screenshake_duration = 100
                if (randint(0,10) == 10):
                    enemy_damage = i.dmg*2
                    player_stats["hp"] -= enemy_damage
                    combat_text.append([combat_text_font.render("Critical Hit!", True, (15, 15, 255)),[i.pos[0],i.pos[1]], 500])
                else:
                    enemy_damage = i.dmg
                    player_stats["hp"] -= enemy_damage
                    combat_text.append([combat_text_font.render(f"-{enemy_damage} HP", True, (15, 15, 255)),[player_x, player_y], 500])
                for j in range(enemy_damage):
                    damage_particle.pos = [player_hitbox.center[0]+randint(-20,20), player_hitbox.center[1]+randint(-20,20)]
                    damage_particle.spawn_particle()
                pygame.event.post(pygame.event.Event(player_gothit))
                enemy_projectiles.remove(i)
                invincibility_frames = 20
                animations.append(classes.animation_effect.Effect((sprites["enemy death"][1], sprites["enemy death"][2], sprites["enemy death"][3]), 500, (i.pos[0], i.pos[1])))
                if (player_stats["hp"] <= 0 and i.texture == sprites["slimeball"]):
                     died_to = "Player was shot by a projectile"
                elif (player_stats["hp"] <= 0 and i.texture == sprites["stomp"]):
                     died_to = "Player was stomped to death" 
        for i in exits:
            if (room_dict[current_room].exits[exits.index(i)] != None and type(room_dict[current_room].exits[exits.index(i)]) != classes.room.Lock):
                 if (exits.index(i) == 0):
                      screen.blit(sprites["door"], (i[0], i[1] - 30))
                 elif (exits.index(i) == 2):
                      screen.blit(pygame.transform.rotate(sprites["door"], 90), i)
                 elif (exits.index(i) == 3):
                      screen.blit(pygame.transform.rotate(sprites["door"], 90), (i[0]-30, i[1]))
                 else:    
                      screen.blit(sprites["door"], i)
            elif (type(room_dict[current_room].exits[exits.index(i)]) == classes.room.Lock):
                if (exits.index(i) == 0):
                      screen.blit(sprites["locked door"], (i[0], i[1] - 30))
                elif (exits.index(i) == 2):
                      screen.blit(pygame.transform.rotate(sprites["door"], 90), i)
                elif (exits.index(i) == 3):
                      screen.blit(pygame.transform.rotate(sprites["locked door"], 90), (i[0]-30, i[1]))
                else:    
                      screen.blit(sprites["locked door"], i)
        for i in wall_list:
            screen.blit(i.texture, i.pos)
            if (randint(0,20) == 15):
                flame_particle_1.pos[0] = choice([i.hitbox.midleft[0], i.hitbox.midright[0], i.hitbox.center[0]])
                flame_particle_1.pos[1] = choice([i.hitbox.midleft[1], i.hitbox.midright[1], i.hitbox.center[1]])
                flame_particle_2.pos[0] = choice([i.hitbox.midleft[0], i.hitbox.midright[0], i.hitbox.center[0]])
                flame_particle_2.pos[1] = choice([i.hitbox.midleft[1], i.hitbox.midright[1], i.hitbox.center[1]])
                if (randint(0,1) == 1):
                    flame_particle_1.spawn_particle()
                elif (randint(0,1) == 0):
                    flame_particle_2.spawn_particle()
            if (i.hitbox.colliderect(player_hitbox)):
                 direction_of_collide = checkfor_collision_dir(i, player_x, player_y)
                 if (direction_of_collide == "up"):
                    player_y = i.hitbox.bottom
                 if (direction_of_collide == "down"):
                    player_y = i.hitbox.top - 50
                 if (direction_of_collide == "left"):
                    player_x = i.hitbox.midright[0]
                 if (direction_of_collide == "right"):
                    player_x = i.hitbox.midleft[0] - 50
            for j in enemies:
                if (i.hitbox.colliderect(j.hitbox)):
                 direction_of_collide = checkfor_collision_dir(i, j.pos[0], j.pos[1])
                 if (direction_of_collide == "up"):
                    j.pos[1] = i.hitbox.bottom
                 if (direction_of_collide == "down"):
                    j.pos[1] = i.hitbox.top - 50
                 if (direction_of_collide == "left"):
                    j.pos[0] = i.hitbox.midright[0]
                 if (direction_of_collide == "right"):
                    j.pos[0] = i.hitbox.midleft[0] - 50
        for i in pot_list:
            screen.blit(i.texture, i.pos)
            if (i.hitbox.colliderect(player_hitbox)):
                 direction_of_collide = checkfor_collision_dir(i, player_x, player_y)
                 if (direction_of_collide == "up"):
                    player_y = i.hitbox.bottom
                 if (direction_of_collide == "down"):
                    player_y = i.hitbox.top - 50
                 if (direction_of_collide == "left"):
                    player_x = i.hitbox.midright[0]
                 if (direction_of_collide == "right"):
                    player_x = i.hitbox.midleft[0] - 50
            for j in enemies:
                if (i.hitbox.colliderect(j.hitbox)):
                 direction_of_collide = checkfor_collision_dir(i, j.pos[0], j.pos[1])
                 if (direction_of_collide == "up"):
                    j.pos[1] = i.hitbox.bottom
                 if (direction_of_collide == "down"):
                    j.pos[1] = i.hitbox.top - 50
                 if (direction_of_collide == "left"):
                    j.pos[0] = i.hitbox.midright[0]
                 if (direction_of_collide == "right"):
                    j.pos[0] = i.hitbox.midleft[0] - 50
            if (sword_pause and i.hitbox.colliderect(sword_rect)):
                animations.append(classes.animation_effect.Effect((sprites["enemy death"][1], sprites["enemy death"][2], sprites["enemy death"][3]), 500, (i.pos[0], i.pos[1])))
                sound_effects["defeat enemy"].play()
                drop = choice(i.drops)
                if (drop != None and drop[0] == "coins"):
                    player_stats["gold"] += drop[1]
                    combat_text.append([combat_text_font.render(f"+{drop[1]} coins", True, (255, 196, 0)),[i.pos[0],i.pos[1]], 500])
                pot_list.remove(i)
        for i in combat_text:
            screen.blit(i[0], i[1])
            i[1][1] -= 2
            i[2] -= clock.get_time()
            if (i[2] <= 0):
                combat_text.remove(i)
        flame_particle_1.setup(screen,clock)
        flame_particle_2.setup(screen,clock)
        damage_particle.setup(screen,clock)
        if (player_stats["hp"] <= 0):
            pygame.event.post(pygame.event.Event(player_death))
        if (invincibility_frames > 0):
             invincibility_frames = invincibility_frames - 1
        if (screenshake_duration > 0):
            screenshake()
        if (pygame.mouse.get_focused()):
             screen.blit(sprites["cursor"], cursor_rect)
        if (not pygame.mixer.music.get_busy()):
            if (current_music == music[0]):
                current_music = music[2]
            elif (current_music == music[2]):
                current_music = music[3]
            elif (current_music == music[3]):
                current_music = music[4]
            elif (current_music == music[4]):
                current_music = music[0]
            play_music(current_music, False)
        screen.blit(dark_surf, (0,0))
        pygame.display.update()
        if (transition):
            fade2()
            transition = False
        clock.tick(60)
        moved = False
#--------------------
def fade():
    current_screen = screen.copy()
    surf = pygame.Surface((600,600))
    surf.fill("black")
    surf.set_alpha(0)
    alpha = 0
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
        alpha += 8
        if (alpha >= 255):
            break
        surf.set_alpha(alpha)
        screen.blit(current_screen, (0,0))
        screen.blit(surf,(0,0))
        pygame.display.update()
        clock.tick(60)
#--------------------
def fade2():
    current_screen = screen.copy()
    surf = pygame.Surface((600,600))
    surf.fill("black")
    surf.set_alpha(255)
    alpha = 255
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
        alpha -= 8
        if (alpha <= 0):
            break
        surf.set_alpha(alpha)
        screen.blit(current_screen, (0,0))
        screen.blit(surf,(0,0))
        pygame.display.update()
        clock.tick(60)
#--------------------
def gameloop():
    while True:
        title()
        fade()
        game()
#--------------------