"""
This script will log console output
Opens Hyper terminal, does necessary configurations
Reads console output and writes to path mentioned in configuration

Dependenciescies : install pywinauto, set hypertrm executable file to PATH

Installing pywinauto:

$pip install pywinauto

Executing script:

$python consolelog.py start

    -- to start logging
	
$python consolelog.py stop

    -- to stop logging
	
$python consolelog.py exit

    -- to close hyperterminal window
"""

import sys
from time import sleep
from pywinauto import application, findwindows

FILE_PATH = "C:\\Users\\28520\\console.txt"
HYPERTERM_CONFIG_NAME = "Console_Log"

class LogConsoleOutput(object):
    """ Class to log console output
    Main functions include creating hyperterminal configuration
    And reading console output and writing to file system
    """

    def __init__(self, file_path):
        """ Constructor, does nothing as of now"""
        self.file_path = file_path

    def create_configuration(self, HYPER_TERM_APP):
        """ This will intiate hyper terminal"""
        pwa_app = application.Application()
        w_handle = findwindows.find_windows(title=u'Connection Description')[0]
        window = pwa_app.window_(handle=w_handle)
        ctr = window['Edit']
        ctr.TypeKeys(HYPERTERM_CONFIG_NAME, with_spaces=True)
        sleep(1)
        window.OK.Click()
        sleep(2)

        self.configure_connect_to_screen(HYPER_TERM_APP)
        sleep(2)
        self.configure_com_properties_screen()
        sleep(1)
        return

    def configure_connect_to_screen(self, HYPER_TERM_APP):
        """ This method will configure connect to screen"""
        pwa1_app = application.Application()
        w1_handle = findwindows.find_windows(title=u'Connect To')[0]
        window1 = pwa1_app.window_(handle=w1_handle)
        #import pdb;pdb.set_trace()
        print 'Selecting COM3 from drop down'
        try:
            window1.ComboBox2.Select('COM3')
            window1.OK.Click()
            sleep(1)
        except ValueError:
            window1.Cancel.Click()
            file_option = HYPER_TERM_APP[HYPERTERM_CONFIG_NAME +  ' - HyperTerminal']
            file_option.MenuSelect('File->Exit')
            sleep(1)
            w2_handle = findwindows.find_windows(title=u'HyperTerminal')[0]
            window2 = pwa1_app.window_(handle=w2_handle)
            window2.Yes.Click()
            try:
                w3_handle = findwindows.find_windows(title=u'HyperTerminal')[0]
                window3 = pwa1_app.window_(handle=w3_handle)
                window3.Yes.Click()
            except IndexError:
                pass
            sys.exit('Please connect com port')
        return

    def configure_com_properties_screen(self):
        """ This method will configure final screen"""
        pwa1_app = application.Application()
        w1_handle = findwindows.find_windows(title=u'COM3 Properties')[0]
        window1 = pwa1_app.window_(handle=w1_handle)
        import pdb;pdb.set_trace()
        window1.ComboBox1.Select('115200')
        sleep(1)
        window1.ComboBox5.Select('None')
        sleep(1)
        window1.OK.Click()
        return

    def start_capture_text(self, HYPER_TERM_APP):
        """ This method will capture Console Text"""
        print "start capturing text"
        file_option = HYPER_TERM_APP[HYPERTERM_CONFIG_NAME +  ' - HyperTerminal']
        file_option.MenuSelect('Transfer->Capture Text')

        # open capture text window
        pwa_app = application.Application()
        w_handle = findwindows.find_windows(title=u'Capture Text')[0]
        window1 = pwa_app.window_(handle=w_handle)
        window1.Browse.Click()

        wh_handle = findwindows.find_windows(title=u'Select Capture File')[0]
        window2 = pwa_app.window_(handle=wh_handle)
        ctrl1 = window2['Edit']
        ctrl1.TypeKeys(FILE_PATH)
        sleep(2)
        window2.Save.Click()

        try:
            wh1_handle = findwindows.find_windows(title=u'Confirm Save As')[0]
            window3 = pwa_app.window_(handle=wh1_handle)
            window3.Yes.Click()
            sleep(1)
        except IndexError:
            sleep(1)
            pass
        window1.Start.Click()
        return

    def stop_capture_text(self):
        """ This method will stop capturing text"""
        pwa_app = application.Application()
        try:
            w_handle = findwindows.find_windows(title=HYPERTERM_CONFIG_NAME +  ' - HyperTerminal')[0]
        except IndexError:
            sys.exit('Hyper Terminal is not running...:)')
        window = pwa_app.window_(handle=w_handle)
        try:
            window.MenuSelect('Transfer->Capture Text->Stop')
        except:
            sys.exit('Capturing is not started, Please start capture...')
        return

    def exit_hyper_terminal(self):
        """ This method is used to exit hyper terminal"""
        pwa_app = application.Application()
        try:
            w_handle = findwindows.find_windows(title=HYPERTERM_CONFIG_NAME +  ' - HyperTerminal')[0]
        except IndexError:
            sys.exit('Hyper Terminal is not running...:)')
        window = pwa_app.window_(handle=w_handle)
        window.MenuSelect('File->Exit')
        sleep(1)
        w2_handle = findwindows.find_windows(title=u'HyperTerminal')[0]
        window2 = pwa_app.window_(handle=w2_handle)
        window2.Yes.Click()
        try:
            w3_handle = findwindows.find_windows(title=u'HyperTerminal')[0]
            window3 = pwa_app.window_(handle=w3_handle)
            window3['&Yes'].Click()
            sleep(1)
            try:
                w4_handle = findwindows.find_windows(title=u'HyperTerminal')[0]
                window4 = pwa_app.window_(handle=w4_handle)
                window4['Yes'].Click()
            except IndexError:
                pass
        except IndexError:
            pass
        return

    def log_console_output(self, HYPER_TERM_APP):
        """ main function to intiatiate this script"""
        print "configuring hyperterm window"
        self.create_configuration(HYPER_TERM_APP)
        sleep(1)
        self.start_capture_text(HYPER_TERM_APP)
        return

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: %s <<start/stop/exit>>' % sys.argv[0])
    excute_option = sys.argv[1]
    LOGCONSOLE = LogConsoleOutput('FILE_PATH')
    if excute_option == 'start':
        HYPER_TERM_APP = application.Application.Start("notepad++.exe")
        LOGCONSOLE.log_console_output(HYPER_TERM_APP)
        sys.exit('Started logging console output')
    elif excute_option == 'stop':
        LOGCONSOLE.stop_capture_text()
        sys.exit('Stopped logging console output')
    elif excute_option == 'exit':
        LOGCONSOLE.exit_hyper_terminal()
        sys.exit('Closed Hyper Terminal')
    else:
        sys.exit('Usage: %s <<start/stop/exit>>' % sys.argv[0])

