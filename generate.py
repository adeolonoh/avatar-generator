import string
from shutil import copyfile
from avatar_generator import Avatar
from PIL import Image as PILImage, ImageOps as PILImageOps

def create(text, name=None):
    if not name:
        name = text

    file_og = 'out/original/%s.png' % name.lower()
    file_lg = 'out/500x500/%s.png'  % name.lower()
    file_md = 'out/180x180/%s.png'  % name.lower()
    file_sm = 'out/60x60/%s.png'    % name.lower()

    print file_og

    avatar = Avatar.generate(500, 255, text, 'PNG',
        (236, 238, 241), (170, 181, 194))
    with open(file_og, 'wb') as f:
        f.write(avatar)
    f.close()

    copyfile(file_og, file_lg)

    img = PILImage.open(file_og)

    md = PILImageOps.fit(img, (180, 180), PILImage.ANTIALIAS)
    md.save(file_md, 'PNG', optimize=True)

    sm = PILImageOps.fit(img, (60, 60), PILImage.ANTIALIAS)
    sm.save(file_sm, 'PNG', optimize=True)

create('', name='_')
for i in string.ascii_uppercase:
    create(i)
    for j in string.ascii_uppercase:
        create('%s%s' % (i, j))
