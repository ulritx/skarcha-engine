import pygame
pygame.init()

class Background(pygame.sprite.Sprite):
    """This class is the definition of the background object, a very simple sprite which has the same size as the screen and is draw behind all other sprites in the menu
    Atributes:
        mode(Default=Background.COLOR): this atribute defines the type of image the bakcground has
        background (Default = pygame.Surface(self.menu.screen.get_size()))= is the surface displayed as the image of the sprite can be an external image or a sigle color surface (don't confuse it with the background atribute of the label class, this one is always a surface)
        imgMaster (Default = None) = is the image used to the scale transformations
        bgColor (Default = (255,0,0) = is the color that the background has if mode equals to Background.COLOR
    Methods
        Edition methods:
            set_background (type[Background.IMAGE/Background.COLOR constants],color[(red,green,blue)]/image file name): with this method the background atribute can be changed
        Atribute methods:
            get_background:returns the background surface
        """
    def __init__(self, menu):
        pygame.sprite.Sprite.__init__(self)
        
        #constants
        self.IMAGE = 0
        self.COLOR = 1
        
        #general data
        self.menu = menu
        self.mode = self.COLOR
        self.bgColor = (255,0,0)
        self.background = pygame.Surface(self.menu.screen.get_size())
        self.background.fill(self.bgColor)
        self.imgMaster = None
    
    def update(self,menu):
        self.menu = menu
        #ensure that in resolution changing the background will change
        #mode color
        if self.mode == self.COLOR:
            self.background = pygame.Surface(self.menu.screen.get_size())
            self.background.fill(self.bgColor)
            self.image = self.background
        #mode image
        elif self.mode == self.IMAGE:
            self.background = pygame.transform.scale(self.imgMaster,(self.menu.screen.get_width(),self.menu.screen.get_height()))
            self.image = self.background
            
        #update phisical atributes
        self.rect = self.image.get_rect()
        self.center = (self.menu.screen.get_width() / 2, self.menu.screen.get_height() / 2)
        
    def set_background(self,mode,background):
        self.mode = mode
        if self.mode == self.COLOR:
            self.background = pygame.Surface(self.menu.screen.get_size())
            self.bgColor = background
            self.background.fill(self.bgColor)
        elif self.mode == self.IMAGE:
            self.background = pygame.image.load(background)
            self.background = self.background.convert()
            self.imgMaster = self.background
    
    def get_background(self):
        return background
        

