import turtle,time,sys,os,datetime,webbrowser
bg = turtle.Screen()
bg.setup(width = 1280, height = 720)
bg.bgpic('background.gif')
sys.setrecursionlimit(2147483617)
class turt(turtle.Turtle):
    def __init__(self,pos,size,colour,shape,hide):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.goto(pos)
        self.pos = pos
        if hide:
            self.hideturtle()
        self.color(colour)
        self.turtlesize(float(size[0]),float(size[1]),float(size[2]))
        self.shape(shape)
    def addallshapes(direct):
        for x in os.listdir(direct):
            if os.path.isfile(os.path.join(direct,x)) and x[-4:] == '.gif':
                bg.addshape(os.path.join(direct,x))
def createtextbox():
        textbox = turt((-5,-230),(12,63,1),'white','square',True)
        textwrite = turt((-620,-160),(1,1,1),'white','square',True)
        charbox = turt((-500,-60),(5,10,1),'white','square',True)
        charname = turt((-500,-90),(1,1,1),'white','square',True)
def click(x,y):
    global clicked
    clicked = True
def mainmenu():
    global screenno
    pos = 10000,10000
    bg.clear()
    bg.tracer(0)
    bg.bgcolor('black')
    screenoutline = turt((0,0),(36,64,0),"black",os.getcwd()+'\\background.gif',False)
    mainscreentext = turt((0,250),(1,1,1),'black','square',True)
    startbutton = turt((0,0),(10,20,1),'orange','square',False)
    startbuttontext = turt((0,-50),(1,1,1),'blue','square',True)
    turtle.onscreenclick(screenclick)
    bg.update()
    mainscreentext.write("CLIMATTERS",False,align='center',font=("Arial",64,'normal'))
    mainscreentext.forward(-5)
    mainscreentext.color((0,1,0))
    mainscreentext.write("CLIMATTERS",False,align='center',font=("Arial",64,'normal'))
    startbuttontext.write("START",False,align='center',font=("Arial",64,'bold'))
    while screenno == 0:
        time.sleep(0.05)
        try:
            startbuttontext.clear()
            startbuttontext.write("START",False,align='center',font=("Arial",64,'bold'))
        except:
            return end()
    bg.update()
    return checkscreen(screenno)
def mainscreen():
    global screenno
    pos = 10000,10000
    bg.clear()
    bg.tracer(0)
    bg.bgcolor('black')
    screenoutline = turt((0,0),(36,64,0),"black",'square',False)
    screen = turt((0,0),(35,63,0),(1, 221/255, 204/255),'square',False)
    mainscreentext = turt((0,250),(1,1,1),'black','square',True)
    backbutton = turt((-535,-300),(5,9.5,1),'blue','square',False)
    backbuttontext = turt((-540,-330),(1,1,1),'orange','square',True)
    timetxt = turt((460,-350),(1,1,1),'black','square',True)
    dailyactbutton = turt((-400,0),(5,10,1),(1,0,0),'square',False)
    dailyactbuttontext = turt((-400,-10,),(1,1,1,),'black','square',True)
    weeklytotalbutton = turt((0,0),(5,10,1),(0,1,0),'square',False)
    weeklytotalbuttontext = turt((0,-10),(1,1,1),'black','square',True)
    weeklyresettext = turt((0,-200),(1,1,1),'black','square',True)
    linkbutton = turt((400,0),(5,10,1),(0.5,0,1),'square',False)
    linkbuttontext = turt((400,-20),(1,1,1),'black','square',True)
    bg.update()
    backbuttontext.write("Back",False,align='center',font=("Arial",32,'normal'))
    mainscreentext.write("Welcome User",False,align='center',font=("Arial",64,'normal'))
    mainscreentext.forward(-5)
    mainscreentext.color((0,1,0))
    mainscreentext.write("Welcome User",False,align='center',font=("Arial",64,'normal'))
    dailyactbuttontext.write("Input Daily Activities",False,align='center',font=("Arial",15,'normal'))
    weeklytotalbuttontext.write("Check Weekly Total",False,align='center',font=("Arial",15,'normal'))
    linkbuttontext.write("Click here to\nfind out more",False,align='center',font=("Arial",15,'normal'))
    currenttime = time.strftime("%a, %d %b %Y %H:%M:%S")
    timetxt.write(currenttime,False,align='center',font=("Arial",20,'normal'))
    data = open("Datafile.txt",'r')
    dataread = data.readlines()
    data.close()
    weeklyresettext.write('WEEKLY RESET DATE DURING NEXT LOGIN: ' + time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime(float(dataread[13].rstrip()))),False,'center',font=('Arial',15,'normal'))
    turtle.onscreenclick(screenclick)
    while screenno == 1:
        time.sleep(0.05)
        try:
            timetxt.clear()
            timetxt.write(time.strftime("%a, %d %b %Y %H:%M:%S"),False,align='center',font=("Arial",20,'normal'))
        except:
            return end()
    return checkscreen(screenno)
