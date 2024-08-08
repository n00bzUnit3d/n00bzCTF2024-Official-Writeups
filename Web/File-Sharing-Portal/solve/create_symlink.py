import tarfile

def create_tar_with_symlinks(tar_path, path):
    with tarfile.open(tar_path, 'w') as tar:
        tar.add(path, arcname=path)


create_tar_with_symlinks('read_ls_txt.tar', 'dummy.txt') # Read dummy.txt to read the `ls.txt`