class Label(pygame.sprite.Sprite):
    """A Label that displayes text (admits the fontName and fontSize argument in it's initiation, the default values are fontName = None, fontSize=20)
    Atributes:
        fontName(Default=None): the name of the font file used to display the text (must be a string, the None value sets the font as the default pygame font)
        fontSize(Default=20): the size of the font used to display the text
        antiAlising(Default=False): its a bool that determines if the antialising is applied in the text (recomended if the bgColor is set to None)
        text(Default="Hello World"): the text displayed in the label (the None value eliminates the text in the label)
        txtColor(Default = (0,0,0): the color of the text displayed
        background(Default = False): this bool defines if the label has any background
        backgroundImg(Default = pygame.Surface(self.size)\ self.backgroundImg.fill((255,0,0))): this atribute is the background image of the label
        txtAlign(Default = (self.CENTER,self.MIDDLE): the aliniation of the text in the label (Label.LEFT/Label.CENTER/Label.RIGHT,Label.TOP/Label.MIDDLE/Lable.BOTTOM)
        center(Default = [400,300]): the coordenates of the center of the label [xValue,yValue]
        size(Default = [150,30]: the size of the bounding box of the label [width,height]
        withText(Default = True): it's a bool that defines if is going to be any text in the label
    Methodes:
        Edition methods:
            set_fontName: change the font file name
            set_fontSize: change the font size
            set_aa: activate or desactivate the anti alising (True/False)
            set_text: change the text that must be displayed in the label
            set_txtColor: set the color of the text in the label (the argument must be a turple with 3 numbers 0-255 (red,green,blue))
            set_background: activate or desactivate the background (True/False)
            set_backgroundImg: set the color (the argumen must be a turple with 3 numbers 0-255 (red,green,blue)) or the image of the backgroud of the label, this method must have 2 arguments (Label.IMAGE/Label.COLOR,"%imgFileName"/(red,green,blue))
            set_txtAlign: set the aliniation of the text (use the contants (Label.LEFT,Label.CENTER,Label.RIGHT) and (Label.TOP,Label.MIDDLE,Label.BOTTOM) as arguments)
            set_center: set the coordinates of the center of the label [xVal, yVal]
            set_left: set the x value of the left side of the rect of the label
            set_right: set the x value of the left side of the rect of the label
            set_top: set the y value of the top of the rect of the label
            set_bottom: set the y value of the bottom of the rect of the label 
            set_size: set the size of the label [width, height] 
        Atribute methods (they all return the atribute in their name):
            get_fontName
            get_fontSize
            get_aa: returns the antiAlising atribute
            get_text
            get_txtColor
            get_background
            get_backgroundImg
            get_txtAlign
            get_center
            get_size
            get_withText
        """
    
    
    def __init__(self,menu):
        pygame.sprite.Sprite.__init__(self)
        
        #constants
        self.LEFT = 0
        self.CENTER = 1
        self.RIGHT = 2
        self.TOP = 0
        self.MIDDLE = 1
        self.BOTTOM = 2
        self.COLOR = 0
        self.IMAGE = 1
        
        #inport menu
        self.menu = menu
        
        #label's phisical setings
        self.center = [400,300]
        self.size = [150,30]
        
        #general settings
        self.background = False
        self.backgroundImg = pygame.Surface(self.size)
        self.backgroundImg.fill((255,0,0))
        self.withText = True
        self.withImage = False
    
        #font setings
        self.fontName = None
        self.fontSize = 20
        
        #text setings
        self.text = "Hello World"
        self.txtColor = (0,0,0)
        self.txtAlign = (self.CENTER,self.MIDDLE)
        self.antiAlising = False
        
    def update(self,menu):
        
        #background surface
        self.setup_background()
        
        if self.withText:        
            #font surface
            self.setup_fontSurface()
            
                #align the text
            self.alignText()
            
            #insert the text in the background
            self.image.blit(self.fontSurface, (self.textPosX,self.textPosY))
        
        #refrech phisical information
        self.menu = menu
        self.rect = self.image.get_rect()
        if self.menu.screen.get_size() == (800,600):
            xVal,yVal = self.center
        else:
            xVal = int(self.menu.screen.get_width() / (800.0 / self.center[0]))
            yVal = int(self.menu.screen.get_height() / (600.0 / self.center[1]))
        self.rect.center = (xVal,yVal)
        
    def setup_background(self):
        if self.background:
            tempMasterImg = self.backgroundImg
            tempImage = tempMasterImg
            if self.menu.screen.get_size() == (800,600):
                if not tempImage.get_size() == self.size:
                    tempImage = pygame.transform.scale(tempMasterImg,self.size)
            else:
                tempImage = pygame.transform.scale(tempMasterImg,(int(self.menu.screen.get_width() / (800.0 / self.size[0])),int(self.menu.screen.get_height() / (600.0/self.size[1]))))
        
        else:
            #set the transparent color ensuring that this color isn't ecual to the text color
            if self.txtColor == (0,0,0):
                self.colorKey = (255,0,0)
            else:
                self.colorKey = (0,0,0)
            
            if self.menu.screen.get_size() == (800,600):
                tempImage = pygame.Surface(self.size)
            else:
                tempImage = pygame.Surface((int(self.menu.screen.get_width() / (800.0 / self.size[0])),int(self.menu.screen.get_height() / (600.0 / self.size[1]))))
            tempImage.fill(self.colorKey)
            
        self.image = tempImage
            
    def setup_fontSurface(self):
        
        if self.menu.screen.get_size() == (800,600):
            self.font = pygame.font.Font(self.fontName,self.fontSize)
        else:
            self.font = pygame.font.Font(self.fontName,int(self.menu.screen.get_height() / (600.0 / self.fontSize)))
            
        self.fontSurface = self.font.render(self.text, self.antiAlising, self.txtColor)
            
    def alignText(self):
        xAlign = self.txtAlign[0]
        yAlign = self.txtAlign[1]
        
        if xAlign == self.LEFT:
            self.textPosX = 0
        elif xAlign == self.CENTER:
            self.textPosX = (self.image.get_width() - self.fontSurface.get_width()) / 2
        elif xAlign == self.RIGHT:
            self.textPosX = self.image.get_width() - self.fontSurface.get_width()
        if yAlign == self.TOP:
            self.textPosY = 0
        elif yAlign == self.MIDDLE:
            self.textPosY = (self.image.get_height() - self.fontSurface.get_height()) / 2
        elif yAlign == self.BOTTOM:
            self.textPosY = self.image.get_height() - self.fontSurface.get_height()
            
    def set_fontName(self,name):
        self.fontName = name
    def set_fontSize(self,size):
        self.fontSize = size
    def set_aa(self, aa):
        self.antiAlising = aa
    def set_text(self,text):
        if text:
            self.text = text
            self.withText = True
        else:
            self.withText = False
    def set_txtColor(self,color):
        self.txtColor = color
    def set_background(self,mode):
        self.background = mode
    def set_backgroundImg(self,type,argument):
        self.background = True
        if type == self.IMAGE:
            self.backgroundImg = pygame.image.load(argument)
            self.backgroundImg = self.backgroundImg.convert_alpha()
        elif type == self.COLOR:
            self.backgoundImg = pygame.Surface(self.size)
            self.backgroundImg.fill(argument)
    def set_txtAlign(self,align):
        self.txtAlign = align
    def set_center(self,center):
        self.center = center
    def set_left(self,left):
        self.center[0] = left + self.size[0]/2
    def set_right(self,right):
        self.center[0] = right - self.size[0]/2
    def set_top(self,top):
        self.center[1] = top + self.size[1]/2
    def set_bottom(self,bottom):
        self.center[1] = bottom - self.size[1]/2
    def set_size(self,size):
        self.size = size
    
    def get_fontName(self):
        return self.fontName
    def get_fontSize(self):
        return self.fontSize
    def get_aa(self):
        return self.antiAlising
    def get_text(self):
        return self.text
    def get_txtColor(self):
        return self.txtColor
    def get_background(self):
        return self.background
    def get_backgroundImg(self):
        return self.backgroundImg
    def get_txtAlign(self):
        return self.txtAlign
    def get_center(self):
        return self.center
    def get_size(self):
        return self.size
    def get_withText(self):
        return self.withText
    def get_withImage(self):
        return self.withImage

