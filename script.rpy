init:
    $ locpos = Position (xpos = 917,ypos = 411)
    $ mmpos = Position (xpos = 1122,ypos = 696)




style action_button_text:
    #idle_color "#17F180"
    idle_color "#00E000"
    #hover_color "#FFFFAA"
    hover_color "#FFFF99"
    insensitive_color "#79796a"
    
#style status_screen_text:
    #color "#00E000"



# Настройки
#define narrator = nvl_narrator
#define dismiss_pause = False
$_dismiss_pause = False
define config.hard_rollback_limit = 0
define config.allow_skipping = False





# Переменные состояния

define hp = 100             # Здоровье
define maxhp = 100
define hp_displayed = 0

define ep = 100             # Энергия, стамина
define maxep = 100
define ep_displayed = 0

define hunger = 100         # Голод
define maxhunger = 100 
define hunger_displayed = 0

define thirst = 100         # Жажда
define maxthirst = 100 
define thirst_displayed = 0

define radiation = 0        # Облучение, радиация
define maxradiation = 100
define radiation_displayed = 0

define weight_total = 0


define bleeding = 0         # Кровотечение   
define intoxication = 0     # Интоксикация, отравление
define wet = 0              # Степени промокания
define cold = 0             # Холод    
define heat = 0             # Жара
define disease = 0          # Болезнь
define pain = 0             # Боль

define shock = 0            # Шок, оглушение
define coma = 0             # Кома
define drunk = 0            # Опьянение
define barefoot = False     # Босой
define naked = False        # Голый


define action_numb = 1      # Нумерация вариантов действий 

define character_status = ""    
define hp_status = ""
define ep_status = ""
define hunger_status = ""
define thirst_status = ""

define radiation_status = ""
define bleeding_status = ""
define intoxication_status = ""
define wet_status = ""
define cold_status = ""
define heat_status = "" 
define disease_status = ""
define pain_status = ""


# Переменные предметов
define money = 0
define foundmoney = 0
define crabone = 0
define foundcrab = 0
define cookedcrab = 0



# Переменные событий
define wolfattack = False
define wolfattack_chance = 0
define chestfound = False
define chestfound_chance = 0
define chestopened = False
define mapfound = False
define rain = False
define rain_chance = 0
define campfire = False
define campfirelife = 0



#Переменные времени

define daytime = "day"

define time_in_minutes = 720
define total_hours = time_in_minutes/60
define day = total_hours/24
define hours = total_hours%24
define minutes = time_in_minutes%60
define month = day/28




image bgd:
    "images/bgd1.png"
    pause 0.15
    "images/bgd2.png"
    pause 0.15
    "images/bgd3.png"
    pause 0.15
    "images/bgd4.png"
    pause 0.15
    "images/bgd5.png"
    pause 0.15
    "images/bgd6.png"
    pause 0.15
    "images/bgd7.png"
    pause 0.15
    "images/bgd8.png"
    pause 0.15
    "images/bgd9.png"
    pause 0.15
    "images/bgd10.png"
    pause 0.15
    "images/bgd11.png"
    pause 0.15
    "images/bgd12.png"
    pause 0.15
    "images/bgd13.png"
    repeat
    
image bgd2:
    "images/bgd2-1.png"
    pause 0.15
    "images/bgd2-2.png"
    pause 0.15
    "images/bgd2-3.png"
    pause 0.15
    "images/bgd2-4.png"
    pause 0.15
    repeat

image abg:
    "images/abg/bg01.png"
    pause 0.15
    "images/abg/bg02.png"
    pause 0.15
    "images/abg/bg03.png"
    pause 0.15
    "images/abg/bg04.png"
    pause 0.15
    "images/abg/bg05.png"
    pause 0.15
    repeat


        
screen testbar:
    #vbox xpos 848 ypos 445:
    bar: # HP
        xsize 103
        ysize 13
        value hp
        range maxhp
        xpos 848
        ypos 453
        left_bar Frame("gui/bar_hp.png")
        right_bar Frame("gui/bar_empty.png")
        #left_gutter 0
        #right_gutter 0
        thumb None
        thumb_shadow None
    
    bar: # EP
        xsize 103
        ysize 13
        value ep
        range maxep
        xpos 848
        ypos 505
        left_bar Frame("gui/bar_energy.png")
        right_bar Frame("gui/bar_empty.png")
        #left_gutter 0
        #right_gutter 0
        thumb None
        thumb_shadow None
        
    bar: # FOOD
        xsize 103
        ysize 13
        value hunger
        range maxhunger
        xpos 848
        ypos 557
        left_bar Frame("gui/bar_food.png")
        right_bar Frame("gui/bar_empty.png")
        #left_gutter 0
        #right_gutter 0
        thumb None
        thumb_shadow None
        
    bar: # WATER
        xsize 103
        ysize 13
        value thirst
        range maxthirst
        xpos 848
        ypos 609
        left_bar Frame("gui/bar_water.png")
        right_bar Frame("gui/bar_empty.png")
        #left_gutter 0
        #right_gutter 0
        thumb None
        thumb_shadow None
        
    bar: # RAD
        xsize 103
        ysize 13
        value radiation
        range maxradiation
        xpos 848
        ypos 661
        left_bar Frame("gui/bar_rad.png")
        right_bar Frame("gui/bar_empty.png")
        #left_gutter 0
        #right_gutter 0
        thumb None
        thumb_shadow None

screen minimap:
    layer "master"
    viewport:
        xpos 987 ypos 429 xysize (272, 267)
        
        xinitial 1702
        yinitial 1702
        
        draggable True
        
        add "minimap2"
        #add "gui/minimap_frame.png"

# Экраны времени

screen time_overlay:
    vbox xpos 1000 ypos 450:
        $ minutes = time_in_minutes % 60
        $ hours = (time_in_minutes / 60) % 24 
        text ("{size=35}{font=font_dc.ttf}%d:%02d{/font}{/size}" % (hours, minutes))
        
        $ day = (time_in_minutes / 60 / 24) % 28
        $ month = (time_in_minutes / 60/ 24 / 28) % 12
        text ("День %d" % (day))
        text ("Месяц %d" % (month))

screen weight_overlay:
    vbox xpos 1000 ypos 575:
        $ weight_total = 0
    
        if player_inv.qty(meat): 
            $ qty = player_inv.qty(meat)
            #$ weight = player_inv.weight(meat)
            $ weight_total = weight_total + (qty*5)
        
        text ("Вес %d" % (weight_total))


# Экраны действий

screen inv_buttons: # Значки инвентаря, торговли и хранилища
    tag inv_buttons
    #modal True
    
    imagemap:
        idle "gui/inv_buttons_idle.png"
        hover "gui/inv_buttons_hover.png"
        
        hotspot (561, 604, 100, 100) action Show("inventory_screen", first_inventory=player_inv)
        hotspot (661, 604, 100, 100) action Show("inventory_screen", first_inventory=player_inv, second_inventory=vendor_inv)
        hotspot (761, 604, 100, 100) action Show("inventory_screen", first_inventory=player_inv, second_inventory=chest, trade_mode=True, bank_mode=True) 

