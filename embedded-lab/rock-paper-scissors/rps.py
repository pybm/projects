import time
from machine import Pin, ADC, PWM
from random import randint

# LED-uri si buton
led_power = Pin(25, Pin.OUT)
led_start = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)

# LED-uri player
led_red = Pin(21, Pin.OUT)
led_blue = Pin(19, Pin.OUT)
led_green = Pin(20, Pin.OUT)
led_green.off # Default stins
led_red.off
led_blue.off

# LED-uri AI
led_red_ai = Pin(3, Pin.OUT)
led_blue_ai = Pin(5, Pin.OUT)
led_green_ai = Pin(4, Pin.OUT)

# Potentiometru
adc = ADC(26)

# LED RGB
pin_r = PWM(Pin(13))
pin_g = PWM(Pin(12))
pin_b = PWM(Pin(11))

pin_r.freq(1000)
pin_g.freq(1000)
pin_b.freq(1000)

# Variabile globale
joc_pornit = False
voltage = 0
choice = 0
ultima_stare_buton = 1

# Porneste ledul de alimentare
def power_led():
    led_power.value(1)

# Functie PWM pentru LED RGB
def rgb(r, g, b):
    pin_r.duty_u16(65535 - r)
    pin_g.duty_u16(65535 - g)
    pin_b.duty_u16(65535 - b)

# Functie pentru buton ON/OFF joc
def verificare_buton():
    global joc_pornit, ultima_stare_buton
    stare_curenta = button.value()
    if ultima_stare_buton == 1 and stare_curenta == 0:
        joc_pornit = not joc_pornit
        if joc_pornit:
            led_start.value(1)
            print("Joc pornit")
        else:
            led_start.value(0)
            print("Joc oprit")
            reset_leduri()
            rgb(0, 0, 0)
            time.sleep(0.5)
    ultima_stare_buton = stare_curenta

# Reseteaza toate LED-urile
def reset_leduri():
    led_red.value(0)
    led_green.value(0)
    led_blue.value(0)
    led_red_ai.value(0)
    led_green_ai.value(0)
    led_blue_ai.value(0)
    rgb(0, 0, 0)

# Citeste potentiometrul si aprinde LED-ul corespunzator
def citire_pot():
    global voltage
    adcValue = adc.read_u16()
    voltage = adcValue / 65535.0 * 3.3

    if 0 <= voltage <= 1.1:
        led_red.value(0)
        led_green.value(0)
        led_blue.value(1)
    elif 1.2 <= voltage <= 2.2:
        led_red.value(0)
        led_green.value(1)
        led_blue.value(0)
    elif 2.3 <= voltage <= 3.3:
        led_red.value(1)
        led_green.value(0)
        led_blue.value(0)
    else:
        reset_leduri()

# Asteapta stabilitate la potentiometru
def asteapta_stabilitate():
    start = time.time()
    last_voltage = adc.read_u16() / 65535.0 * 3.3
    while time.time() - start < 2:
        verificare_buton()
        if not joc_pornit:
            return None
        curent = adc.read_u16() / 65535.0 * 3.3
        if abs(curent - last_voltage) > 0.02:
            last_voltage = curent
            start = time.time()
        citire_pot()
        time.sleep(0.1)
    return last_voltage

evil_sequence = []
evil_mode = False
previous_evil_mode = False  # Ne ajută să știm dacă s-a schimbat modul

def evil_power():
    global evil_mode, previous_evil_mode
    if 0 <= voltage <= 1.1:
        evil_sequence.append(1)
        if evil_sequence == [1, 1, 1]:
            if evil_mode == False:
                evil_mode = True
                if previous_evil_mode == False:
                    feedback_rgb("evil")  # Activezi feedback vizual doar o dată
            elif evil_mode == True:
                evil_mode = False
                if previous_evil_mode == True:
                    feedback_rgb("random")  # Dezactivezi cu alt efect
            previous_evil_mode = evil_mode  # actualizezi starea
            evil_sequence.clear()
    else:
        evil_sequence.clear()

