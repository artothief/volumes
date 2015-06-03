__author__ = 'artothief'


import sqlite3


def save_db(database, liststore, cb_list, combo_list, entry_list):
    conn = sqlite3.connect(database)
    c = conn.cursor()

    for d in cb_list:
        ind = str(cb_list.index(d))
        value = d.get_active()
        c.execute("UPDATE OR IGNORE checkbuttons SET id = {0}, cb = ? WHERE id = {1}".format(ind, ind), (value,))
        c.execute('INSERT OR IGNORE INTO checkbuttons(id, cb) VALUES ({0}, ?)'.format(ind), (d.get_active(),))

    for a in combo_list:
        ind = str(combo_list.index(a))
        value = a.get_active()
        c.execute('UPDATE OR IGNORE combos SET id = {0}, com = ? WHERE id = {1}'.format(ind, ind), (value,))
        c.execute('INSERT OR IGNORE INTO combos(id, com) VALUES ({0}, ?)'.format(ind), (a.get_active(),))

    for e in entry_list:
        ind = str(entry_list.index(e))
        value = e.get_text()
        c.execute('UPDATE OR IGNORE entries SET id = {0}, ent = ? WHERE id = {1}'.format(ind, ind), (value,))
        c.execute('INSERT OR IGNORE INTO entries(id, ent) VALUES ({0}, ?)'.format(ind), (e.get_text(),))

    for val in liststore[0]:
        print(val[0])
        c.execute('''UPDATE OR IGNORE add_DP SET Name = ?, Capacity = ?, CE_Capacity = ?
                  WHERE Name = ? ''', (val[0], val[1], val[2], val[0]))
        c.execute('INSERT OR IGNORE INTO add_DP(Name, Capacity, CE_Capacity) VALUES (?,?,?)', (val[0], val[1], val[2]))

    for val in liststore[2]:
        c.execute('''UPDATE OR IGNORE add_HWDP SET Name = ?, Capacity = ?, CE_Capacity = ?
                  WHERE Name = ? ''', (val[0], val[1], val[2], val[0]))
        c.execute('INSERT OR IGNORE INTO add_HWDP(Name, Capacity, CE_Capacity) VALUES (?,?,?)', (val[0], val[1], val[2]))

    for val in liststore[3]:
        c.execute('''UPDATE OR IGNORE add_DC SET Name = ?, Capacity = ?, CE_Capacity = ?
                  WHERE Name = ? ''', (val[0], val[1], val[2], val[0]))
        c.execute('INSERT OR IGNORE INTO add_DC(Name, Capacity, CE_Capacity) VALUES (?,?,?)', (val[0], val[1], val[2]))

    for val in liststore[4]:
        c.execute('''UPDATE OR IGNORE add_MP SET Name = ?, Capacity = ?
                  WHERE Name = ? ''', (val[0], val[1], val[0]))
        c.execute('INSERT OR IGNORE INTO add_MP(Name, Capacity) VALUES (?,?)', (val[0], val[1]))

    for val in liststore[5]:
        c.execute('''UPDATE OR IGNORE add_OH SET Name = ?, Capacity = ?
                  WHERE Name = ? ''', (val[0], val[1], val[0]))
        c.execute('INSERT OR IGNORE INTO add_OH(Name, Capacity) VALUES (?,?)', (val[0], val[1]))

    conn.commit()
    c.close()
    return


def load_db(database, liststore):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS add_DP(Name VARCHAR UNIQUE , Capacity text, CE_Capacity)')
    c.execute('CREATE TABLE IF NOT EXISTS add_HWDP(Name VARCHAR UNIQUE, Capacity text, CE_Capacity)')
    c.execute('CREATE TABLE IF NOT EXISTS add_DC(Name VARCHAR UNIQUE, Capacity text, CE_Capacity)')
    c.execute('CREATE TABLE IF NOT EXISTS add_MP(Name VARCHAR UNIQUE, Capacity text)')
    c.execute('CREATE TABLE IF NOT EXISTS add_OH(Name VARCHAR UNIQUE, Capacity text)')

    c.execute('CREATE TABLE IF NOT EXISTS checkbuttons(id INTEGER PRIMARY KEY, cb BOOLEAN)')
    c.execute('CREATE TABLE IF NOT EXISTS combos(id INTEGER PRIMARY KEY, com INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS entries(id INTEGER PRIMARY KEY ,ent TEXT)')
    try:
        for row in c.execute('SELECT * FROM add_dp'):
                liststore[0].append(row)
    except Exception as e:
        print(e, 'No entries in Pipe database')

    try:
        for row in c.execute('SELECT * FROM add_HWDP'):
                liststore[2].append(row)
    except Exception as e:
        print(e, 'No entries in HWDP database')

    try:
        for row in c.execute('SELECT * FROM add_DC'):
                liststore[3].append(row)
    except Exception as e:
        print(e, 'No entries in DC database')

    try:
        for row in c.execute('SELECT * FROM add_MP'):
                liststore[4].append(row)
    except Exception as e:
        print(e, 'No entries in Mud Pump Liner database')

    try:
        for row in c.execute('SELECT * FROM add_OH'):
                liststore[5].append(row)
    except Exception as e:
        print(e, 'No entries in Open Hole database')

    try:
        c.execute('SELECT ent FROM entries')
        x = [record[0] for record in c.fetchall()]
        print(x)
    except Exception as e:
        x = []
        print(e, 'Ok, if first time using app! Entries retrieve table from db')

    try:
        c.execute('SELECT com FROM combos')
        y = [record[0] for record in c.fetchall()]
        print(y)
    except Exception as e:
        y = []
        print(e, 'Ok, if first time using app! Combos retrieve table from db')

    try:
        c.execute('SELECT cb FROM checkbuttons')
        z = [record[0] for record in c.fetchall()]
        print(z)
    except Exception as e:
        z = []
        print(e, 'Ok, if first time using app! Checkboxes retrieve table from db')
        c.close()
    return x, y, z


def delete_entry(database, table, pipe_rem):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('DELETE FROM ' + table + ' WHERE Name=?', (pipe_rem,))
    conn.commit()
    c.close()
    return

def update_entry(database, value):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('UPDATE OR IGNORE checkbuttons SET cb = ? WHERE id = ? ', (value, 16))
    conn.commit()
    c.close()

    return


def close_db(database):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.close()
    print('Database closed')