screen charicons:   
    tag inv_buttons
        
    imagemap:
        idle "gui/charicons2_idle.png"
        hover "gui/charicons2_hover.png"
        
        hotspot (576, 605, 73, 89) action Show("inventory_screen", first_inventory=player_inv)
        hotspot (651, 605, 73, 89) action Show("inventory_screen", first_inventory=player_inv)
        hotspot (726, 605, 73, 89) action Show("inventory_screen", first_inventory=player_inv)

            

screen chestinforest: # Значок обыска сундука
    tag forestchest
    
    imagemap:
        idle "gui/chest1.png"
        hover "gui/chest2.png"
    
        hotspot (865, 259, 50, 50) action Jump ("loc2chest")# Сундук

screen chest_open: # Действия. Сундук
    tag action
    style_prefix "action"
    key "1":
        if chestopened:
            action Call ("chestalreadypened")
        else:
            action Call ("chestmoney_chance")   
            
    key "2" action [Jump("loc2.loc2_2")]

    vbox xpos 35 ypos 440:
        textbutton "1. Обыскать сундук":
            if chestopened:
                action Call ("chestalreadypened")
            else:
                action Call ("chestmoney_chance")
        textbutton "2. Не трогать сундук" action Jump("loc2.loc2_2")


screen action_loc0: # Действия. Лагерь
    tag action   
    style_prefix "action"
    vbox xpos 35 ypos 440:
        
        $ action_numb = 1
        textbutton "[action_numb]. Отдохнуть" action Call("rest_normal_zone")keysym str(action_numb)
        $ action_numb = action_numb + 1

        textbutton "[action_numb]. Осмотреться" action Show("inventory_screen", first_inventory=player_inv, second_inventory=loc0_inv, trade_mode=True, bank_mode=False)keysym str(action_numb)
        $ action_numb = action_numb + 1 

        textbutton "[action_numb]. Зайти в дом" action Jump("loc01")keysym str(action_numb)
        $ action_numb = action_numb + 1

        textbutton "[action_numb]. Развести костер" action Call("campfire")keysym str(action_numb)
        $ action_numb = action_numb + 1
        
        $ action_numb = 1

screen action_loc1: # Действия. Поле
    tag action
    style_prefix "action"
    vbox xpos 35 ypos 440:

        $ action_numb = 1
        textbutton "[action_numb]. Отдохнуть" action Call("rest_normal_zone")keysym str(action_numb)
        $ action_numb = action_numb + 1   
        
        textbutton "[action_numb]. Осмотреться" action Show("inventory_screen", first_inventory=player_inv, second_inventory=loc1_inv, trade_mode=True, bank_mode=False)keysym str(action_numb)
        $ action_numb = action_numb + 1 
        
        $ action_numb = 1

screen action_loc2: # Действия. Лес
    tag action
    style_prefix "action"
    vbox xpos 35 ypos 440:
        
        $ action_numb = 1
        textbutton "[action_numb]. Отдохнуть" action Call("rest_normal_zone")keysym str(action_numb)
        $ action_numb = action_numb + 1         
        
        textbutton "[action_numb]. Осмотреться" action Show("inventory_screen", first_inventory=player_inv, second_inventory=loc2_inv, trade_mode=True, bank_mode=False)keysym str(action_numb)
        $ action_numb = action_numb + 1 
  
        if chestfound:
            textbutton "[action_numb]. Подойти к сундуку" action Jump("loc2chest")keysym str(action_numb)
            $ action_numb = action_numb + 1 
        else:
            pass
        
        $ action_numb = 1

screen action_loc3: # Действия. Горы
    tag action
    style_prefix "action"
    vbox xpos 35 ypos 440:
    
        $ action_numb = 1
        textbutton "[action_numb]. Отдохнуть" action Call("rest_normal_zone")keysym str(action_numb)
        $ action_numb = action_numb + 1
        
        textbutton "[action_numb]. Осмотреться" action Show("inventory_screen", first_inventory=player_inv, second_inventory=loc3_inv, trade_mode=True, bank_mode=False)keysym str(action_numb)
        $ action_numb = action_numb + 1 

        $ action_numb = 1

screen action_loc4: # Действия. Болото
    tag action
    style_prefix "action"
    vbox xpos 35 ypos 440:
        
        $ action_numb = 1
        textbutton "[action_numb]. Отдохнуть" action Call("rest_radiation_zone")keysym str(action_numb)
        $ action_numb = action_numb + 1

        textbutton "[action_numb]. Осмотреться" action Show("inventory_screen", first_inventory=player_inv, second_inventory=loc4_inv, trade_mode=True, bank_mode=False)keysym str(action_numb)
        $ action_numb = action_numb + 1 

        textbutton "[action_numb]. Искать предметы":
            if mapfound:
                action Call("notfound")keysym str(action_numb)

            else:
                action Call("map_found")keysym str(action_numb)
        $ action_numb = action_numb + 1


        $ action_numb = 1

screen action_loc01: # Действия. Дом
    tag action
    style_prefix "action"
    vbox xpos 35 ypos 440:
        
        $ action_numb = 1
        textbutton "[action_numb]. Выйти из дома" action Jump("loc0.bg")keysym str(action_numb)
        $ action_numb = action_numb + 1
        
        textbutton "[action_numb]. Спуститься в бункер" action Jump("loc0b1")keysym str(action_numb)
        $ action_numb = action_numb + 1
        
        
        $ action_numb = 1

screen action_loc0b1: # Действия. Бункер
    tag action
    style_prefix "action"
    vbox xpos 35 ypos 440:
    
        $ action_numb = 1
        textbutton "[action_numb]. Проверить радио" action Call("loc0b1radio")keysym str(action_numb)
        $ action_numb = action_numb + 1
        
        textbutton "[action_numb]. Подняться в дом" action Jump("loc01")keysym str(action_numb)
        $ action_numb = action_numb + 1
        
        textbutton "[action_numb]. Открыть хранилище" action Show("inventory_screen", first_inventory=player_inv, second_inventory=chest, trade_mode=True, bank_mode=True)keysym str(action_numb)
        $ action_numb = action_numb + 1
        
        textbutton "[action_numb]. Торговец оружием" action Show("inventory_screen", first_inventory=player_inv, second_inventory=weapon_vendor_inv)keysym str(action_numb)
        $ action_numb = action_numb + 1
        
        textbutton "[action_numb]. Торговец броней" action Show("inventory_screen", first_inventory=player_inv, second_inventory=armor_vendor_inv)keysym str(action_numb)
        $ action_numb = action_numb + 1
        
        textbutton "[action_numb]. Торговец едой" action Show("inventory_screen", first_inventory=player_inv, second_inventory=food_vendor_inv)keysym str(action_numb)
        $ action_numb = action_numb + 1
        
        
        $ action_numb = 1



# Экраны навигации