def dailyactivities():
    global screenno
    pos = 10000,10000
    bg.clear()
    bg.tracer(0)
    bg.bgcolor('black')
    screenoutline = turt((0,0),(36,64,0),"black",'square',False)
    screen = turt((0,0),(35,63,0),(1,0.752941176471,0.796078431373),'square',False)
    title = turt((0,250),(1,1,1),'black','square',True)
    backbutton = turt((-535,-300),(5,9.5,1),'blue','square',False)
    backbuttontext = turt((-540,-330),(1,1,1),'orange','square',True)
    savebutton = turt((440,0),(5,10,1),(0,1,0),'square',False)
    savebuttontext = turt((440,-25),(1,1,1),'black','square',True)
    instructions = turt((-500,0),(1,1,1),'black','square',True)
    names = ["Driving Personal Car (in Minutes)","Turning on the Aircon (in Hours)","Turning on LED lights (in Hours)","Cooking (in Minutes)","Waste Produced (in KG)","Others"]
    for nameno in range(len(names)):
        globals()["title"+str(nameno)] = turt((-150,200-nameno*100),(1,1,1),'black','square',True)
        globals()["titleval"+str(nameno)] = turt((150,200-nameno*100),(1,1,1),'white','square',True)
        globals()["titlevalbox"+str(nameno)] =  turt((150,210-nameno*100),(2.5,5,1),'black','square',False)
    bg.update()
    backbuttontext.write("Back",False,align='center',font=("Arial",32,'normal'))
    title.write("Input Daily Activities",False,'center',('Arial',64,'normal'))
    title.forward(-5)
    title.color((1,0,0))
    title.write("Input Daily Activities",False,align='center',font=("Arial",64,'normal'))
    instructions.write("Press on the\nvalue to change.",False,'center',("Arial",20,'normal'))
    savebuttontext.write("SAVE",False,'center',("Arial",32,'normal'))
    data = open("Datafile.txt","r")
    datafileread = data.readlines()
    for nameno in range(len(names)):
        globals()["title"+str(nameno)].write(names[nameno],False,'center',('Arial',15,'normal'))
        globals()["titleval"+str(nameno)].write(datafileread[nameno+1].rstrip(),False,'center',('Arial',15,'normal'))
    data.close()
    turtle.onscreenclick(screenclick)
    while screenno == 2:
        time.sleep(0.05)
        try:
            backbuttontext.clear()
            backbuttontext.write("Back",False,align='center',font=("Arial",32,'normal'))
        except:
            return end()
    return checkscreen(screenno)
