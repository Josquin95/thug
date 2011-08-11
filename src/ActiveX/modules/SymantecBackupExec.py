# Symantec BackupExec
# CVE-2007-6016,CVE-2007-6017

acct = ActiveXAcct[self]

def Set_DOWText0(val):
    global acct

    if len(val) > 255:
        acct.add_alert('SymantecBackupExec overflow with property _DOWText0')

def Set_DOWText6(val):
    global acct

    if len(val) > 255:
        acct.add_alert('SymantecBackupExec overflow with property _DOWText6')

def Set_MonthText0(val):
    global acct

    if len(val) > 255:
        acct.add_alert('SymantecBackupExec overflow with property _MonthText0')

def Set_MonthText11(val):
    global acct

    if len(val) > 255:
        acct.add_alert('SymantecBackupExec overflow with property _MonthText11')

def Save(a, b):
    return

Attr2Fun['_DOWText0']    = Set_DOWText0
Attr2Fun['_DOWtext6']    = Set_DOWText6
Attr2Fun['_MonthText0']  = Set_MonthText0
Attr2Fun['_MonthText11'] = Set_MonthText11
self.Save                = Save