screen navigation_loc0: # Навигация. Лагерь
    tag navi
    #modal True
    
    key "K_UP":
        
        if ep <= 0:
            #"Я слишком устал для перемещения"
            action Call("exhausted")
        else:
            action [Jump ("loc3")]

    key "K_LEFT": 
        if ep <= 0:
            #"Я слишком устал для перемещения"
            action Call("exhausted")   
        else:
            action [Jump ("loc1")]
    
    key "K_RIGHT":
        if ep <= 0:
            #"Я слишком устал для перемещения"
            action Call("exhausted")   
        else:
            action [Jump ("loc2")]
            
    key "K_DOWN":
        if ep <= 0:
            #"Я слишком устал для перемещения"
            action Call("exhausted")   
        else:
            action [Jump ("loc4")]

    imagemap:
        idle "gui/navi3_idle.png"
        hover "gui/navi3_hover.png"
        
        hotspot (630, 436, 48, 48):#вверх
            if ep <= 0:
                #"Я слишком устал для перемещения"
                action Call ("exhausted")
            else:
                action Jump ("loc3")
        
        hotspot (577, 489, 48, 48):#влево
            if ep <= 0:
                #"Я слишком устал для перемещения"
                action Call ("exhausted")
            else:
                action Jump ("loc1")
                
        hotspot (683, 489, 48, 48):#вправо
            if ep <= 0:
                #"Я слишком устал для перемещения"
                action Call ("exhausted")
            else:
                action Jump ("loc2")
        
        hotspot (630, 542, 48, 48):#вниз 
            if ep <= 0:
                #"Я слишком устал для перемещения"
                action Call ("exhausted")
            else:
                action Jump ("loc4")

screen navigation_loc0b1: # Навигация. Бункер
    tag navi
    key "K_RIGHT" action [Jump ("loc0b2")]
    imagemap:
        idle "gui/navi3_right_idle.png"
        hover "gui/navi3_right_hover.png"
        
        hotspot (683, 489, 48, 48) action Jump ("loc0b2")#вправо

screen navigation_loc0b2: # Навигация. Бункер
    tag navi
    key "K_LEFT" action [Jump ("loc0b1")]
    imagemap:
        idle "gui/navi3_left_idle.png"
        hover "gui/navi3_left_hover.png"
        
        hotspot (577, 489, 48, 48) action Jump ("loc0b1")#влево

screen navigation_loc1: # Навигация. Поле
    tag navi
    
    key "K_RIGHT":
        if ep <= 0:
            action Jump ("exhausted")   
        else:
            action Jump ("loc0")

    imagemap:
        idle "gui/navi3_right_idle.png"
        hover "gui/navi3_right_hover.png"
        
        hotspot (683, 489, 48, 48):#вправо
            if ep <= 0:
                action Jump ("exhausted")
            else:
                action Jump ("loc0")

screen navigation_loc2: # Навигация. Лес
    tag navi
    
    key "K_LEFT":
        if ep <= 0:
            action Jump ("exhausted")   
        else:
            action [Jump ("loc0")]
    
    imagemap:
        idle "gui/navi3_left_idle.png"
        hover "gui/navi3_left_hover.png"
        
        hotspot (577, 489, 48, 48):#влево
            if ep <= 0:
                action Jump ("exhausted")
            else:
                action Jump ("loc0")

screen navigation_loc3: # Навигация. Горы
    tag navi
    
    key "K_DOWN":
        if ep <= 0:
            action Jump ("exhausted")   
        else:
            action [Jump ("loc0")]
    
    imagemap:
        idle "gui/navi3_down_idle.png"
        hover "gui/navi3_down_hover.png"
        
        hotspot (630, 542, 48, 48):#вниз
            if ep <= 0:
                action Jump ("exhausted")
            else:
                action Jump ("loc0")

screen navigation_loc4: # Навигация. Болото
    tag navi
    
    key "K_UP":
        if ep <= 0:
            action Jump ("exhausted")   
        else:
            action [Jump ("loc0")]
    
    imagemap:
        idle "gui/navi3_up_idle.png"
        hover "gui/navi3_up_hover.png"
        
        hotspot (630, 436, 48, 48):#вверх 
            if ep <= 0:
                action Jump ("exhausted")
            else:
                action Jump ("loc0")


screen indicators:
    tag parameters_image
    imagemap:
        idle "gui/indicators.png"
        
screen parameters_image: # Иконки параметров
    tag parameters_image
    imagemap:
        idle "gui/param.png"

screen parameters: # Значения параметров
    tag parameters
    vbox xalign 0.735 yalign 0.87:
        
        $ hp_displayed = int(hp)
        $ ep_displayed = int(ep)
        $ hunger_displayed = int(hunger)
        $ thirst_displayed = int(thirst)
        $ radiation_displayed = int(radiation)

        text "[hp_displayed]"
        null height 30
        text "[ep_displayed]"
        null height 30
        text "[hunger_displayed]"
        null height 30
        text "[thirst_displayed]"
        null height 30
        text "[radiation_displayed]"

screen location_icons:
    tag locicons
    hbox xpos 580 ypos 297:
        if campfire:
            imagebutton:
                idle "gui/campfire.png"
                action None
        else:
            pass



# Экраны статуса локации

