"""
Aufgabe K11 | A2: Folgendes Dictionary ist gegeben:
tel = {
    'arbeit': {'Jan': '50', 'Mark': '81'},
    'private': {'Julia': '0151438924', 'Mark': '016932834'}
}

Folgende Operationen sollen durchgeführt werden:
1. Ändere nachträglich die interne Durchwahl von Mark zu 80.
2. Lösche die Eintrag von Julia inkl. Handynummer
3. Ändere den Namen Mark im privaten Bereich in „Murad“
"""


tel = {
    'arbeit': {'Jan': '50', 'Mark': '81'},
    'private': {'Julia': '0151438924', 'Mark': '016932834'}
}

tel['arbeit']['Mark'] = '0'
del tel['private']['Julia']
tel['private']['Samuel'] = tel['private'].pop('Mark')
print(tel)
