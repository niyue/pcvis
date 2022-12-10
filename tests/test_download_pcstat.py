from pcvis.pcvis import _downlad_pcstat, install_pcstat_cmd
import os
import tempfile

def test_download_pcstat():
    download_dir = tempfile.gettempdir()
    pcstat_file = f"{download_dir}/pcstat.tar.gz"
    import shutil
    if os.path.exists(pcstat_file):
        os.remove(pcstat_file)
    _downlad_pcstat(download_dir)
    assert os.path.exists(pcstat_file)

def test_install_pcstat():
    install_dir = tempfile.gettempdir()
    install_pcstat_cmd(install_dir)
    assert os.path.exists(f"{install_dir}/pcstat")