screen status_loc0:
    #style_prefix "status"
    tag status
    vbox xpos 45 ypos 45 xsize 490:
        #fixed:
            #xsize 400 ysize 500
        
        text "{color=#47FF47}Лагерь. Стартовая точка.{/color}"
        
        #text "{color=#47FF47}Каждое свойство стиля ожидает определенный тип данных. Многие из них являются стандартными типами в Python, но некоторые из них являются новыми.{/color}"
        
        #text "{color=#47FF47}Палетка 1. Не говори мне ничего. И дай минуту мне подумать. Я пью шотландское вино.{/color}"
        
        #text "{color=#00E000}Палетка 2. Не говори мне ничего. И дай минуту мне подумать. Я пью шотландское вино.{/color}"
        
        #text "{color=#00CC00}Каждое свойство стиля ожидает определенный тип данных. Многие из них являются стандартными типами в Python, но некоторые из них являются новыми.{/color}"
        
        
        #text "[weight_total]"
        
        #text "{color=#70FF70}Палетка 2. Пытаюсь мыслями запутать. Не говори мне о любви. Которой нету в твоём сердце.{/color}"
        
        #text "{color=#1FFF1F}Палетка 3. И не зови меня своим. Ты перешла мои границы. А горький вкус твоей любви. Меня убил, теперь без сил.{/color}"
        
        #text "{color=#6AB18F}Вариант цвета текста #1. Не говори мне ничего. И дай минуту мне подумать. Я пью шотландское вино. Пытаюсь мыслями запутать {/color}"
        
        #text "{color=#C1FBC0}Вариант цвета текста #2. Не говори мне о любви. Которой нету в твоём сердце. И не зови меня своим. Ты перешла мои границы{/color}"
        
        #text "{color=#00F200}Вариант цвета текста #3. А горький вкус твоей любви. Меня убил, теперь без сил. А ты змея пустила яд. Любовный яд, а я так рад{/color}"

        #text "{color=#00CD62}Вариант цвета текста #4. Что всё прошло, а может быть. И не было и ничего. Прощай, прощай и никогда. Меня, прошу, не вспоминай{/color}"

        #text "{color=#3BFBFF}Вариант цвета текста #5. А горький вкус твоей любви. Меня убил, теперь без сил. А ты змея пустила яд. Любовный яд, а я так рад{/color}"
        
        #text "{color=#33FFAC}Вариант цвета текста #6. Что всё прошло, а может быть. И не было и ничего. Прощай, прощай и никогда. Меня, прошу, не вспоминай{/color}"
        
        #text "{color=#FFCA15}Вариант цвета текста #7. Зачем нужна твоя любовь. Когда слова твои пустые. Зачем же нужно столько лгать. Я понял всё теперь отныне{/color}"        
        
        #text "{color=#17F180}Вариант цвета текста #8. Ты уходи, ты уходи. Мне не нужна такая дура. И за слова мои прости. Ведь такова твоя натура{/color}"

        #text "{color=#00FF00}Вариант цвета текста #Фаллаут idle. Не говори мне ничего. И дай минуту мне подумать. Я пью шотландское вино. Пытаюсь мыслями запутать{/color}"
        #text "{color=#FFFFAA}Вариант цвета текста #Фаллаут hover. Не говори мне о любви. Которой нету в твоём сердце. И не зови меня своим. Ты перешла мои границы{/color}"
        #text "{color=#0CFF07}Вариант цвета текста #JA2. А горький вкус твоей любви. Меня убил, теперь без сил. А ты змея пустила яд. Любовный яд, а я так рад{/color}"
        #text "{color=#E2E3BB}Вариант цвета текста #JA2. Что всё прошло, а может быть. И не было и ничего. Прощай, прощай и никогда. Меня, прошу, не вспоминай{/color}"

        #text "{color=#9EEE58}1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30{/color}"       

        hbox:
                
            if hp >= 90 and ep >= 66 and hunger >= 75 and thirst >= 75:
                text "Я в порядке"

            else:
                $ hp_status = str(hp_status)
                $ ep_status = str(ep_status)
                $ hunger_status = str(hunger_status)
                $ thirst_status = str(thirst_status)
                $ character_status = str(character_status)
                
                if hp < 90:
                    $ character_status = character_status + hp_status
                    if ep < 66 or hunger < 75 or thirst < 75:
                        $ character_status = character_status + ', '
                    else:
                        $ character_status = character_status + '.'   
                else:
                    pass
                    
                if ep < 66:
                    $ character_status = character_status + ep_status
                    if hunger < 75 or thirst < 75:
                        $ character_status = character_status + ', '
                    else:
                        $ character_status = character_status + '.'                         
                else:
                    pass
                    
                if hunger < 75:
                    $ character_status = character_status + hunger_status
                    if thirst < 75:
                        $ character_status = character_status + ', '
                    else:
                        $ character_status = character_status + '.'               
                else:
                    pass
                    
                if thirst < 75:
                    $ character_status = character_status + thirst_status + '.'
                else: 
                    pass
                
                text "Я [character_status]"
                $ character_status = ""
        text "Время суток - [daytime]"
        
        
screen status_loc1:
    tag status
    vbox xpos 35 ypos 35 xsize 500:
        
        text "Поле. Локация слева от лагеря."
        
        hbox:
                
            if hp >= 90 and ep >= 66 and hunger >= 75 and thirst >= 75:
                text "Я в порядке"

            else:
                $ hp_status = str(hp_status)
                $ ep_status = str(ep_status)
                $ hunger_status = str(hunger_status)
                $ thirst_status = str(thirst_status)
                $ character_status = str(character_status)
                
                if hp < 90:
                    $ character_status = character_status + hp_status
                    if ep < 66 or hunger < 75 or thirst < 75:
                        $ character_status = character_status + ', '
                    else:
                        $ character_status = character_status + '.'   
                else:
                    pass
                    
                if ep < 66:
                    $ character_status = character_status + ep_status
                    if hunger < 75 or thirst < 75:
                        $ character_status = character_status + ', '
                    else:
                        $ character_status = character_status + '.'                         
                else:
                    pass
                    
                if hunger < 75:
                    $ character_status = character_status + hunger_status
                    if thirst < 75:
                        $ character_status = character_status + ', '
                    else:
                        $ character_status = character_status + '.'               
                else:
                    pass
                    
                if thirst < 75:
                    $ character_status = character_status + thirst_status + '.'
                else: 
                    pass
                
                text "Я [character_status]"
                $ character_status = ""
               
        if rain:
            text "Сейчас идет дожль"
        else:
            pass

screen status_loc2:
    tag status
    vbox xpos 35 ypos 35 xsize 500:
        
        text "Лес. Локация справа от лагеря."

        hbox:
                
            if hp >= 90 and ep >= 66 and hunger >= 75 and thirst >= 75:
                text "Я в порядке"

            else:
                $ hp_status = str(hp_status)
                $ ep_status = str(ep_status)
                $ hunger_status = str(hunger_status)
                $ thirst_status = str(thirst_status)
                $ character_status = str(character_status)
                
                if hp < 90:
                    $ character_status = character_status + hp_status
                    if ep < 66 or hunger < 75 or thirst < 75:
                        $ character_status = character_status + ', '
                    else:
                        $ character_status = character_status + '.'   
                else:
                    pass
                    
                if ep < 66:
                    $ character_status = character_status + ep_status
                    if hunger < 75 or thirst < 75:
                        $ character_status = character_status + ', '
                    else:
                        $ character_status = character_status + '.'                         
                else:
                    pass
                    
                if hunger < 75:
                    $ character_status = character_status + hunger_status
                    if thirst < 75:
                        $ character_status = character_status + ', '
                    else:
                        $ character_status = character_status + '.'               
                else:
                    pass
                    
                if thirst < 75:
                    $ character_status = character_status + thirst_status + '.'
                else: 
                    pass
                
                text "Я [character_status]"
                $ character_status = ""
        
        if chestfound:
            text "Я нашел в этой локации сундук."
        else:
            pass

screen status_loc3:
    tag status
    vbox xpos 35 ypos 35 xsize 500:
        
        text "Горы. Локация сверху от лагеря."

        hbox:
                
            if hp >= 90 and ep >= 66 and hunger >= 75 and thirst >= 75:
                text "Я в порядке"

            else:
                $ hp_status = str(hp_status)
                $ ep_status = str(ep_status)
                $ hunger_status = str(hunger_status)
                $ thirst_status = str(thirst_status)
                $ character_status = str(character_status)
                
                if hp < 90:
                    $ character_status = character_status + hp_status
                    if ep < 66 or hunger < 75 or thirst < 75:
                        $ character_status = character_status + ', '
                    else:
                        $ character_status = character_status + '.'   
                else:
                    pass
                    
                if ep < 66:
                    $ character_status = character_status + ep_status
                    if hunger < 75 or thirst < 75:
                        $ character_status = character_status + ', '
                    else:
                        $ character_status = character_status + '.'                         
                else:
                    pass
                    
                if hunger < 75:
                    $ character_status = character_status + hunger_status
                    if thirst < 75:
                        $ character_status = character_status + ', '
                    else:
                        $ character_status = character_status + '.'               
                else:
                    pass
                    
                if thirst < 75:
                    $ character_status = character_status + thirst_status + '.'
                else: 
                    pass
                
                text "Я [character_status]"
                $ character_status = ""

