import pygame,gui

class MainMenu(object):
    """This class is the definition of the Main Menu of the game
    """
    
    def __init__(self,Skarcha):
        #constants
        self.MAINMENU = 0
        self.INGAME = 1
        self.SETTINGS = 2
        self.VSETTINGS = 3
        
        #create main entities
        self.Skarcha = Skarcha
        self.screen = self.Skarcha.screen
        
        #create the background object
        self.background = gui.Background(self)
        self.background.set_background(self.background.IMAGE,"Graphics/Menu/background.jpg")
        self.backgroundGroup = pygame.sprite.Group(self.background)
        
        #error hadling
            #error contants
        self.RESERROR = 0
            #error generar variables
        self.isError = False
        self.errorType = self.RESERROR
        self.errorCount = 1500
        
        #create main variables
        self.keepGoing = True
        self.stage = self.MAINMENU
        self.clock = pygame.time.Clock()
        
        #create the sprite group
        self.actualGroup = None
        
    def start(self):
        #crete all the sprites in the menu
        self.createSprites()
        self.createErrorSprites()
        
        while self.keepGoing:
            self.clock.tick(30)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.keepGoing = False
                    self.Skarcha.quit()
                    
            self.errorGroup = self.checkError()
            
            self.actualGroup = self.checkStage()
            
            self.errorCountDown()
                    
            self.backgroundGroup.update(self)
            self.actualGroup.update(self)
            if self.isError:
                self.errorGroup.update(self)
            self.backgroundGroup.draw(self.screen)
            self.actualGroup.draw(self.screen)
            if self.isError:
                self.errorGroup.draw(self.screen)
            
            pygame.display.flip()
            
    def errorCountDown(self):
        if self.isError and self.errorCount:
            self.isError = True
            self.errorCount -= 1
        else:
            self.isError = False
            self.errorCount = 150
            
    def createErrorSprites(self):
        #here are created all the error sprites
        self.createResErrorSprites()
        
    def checkError(self):
        if self.errorType == self.RESERROR:
            errorGroup = self.resErrorGroup
        return errorGroup
    def createResErrorSprites(self):
        errorLabel = gui.Label(self)
        errorLabel.set_size((300,50))
        errorLabel.set_center((400,300))
        errorLabel.set_text("This resolution is too big for your screen")
        
        self.resErrorGroup = pygame.sprite.Group(errorLabel)
            
    def createSprites(self):
        #here can be created the different groups of sprites (menus)
        self.createMainMenuSprites()
        self.createInGameSprites()
        self.createSettingsSprites()
        self.createVSettingsSprites()
        
    def checkStage(self):
        #here each stage constant can be asigned to an sprite group
        if self.stage == self.MAINMENU:
            actualGroup = self.mainMenuGroup
        elif self.stage == self.INGAME:
            actualGroup = self.inGameGroup
        elif self.stage == self.SETTINGS:
            actualGroup = self.settingsGroup
        elif self.stage == self.VSETTINGS:
            actualGroup = self.vSettingsGroup
        return actualGroup
            
    def createMainMenuSprites(self):
        label = gui.Label(self)
        label.set_fontSize(50)
        label.set_text("Skarcha")
        label.set_size((200,70))
        label.set_center((400,100))
        label.set_backgroundImg(label.COLOR,(255,255,255))
        label.set_aa(True)
        label.set_fontName("Graphics/Menu/Fonts/BIRTH_OF_A_HERO.ttf")
        
        startGame = gui.GoTo(self)
        startGame.set_text("New Game")
        startGame.set_size((150,40))
        startGame.set_center((160,200))
        startGame.set_normBg(startGame.IMAGE, "Graphics/Menu/button.png")
        startGame.set_activeBg(startGame.IMAGE, "Graphics/Menu/button_active.png")
        startGame.set_clickedBg(startGame.IMAGE, "Graphics/Menu/button_clicked.png")
        startGame.set_aa(True)
        startGame.set_fontName("Graphics/Menu/Fonts/Harabara.ttf")
        
        settings = gui.GoTo(self)
        settings.set_goto(self.SETTINGS)
        settings.set_text("Settings")
        settings.set_size((150,40))
        settings.set_center((160,300))
        settings.set_normBg(settings.IMAGE, "Graphics/Menu/button.png")
        settings.set_activeBg(settings.IMAGE, "Graphics/Menu/button_active.png")
        settings.set_clickedBg(settings.IMAGE, "Graphics/Menu/button_clicked.png")
        settings.set_aa(True)
        settings.set_fontName("Graphics/Menu/Fonts/coolvetica_rg.ttf")
        
        quit = gui.Quit(self)
        quit.set_fontSize(40)
        quit.set_text("QUIT")
        quit.set_size((150,40))
        quit.set_center((160,500))
        quit.set_normBg(quit.IMAGE, "Graphics/Menu/button.png")
        quit.set_activeBg(quit.IMAGE, "Graphics/Menu/button_active.png")
        quit.set_clickedBg(quit.IMAGE, "Graphics/Menu/button_clicked.png")
        quit.set_aa(True)
        
        self.mainMenuGroup = pygame.sprite.Group(label,startGame,settings,quit)
        
    def createInGameSprites(self):
        label = gui.Label(self)
        label.set_fontSize(50)
        label.set_text("IN GAME!")
        label.set_size((200,70))
        label.set_center((400,100))
        label.set_backgroundImg(label.COLOR,(255,255,255))
        label.set_aa(True)
        
        backButton = gui.GoTo(self)
        backButton.set_goto(self.MAINMENU)
        backButton.set_text("Back")
        backButton.set_center((400,400))
        backButton.set_normBg(backButton.IMAGE, "Graphics/Menu/button.png")
        backButton.set_activeBg(backButton.IMAGE, "Graphics/Menu/button_active.png")
        backButton.set_clickedBg(backButton.IMAGE, "Graphics/Menu/button_clicked.png")
        backButton.set_aa(True)
        
        self.inGameGroup = pygame.sprite.Group(label,backButton)
        
    def createSettingsSprites(self):
        label = gui.Label(self)
        label.set_fontSize(50)
        label.set_text("SETTINGS")
        label.set_size((200,70))
        label.set_center((400,100))
        label.set_backgroundImg(label.COLOR,(255,255,255))
        label.set_aa(True)
        
        videoSet = gui.GoTo(self)
        videoSet.set_goto(self.VSETTINGS)
        videoSet.set_text("Video settings")
        videoSet.set_size((150,40))
        videoSet.set_center((160,200))
        videoSet.set_normBg(videoSet.IMAGE, "Graphics/Menu/button.png")
        videoSet.set_activeBg(videoSet.IMAGE, "Graphics/Menu/button_active.png")
        videoSet.set_clickedBg(videoSet.IMAGE, "Graphics/Menu/button_clicked.png")
        videoSet.set_aa(True)
        
        backButton = gui.GoTo(self)
        backButton.set_goto(self.MAINMENU)
        backButton.set_text("Back")
        backButton.set_center((400,500))
        backButton.set_normBg(backButton.IMAGE, "Graphics/Menu/button.png")
        backButton.set_activeBg(backButton.IMAGE, "Graphics/Menu/button_active.png")
        backButton.set_clickedBg(backButton.IMAGE, "Graphics/Menu/button_clicked.png")
        backButton.set_aa(True)
        
        self.settingsGroup = pygame.sprite.Group(label,videoSet,backButton)
        
    def createVSettingsSprites(self):
        label = gui.Label(self)
        label.set_fontSize(50)
        label.set_text("VIDEO SETTINGS")
        label.set_size((300,70))
        label.set_center((400,100))
        label.set_backgroundImg(label.COLOR,(255,255,255))
        label.set_aa(True)
        
        resLabel = gui.Label(self)
        resLabel.set_text("Resolution")
        resLabel.set_size((100,50))
        resLabel.set_center((110,200))
        resLabel.set_backgroundImg(resLabel.COLOR,(0,255,0))
        resLabel.set_aa(True)
        
        resScroller = gui.Scroller(self)
        resScroller.set_center((500,200))
        resScroller.set_normBg(resScroller.COLOR, (0,255,0))
        resScroller.set_activeBg(resScroller.COLOR, (0,255,0))
        resScroller.set_clickedBg(resScroller.COLOR, (0,255,0))
        resScroller.set_aa(True)
        #resolution turple
        resolutions = ("320x240","640x480","800x600","1024x768","1152x864","1280x720","1280x800","1280x960","1280x960","1280x1024","1360x768","1366x768","1440x900","1600x900","1600x1200","1680x1050","1920x1080","1920x1200","2560x1440")
        resScroller.set_scrollVal(resScroller.LIST,resolutions,2,1)
        
        winModeLabel = gui.Label(self)
        winModeLabel.set_text("Resolution")
        winModeLabel.set_size((100,50))
        winModeLabel.set_center((110,300))
        winModeLabel.set_backgroundImg(winModeLabel.COLOR,(0,255,0))
        winModeLabel.set_aa(True)
        
        winModeScroller = gui.Scroller(self)
        winModeScroller.set_center((500,300))
        winModeScroller.set_normBg(winModeScroller.COLOR, (0,255,0))
        winModeScroller.set_activeBg(winModeScroller.COLOR, (0,255,0))
        winModeScroller.set_clickedBg(winModeScroller.COLOR, (0,255,0))
        winModeScroller.set_aa(True)
        #winmode turple
        winmodes = ("Fullscreen","Window mode")
        winModeScroller.set_scrollVal(winModeScroller.LIST,winmodes,0,1)
        
        apply = gui.ApplySettings(self,(resScroller,winModeScroller))
        apply.set_text("Apply")
        apply.set_center((540,500))
        apply.set_normBg(apply.IMAGE, "Graphics/Menu/button.png")
        apply.set_activeBg(apply.IMAGE, "Graphics/Menu/button_active.png")
        apply.set_clickedBg(apply.IMAGE, "Graphics/Menu/button_clicked.png")
        apply.set_aa(True)
        
        backSettings = gui.GoTo(self)
        backSettings.set_goto(self.SETTINGS)
        backSettings.set_text("Back")
        backSettings.set_center((700,500))
        backSettings.set_normBg(backSettings.IMAGE, "Graphics/Menu/button.png")
        backSettings.set_activeBg(backSettings.IMAGE, "Graphics/Menu/button_active.png")
        backSettings.set_clickedBg(backSettings.IMAGE, "Graphics/Menu/button_clicked.png")
        backSettings.set_aa(True)
        
        self.vSettingsGroup = pygame.sprite.Group(label,backSettings,resLabel,resScroller,winModeLabel,winModeScroller,apply)