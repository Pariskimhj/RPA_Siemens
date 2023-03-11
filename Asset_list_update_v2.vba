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
Dim CostCenter_From As String
Dim CostCenter_To As String
Dim Layout As String
Dim Year
Dim Month
Dim Day

Year = Format(Date, "yy")
Month = Format(Date, "mm")
Day = Format(Date, "dd")

Report_date = ActiveWorkbook.ActiveSheet.Cells(2, 3).Value
CostCenter_From = ActiveWorkbook.ActiveSheet.Cells(2, 4).Value
CostCenter_To = ActiveWorkbook.ActiveSheet.Cells(2, 5).Value
Layout = ActiveWorkbook.ActiveSheet.Cells(2, 6).Value
folderPath = ActiveWorkbook.ActiveSheet.Cells(2, 7).Value

session.findById("wnd[0]").maximize
session.findById("wnd[0]/tbar[0]/okcd").Text = "ar01"
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/ctxtBUKRS-LOW").Text = "kr10"
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/ctxtSO_KOSTL-LOW").Text = CostCenter_From
session.findById("wnd[0]/usr/ctxtSO_KOSTL-LOW").SetFocus
session.findById("wnd[0]/usr/ctxtSO_KOSTL-LOW").caretPosition = 6
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/ctxtSO_KOSTL-HIGH").Text = CostCenter_To
session.findById("wnd[0]/usr/ctxtSO_KOSTL-HIGH").SetFocus
session.findById("wnd[0]/usr/ctxtSO_KOSTL-HIGH").caretPosition = 6
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/ctxtBERDATUM").Text = Report_date
session.findById("wnd[0]/usr/ctxtSRTVR").Text = "0014"
session.findById("wnd[0]/usr/ctxtP_VARI").Text = Layout
session.findById("wnd[0]/usr/ctxtP_VARI").SetFocus
session.findById("wnd[0]/usr/ctxtP_VARI").caretPosition = 11
session.findById("wnd[0]/tbar[1]/btn[8]").press
session.findById("wnd[0]/mbar/menu[0]/menu[1]/menu[1]").Select
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/usr/ctxtDY_PATH").Text = folderPath
session.findById("wnd[1]/usr/ctxtDY_FILENAME").Text = Year & Month & Day & " Asset List" & ".XLSX"
session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 5
session.findById("wnd[1]/tbar[0]/btn[0]").press

MsgBox "Asset list Update Completed."


End Sub