class Button(Label):
    """This gui sprite has the same characteristics as the label but also has the functionality of a button(this object must have a menu argument in its initiation)
    Atributes(apart from the ones inherited by label):
        active(Default=False): this atribute it's a bool that determines if the mouse cursor is on the button, becames true if the mouse coordenates are in the rect of the button
        clicked(Default=False): this atribute is a bool that determines if the mouse is clicked on it, becames true if the active atribute is True and the left button of the mouse is clicked
        pulsed(Default=False): this atribute is a bool that determines if the mouse left button is "unpressed", becames true if the clicked atribute is True amd the left mouse button is not pressed
        mode(Default = Button.NORM): this atribute defines the mode of the button
        normBg(Default = pygame.Surface(self.size)\normBG.fill((255,0,0))): this is the image of the button when no button atribute is true
        activeBg(Default = pygame.Surface(self.size)\normBG.fill((255,0,0))): this is the background of the button when only the active atribute is true
        clickedBg(Default = pygame.Surface(self.size)\normBG.fill((255,0,0))): this is the background of the button when the clicked atribute is true
    Methods:
        do: this method is empty in this class, is made to enter in it whatever the button has to do when is pulsed
        update: the update method is changed a bit in this class
        checkButton: this method updates the button atributes
        setup_background: this method must be changed to handle with the three button images
        check_backgroundImg: this method assings the actual button image to the backgroundImg atribute
        
        Editon methods:
            set_mode(mode): with this method the mode atribute can be changed (must have this atributes as arguments: Button.NORM, Button.ACTIVE or Button.CLICKED
            set_normBg(type,argument):set the color (the argumen must be a turple with 3 numbers 0-255 (red,green,blue)) or the image of the backgroud of the button when is not active or clicked, this method must have 2 arguments (Label.IMAGE/Label.COLOR,"%imgFileName"/(red,green,blue))
            set_activeBg(type,argument):set the color (the argumen must be a turple with 3 numbers 0-255 (red,green,blue)) or the image of the backgroud of the button when is active, this method must have 2 arguments (Label.IMAGE/Label.COLOR,"%imgFileName"/(red,green,blue))
            set_clickedBg(type,argument):set the color (the argumen must be a turple with 3 numbers 0-255 (red,green,blue)) or the image of the backgroud of the button when is clicked, this method must have 2 arguments (Label.IMAGE/Label.COLOR,"%imgFileName"/(red,green,blue))
        
        Atribute methods (they all return the atribute in their name):
            get_active
            get_clicked
            get_pulsed
            get_mode
            get_normBg
            get_activeBg
            get_clickedBg
    """
    def __init__(self,menu):
        Label.__init__(self, menu)
        #button constants
        self.NORM = 0
        self.ACTIVE = 1
        self.CLICKED = 2
        
        #button atributes
        self.active = False
        self.clicked = False
        self.pulsed = False
        self.mode = self.NORM
        
        #button images
        self.normBg = pygame.Surface(self.size)
        self.normBg.fill((255,0,0))
        self.activeBg = pygame.Surface(self.size)
        self.activeBg.fill((255,0,0))
        self.clickedBg = pygame.Surface(self.size)
        self.clickedBg.fill((255,0,0))
        
    def setup_background(self):
        self.check_backgroundImg()
        
        Label.setup_background(self)
        
    def check_backgroundImg(self):
        if self.mode == self.NORM:
            self.backgroundImg = self.normBg
        elif self.mode == self.ACTIVE:
            self.backgroundImg = self.activeBg
        elif self.mode == self.CLICKED:
            self.backgroundImg = self.clickedBg
        
    def update(self,menu):
        #execute the label update method
        Label.update(self,menu)
        
        #check button atributes and execute the do method if pulsed
        self.checkButton()
        
    def checkButton(self):
        #check active atribute
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.active = True
            self.mode = self.ACTIVE
        else:
            self.mode = self.NORM
            self.active = False
            
        #check clicked atribute
        if self.active and pygame.mouse.get_pressed() == (1,0,0):
            self.clicked = True
            self.mode = self.CLICKED
            
        #check pulsed atribute
        if self.clicked and pygame.mouse.get_pressed() == (0,0,0):
            self.pulsed = True
            self.clicked = False
            self.mode = self.NORM
            if self.active:
                self.do()
        else:
            self.pulsed = False
            
    def do(self):
        pass
        
    def set_mode(self,mode):
        self.mode = mode
    def set_normBg(self,type,argument):
        self.background = True
        if type == self.IMAGE:
            self.normBg = pygame.image.load(argument)
            self.normBg = self.normBg.convert_alpha()
        elif type == self.COLOR:
            self.normBg = pygame.Surface(self.size)
            self.normBg.fill(argument)
    def set_activeBg(self,type,argument):
        self.background = True
        if type == self.IMAGE:
            self.activeBg = pygame.image.load(argument)
            self.activeBg = self.activeBg.convert_alpha()
        elif type == self.COLOR:
            self.activeBg = pygame.Surface(self.size)
            self.activeBg.fill(argument)
    def set_clickedBg(self,type,argument):
        self.background = True
        if type == self.IMAGE:
            self.clickedBg = pygame.image.load(argument)
            self.clickedBg = self.clickedBg.convert_alpha()
        elif type == self.COLOR:
            self.clickedBg = pygame.Surface(self.size)
            self.clickedBg.fill(argument)
            
    def get_active(self):
        return self.active
    def get_clicked(self):
        return self.clicked
    def get_pulsed(self):
        return self.pulsed
    def get_mode(self):
        return self.mode
    def get_normBg(self):
        return self.normBg
    def get_activeBg(self):
        return self.activeBg
    def get_clickedBg(self):
        return self.clickedBg
        
        
