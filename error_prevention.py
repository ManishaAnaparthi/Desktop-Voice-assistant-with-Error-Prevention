import pyttsx3
import pywhatkit as pk
import wikipedia as wiki
import subprocess
import os
from textblob import TextBlob
from gingerit.gingerit import GingerIt
import speech_recognition as sr
listener=sr.Recognizer()


en = pyttsx3.init()
rate=en.getProperty('rate')
en.setProperty('rate',150)
parser=GingerIt()

def p():
    en.say("Please Enter your File")
    en.runAndWait()
    fname = input("Enter your file:")
    file = open(fname + '.txt', "w")
    file.write(result)
    file.close()
    en.say("if you want to add more text")
    en.runAndWait()
    en.say("please give conformation yes/no")
    en.runAndWait()
    conf = input("yes/no")
    if (conf == "yes"):
        en.say("please enter your text")
        en.runAndWait()

        text5 = input("enter text:")
        print("spaking....")
        en.say("analyzing your text")

        en.say("detecting errors.")

        en.say("correcting mistakes")
        en.runAndWait()
        correct = parser.parse(text5)
        result5 = str(correct["result"])

        en.say("the final output your text is")
        en.runAndWait()
        print("final output:" + result5)
        en.say("your text is verified")
        en.runAndWait()
        en.say("if you want save the text into the document")
        en.runAndWait()
        en.say("please say yes/no")
        en.runAndWait()
        cona = input("Enter yes/no:")
        if (cona == 'yes'):
            file1 = open(fname + '.txt', 'a')
            file1.write(result5)
            file1.close()
            en.say("your text append successfully")
            en.runAndWait()
            en.say("if you want to add more text")
            en.runAndWait()
            en.say("please give conformation yes/no")
            en.runAndWait()
            conf = input("yes/no")
            if (conf == "yes"):
                redoc()
            else:
                en.say("if want to read or listen your document data")
                en.runAndWait()
                en.say("please give your confirmation yes or no")
                en.runAndWait()
                conff = input("yes/no")
                if (conff == 'yes'):
                    doc = open(fname + '.txt', 'r')
                    dtext = doc.read()
                    en.say(dtext)
                    en.runAndWait()
                else:
                    en.say("it was nice talking to you" + name)
                    en.runAndWait()
                    en.say("good bye my friend")
                    en.runAndWait()
    else:
        en.say("if want to read or listen your document data")
        en.runAndWait()
        en.say("please give your confirmation yes or no")
        en.runAndWait()
        conff = input("yes/no")
        if (conff == 'yes'):
            doc = open(fname + '.txt', 'r')
            dtext = doc.read()
            en.say(dtext)
            en.runAndWait()
        else:
            en.say("it was nice talking to you" + name)
            en.runAndWait()
            en.say("good bye my friend")
            en.runAndWait()


def redoc():
    en.say("if you want to add more text")
    en.runAndWait()
    en.say("please give conformation yes/no")
    en.runAndWait()
    conf = input("yes/no")
    if (conf == "yes"):
        en.say("please enter your text")
        en.runAndWait()

        text3 = input("enter text:")
        print("spaking....")
        en.say("analyzing your text")

        en.say("detecting errors.")

        en.say("correcting mistakes")
        en.runAndWait()
        correct = parser.parse(text3)
        result3 = str(correct["result"])

        en.say("the final output your text is")
        en.runAndWait()
        print("final output:" + result3)
        en.say("your text is verified")
        en.runAndWait()
        en.say("if you want save the text into the document")
        en.runAndWait()
        en.say("please say yes/no")
        en.runAndWait()
        cona = input("Enter yes/no:")
        if (cona == 'yes'):
            file1 = open(fname + '.txt', 'a')
            file1.write(result3)
            file1.close()

            en.say("if want to read or listen your document data")
            en.runAndWait()
            en.say("please give your confirmation yes or no")
            en.runAndWait()
            conff = input("yes/no")
            if (conff == 'yes'):
                doc = open(fname + '.txt', 'r')
                dtext = doc.read()
                en.say(dtext)
                en.runAndWait()
                en.say("Your text is append successfully")
                en.runAndWait()
                en.say("if you want add more text")
                en.runAndWait()
                en.say("Give conformation yes or no")
                en.runAndWait()
                inpt = input("yes or no :")
                if (inpt == "yes"):
                    redoc()
                else:
                    en.say("it was nice talking to you" + name)
                    en.runAndWait()
                    en.say("good bye my friend")
                    en.runAndWait()

    else:
            en.say("if you want to retype the text")
            en.runAndWait()
            en.say("Give conformation yes or no")
            en.runAndWait()
            inpt = input("yes or no :")
            if (inpt == "yes"):
                redoc()
            else:
                en.say("it was nice talking to you" + name)
                en.runAndWait()
                en.say("good bye my friend")
                en.runAndWait()

