'''
Author: Matheo Marumo   
Email:  matheomarumo@gmail.com
'''
import ctypes
import time

imgDay = r"C:\Users\..."    #Localização da imagem do dia
imgNight = r"C:\Users\..."  #Localização da imagem da noite

def getHour()->int:
    ctime = time.localtime(time.time())
    hour = ctime.tm_hour
    return hour

def getPeriod(hour:int) -> bool:
    '''Periodo do dia 
    
    Param:
        hour(int): Hora do dia 
    Returns:
        True:Se for dia (Entre 7 horas e 10)
        False: Se for noite
    '''
    if(hour >= 7 and hour < 19):
        return True
    else:
        return False

def changeWallpaper(periodo:bool)->None:
    '''Muda o papel de parede\n
    Param:
        periodo(bool): O periodo do dia. True se for dia, False se for noite
    '''
    if(periodo):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, imgDay, 0)
    else:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, imgNight, 0)

def main():
    print("==Wallpaper changer==")
    hora = getHour()
    periodoDia = getPeriod(hora)
    changeWallpaper(periodoDia)

    while(True):
        time.sleep(60)
        hora = getHour()
        if(periodoDia != getPeriod(hora)):
            periodoDia = getPeriod(hora)
            changeWallpaper(periodoDia)
        else:
            pass
            

if __name__ == "__main__":
   main() 

    