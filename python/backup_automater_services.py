import shutil
import datetime
import os

today = datetime.date.today()
todaystr = today.isoformat()

confdir = os.getenv('my_config')
dropbox = os.getenv('dropbox')
