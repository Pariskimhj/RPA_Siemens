Public Sub Asset_list_Update()

Dim SapGuiAuto As Object
Dim Application As Object
Dim Connection As Object
Dim session As Object

Set SapGuiAuto = GetObject("SAPGUI")
Set Application = SapGuiAuto.GetScriptingEngine
Set Connection = Application.Children(0)
Set session = Connection.Children(0)

Dim folderPath As String
Dim Report_date As String
Dim Year
Dim Month
Dim Day

Year = Format(Date, "yy")
Month = Format(Date, "mm")
Day = Format(Date, "dd")

folderPath = ActiveWorkbook.ActiveSheet.Cells(2, 4).Value
Report_date = ActiveWorkbook.ActiveSheet.Cells(2, 3).Value

session.findById("wnd[0]").Maximize
session.findById("wnd[0]/tbar[0]/okcd").Text = "ar01"
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/ctxtBUKRS-LOW").Text = "kr10"
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/ctxtSO_KOSTL-LOW").Text = "652000"
session.findById("wnd[0]/usr/ctxtSO_KOSTL-LOW").SetFocus
session.findById("wnd[0]/usr/ctxtSO_KOSTL-LOW").caretPosition = 6
session.findById("wnd[0]").sendVKey 4
session.findById("wnd[1]").Close
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/ctxtSO_KOSTL-HIGH").Text = "652002"
session.findById("wnd[0]/usr/ctxtSO_KOSTL-HIGH").SetFocus
session.findById("wnd[0]/usr/ctxtSO_KOSTL-HIGH").caretPosition = 6
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/ctxtBERDATUM").Text = Report_date
session.findById("wnd[0]/usr/ctxtSRTVR").Text = "0014"
session.findById("wnd[0]/usr/ctxtSRTVR").SetFocus
session.findById("wnd[0]/usr/ctxtSRTVR").caretPosition = 4
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/tbar[1]/btn[8]").press
session.findById("wnd[0]/tbar[1]/btn[33]").press
session.findById("wnd[1]/usr/lbl[14,18]").SetFocus
session.findById("wnd[1]/usr/lbl[14,18]").caretPosition = 8
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[0]/mbar/menu[0]/menu[1]/menu[1]").Select
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/usr/ctxtDY_PATH").Text = folderPath
session.findById("wnd[1]/usr/ctxtDY_FILENAME").Text = Year & Month & Day & " Asset List" & ".XLSX"
session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 5
session.findById("wnd[1]/tbar[0]/btn[0]").press

MsgBox "Asset list Update Completed."


End Sub