def checkweeklytotal():
    global screenno
    pos = 10000,10000
    bg.clear()
    bg.tracer(0)
    bg.bgcolor('black')
    screenoutline = turt((0,0),(36,64,0),"black",'square',False)
    screen = turt((0,0),(35,63,0),(0.75,1,0.75),'square',False)
    title = turt((0,275),(1,1,1),'black','square',True)
    backbutton = turt((-535,-300),(5,9.5,1),'blue','square',False)
    backbuttontext = turt((-540,-330),(1,1,1),'orange','square',True)
    totaltext = turt((450,50),(1,1,1),'black','square',True)
    total = turt((450,-50),(1,1,1),'black','square',True)
    turtle.onscreenclick(screenclick)
    names = ["Driving Personal Car (in Minutes)","Turning on the Aircon (in Hours)","Turning on lights (in Hours)","Cooking (in Minutes)","Waste Produced (in KG)","Others"]
    val = ["0.090","8.750","0.023","0.907","0.150","1.000"]
    for nameno in range(len(names)):
        globals()["title"+str(nameno)] = turt((-350,200-nameno*100),(1,1,1),'black','square',True)
        globals()["titleval"+str(nameno)] = turt((-150,200-nameno*100),(1,1,1),'black','square',True)
        globals()["value"+str(nameno)] = turt((100,200-nameno*100),(1,1,1),'black','square',True)
    bg.update()
    data = open("Datafile.txt","r")
    datafileread = data.readlines()
    for nameno in range(len(names)):
        globals()["title"+str(nameno)].write(names[nameno],False,'center',('Arial',15,'normal'))
        globals()["titleval"+str(nameno)].write(datafileread[nameno+7].rstrip() + ' X ',False,'center',('Arial',15,'normal'))
        globals()["value"+str(nameno)].write(val[nameno] + "             =             " + (str(round(float(val[nameno])*float(datafileread[nameno+7].rstrip()),5))),False,'center',('Arial',15,'normal'))
    backbuttontext.write("Back",False,align='center',font=("Arial",32,'normal'))
    totaltext.write("TOTAL: ",False,align='center',font =('Arial',32,'normal'))
    totalnum = 0
    for lineno in range(6):
        totalnum += float(val[lineno])*float(datafileread[lineno+7].rstrip())
    total.write(str(round(totalnum,5))+" KG\nof Co2",False,'center',('Arial',32,'normal'))
    title.write("WEEKLY CARBON PRODUCTION",False,'center',('Arial',40,'normal'))
    title.forward(-5)
    title.color((0.5,0.75,1))
    title.write("WEEKLY CARBON PRODUCTION",False,align='center',font=("Arial",40,'normal'))
    data.close()
    while screenno == 3:
        time.sleep(0.05)
        try:
            backbuttontext.clear()
            backbuttontext.write("Back",False,align='center',font=("Arial",32,'normal'))
        except:
            return end()
    return checkscreen(screenno)
def links():
    global screenno
    pos = 10000,10000
    bg.clear()
    bg.tracer(0)
    bg.bgcolor('black')
    screenoutline = turt((0,0),(36,64,0),"black",'square',False)
    screen = turt((0,0),(35,63,0),(0.75,0.5,1),'square',False)
    title = turt((0,250),(1,1,1),'black','square',True)
    backbutton = turt((-535,-300),(5,9.5,1),'blue','square',False)
    backbuttontext = turt((-540,-330),(1,1,1),'orange','square',True)
    titles = ['Heatwave&Draught\nin China 2022','Pakistan Floods\nin 2022','Carbon Emissions\nfrom Electricity','Carbon Emissions\nfrom Air conditioning','Carbon Emissions\nfrom Household Stoves']
    for linkno in range(5):
        globals()['link'+str(linkno)] = turt((0,280-150*linkno),(1,1,1),'white','square',True)
        globals()['linkbox'+str(linkno)] = turt((0,300-150*linkno),(4,20,1),'black','square',False)
    bg.update()
    for linkno in range(5):
        globals()['link'+str(linkno)].write(titles[linkno],False,'center',('Arial',16,'normal'))
    turtle.onscreenclick(screenclick)
    backbuttontext.write("Back",False,align='center',font=("Arial",32,'normal'))
    while screenno == 4:
        time.sleep(0.05)
        try:
            backbuttontext.clear()
            backbuttontext.write("Back",False,align='center',font=("Arial",32,'normal'))
        except:
            return end()
    return checkscreen(screenno)
