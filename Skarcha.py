import pygame,menu

class Skarcha(object):
    """This is the definition of the object that controles the hole game
    """
    def __init__(self):
        #constants
        self.INMENU = 0
        
        #initiate pygame
        pygame.init()
        
        #setup main settings
        self.setUp_Settings()
    
        #initiate the screen
        if self.winMode == self.WINDOW:
            self.screen = pygame.display.set_mode(self.resolution)
        elif self.winMode == self.FULLSCREEN:
            self.screen = pygame.display.set_mode(self.resolution,pygame.FULLSCREEN)
        
        #initiate the game stages
        self.mainMenu = menu.MainMenu(self)
        
        #assing principal variables
        self.keepGoing = True
        self.stage = self.INMENU
        
        
    def start(self):
        while self.keepGoing:
            if self.stage == self.INMENU:
                self.mainMenu.start()
                
    def quit(self):
        self.keepGoing = False
        
    def setUp_Settings(self):
        
        #set up resolution
        configFile = open("Data/config.ska","r")
        configText = configFile.readlines()
        xRes = ""
        yRes = ""
        tempVal = ""
        for char in configText[0]:
            tempVal += char
            if char == "x":
                xRes = tempVal[:-1]
                tempVal = ""
            elif char == configText[0][(len(configText[0])-1)]:
                yRes = tempVal
                
        self.resolution = (int(xRes),int(yRes))
        
        #set up fullscreen/window
            #winmode constants
        self.FULLSCREEN = 0
        self.WINDOW = 1
        mode = configText[1].strip()
        if mode == "FULLSCREEN":
            winMode = self.FULLSCREEN
        elif mode == "WINDOW":
            winMode = self.WINDOW
         
        
        self.winMode = winMode
        configFile.close()

def main():
    skarcha = Skarcha()
    skarcha.start()
    
if __name__ == "__main__":
    main()