class GoTo(Button):
    """This button is used to change from a menu to another
    Atributes:
    
    Methods:
        Edition methods:
            set_goto(menu): this methods sets the menu changing "direction" must have a menu constant
        Atribute methods:
            get_goto: returns the actual goto value"""
    def __init__(self,menu):
        Button.__init__(self,menu)
        
        self.goto = self.menu.INGAME
        
    def do(self):
        self.menu.stage = self.goto
        
    def set_goto(self,menu):
        self.goto = menu
        
    def get_goto(self):
        return self.goto
    
class Quit(Button):
    """This button class has a special and unique function: Quit the game
    """
    def do(self):
        self.menu.keepGoing = False
        self.menu.Skarcha.quit()
class VideoSettings(Button):
    """Clicking this button you can go to the video settings menu
    """
    def do(self):
        self.menu.stage = self.menu.VSETTINGS
class AcceptSettings(Button):
    """Clicking this button you'll save the settings in the correspondient file
    Atributes:
        self.resScroller = the scroller that manages the resolution
        self.winModeScroller = the scroller that manages the window mode
    """
    def __init__(self,menu,scrollers):
        Button.__init__(self,menu)
        
        self.resScroller = scrollers[0]
        self.winModeScroller = scrollers[1]
        
    def do(self):
        configFile = open("Data/config.ska","w")
        if self.winModeScroller.get_scrollMoment() == 0:
            winMode = "FULLSCREEN"
        elif self.winModeScroller.get_scrollMoment() == 1:
            winMode = "WINDOW"
        configFile.writelines(["%s\n" % self.resScroller.get_text(),"%s\n" % winMode])
        configFile.close()
