install_path = join_paths(get_option('prefix'), get_option('libdir'), 'lyricsource', 'daemon')

conf_data = configuration_data()
conf_data.set('PROGRAM_NAME', meson.project_name ())
conf_data.set('PACKAGE_NAME', meson.project_name ())
conf_data.set('PACKAGE_VERSION', meson.project_version ())
conf_data.set('PYTHON', find_program('python2').path())
conf_data.set('PATH', install_path)

configure_file (
    input: 'lyricsource-daemon.in',
    output: 'lyricsource-daemon',
    configuration: conf_data,
    install_dir: join_paths(get_option('bindir')),
    install_mode: 'rwxrwxr-x',
)

configure_file (
    input: 'config.py.in',
    output: 'config.py',
    configuration: conf_data,
    install_dir: install_path,
)

install_data(
    'errors.py',
    'ini_config.py',
    'lrcdb.py',
    'lyricsource.py',
    'lyrics.py',
    'main.py',
    'player.py',
    install_dir : install_path,
)