plugins = [
    'lrc123',
    'netease',
    'viewlyrics',
    'xiami',
]

foreach  plugin : plugins
    install_subdir (plugin, install_dir: join_paths(get_option('libdir'), 'lyricsource', 'plugins'))

    conf_data = configuration_data()
    conf_data.set('name', 'org.lyricsource.LyricSourcePlugin.'+plugin)
    conf_data.set(
        'path',
        find_program('python2').path() + ' ' +
        join_paths(get_option('prefix'), get_option('libdir'), 'lyricsource', 'plugins', plugin, plugin+'.py')
    )

    configure_file (
        input: 'service.in',
        output: 'org.lyricsource.LyricSourcePlugin.'+plugin+'.service',
        configuration: conf_data,
        install_dir : join_paths(get_option('datadir'), 'dbus-1/services')
    )
endforeach