class ApplySettings(AcceptSettings):
    """Clicking this button you'll save the settings in the correspondient file and apply them
    """    
    def do(self):
        AcceptSettings.do(self)
        #resolution
        self.menu.Skarcha.setUp_Settings()
        try:
            if self.menu.Skarcha.winMode == self.menu.Skarcha.WINDOW:
                self.menu.Skarcha.screen = pygame.display.set_mode(self.menu.Skarcha.resolution)
            elif self.menu.Skarcha.winMode == self.menu.Skarcha.FULLSCREEN:
                self.menu.Skarcha.screen = pygame.display.set_mode(self.menu.Skarcha.resolution,pygame.FULLSCREEN)
            self.menu.screen = self.menu.Skarcha.screen
        except pygame.error:
            self.menu.isError = True
            self.menu.errorType = self.menu.RESERROR

class Scroller(Button):
    """This is a special subclass of button which makes a different action when is pulsed in the right side of the scroller or in the left side of the scroller.
    New atributes:
        leftActive(Default=False): becames true when is active on the left side
        rightActive(Default=False): becames true when is active on the right side
        leftClicked(Default=False): becames true when is clicked on the left side
        rightClicked(Default=False): becames true when is clicked on the right side
        leftPulsed(Default=False): becames true when is pulsed on the left side
        rightPulsed(Default=True): becames true when is pulsed on the right side
        scrollType(Default=Scroller.Num): determines if the scroller scrolles in a list of values or simply changes a numerical value (Scroller.NUM,Scroller.LIST)
        scrollInitVal(Default=0): this is initial value that the scroller has (or the position on the list)
        scrollValue(Default=0): this is the scrolled value (can be a numer or a list)
        scrollMoment(Default=scrollInitVal): the actual value of the scrolled value (if it is a list is the intex in the list)
        changeRange(Default=1): this number determines how much values are scrolled each time
    New methods:
        update: updateText is added to it
        checkButton: this method is compleatly changed to manage the left-right clicking
        do: this method is mantained in the class but does nothing, so is recommended not to use it.
        updateText: updates the text displayed
        leftDo: this method decreases the numerical value or passes to the previous value of a list
        rightDo: this method increases the numerical value or passes to the next value of a list
        set_scrollVal(type,value,initialValue,changeRange): this method can be used to edit the value on which the scroller scrolles
        
        Atribute methods (they all return the atribute in their name:
            get_leftActive
            get_rightActive
            get_leftClicked
            get_rightClicked
            get_leftPulsed
            get_rightPulsed
            get_scrollType
            get_scrollInitVal
            get_scrollValue
            get_scrollMoment
            get_changeRange
    """
    def __init__(self,menu):
        Button.__init__(self,menu)
        
        #scroller constatnts
        self.NUM=0
        self.LIST=1
        
        #create the scroller variables
        self.leftActive=False
        self.rightActive=False
        self.leftClicked=False
        self.rightClicked=False
        self.leftPulsed=False
        self.rightPulsed=False
        
        self.scrollType = self.NUM
        self.scrollInitVal = 0
        self.scrollValue = 0
        self.scrollMoment = self.scrollInitVal
        self.changeRange = 1
        
    def update(self,menu):       
        self.updateText()
        
        Button.update(self,menu)
        
    def checkButton(self):
        #check the active atribute
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.active = True
            
            if pygame.mouse.get_pos()[0] <= self.rect.center[0]:
                self.leftActive = True
                self.rightActive = False
            elif pygame.mouse.get_pos()[0] >= self.rect.center[0]:
                self.rightActive = True
                self.leftActive = False
                
        else:
            self.active = False
            self.leftActive = False
            self.rightActive = False
            
        #check the clicked atribute
        if self.active and pygame.mouse.get_pressed() == (1,0,0):
            self.clicked = True
            if self.leftActive == True:
                self.leftClicked = True
                self.rightClicked = False
                if self.scrollType == self.NUM:
                    self.leftDo()
            elif self.rightActive:
                self.rightClicked = True
                self.leftClicked = False
                if self.scrollType == self.NUM:
                    self.rightDo()
        #check the pulsed atribute
        if self.clicked and pygame.mouse.get_pressed() == (0,0,0):
            self.pulsed = True
            self.clicked = False
            if self.leftClicked == True:
                self.leftPulsed = True
                self.rightPulsed = False
                self.leftClicked = False
                if self.scrollType == self.LIST:
                    self.leftDo()
            elif self.rightClicked == True:
                self.rightPulsed = True
                self.leftPulsed = False
                self.rightClicked = False
                if self.scrollType == self.LIST:
                    self.rightDo()
                
        else:
            self.pulsed = False
            self.leftPulsed = False
            self.rightPulsed = False
            
    def updateText(self):
        if self.scrollType == self.NUM:
            self.scrollValue = self.scrollMoment
            self.text = str(self.scrollValue)
        elif self.scrollType == self.LIST:
            if self.scrollMoment > len(self.scrollValue) - 1:
                self.scrollMoment = 0
            elif self.scrollMoment < 0:
                self.scrollMoment = len(self.scrollValue) - 1
            self.text = str(self.scrollValue[self.scrollMoment])
            
    def leftDo(self):
        self.scrollMoment -= self.changeRange
        
    def rightDo(self):
        self.scrollMoment += self.changeRange
    def set_scrollVal(self,type,value,initialValue,changeRange):
        self.scrollType = type
        self.scrollValue = value
        self.scrollInitVal = initialValue
        self.scrollMoment = self.scrollInitVal
        self.changeRange = changeRange
    
    def get_leftActive(self):
        return self.leftActive
    def get_rightActive(self):
        return self.rightActive
    def get_leftClicked(self):
        return self.leftClicked
    def get_rightClicked(self):
        return self.rightClicked
    def get_leftPulsed(self):
        return self.leftPulsed
    def get_rightPulsed(self):
        return self.rightPulsed
    def get_scrollType(self):
        return self.scrollType
    def get_scrollInitVal(self):
        return self.scrollInitVal
    def get_scrollValue(self):
        return self.scrollValue
    def get_scrollMoment(self):
        return self.scrollMoment
    def get_changeRange(self):
        return self.changeRange