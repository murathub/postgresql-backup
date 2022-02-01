#!/usr/bin/python3
# -*- coding: utf8 -*-
import os
import time
import datetime
import dropbox

access_token = 'EI4xgQtc***************************-p' # dropbox access token

def main():
    # if True:
    if '06:' in str(newDate()) and int(datetime.datetime.today().weekday()) == 4:
        filepath = '{}{}{}'.format('/home/toor/Documents/', time.strftime('%d.%m.%Y', time.localtime()).strip(),".gz")
        execute = 'pg_dump --dbname=postgresql://user:pass@127.0.0.1:5432/backupthis_db -Z6 > {}'.format( filepath )
        os.system(execute)

        dropboxUpload(filepath);
        # everything is case sensitive, make sure you insert everything correctly and to import withadminer

def newDate():
    return time.strftime('%d.%m.%Y %H:%M', time.localtime())

def dropboxUpload(_filepath):
    dbx = dropbox.Dropbox(access_token)
    dbx.files_upload( open(_filepath, 'rb').read(), "/" + os.path.basename(_filepath) )
    print('Backup: {} [{}]'.format(os.path.basename(_filepath), newDate() ) );
    os.system('rm -r ' + _filepath) # enable this if you want to delete after upload

if __name__ == '__main__':
    while True:
        try:
            main()
            time.sleep(3600);
        except Exception as err:
            print(err)
            time.sleep(3600);
        except KeyboardInterrupt:
            break