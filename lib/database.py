import re
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)

    except Error as e:
        print(e)

    return conn


def parse_application_state(conn, application):
    cursor = conn.cursor()
    cursor.execute('''SELECT application_identifier_tab.id, application_identifier_tab.application_identifier,kvs.value
                      FROM kvs, application_identifier_tab, key_tab
                      WHERE application_identifier_tab.id = kvs.application_identifier
                      AND key_tab.key = 'compatibilityInfo'
                      AND key_tab.id = kvs.key
                  ''')

    all_rows = cursor.fetchall()

    for row in all_rows:
        display = True
        appid = row[0]
        bundleid = row[1]
        wbplist = row[2]

        if application != "":
            if application != bundleid:
                display = False

        regex_bundle = r"/private/var/containers/Bundle/Application/\w{8}-\w{4}-\w{4}-\w{4}-\w{12}"
        matches_bundle = re.search(regex_bundle, str(wbplist))

        if matches_bundle:
            bundle = matches_bundle.group()
        else:
            display = False

        regex_data = r"/private/var/mobile/Containers/Data/Application/\w{8}-\w{4}-\w{4}-\w{4}-\w{12}"
        matches_data = re.search(regex_data, str(wbplist))

        if matches_data:
            data = matches_data.group()
        else:
            display = False

        if display:
            print('Processing: %s' % bundleid)
            print(' > ID: %d' % appid)
            print(' > BundlePath: %s ' % bundle)
            print(' > CachesDirectory: %s/Library/Caches' % data)
            print(' > LibraryDirectory: %s/Documents' % data)
            print(' > DocumentDirectory: %s/Library' % data)
            print()
