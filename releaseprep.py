# python3 script
import os
import shutil
from pathlib import Path

root_path = Path('./')
template_path = Path(root_path / 'email_templates')
release_path = Path(root_path / 'release_files')

#ensure latest compilation before publishing
os.system("python compile.py")

for filename in os.listdir(template_path):
    shutil.copy(template_path / filename, release_path / (filename[:-4] + 'txt'))

shutil.copy(root_path / 'email.min.html', release_path / 'emailformatter.html')