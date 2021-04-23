# This is the main file of Mellow Flow APP
import loginGui
import mainGui



def startMellowFlowApp():
    while(True):

        try:
            loginGui.main_account_screen()
            mainGui.startMain()
        except:
            return




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startMellowFlowApp()

