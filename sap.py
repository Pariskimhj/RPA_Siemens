import win32com.client
import sys
import subprocess
import time
import pyautogui
from datetime import date

class SapGui():
    def __init__(self):
        self.path = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
        subprocess.Popen(self.path)
        time.sleep(5)
        
        self.SapGuiAuto = win32com.client.GetObject("SAPGUI")
        if not type(self.SapGuiAuto) == win32com.client.CDispatch:
            return
        
        application = self.SapGuiAuto.GetScriptingEngine
        # self.connection = application.OpenConnection("AP0 SSO - Spiridon - Productive Singapore", True)
        self.connection = application.OpenConnection("P41 - SHS - ERP Production", True)
        time.sleep(3)
        self.session = self.connection.Children(0)

    def Asset_list(self):
        Report_date = pyautogui.prompt(title = 'Report date', text = '조회하고자하는 Report date를 입력하세요. (ex. 01.11.2022)')
        today = date.today().strftime("%y%m%d")
        folderpath = r"W:\050 PLM\091. Asset\Archived\Updated Asset List"
        # Report_date = input('Report date를 입력하세요(ex. 01.11.2022)')
        
        self.session.findById("wnd[0]").maximize
        self.session.findById("wnd[0]/tbar[0]/okcd").text = "ar01"
        self.session.findById("wnd[0]").sendVKey(0)
        self.session.findById("wnd[0]/usr/ctxtBUKRS-LOW").text = "kr10"
        self.session.findById("wnd[0]").sendVKey(0)
        self.session.findById("wnd[0]/usr/ctxtSO_KOSTL-LOW").text = "652000"
        self.session.findById("wnd[0]/usr/ctxtSO_KOSTL-HIGH").text = "652002"
        self.session.findById("wnd[0]/usr/ctxtSO_KOSTL-HIGH").setFocus
        self.session.findById("wnd[0]/usr/ctxtSO_KOSTL-HIGH").caretPosition = 6
        self.session.findById("wnd[0]").sendVKey(0)
        self.session.findById("wnd[0]/usr/ctxtBERDATUM").text = Report_date
        self.session.findById("wnd[0]/usr/ctxtSRTVR").text = "0014"
        self.session.findById("wnd[0]/usr/ctxtP_VARI").text = "SUSKO ASSET"
        self.session.findById("wnd[0]/usr/ctxtP_VARI").setFocus
        self.session.findById("wnd[0]/usr/ctxtP_VARI").caretPosition = 11
        self.session.findById("wnd[0]").sendVKey(0)
        time.sleep(3)
        self.session.findById("wnd[0]/tbar[1]/btn[8]").press()
        self.session.findById("wnd[0]/mbar/menu[0]/menu[1]/menu[1]").select
        self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = folderpath
        self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = today + " Asset List.XLSX"
        self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 6
        self.session.findById("wnd[1]/tbar[0]/btn[0]").press()


if __name__ == '__main__':
    window = Tk()
    window.geometry('200x60')
    btn = Button(window, text="Login SAP", command= lambda : SapGui())
    btn.pack()
    mainloop()