def repbrow():
    en.say("please enter your command")
    en.runAndWait()
    print("please type your command!")
    txt = input("search:")
    correct = parser.parse(txt)
    result = str(correct["result"])
    print("speaking.................")
    en.say(f"Are you looking for :" + result)
    en.say("give your validation in yes/no")
    en.runAndWait()
    print(f"final user query is:" + result)
    print("speaking....")
    valid = (input("Are you looking for above final query your answer(Y/N):"))
    if ((valid == 'y') | (valid == "Y")):
        en.say("we are  searching query ")
        en.runAndWait()
        if 'play' in result:
            result = result.replace('play', '')
            print('playing' + result)
            en.say('playing' + result + 'enjoy my friend')
            en.runAndWait()
            pk.playonyt(result)
        elif 'search for' in result or 'google' in result:
            result = result.replace('search for', '')
            result = result.replace('google', '')
            print('searching for' + result)
            en.say('searchimg for' + result)
            en.runAndWait()
            pk.search(result)
        elif 'who is' in result or 'what is' in result:
            result = result.replace('who is', '')
            result = result.replace('what is', '')
            print('searching for' + result)
            info = wiki.summary(result, 3)
            print(info)
            en.say(info)
            en.runAndWait()
            en.say('if u want to browse anything?')
            en.runAndWait()
            repeat = input("please enter yes or no:")
            if (repeat == "yes"):
                repbrow();
            else:
                en.say("it was nice talking to you ")
                en.say("See you again my friend")
                en.runAndWait()


    else:
        print("speaking.....")
        en.say("invalid browsing url")
        en.say("Are you retype the Browsing Url")
        en.say("please type yes/no")
        en.runAndWait()
        retype = input("yes/no:")
        if ((retype == "yes") | (retype == "YES")):
            retypequery()

        else:
            print("speaking.....")
            en.say("has a nice talking to you my dear friend")
            en.say("bye")
            en.runAndWait();