screen status_loc4:
    tag status
    vbox xpos 35 ypos 35 xsize 500:
        
        text "Болото. Локация снизу от лагеря."

        hbox:
                
            if hp >= 90 and ep >= 66 and hunger >= 75 and thirst >= 75:
                text "Я в порядке"

            else:
                $ hp_status = str(hp_status)
                $ ep_status = str(ep_status)
                $ hunger_status = str(hunger_status)
                $ thirst_status = str(thirst_status)
                $ character_status = str(character_status)
                
                if hp < 90:
                    $ character_status = character_status + hp_status
                    if ep < 66 or hunger < 75 or thirst < 75:
                        $ character_status = character_status + ', '
                    else:
                        $ character_status = character_status + '.'   
                else:
                    pass
                    
                if ep < 66:
                    $ character_status = character_status + ep_status
                    if hunger < 75 or thirst < 75:
                        $ character_status = character_status + ', '
                    else:
                        $ character_status = character_status + '.'                         
                else:
                    pass
                    
                if hunger < 75:
                    $ character_status = character_status + hunger_status
                    if thirst < 75:
                        $ character_status = character_status + ', '
                    else:
                        $ character_status = character_status + '.'               
                else:
                    pass
                    
                if thirst < 75:
                    $ character_status = character_status + thirst_status + '.'
                else: 
                    pass
                
                text "Я [character_status]"
                $ character_status = ""


 
#Блоки локаций

