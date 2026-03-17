import subprocess
import psutil
import pygetwindow as gw
import time
import pyautogui

OPS = set()
nomPubs_file = open("nomPubs.txt")
for str in nomPubs_file :
    OPS.add(str.strip()) 
print(f"pubs connues ; {OPS}")

SPOTIFY_PATH = r"C:\Users\Igor\AppData\Roaming\Spotify\Spotify.exe" 
def nom_fenetre():
    titres = gw.getAllTitles()
    print('TITRES : ////////////////////////////')
    for titre in titres :
        print(titre)
        if titre in OPS :
            return titre  
        #elif titre == "Spotify Free" :
        #    return "Spotify Free"
    return None

def kill_spotify():
    for proc in psutil.process_iter(['name']):
        if 'spotify' in proc.info['name'].lower():
            proc.kill()

def launch_spotify():
    subprocess.Popen([SPOTIFY_PATH])
    print("Spotify launched.")

def resume_spotify():   
    pyautogui.press('playpause')                 

with open ("count.txt",'r') as f:
    texte = f.read()
    #print(len(texte))
    #print(texte[27:])
    k = int(texte[27:])

while True:
    nom_atm = nom_fenetre()
    print(nom_atm)
    if (nom_atm in OPS): 
        with open("count.txt",'w') as f:
            k +=1
            f.write(f"Number of ads turned evil : {k}")
        kill_spotify()      
        launch_spotify()
        time.sleep(3)
        resume_spotify()

    #if (nom_atm == "Spotify Free"):
    #    resume_spotify()
    time.sleep(3)