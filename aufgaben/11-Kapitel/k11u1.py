"""
Aufgabe K11 | A1: Folgendes Dictionary ist gegeben:

tel = {
‘arbeit: {‘Jan‘: ‘50‘, ‘Mark‘: ‘81'},
'private': {'Julia': '0151438924', 'Mark': '016932834'}
}

Welche Ausgaben liefern folgende Befehle:
1. len(tel)
2. len(tel['arbeit'])
3. tel['arbeit'].get('Mark'')
4. 'Jan' in tel['arbeit']
5. list(tel['private'].values())
6. tel['private'].copy()
"""


tel = {
    'arbeit': {'Jan': '50', 'Mark': '81'},
    'private': {'Julia': '0151438924', 'Mark': '016932834'}
}


print(len(tel))
print(len(tel['arbeit']))
print(tel['arbeit'].get('Mark'))
print('Jan' in tel['arbeit'])
print(list(tel['private'].values()))
print(tel['private'].copy())