def screenclick(x,y):
    print(x,y)
    global screenno
    if screenno == 0:
        if abs(x) <= 200 and abs(y) <= 100:
            screenno = 1
    elif screenno == 1:
        if x > -630 and x < -440 and y > -350 and y < -260:
            screenno = 0
        if abs(y) <= 50 and x >= -500 and x <= -300:
            screenno = 2
        if abs(x) <= 100 and abs(y) <= 50:
            screenno = 3
        elif abs(y) <= 50 and x > 300 and x < 500:
            screenno = 4
    elif screenno == 2:
        if x > -630 and x < -440 and y > -350 and y < -260:
            screenno = 1
        if abs(y) <= 50 and x > 340 and y < 540:
            data = open("Datafile.txt",'r')
            dataread = data.readlines()
            for datano in range(6):
                dataread[7+datano] = str(float(dataread[7+datano].rstrip()) + float(dataread[1+datano].rstrip())) + "\n"
                dataread[1+datano] = '0\n'
            data.close()
            data = open("Datafile.txt",'w')
            data.writelines(dataread)
            data.close()
            screenno = 1
        if x > 100 and x < 200:
            if y > 185 and y < 235: # car
                valinput = turtle.textinput("Car Prodcution", "Please input Car drive time (in Minutes) from 0-1440")
                while (not valinput.replace('.','',1).isdigit() or float(valinput) > 1440):
                    valinput = turtle.textinput("Car Prodcution", "Invalid Input! Please input Car drive time (in Hours) from 0-1440")
                data = open("Datafile.txt",'r')
                dataread = data.readlines()
                dataread[1] = valinput+'\n'
                data.close()
                data = open("datafile.txt",'w')
                data.writelines(dataread)
                data.close()
                return dailyactivities()
            if y > 85 and y < 135: # aircon
                valinput = turtle.textinput("Air Conditioning Production", "Please input Air Conditioning usage time (in Hours) from 0-24")
                while (not valinput.replace('.','',1).isdigit() or float(valinput) > 24):
                    valinput = turtle.textinput("Air Conditioning Production", "Invalid Input! Please input Air Conditioning usage time (in Hours) from 0-24")
                data = open("Datafile.txt",'r')
                dataread = data.readlines()
                dataread[2] = valinput+'\n'
                data.close()
                data = open("datafile.txt",'w')
                data.writelines(dataread)
                data.close()
                return dailyactivities()
            if y > -15 and y < 35: # lights
                valinput = turtle.textinput("Lights Production", "Please input Lights usage time (in Hours) from 0-24")
                while (not valinput.replace('.','',1).isdigit() or float(valinput) < 0 or float(valinput) > 24):
                    valinput = turtle.textinput("Lights Prodcution", "Invalid Input! Please input Lights usage time (in Hours) from 0-24")
                data = open("Datafile.txt",'r')
                dataread = data.readlines()
                dataread[3] = valinput+'\n'
                data.close()
                data = open("datafile.txt",'w')
                data.writelines(dataread)
                data.close()
                return dailyactivities()
            if y > -115 and y < -65: # cooking
                valinput = turtle.textinput("Cooking Production", "Please input cooking time (in Minutes) from 0-1440")
                while (not valinput.replace('.','',1).isdigit() or float(valinput) < 0 or float(valinput) > 1440):
                    valinput = turtle.textinput("Cooking Prodcution", "Invalid Input! Please input cooking time (in Minutes) from 0-1440")
                data = open("Datafile.txt",'r')
                dataread = data.readlines()
                dataread[4] = valinput+'\n'
                data.close()
                data = open("datafile.txt",'w')
                data.writelines(dataread)
                data.close()
                return dailyactivities()
            if y > -215 and y < -165: # waste
                valinput = turtle.textinput("Waste Production", "Please input waste produced (in KG) from 0-999999")
                while (not valinput.replace('.','',1).isdigit() or float(valinput) < 0 or float(valinput) > 999999):
                    valinput = turtle.textinput("Waste Prodcution", "Invalid Input! Please input waste produced (in KG) from 0-999999")
                data = open("Datafile.txt",'r')
                dataread = data.readlines()
                dataread[5] = valinput+'\n'
                data.close()
                data = open("datafile.txt",'w')
                data.writelines(dataread)
                data.close()
                return dailyactivities()
            if y > -315 and y < -265: # others
                valinput = turtle.textinput("Others", "Please input How much greenhouse gases were produced from 0-999999")
                while (not valinput.replace('.','',1).isdigit() or float(valinput) < 0 or float(valinput) > 999999):
                    valinput = turtle.textinput("Others", "Please input How much greenhouse gases were produced from 0-999999")
                data = open("Datafile.txt",'r')
                dataread = data.readlines()
                dataread[6] = valinput+'\n'
                data.close()
                data = open("datafile.txt",'w')
                data.writelines(dataread)
                data.close()
                return dailyactivities()
    elif screenno == 3:
        if x > -630 and x < -440 and y > -350 and y < -260:
            screenno = 1
    elif screenno == 4:
        if x > -630 and x < -440 and y > -350 and y < -260:
            screenno = 1
        if abs(x) <= 200:
            if y <= 340 and y >= 260:
                webbrowser.open("https://multimedia.scmp.com/infographics/news/china/article/3190803/china-drought/index.html")
            elif y >= 110 and y <= 190:
                webbrowser.open('https://www.channelnewsasia.com/commentary/climate-change-floods-drought-pakistan-europe-extreme-weather-2911976')
            elif abs(y) <= 40:
                webbrowser.open('https://www.world-nuclear.org/information-library/energy-and-the-environment/carbon-dioxide-emissions-from-electricity.aspx')
            elif y >= -190 and y <= -110:
                webbrowser.open('https://www.channelnewsasia.com/commentary/air-con-unit-electricity-energy-carbon-emissions-climate-change-1339326#:~:text=A%20standard%202%20kilowatt%20AC,tonnes%20of%20carbon%20emissions%20annually')
            elif y >= -340 and y <= -260:    
                webbrowser.open('https://www.forbes.com/sites/jeffkart/2022/01/27/your-natural-gas-stove-is-fueling-climate-change-and-harming-your-health-and-its-worse-than-scientists-thought/?sh=34e3d1152c63')

def checkscreen(screenno):
    if screenno == 0:
        return mainmenu()
    elif screenno == 1:
        return mainscreen()
    elif screenno == 2:
        return dailyactivities()
    elif screenno == 3:
        return checkweeklytotal()
    elif screenno == 4:
        return links()
def end():
    return
screenno = 0
data = open("datafile.txt",'r')
dataread = data.readlines()
data.close()
if dataread[13].rstrip() == '0': #logging in for the first time
    dataread[13] = str(time.time() // 604800 * 604800 + 345600)+'\n'
    data = open("datafile.txt",'w')
    data.writelines(dataread)
    print(dataread[13])
    data.close()
if time.time() - float(dataread[13].rstrip()) >= 0: #weeklyreset
    dataread[13] =  str(float(dataread[13].rstrip()) + (((time.time() -  float(dataread[13].rstrip())) // 604800 +1)) * 604800)+'\n'
    for lineno in range(1,13):
        dataread[lineno] = "0\n"
    data = open("datafile.txt",'w')
    data.writelines(dataread)
    data.close()
turt.addallshapes(os.getcwd())
mainmenu()