label start: 
    
    ## If using the crafting feature, add an empty cookbook list after start to keep track of recipes
    $ cookbook = list() 
   
    ######### DEFINE INVENTORIES ##########    
    $ player_inv = Inventory("Персонаж [weight_total]")
    
    $ loc0_inv = Inventory("Предметы в секторе")
    $ loc1_inv = Inventory("Предметы в секторе")
    $ loc2_inv = Inventory("Предметы в секторе")
    $ loc3_inv = Inventory("Предметы в секторе")
    $ loc4_inv = Inventory("Предметы в секторе")
    
    ######### DEFINE ITEM OBJECTS ##########
    ### The format is name, description, icon image (if applicable), value (if applicable, selling/buying value), action (screen language action to be performed when icon is clicked on inventory screen), and recipe (if craftable).
    
    ### Items without icons are created like this:      
    #$ quarter = Item("Quarter", "A new quarter)
    
    ### Items with icons are created like this:
    $ eye = Item(name="Eyeball", desc="A human eyeball, how creepy!", icon="images/eye.png", value=250, weight=5)

    # Items that can be used in crafting
    $ meat = Item("meat", "meat", "images/meat.png", 15, 5, act=Show("inventory_popup", message="Используется для приговлении пищи"))
    
    $ ak = Item("ak", "АК", "images/ak.png", 500, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ ak74m = Item("ak74m", "АК74м", "images/74m.png", 600, act=Show("inventory_popup", message="Может быть экипирован"))
    $ ak74m2 = Item("ak74m2", "АК74м2", "images/ak2.png", 600, act=Show("inventory_popup", message="Может быть экипирован"))
    $ ak74m3 = Item("ak74m3", "АК74м3", "images/ak3.png", 600, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ ppsh41 = Item("ppsh41", "ppsh41", "images/ppsh41.png", 300, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ sks = Item("sks", "sks", "images/sks.png", 300, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ mosin = Item("mosin", "mosin", "images/mosin.png", 250, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ knife = Item("knife", "knife", "images/knife.png", 100, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ pkm = Item("pkm", "pkm", "images/pkm.png", 650, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ axe = Item("axe", "axe", "images/axe.png", 100, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ dbshotgun = Item("dbshotgun", "dbshotgun", "images/dbshotgun.png", 150, act=Show("inventory_popup", message="Может быть экипирован"))

    $ rpk74m = Item("rpk74m", "rpk74m", "images/rpk74m.png", 500, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ toz34 = Item("toz34", "toz34", "images/toz34.png", 200, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ tt = Item("tt", "tt", "images/tt.png", 125, act=Show("inventory_popup", message="Может быть экипирован"))

    $ gorka = Item("gorka", "gorka", "images/gorka.png", 150, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ bag = Item("bag", "bag", "images/bag.png", 75, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ gasmask = Item("gasmask", "gasmask", "images/gasmask.png", 50, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ ushanka = Item("ushanka", "ushanka", "images/ushanka.png", 35, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ grenade = Item("grenade", "grenade", "images/grenade.png", 50, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ flashlight = Item("flashlight", "flashlight", "images/flashlight.png", 25, act=Show("inventory_popup", message="Может быть экипирован"))
    
    $ bandage = Item("bandage", "bandage", "images/bandage.png", 25, act=Show("inventory_popup", message="Снимает кровотечение"))
    
    $ medkit = Item("medkit", "medkit", "images/medkit.png", 50, act=Show("inventory_popup", message="Восстанавливает здоровье"))
    
    $ multitool = Item("multitool", "multitool", "images/multitool.png", 50, act=Show("inventory_popup", message="Инструмент"))
    
    $ doorkey = Item("doorkey", "doorkey", "images/doorkey.png", 1, act=Show("inventory_popup", message="Квестовый предмет"))
    
    $ akmag = Item("akmag", "akmag", "images/akmag.png", 10, act=Show("inventory_popup", message="Амуниция"))
    
    $ pistolmag = Item("pistolmag", "pistolmag", "images/pistolmag.png", 5, act=Show("inventory_popup", message="Амуниция"))
    
    $ cal12 = Item("cal12", "cal12", "images/cal12.png", 3, act=Show("inventory_popup", message="Амуниция"))
    
    $ akammo = Item("akammo", "akammo", "images/akammo.png", 5, act=Show("inventory_popup", message="Амуниция"))
    
    $ pils = Item("pils", "pils", "images/pils.png", 75, act=Show("inventory_popup", message="Антибиотики"))
    
    $ meattin = Item("meattin", "meattin", "images/meattin.png", 10, act=Show("inventory_popup", message="Еда"))
    
    $ waterbottle = Item("waterbottle", "waterbottle", "images/waterbottle.png", 7, act=Show("inventory_popup", message="Бутылка воды"))
    
    $ chocolate = Item("chocolate", "chocolate", "images/chocolate.png", 15, act=Show("inventory_popup", message="Шоколад"))
    
    #$ canteen = Item("canteen", "canteen", "images/canteen.png", 25, act=Show("inventory_popup", message="Фляга"), recipe=[[akammo,3],[cal12,2]])
    $ canteen = Item("canteen", "canteen", "images/canteen.png", 25, act=Show("inventory_popup", message="Фляга"))
    
    $ crab = Item("crab", "crab", "images/crab.png", 5, act=Show("inventory_popup", message="Краб!"))
    
    
    $ player_inv.take(crab,1)
    $ player_inv.take(ak74m2,1)
    $ player_inv.take(ak74m3,1)
    
    $ player_inv.money = 5000  
    $ vendor_inv = Inventory("Торговец", 500, 75)
    $ vendor_inv.take(akammo,500)
    $ vendor_inv.take(cal12,100)
    $ vendor_inv.take(medkit,25)
     
    
    $ weapon_vendor_inv = Inventory("Торговец оружием", 2500, 75)
    $ weapon_vendor_inv.take(ak,2) 
    $ weapon_vendor_inv.take(akammo,500)
    $ weapon_vendor_inv.take(akmag,25) 
    $ weapon_vendor_inv.take(cal12,150)
    $ weapon_vendor_inv.take(ak74m)
    $ weapon_vendor_inv.take(dbshotgun)
    $ weapon_vendor_inv.take(grenade,2)
    $ weapon_vendor_inv.take(mosin,2) 
    $ weapon_vendor_inv.take(pistolmag,10) 
    $ weapon_vendor_inv.take(pkm)
    $ weapon_vendor_inv.take(ppsh41,3)
    $ weapon_vendor_inv.take(rpk74m) 
    $ weapon_vendor_inv.take(sks,2) 
    $ weapon_vendor_inv.take(toz34,2)
    $ weapon_vendor_inv.take(tt,2)
    
    
    $ armor_vendor_inv = Inventory("Торговец броней", 1500, 75)
    $ armor_vendor_inv.take(ushanka,3) 
    $ armor_vendor_inv.take(gorka,2) 
    $ armor_vendor_inv.take(gasmask,2)
    $ armor_vendor_inv.take(bag)

    $ food_vendor_inv = Inventory("Торговец едой", 1000, 75)
    $ food_vendor_inv.take(chocolate,15) 
    $ food_vendor_inv.take(meattin,30)
    $ food_vendor_inv.take(waterbottle,50)
    
    
    
    $ chest = Inventory("Хранилище")    
    $ chest.take(akammo,100)
    $ chest.take(akmag,5)
    $ chest.take(axe, 2)
    $ chest.take(bag)
    $ chest.take(bandage,5)
    $ chest.take(cal12,25)   
    $ chest.take(ak) 
    $ chest.take(ak74m) 
    $ chest.take(canteen) 
    $ chest.take(chocolate,3) 
    $ chest.take(dbshotgun) 
    $ chest.take(doorkey) 
    $ chest.take(flashlight) 
    $ chest.take(gasmask) 
    $ chest.take(gorka) 
    $ chest.take(grenade,2) 
    $ chest.take(knife) 
    $ chest.take(meattin,10) 
    $ chest.take(medkit,5) 
    $ chest.take(mosin) 
    $ chest.take(multitool) 
    $ chest.take(pils,3) 
    $ chest.take(pistolmag,3) 
    $ chest.take(pkm) 
    $ chest.take(ppsh41) 
    $ chest.take(rpk74m) 
    $ chest.take(sks) 
    $ chest.take(toz34) 
    $ chest.take(tt) 
    $ chest.take(ushanka) 
    $ chest.take(waterbottle,10)
    $ chest.take(meat,25)
    
    
    
    
    #show screen overlay    
    
    jump loc0.bg
    return

label loc0: # Лагерь. Стартовая точка. Метка входа
    call transition_state from _call_transition_state
    stop music
    call check from _call_check
    #call check_death
    #call time_calculation
    hide screen forestchest    
label .bg:
    
    #scene black
    
    scene black
    
    show screen minimap
    
    show tbg
    #show minimap at mmpos behind tbg
    if daytime == "day":
        show loc 0 day at locpos behind tbg
    elif daytime == "middle":
       show loc 0 middle at locpos behind tbg
    elif daytime == "night":
        show loc 0 night at locpos behind tbg
    else:
        pass
    
    #show loc 0 at locpos behind tbg # loc - тэг, изображение сменяет другие с таким же тэгом
    with Dissolve (0.5)
    
    show screen weight_overlay
    
    #show screen parameters
    
    #show minimap at mmpos behind tbg
    #show minimap behind tbg:
    #show minimap behind tbg:
        #xanchor 1122 yanchor 696
        #xpos 1122 ypos 696
        #around (108, 108)
    
    #with fade   
label .loc: # Лагерь. Локальная метка
    $_dismiss_pause = False
    call check from _call_check_1
    show screen time_overlay
    show screen charicons
    #show screen inv_buttons
    show screen status_loc0
    show screen testbar

    #with Dissolve (0.5)
    
    
    
    #show minimap at mmpos behind tbg
    #show minimap behind tbg:
    #show minimap:
        #xanchor 987 yanchor 428
        #xpos 0 ypos 0
        
        #xpos 108 ypos 108
        
        
        #around (108, 108)
    
    #show screen minimap 
    
    
    
    #show bgd
    #show loc002 at locpos behind bgd with Dissolve (0.5)
    #show bgd2
    
    hide screen location_icons
    show screen location_icons
    
    show screen testbar
    show screen indicators
    
    #show screen parameters_image
    #show screen parameters
    show screen navigation_loc0
    show screen action_loc0
    

    pause 5
    $ time_in_minutes += 1
    call cycle_state from _call_cycle_state
    jump .loc
    return

label loc01: # Дом
    scene loc01 with Dissolve(0.5)
    hide screen navi
    show screen action_loc01
    
    hide screen status
    "Дом. Отсюда я могу спуститься в бункер."
    call screen action_loc01
    return

label notfound: # Предметов не найдено
    
    hide screen status
    "Предметов не найдено"

    return

label loc0b1: # Бункер
    scene loc0b1 with Dissolve(0.5)
    show screen navigation_loc0b1
    show screen action_loc0b1
    
    hide screen status
    "Бункер."
    call screen navigation_loc0b1
    return

label loc0b2: # Бункер
    scene loc0b2 with Dissolve(0.5)
    hide screen action
    show screen navigation_loc0b2
    
    hide screen status
    "Бункер."
    call screen navigation_loc0b2
    return

label loc0b1radio:
    
    hide screen status
    "Радио не работает"
    jump loc0b1
    return

label loc1: # Поле. Метка входа
    call transition_state from _call_transition_state_1
    stop music
    call check from _call_check_2
    call rain_chance from _call_rain_chance
    if rain:
        play music "audio/rain.wav" fadein 3.5
label .bg:
    
    #scene black
    show tbg
    show loc 1 at locpos behind tbg 
    #with fade
    with Dissolve (0.5)
label .loc: # Поле. Локальная метка
    $_dismiss_pause = False
    call check from _call_check_3
    show screen status_loc1
    
    #scene tbg with fade
    #show loc012 at locpos behind tbg 
    #with Dissolve (0.5)
    #scene loc1 with Dissolve(0.5)
    show screen navigation_loc1
    show screen action_loc1

    
    pause 5
    $ time_in_minutes += 1
    jump .loc
    call screen navigation_loc1
    return



label loc2: # Лес. Метка входа
    call transition_state from _call_transition_state_2
    stop music
    call check from _call_check_4
    play music "audio/forest.mp3" fadein 10
label .bg:

    #scene black
    show tbg
    show loc 2 at locpos behind tbg 
    #with fade
    with Dissolve (0.5)
label .loc2_2:  # Лес. Метка ивента
    
    #scene tbg with fade
    #show loc022 at locpos behind tbg 
    #with Dissolve (0.5)
    #scene loc2 with Dissolve(0.5)
    show screen navigation_loc2
    show screen action_loc2
    
    if mapfound:
        $ chestfound = True
    if chestfound:
        show screen chestinforest
    else:
        call chestfound_chance from _call_chestfound_chance      
        if chestfound:
            show screen chestinforest
label .loc: # Лес. Локальная метка
    $_dismiss_pause = False
    show screen status_loc2
    call check from _call_check_5
    
    pause 5
    $ time_in_minutes += 1
    jump .loc
    call screen navigation_loc2
    return


label loc2chest: # Сундук в лесу
    hide screen forestchest
    hide screen navi
    show screen chest_open
    scene loc2_2 with Dissolve(0.5)
    
    if chestopened:
        hide screen status
        "Сундук. Я уже обыскал его."
    else:
        hide screen status
        "Сундук. Имеет смысл открыть его."
    call screen chest_open
    return



label loc3: # Горы. Метка входа
    call transition_state from _call_transition_state_3
    stop music
    call check from _call_check_6
    play music "audio/mountain.mp3" fadein 10

label .bg:
    #scene black
    show tbg
    show loc 3 at locpos behind tbg 
    #with fade
    with Dissolve (0.5)
label .loc: # Горы. Локальная метка
    $_dismiss_pause = False
    call check from _call_check_7
    
    #scene tbg with fade
    #show loc032 at locpos behind tbg 
    #with Dissolve (0.5)
    
    #scene loc3 with Dissolve(0.5)
    show screen status_loc3
    
    show screen navigation_loc3
    show screen action_loc3
    call wolfattack_chance from _call_wolfattack_chance
    
    pause 5
    $ time_in_minutes += 1
    jump .loc
    call screen navigation_loc3
    return



label loc4: # Болото. Метка входа
    call transition_state from _call_transition_state_4
    stop music
    call check from _call_check_8
    play music "audio/radiation.mp3" fadein 10
    
    #scene tbg with fade
    #show loc042 at locpos behind tbg 
    #with Dissolve (0.5)
label .bg:
    
    #scene black
    show tbg 
    show loc 4 at locpos behind tbg 
    #with fade
    with Dissolve (0.5)
label .loc_cycle: # Метка цикла
    $ radiation += 1
label .loc: # Болото. Локальная метка
    $_dismiss_pause = False
    call check from _call_check_9
    
    #show tbg
    #show loc042 at locpos behind tbg with Dissolve (0.5)
    
    #scene loc4 with Dissolve(0.5)
    show screen status_loc4
    show screen action_loc4
    show screen navigation_loc4
    
    pause 5
    $ time_in_minutes += 1
    jump .loc_cycle
    call screen navigation_loc4
    return



# Блоки механик и состояний

label map_found: # Уведомление о найденной карте
    
    $ mapfound = True
    show screen action_loc4
    hide screen status
    "Найдена карта сундука!"
    
    return

label rain_chance: # Расчет вероятности дождя (33%)
    
    $ rain_chance = renpy.random.randint(1,100)
    
    if rain_chance <= 33:
        $ rain = False
    
    if rain_chance >= 34:
        $ rain = True
    
    return

label chestfound_chance: # Расчет вероятности обнаружения сундука
    
    $ chestfound_chance = renpy.random.randint(1,100)
    
    if chestfound_chance <= 50:
        $ chestfound = False
    
    if chestfound_chance >= 51:
        $ chestfound = True
        show screen chestinforest
        hide screen status
        "Найден сундук!"

    return

label chestmoney_chance: # Расчет найденных монет и крабов

    $ foundmoney = renpy.random.randint(1500,2000)
    $ player_inv.money = player_inv.money + foundmoney
    
    $ foundcrab = renpy.random.randint(1,10)
    $ qty = foundcrab 
    $ player_inv.take(crab,qty)
    
    $ chestopened = True
    hide screen status
    "Я нашел [foundmoney] монет и [foundcrab] крабов!"
    
    return

label wolfattack_chance: # Расчет вероятности нападения волков
    if player_inv.qty(meat):
        $ qty = player_inv.qty(meat)
        
        if qty <= 5:
            $ wolfattack_chance = renpy.random.randint(1,100)
            if wolfattack_chance <= 33:
                $ wolfattack = True
            if wolfattack_chance > 34:
                $ wolfattack = False

        if qty >= 6:
            $ wolfattack_chance = renpy.random.randint(1,100)
            if wolfattack_chance <= 90:
                $ wolfattack = True
            if wolfattack_chance >= 91:
                $ wolfattack = False
    else:
         $ wolfattack = False
    
    if wolfattack:
        jump wolfattack
    else:
        pass
    
    return
    
label wolfattack: # Нападение волков
    
    $ wolfattack = False
    hide screen status
    "Похоже, что запах мяса привлек диких животных."
    
    
    return

label campfire: # Разведение костра
    $ campfire = True
    $ campfirelife = time_in_minutes + 90
    
    hide screen status
    "Костер горит!"
    
    return

label chestalreadypened: # Уведомление о том, что сундук уже открыт
    
    hide screen status
    show screen chest_open
    "Сундук уже пуст."
    call screen chest_open
    
    return

label transition_state: # Изменение состояния при переходе
    
    $ time_in_minutes += 83

    if hp <=0:
        call death from _call_death
    else:
        pass

    $ ep -= 5
    if ep < 0:
        $ ep = 0
    else:
        pass
        
    $ hunger -= 3
    if hunger < 0:
        $ hp -= 1
        $ hunger = 0
    else:
        pass
        
    $ thirst -= 3
    if thirst < 0:
        $ hp -= 1
        $ thirst = 0
    else:
        pass
        
    if radiation > 33:
        $ hp -= 1
    if radiation > 66:
        $ hp -= 25
    if radiation > 100:
        $ hp -= 50
        $ radiation = 100
    else:
        pass
        
    return

label rest_normal_zone: # Изменение состояния при отдыхе в нормальной зоне
    
    $ time_in_minutes += 61
    
    if hp <= 0:
        call death from _call_death_1
    else:
        pass

    $ ep += 25
    if ep < 0:
        $ ep = 0
    if ep > 100:
        $ ep = 100
    else:
        pass
        
    $ hunger -= 2
    if hunger < 0:
        $ hp -= 1
        $ hunger = 0
    if hunger > 100:
        $ hunger = 100
    else:
        pass
    
    $ thirst -= 2
    if thirst < 0:
        $ hp -= 1
        $ thirst = 0
    if thirst > 100:
        $ thirst = 100
    else:
        pass
    
    if radiation > 33:
        $ hp -= 1
    if radiation > 66:
        $ hp -= 25
    if radiation > 100:
        $ hp -= 50
        $ radiation = 100
    else:
        pass
    
    hide screen status
    "Я отдохнул.{nw}"
    return

label rest_radiation_zone: # Изменение состояния при отдыхе в радиоактивной зоне
    
    $ time_in_minutes += 61
    
    if hp <= 0:
        call death from _call_death_2
    else:
        pass

    $ ep += 25
    if ep < 0:
        $ ep = 0
    if ep > 100:
        $ ep = 100
    else:
        pass
    
    $ hunger -= 2
    if hunger < 0:
        $ hp -= 1
        $ hunger = 0
    if hunger > 100:
        $ hunger = 100
    else:
        pass
    
    $ thirst -= 2
    if thirst < 0:
        $ hp -= 1
        $ thirst = 0
    if thirst > 100:
        $ thirst = 100
    else:
        pass
    
    $ radiation += 10
    if radiation > 33:
        $ hp -= 1
    if radiation > 66:
        $ hp -= 25
    if radiation > 100:
        $ hp -= 50
        $ radiation = 100
    else:
        pass
    
    hide screen status
    "Я отдохнул."
    
    return
    
label status_notifications: # Уведомление о состоянии
    
    if ep <= 33:
        extend "\nЯ устал.{nw}"
    if hunger <= 33:
        extend "\nЯ голоден.{nw}"
    if thirst <= 50:
        extend "\nЯ хочу пить."
    
    return

label exhausted: # Уведомлении об усталости при попытке перемещения
    
    hide screen status
    "Я слишком устал для перемещения"
    
    return

label cycle_state: # Изменение состояние при цикле в локации
    
    call time_calculation from _call_time_calculation
    
    if radiation > 33:
        $ hp -= 0.5
    if radiation > 66:
        $ hp -= 1
    if radiation > 100:
        $ hp -= 3
        $ radiation = 100

    if hp <= 0:
        $ hp = 0
        call death from _call_death_3
        
    $ hunger -= 0.25
    if hunger < 0:
        $ hp -= 1
        $ hunger = 0
    
    $ thirst -= 0.33
    if thirst < 0:
        $ hp -= 1
        $ thirst = 0

    return

label check: # Сборник проверок
    
    call check_death from _call_check_death
    call time_calculation from _call_time_calculation_1
    call condition_state from _call_condition_state
    
    call weight_calculation from _call_weight_calculation
    
    return

label condition_state: # Изменение терминов состояний
    
    $ hp_status = str(hp_status)
    $ ep_status = str(ep_status)
    $ hunger_status = str(hunger_status)
    $ thirst_status = str(thirst_status)
    
    if hp <= 10:
        $ hp_status = "{color=#FF2700}в критическом состоянии{/color}"
    elif hp <= 25:
        $ hp_status = "{color=#FF2700}в крайне тяжелом состоянии{/color}"
    elif hp <= 35:
        $ hp_status = "{color=#FBCE43}серьезно ранен{/color}"
    elif hp <= 50:
        $ hp_status = "{color=#FBCE43}ранен{/color}"
    elif hp <= 75:
        $ hp_status = "легко ранен"
    elif hp < 90:
        $ hp_status = "незначительно ранен"    
    else:
        pass
               
    if ep <= 10:
        $ ep_status = "{color=#FF2700}падаю от усталости{/color}"
    elif ep <= 33:
        $ ep_status = "{color=#FBCE43}очень сильно устал{/color}"
    elif ep <= 50:
        $ ep_status = "устал"
    elif ep < 66:
        $ ep_status = "немного устал"   
    else:
        pass
    
    if hunger == 0:
        $ hunger_status = "{color=#FF2700}умираю от голода{/color}"
    elif hunger <= 10:
        $ hunger_status = "{color=#FF2700}голодаю{/color}"
    elif hunger <= 25:    
        $ hunger_status = "{color=#FBCE43}сильно голоден{/color}"
    elif hunger <= 50:    
        $ hunger_status = "голоден"
    elif hunger < 75:    
        $ hunger_status = "слегка проголодался"
    else:
        pass
        
    if thirst == 0:
        $ thirst_status = "{color=#FF2700}умираю от жажды{/color}"
    elif thirst <= 10:
        $ thirst_status = "{color=#FF2700}обезвожен{/color}"
    elif thirst <= 25:    
        $ thirst_status = "{color=#FBCE43}сильно хочу пить{/color}"
    elif thirst <= 50:    
        $ thirst_status = "хочу пить"
    elif thirst < 75:    
        $ thirst_status = "немного хочу пить"
    else:
        pass
    
    return

label campfire_check: # Проверка состояния костра

    if time_in_minutes > campfirelife:
        $ campfire = False
    else:
        pass

    return

label check_death: # Проверка состояния на предмет смерти
    
    if hp <=0:
        call death from _call_death_4
    else:
        pass
    
    return

label time_calculation: # Обновление показателей времени
    
    $ total_hours = time_in_minutes/60
    $ day = total_hours/24
    $ hours = total_hours%24
    $ minutes = time_in_minutes%60
    $ month = day/28
    
    if hours == 0:
        $ daytime = "night"
    elif hours == 1:
        $ daytime = "night"
    elif hours == 2:
        $ daytime = "night"
    elif hours == 3:
        $ daytime = "night"
    elif hours == 4:
        $ daytime = "night"
    elif hours == 5:
        $ daytime = "night"
    elif hours == 6:
        $ daytime = "middle"
    elif hours == 7:
        $ daytime = "middle"
    elif hours == 8:
        $ daytime = "middle"
    elif hours == 9:
        $ daytime = "middle"
    elif hours == 10:
        $ daytime = "day"
    elif hours == 11:
        $ daytime = "day" 
    elif hours == 12:
        $ daytime = "day"
    elif hours == 13:
        $ daytime = "day"
    elif hours == 14:
        $ daytime = "day"
    elif hours == 15:
        $ daytime = "day"
    elif hours == 16:
        $ daytime = "day"
    elif hours == 17:
        $ daytime = "day"
    elif hours == 18:
        $ daytime = "middle"
    elif hours == 19:
        $ daytime = "middle"
    elif hours == 20:
        $ daytime = "middle"
    elif hours == 21:
        $ daytime = "middle"       
    elif hours == 22:
        $ daytime = "night"
    elif hours == 23:
        $ daytime = "night"
    else:
        pass
    
    
    return

label weight_calculation:
    $ weight_total = 0
    
    if player_inv.qty(meat): 
            $ qty = player_inv.qty(meat)
            #$ weight = player_inv.weight(meat)
            $ weight_total = weight_total + (qty*5)
    else:
        pass
    
    return

label death: # Смерть

    stop music
    $_dismiss_pause = False
    hide screen navi
    hide screen action
    hide screen parameters
    hide screen parameters_image
    hide screen time_overlay
    hide screen date_overlay
    hide screen status
    scene death with Dissolve(1.5)
    pause 1.5
    call screen main_menu

    
    return
#
# End code