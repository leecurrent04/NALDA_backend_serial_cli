from lib.MiniLink import MiniLink
from lib.userInputHandler import UserInputHandler

mav = MiniLink()
userInput = UserInputHandler()

port, baudrate = userInput.chooseInit()
mav.connect(port, baudrate)

userInput.updateMessageList(mav.getMessageList())

while True:
    retVal : list = userInput.whileInputHandler()
    match(retVal[0]):
        case 'chg_msg': mav.chooseMessage(retVal[1])
        case 'send_msg' : mav.send(retVal[1])

    # True or False
    data : list = mav.read(enPrint=True, enLog=True)

    # Edit Here
    # If you want to access value
    # if(data != None):
    #     print(data)