def retypeopt():
    print("speaking....")
    en.say("we offered Three types of operations:")
    en.runAndWait()
    en.say("1 Web browsing")
    en.runAndWait()
    print("1.web browsing")
    en.say("2 Documentation")
    en.runAndWait()
    print("2.Documentation")
    en.say("3 searching")
    en.runAndWait()
    print("3.searching")
    en.say("please select one of them")
    en.runAndWait()
    inp = input("choose-1/2/3:")

    if (inp == '1'):
        print("speaking.....")
        en.say("welcome to web browsing")
        en.say("plase type your command or query")
        en.runAndWait()
        print("welcome to web browsing!")
        print("please type your command!")
        txt = input("search:")
        correct = parser.parse(txt)
        result = str(correct["result"])
        print("speaking.................")
        en.say(f"Are you looking for :" + result)
        en.say("give your validation in yes/no")

        en.runAndWait()
        print(f"final user query is:" + result)
        print("speaking....")
        valid = (input("Are you looking for above final query your answer(Y/N):"))
        if ((valid == 'y') | (valid == "Y")):
            en.say("we are  searching query ")
            en.runAndWait()
        else:
            print("speaking.....")
            en.say("invalid browsing url")
            en.say("Are you retype the Browsing Url")
            en.say("please type yes/no")
            en.runAndWait()
            retype = input("yes/no:")
            if ((retype == "yes") | (retype == "YES")):
                retypequery()

            else:
                print("speaking.....")
                en.say("has a nice talking to you my dear friend")
                en.say("bye")
                en.runAndWait();
    elif (inp == '2'):
        en.say("welcome to documentation")
        print("speaking...")
        en.say("please enter your test")
        en.runAndWait()
        print("welcome to documentation!")
        text = input("enter text:")
        print("spaking....")
        en.say("analyzing your text")

        en.say("detecting errors.")

        en.say("correcting mistakes")
        en.runAndWait()
        correct = parser.parse(text)
        result = str(correct["result"])

        en.say("the final output your text is")
        print("final output:" + result)
        en.say("your text is verified")
        en.runAndWait()
    elif (inp == '3'):
        print("speaking....")
        en.say("Welcome to searching system native features")
        en.runAndWait()
        print("welcome to searching system native features!")
        en.say("enter your command:")
        en.runAndWait()
        command = input("enter command:")
        print("speaking.....")
        en.say("verfying your command")
        en.runAndWait()
        en.say("validating your command")
        en.runAndWait()
        correct = parser.parse(command)
        result = str(correct["result"])
        print("Are you looking for:" + result)
        print("speaking.................")
        en.say(f"Are you looking for :" + result)
        en.say("give your validation in yes/no")

        en.runAndWait()
        print(f"final user query is:" + result)
        print("speaking...")
        valid = (input("Are you looking for above final query your answer(Y/N):"))
        if ((valid == 'y') | (valid == "Y")):
            en.say("we are  searching query ")
            en.runAndWait()
        else:
            print("speaking.....")
            en.say("you are entered invalid browsing url")
            en.say("Are you retype the Command")
            en.say("please type yes/no")
            en.runAndWait()
            retype = input("yes/no:")
            if ((retype == "yes") | (retype == "YES")):
                retypecommand()

            else:
                print("speaking....")
                en.say("has a nice talking to you my dear friend")
                en.say("bye")
                en.runAndWait();

    else:
        print("invalid input")
        print("speaking")
        en.say("your choosing invalid operation")
        en.say("if want to select the valid operation one more time")
        en.say("types yes/no")
        en.runAndWait()
        valid = input("yes/no:")
        if (valid == "yes"):
            print("speaking....")
            en.say("carefully listen the we offered operations")
            en.say("choose available operations")
            retypeopt()
        else:
            print("speaking....")
            en.say("it was nice taliking to " + name)
            en.say("good bye my friend")
            en.runAndWait()


