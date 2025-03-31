import os

os.makedirs('/tmp/python1', exist_ok=True)
os.makedirs('/tmp/python2', exist_ok=True)
os.makedirs('/tmp/python3', exist_ok=True)

f = open('/tmp/python1/fileone.txt', 'w+')
f.write('ONE FILE')
f.close()


f = open('/tmp/python1/filetwo.txt', 'w+')
f.write('TWO FILE')
f.close()

import zipfile

comp_file = zipfile.ZipFile('comp_fil.zip', 'w')
comp_file.write('/tmp/python1/fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('/tmp/python1/filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_fil.zip', 'r')
zip_obj.extractall('/tmp/python2')
zip_obj.close()

import shutil
dir_to_zip = '/tmp/python1'
output_filename = '/tmp/python2/all'
shutil.make_archive(output_filename, 'zip', dir_to_zip)

shutil.unpack_archive('/tmp/python2/all.zip', '/tmp/python3', format='zip')








