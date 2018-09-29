project ('lyricsource',
         meson_version: '>=0.47.0',
         license : 'GPL3')

pymod = import('python')
python = pymod.find_installation('python2')

install_subdir ('lyricsource', install_dir: join_paths(python.get_install_dir()))

subdir ('daemon')
# subdir ('lyricsource')
subdir ('plugins')
# subdir ('tools')