project ('lyricsource',
         meson_version: '>=0.47.0',
         license : 'GPL3',
         version: '0.1')

pymod = import('python')
python = pymod.find_installation('python2')

# TODO: Reuse this config data inside plugins config data
conf_data = configuration_data()
conf_data.set('PYTHON', find_program('python2').path())
conf_data.set('PKGLIBDIR', join_paths(get_option('prefix'), get_option('libdir'), 'lyricsources'))

install_subdir ('lyricsources', install_dir: join_paths(python.get_install_dir()))

subdir ('plugins')
subdir ('data')