def retypecommand():
    en.say("enter your command:")
    en.runAndWait()
    command = input("enter command:")
    print("speaking.....")
    en.say("verfying your command")
    en.runAndWait()
    en.say("validating your command")
    en.runAndWait()
    correct = parser.parse(command)
    result = str(correct["result"])
    print("Are you looking for:" + result)
    print("speaking.................")
    en.say(f"Are you looking for :" + result)
    en.say("give your validation in yes/no")

    en.runAndWait()
    print(f"final user query is:" + result)
    print("speaking...")
    valid = (input("Are you looking for above final query your answer(Y/N):"))
    if ((valid == 'y') | (valid == "Y")):
        en.say("we are  searching query ")
        en.runAndWait()
        if (result == 'camera' or result == 'Camera'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.WindowsCamera_2021.105.10.0_x64__8wekyb3d8bbwe/WindowsCamera.exe')
        elif (result == 'internet explorer' or result == 'internetexplorer' or result == 'Internet explorer'):
            subprocess.call('C:/Program Files/Internet Explorer/iexplore.exe')
        elif (result == 'music' or result == 'groovemusic' or result == 'groove music'):
            subprocess.call(
                'C:/Program Files/WindowsApps/Microsoft.ZuneMusic_10.21061.10121.0_x64__8wekyb3d8bbwe/Music.UI.exe')
        elif (result == 'notepad' or result == 'Notepad'):
            subprocess.call(
                'C:/Program Files/WindowsApps/Microsoft.WindowsNotepad_10.2103.6.0_x64__8wekyb3d8bbwe/Notepad/Notepad.exe')
        elif (result == 'Camera' or result == 'camera'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.WindowsCamera_2021.105.10.0_x64__8wekyb3d8bbwe/WindowsCamera.exe')
        elif (result == 'Calculator' or result == 'calculator'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.WindowsCalculator_10.2103.8.0_x64__8wekyb3d8bbwe/Calculator.exe')
        elif (result == 'clock' or result == 'alram' or result == 'Alram' or result == 'Clock'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.WindowsAlarms_10.2101.28.0_x64__8wekyb3d8bbwe/Time.exe')
        elif (result == 'paint' or result == 'Paint'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.Paint_10.2104.17.0_x64__8wekyb3d8bbwe\PaintApp/mspaint.exe')
        elif (result == 'Photos' or result == 'Photos'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.Windows.Photos_2021.21070.22007.0_x64__8wekyb3d8bbwe/Microsoft.Photos.exe')
        elif (result == 'Xbox' or result == 'xbox' or result == 'games' or result == 'Games'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.XboxIdentityProvider_12.80.11001.0_x64__8wekyb3d8bbwe/XboxIdp.exe')
        elif (result == 'powershell' or result == 'Powershell' or result == 'power shell' or result == 'Power shell'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_1.10.2383.0_x64__8wekyb3d8bbwe/WindowsTerminal.exe')
        elif (result == 'store' or result == 'Store' or result == 'Microsoft store' or result == 'microsoft store'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.WindowsStore_12107.1001.15.0_x64__8wekyb3d8bbwe/WinStore.App.exe')
        elif (result == 'weather' or result == 'Weather'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.BingWeather_4.46.31121.0_x64__8wekyb3d8bbwe/Microsoft.Msn.Weather.exe')
        elif (result == 'cortana' or result == 'Cortana'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.549981C3F5F10_3.2108.25001.0_x64__8wekyb3d8bbwe/Cortana.exe')
        elif (result == 'vlc' or result == 'Vlc' or result == 'vlc player' or result == 'Vlc player'):
            subprocess.call('C:\Program Files\VideoLAN\VLC/vlc.exe')
        elif (result == 'Help' or result == 'help' or result == 'gethelp' or result == 'Gethelp'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.GetHelp_10.2108.42454.0_x64__8wekyb3d8bbwe/GetHelp.exe')
        elif (result == 'skype' or result == 'Skype'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.SkypeApp_15.68.96.0_x86__kzf8qxf38zg5c\Skype/Skype.exe')
        elif (result == 'whiteboard' or result == 'Whiteboard'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.Whiteboard_21.10913.5785.0_x64__8wekyb3d8bbwe/WhiteboardWRT.exe')
        elif (
                result == 'microsoft edge' or result == 'Microsoft edge' or result == 'Microsoftedge' or result == 'microsoftedge'):
            subprocess.call('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
        elif (result == 'chrome' or result == 'Chroome' or result == 'google chrome' or result == 'Google chrome '):
            subprocess.call('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        elif (result == 'file explorer' or result == 'File explorer' or result == 'explorer' or result == 'Explorer'):
            subprocess.call("explorer.exe")
        elif (result == 'command prompt' or result == 'Command prompt' or result == 'cmd' or result == 'Cmd'):
            subprocess.call("cmd.exe")
        elif (result == 'settings' or result == 'settings' or result == 'setting' or result == 'Setting'):
            subprocess.call('C:\WINDOWS\System32/control.exe')
        elif (result == 'whatsapp' or result == 'Whatsapp'):
            os.startfile(result + ':')
        else:
            os.startfile(result + ':')
    else:
        print("speaking.....")
        en.say("you are entered invalid browsing url")
        en.say("Are you retype the Command")
        en.say("please type yes/no")
        en.runAndWait()
        retype = input("yes/no:")
        if ((retype == "yes") | (retype == "YES")):
            retypecommand()

        else:
            print("speaking....")
            en.say("has a nice talking to you my dear friend")
            en.say("bye")
            en.runAndWait()


def retypequery():
    en.say("plase type your command or query")
    en.runAndWait()
    print("welcome to web browsing!")
    print("please type your command!")
    txt = input("search:")
    correct = parser.parse(txt)
    result = str(correct["result"])
    print("speaking.................")
    en.say(f"Are you looking for :" + result)
    en.say("give your validation in yes/no")

    en.runAndWait()
    print(f"final user query is:" + result)
    print("speaking....")
    valid = (input("Are you looking for above final query your answer(Y/N):"))
    if ((valid == 'y') | (valid == "Y")):
        en.say("we are  searching query ")
        en.runAndWait()
    else:
        print("speaking.....")
        en.say("invalid browsing url")
        en.say("Are you retype the Browsing Url")
        en.say("please type yes/no")
        en.runAndWait()
        retype = input("yes/no:")
        if ((retype == "yes") | (retype == "YES")):
            retypequery()

        else:
            print("speaking.....")
            en.say("has a nice talking to you my dear friend")
            en.say("bye")
            en.runAndWait()






print("speaking....")
en.say("Hai my dear friend")
en.say("my name is bob")
en.say("what is your name?")
en.runAndWait()
name=input("enter your name:")
print("speaking...")
en.say("hai"+name)
en.say("Welcome to my world!")
en.runAndWait()
print("speaking....")
en.say("we offered Three types of operations:")
en.runAndWait()
en.say("1 Web browsing")
en.runAndWait()
print("1.web browsing")
en.say("2 Documentation")
en.runAndWait()
print("2.Documentation")
en.say("3 searching Native features")
en.runAndWait()
print("3.searching native features")
en.say("please select one of them")
en.runAndWait()
inp=input("choose-1/2/3:")

if(inp=='1'):
    print("speaking.....")
    en.say("welcome to web browsing")
    en.runAndWait()
    print("welcome to web browsing!")
    print("speaking....")
    en.say("plase type your command or query")
    en.runAndWait()
    print("please type your command!")
    txt=input("search:")
    correct=parser.parse(txt)
    result=str(correct["result"])
    print("speaking.................")
    en.say(f"Are you looking for :"+result)
    en.say("give your validation in yes/no")

    en.runAndWait()
    print(f"final user query is:"+result)
    print("speaking....")
    valid = (input("Are you looking for above final query your answer(Y/N):"))
    if ((valid == 'y') | (valid == "Y")):
        en.say("we are  searching query ")
        en.runAndWait()
        if 'play' in result:
            result=result.replace('play','')
            print('playing'+result)
            en.say('playing'+result+'enjoy my friend')
            en.runAndWait()
            pk.playonyt(result)
            en.say('if u want to browse anything?')
            en.runAndWait()
            repeat = input("please enter yes or no:")
            if (repeat == "yes"):
                repbrow();
            else:
                en.say("it was nice talking to you ")
                en.say("See you again my friend")
                en.runAndWait()
        elif 'search for' in result or 'google' in result:
            result=result.replace('search for','')
            result=result.replace('google','')
            print('searching for'+result)
            en.say('searchimg for'+result)
            en.runAndWait()
            pk.search(result)
            en.say('if u want to browse anything?')
            en.runAndWait()
            repeat = input("please enter yes or no:")
            if (repeat == "yes"):
                repbrow();
            else:
                en.say("it was nice talking to you ")
                en.say("See you again my friend")
                en.runAndWait()
        elif 'who is' in result or 'what is' in result:
            result = result.replace('who is', '')
            result = result.replace('what is', '')
            print('searching for' + result)
            info=wiki.summary(result,2)
            print(info)
            en.say(info)
            en.runAndWait()
            print("speaking....")
            en.say('if u want to browse anything?')
            en.runAndWait()
            print("speaking....")
            repeat=input("please enter yes or no:")
            if(repeat=="yes"):
                repbrow();
            else:
                print("speaking....")
                en.say("it was nice talking to you ")
                en.say("See you again my friend")
                en.runAndWait()


    else:
        print("speaking.....")
        en.say("invalid browsing url")
        en.say("Are you retype the Browsing Url")
        en.say("please type yes/no")
        en.runAndWait()
        retype = input("yes/no:")
        if ((retype == "yes") | (retype == "YES")):
            retypequery()

        else:
            print("speaking.....")
            en.say("has a nice talking to you my dear friend")
            en.say("bye")
            en.runAndWait();
elif(inp=='2'):
    en.say("welcome to documentation")
    en.runAndWait()
    print("welcome to documentation!")
    print("speaking...")
    en.say("please enter your text")
    en.runAndWait()

    text=input("enter text:")
    print("spaking....")
    en.say("analyzing user command")
    en.runAndWait()
    print("Analyzing user command!")
    en.say("detecting errors.")
    en.runAndWait()
    print("Detecting Errors!")
    en.say("correcting mistakes")
    en.runAndWait()
    print("Correcting Mistakes!")
    correct = parser.parse(text)
    result = str(correct["result"])

    en.say("the final output your text is")
    en.runAndWait()
    print("final output:"+result)
    en.say("your text is verified")
    en.runAndWait()
    en.say("if you want save the text into the document")
    en.runAndWait()
    en.say("please say yes/no")
    en.runAndWait()
    con=input("Enter yes/no:")
    if(con=='yes'):
        en.say("Please Enter your File name")
        en.runAndWait()
        fname = input("Enter your file name:")
        file = open(fname + '.txt', "w")
        file.write(result)
        file.close()
        en.say("Your text is successfully insert into the file")
        en.runAndWait()
        en.say("if you want to add more text")
        en.runAndWait()
        en.say("please give conformation yes/no")
        en.runAndWait()
        conf = input("yes/no")
        if (conf == "yes"):
            en.say("please enter your text")
            en.runAndWait()

            text5 = input("enter text:")
            print("spaking....")
            en.say("analyzing user command!")
            en.runAndWait()
            print("Analyzing user command!")
            print("speaking....")
            en.say("detecting errors.")
            en.runAndWait()
            print("Detecting Errors!")
            print("Speaking....")
            en.say("correcting mistakes")
            en.runAndWait()
            print("Correcting Mistakes!")
            print("speaking....")
            correct = parser.parse(text5)
            result5 = str(correct["result"])

            en.say("the final output your text is")
            en.runAndWait()
            print("final output:" + result5)
            en.say("your text is verified")
            en.runAndWait()
            en.say("if you want save the text into the document")
            en.runAndWait()
            en.say("please say yes/no")
            en.runAndWait()
            cona = input("Enter yes/no:")
            if (cona == 'yes'):
                file1 = open(fname + '.txt', 'a')
                file1.write(result5)
                file1.close()
                en.say("your text append successfully")
                en.runAndWait()
                en.say("if you want to add more text")
                en.runAndWait()
                en.say("please give conformation yes/no")
                en.runAndWait()
                conf = input("yes/no")
                if (conf == "yes"):
                    redoc()
                else:
                    en.say("if want to read or listen your document data")
                    en.runAndWait()
                    en.say("please give your confirmation yes or no")
                    en.runAndWait()
                    conff = input("yes/no")
                    if (conff == 'yes'):
                        doc = open(fname + '.txt', 'r')
                        dtext = doc.read()
                        en.say(dtext)
                        en.runAndWait()
                        print(dtext)
                        en.say("It was nice talking to you my dear friend!")
                        en.say("Good bye  my friend")
                        en.runAndWait()
        else:
            en.say("if want to read or listen your document data")
            en.runAndWait()
            en.say("please give your confirmation yes or no")
            en.runAndWait()
            conff = input("yes/no")
            if (conff == 'yes'):
                doc = open(fname + '.txt', 'r')
                dtext = doc.read()
                en.say(dtext)
                en.runAndWait()
                print(dtext)
            else:
                en.say("it was nice talking to you" + name)
                en.runAndWait()
                en.say("good bye my friend")
                en.runAndWait()


    else:
            en.say("if you want to retype the text")
            en.runAndWait()
            en.say("Give conformation yes or no")
            en.runAndWait()
            inpt=input("yes or no :")
            if(inpt=="yes"):
                redoc()
            else:
                    en.say("it was nice talking to you"+name)
                    en.runAndWait()
                    en.say("good bye my friend")
                    en.runAndWait()

elif(inp=='3'):
    print("speaking....")
    en.say("Welcome to searching system native features")
    en.runAndWait()
    print("welcome to searching system native features!")
    en.say("enter your command:")
    en.runAndWait()
    command=input("enter command:")
    print("speaking.....")
    en.say("verfying user command")
    en.runAndWait()
    print("Verifying user command!")
    print("speaking....")
    en.say("validating your command")
    en.runAndWait()
    print("Validating user command!")
    correct = parser.parse(command)
    result = str(correct["result"])
    print("speaking....")
    print("Are you looking for:"+result)
    print("speaking.................")
    en.say(f"Are you looking for :"+result)
    en.say("give your validation in yes/no")

    en.runAndWait()
    print(f"final user query is:"+result)
    print("speaking...")
    valid = (input("Are you looking for above final query your answer(Y/N):"))
    if ((valid == 'y') | (valid == "Y")):
        en.say("we are  searching query ")
        en.runAndWait()
        if (result == 'camera' or result == 'Camera'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.WindowsCamera_2021.105.10.0_x64__8wekyb3d8bbwe/WindowsCamera.exe')
        elif (result == 'internet explorer' or result == 'internetexplorer' or result == 'Internet explorer'):
            subprocess.call('C:/Program Files/Internet Explorer/iexplore.exe')
        elif (result == 'music' or result == 'groovemusic' or result == 'groove music'):
            subprocess.call(
                'C:/Program Files/WindowsApps/Microsoft.ZuneMusic_10.21061.10121.0_x64__8wekyb3d8bbwe/Music.UI.exe')
        elif (result == 'notepad' or result == 'Notepad'):
            subprocess.call(
                'C:/Program Files/WindowsApps/Microsoft.WindowsNotepad_10.2103.6.0_x64__8wekyb3d8bbwe/Notepad/Notepad.exe')
        elif (result == 'Camera' or result == 'camera'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.WindowsCamera_2021.105.10.0_x64__8wekyb3d8bbwe/WindowsCamera.exe')
        elif (result == 'Calculator' or result == 'calculator'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.WindowsCalculator_10.2103.8.0_x64__8wekyb3d8bbwe/Calculator.exe')
        elif (result == 'clock' or result == 'alram' or result == 'Alram' or result == 'Clock'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.WindowsAlarms_10.2101.28.0_x64__8wekyb3d8bbwe/Time.exe')
        elif (result == 'paint' or result == 'Paint'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.Paint_10.2104.17.0_x64__8wekyb3d8bbwe\PaintApp/mspaint.exe')
        elif (result == 'Photos' or result == 'Photos'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.Windows.Photos_2021.21070.22007.0_x64__8wekyb3d8bbwe/Microsoft.Photos.exe')
        elif (result == 'Xbox' or result == 'xbox' or result == 'games' or result == 'Games'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.XboxIdentityProvider_12.80.11001.0_x64__8wekyb3d8bbwe/XboxIdp.exe')
        elif (result == 'powershell' or result == 'Powershell' or result == 'power shell' or result == 'Power shell'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_1.10.2383.0_x64__8wekyb3d8bbwe/WindowsTerminal.exe')
        elif (result == 'store' or result == 'Store' or result == 'Microsoft store' or result == 'microsoft store'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.WindowsStore_12107.1001.15.0_x64__8wekyb3d8bbwe/WinStore.App.exe')
        elif (result == 'weather' or result == 'Weather'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.BingWeather_4.46.31121.0_x64__8wekyb3d8bbwe/Microsoft.Msn.Weather.exe')
        elif (result == 'cortana' or result == 'Cortana'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.549981C3F5F10_3.2108.25001.0_x64__8wekyb3d8bbwe/Cortana.exe')
        elif (result == 'vlc' or result == 'Vlc' or result == 'vlc player' or result == 'Vlc player'):
            subprocess.call('C:\Program Files\VideoLAN\VLC/vlc.exe')
        elif (result == 'Help' or result == 'help' or result == 'gethelp' or result == 'Gethelp'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.GetHelp_10.2108.42454.0_x64__8wekyb3d8bbwe/GetHelp.exe')
        elif (result == 'skype' or result == 'Skype'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.SkypeApp_15.68.96.0_x86__kzf8qxf38zg5c\Skype/Skype.exe')
        elif (result == 'whiteboard' or result == 'Whiteboard'):
            subprocess.call(
                'C:\Program Files\WindowsApps\Microsoft.Whiteboard_21.10913.5785.0_x64__8wekyb3d8bbwe/WhiteboardWRT.exe')
        elif (
                result == 'microsoft edge' or result == 'Microsoft edge' or result == 'Microsoftedge' or result == 'microsoftedge'):
            subprocess.call('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
        elif (result == 'chrome' or result == 'Chroome' or result == 'google chrome' or result == 'Google chrome '):
            subprocess.call('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        elif (result == 'file explorer' or result == 'File explorer' or result == 'explorer' or result == 'Explorer'):
            subprocess.call("explorer.exe")
        elif (result == 'command prompt' or result == 'Command prompt' or result == 'cmd' or result == 'Cmd'):
            subprocess.call("cmd.exe")
        elif (result == 'settings' or result == 'settings' or result == 'setting' or result == 'Setting'):
            subprocess.call('C:\WINDOWS\System32/control.exe')
        elif (result == 'whatsapp' or result == 'Whatsapp'):
            os.startfile(result + ':')
        else:
            os.startfile(result + ':')
    else:
        print("speaking.....")
        en.say("you are entered invalid browsing url")
        en.say("Are you retype the Command")
        en.say("please type yes/no")
        en.runAndWait()
        retype = input("yes/no:")
        if ((retype == "yes") | (retype == "YES")):
            retypecommand()

        else:
            print("speaking....")
            en.say("has a nice talking to you my dear friend")
            en.say("bye")
            en.runAndWait();

else:
    print("invalid input")
    print("speaking....")
    en.say("your choosing invalid operation");
    en.say("if want to select the valid operation one more time")
    en.say("types yes/no")
    en.runAndWait()
    valid=input("yes/no:")
    if(valid=="yes"):
        print("speaking....")
        en.say("carefully listen the we offered operations")
        en.say("choose available operations")
        retypeopt()
    else:
        print("speaking....")
        en.say("it was nice meeting to "+name)
        en.say("good bye my friend")
        en.runAndWait()

