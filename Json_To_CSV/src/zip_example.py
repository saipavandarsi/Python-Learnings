import zipfile
from path import Path
from os.path import basename
import datetime

def __init__(self, work_dir):
    self._work_dir = work_dir
    self._start_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

def write_to_zip(self):
    master_zipfilename = Path('A_{}_{}.zip'.format(
        self._start_time,
        "112233",
    ))
    files_dir = Path.getcwd()
    master_zipfile = Path(files_dir) + master_zipfilename
    print master_zipfile
    print files_dir
    with zipfile.ZipFile(master_zipfile, 'w', allowZip64=True) as zf:
        pass
    p = files_dir
    with zipfile.ZipFile(master_zipfile, 'w', allowZip64=True) as zf:
        for f in p.walkfiles():
            if basename(f).startswith("merged"):
                zf.write(f, f.relpath(p))