def AI(mode="random"):
    global choice

    if mode == "random":
        choice = randint(0, 2)
        print("AI a ales:", choice)
        if choice == 0:
            led_blue_ai.value(1)
        elif choice == 1:
            led_green_ai.value(1)
        elif choice == 2:
            led_red_ai.value(1)

    elif mode == "evil":
        if 0 <= voltage <= 1.1:
            choice = 1  # AI alege foarfecă (bate foaia)
            led_green_ai.value(1)
            print("AI a ales: 1")
        elif 1.2 <= voltage <= 2.2:
            choice = 2  # AI alege piatră (bate foarfecă)
            led_red_ai.value(1)
            print("AI a ales: 2")
        elif 2.3 <= voltage <= 3.3:
            choice = 0  # AI alege foaie (bate piatra)
            led_blue_ai.value(1)
            print("AI a ales: 0")

def feedback_rgb(mode):
    if mode == "evil":
        for r in range(10000, 60001, 10000):
            pin_r.duty_u16(65535 - r)
            time.sleep(0.2)
        rgb(0, 0, 0)  # Stinge după efect
    elif mode == "random":
        for g in range(10000, 60001, 10000):
            pin_g.duty_u16(65535 - g)
            time.sleep(0.2)
        rgb(0, 0, 0)


# Converteste voltajul in alegere (0, 1, 2)
def get_player_choice(voltage):
    if 0 <= voltage <= 1.1:
        return 0  # FOAIE
    elif 1.2 <= voltage <= 2.2:
        return 1  # FOARFECA
    elif 2.3 <= voltage <= 3.3:
        return 2  # PIATRA
    else:
        return -1  # Eroare

# Animatie leduri AI
def animatie_leduri_ai(durata_secunde=2):
    start_time = time.time()
    while time.time() - start_time < durata_secunde:
        verificare_buton()
        if not joc_pornit:
            return
        reset_leduri_ai()
        alegere = randint(0, 2)
        if alegere == 0:
            led_blue_ai.value(1)
        elif alegere == 1:
            led_green_ai.value(1)
        elif alegere == 2:
            led_red_ai.value(1)
        time.sleep(0.2)

def reset_leduri_ai():
    led_red_ai.value(0)
    led_green_ai.value(0)
    led_blue_ai.value(0)

# Afiseaza rezultatul
def rezultat(voltage):
    player_choice = get_player_choice(voltage)

    if player_choice == -1:
        print("Eroare: Voltaj invalid")
        return

    if player_choice == choice:
        show_result("Remiza!")
    elif (player_choice == 0 and choice == 1) or \
         (player_choice == 1 and choice == 2) or \
         (player_choice == 2 and choice == 0):
        show_result("Ai pierdut!")
    else:
        show_result("Ai castigat!")

# Show rezultat pe LED RGB
def show_result(result):
    if result == "Ai castigat!":
        for _ in range(4):
            verificare_buton()
            if not joc_pornit:
                return
            rgb(0, 40000, 0)  # Verde
            time.sleep(0.2)
            rgb(0, 0, 0)
            time.sleep(0.2)
    elif result == "Ai pierdut!":
        for _ in range(2):
            verificare_buton()
            if not joc_pornit:
                return
            rgb(40000, 0, 0)  # Rosu
            time.sleep(0.6)
            rgb(0, 0, 0)
            time.sleep(0.6)
    elif result == "Remiza!":
        for _ in range(30):  # 3 secunde alb cu verificare la fiecare 0.1s
            verificare_buton()
            if not joc_pornit:
                return
            rgb(30000, 30000, 30000)
            time.sleep(0.1)
        rgb(0, 0, 0)

# --- Main Program ---
power_led()

while True:
    verificare_buton()
    if joc_pornit:
        citire_pot()
        print("Astept stabilitate...")
        valoare_finala = asteapta_stabilitate()
        if valoare_finala is None:
            continue
        print("Valoare blocata:", valoare_finala)
        time.sleep(1)
        evil_power()
        if evil_mode:
           AI(mode="evil")
        else:
           AI(mode="random")
        animatie_leduri_ai(2)  # animatie fake
        reset_leduri_ai()  # opreste toate LED-urile AI
        
        # REAPRINDE LED-ul ales de AI real
        if choice == 0:
            led_blue_ai.value(1)
        elif choice == 1:
            led_green_ai.value(1)
        elif choice == 2:
            led_red_ai.value(1)
        
        time.sleep(0.5)
        rezultat(valoare_finala)
        reset_leduri_ai()
        reset_leduri()
    time.sleep(0.1)



