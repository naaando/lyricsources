configure_file (
    input: 'org.lyricsource.Config.service.in',
    output: 'org.lyricsource.Config.service',
    configuration: conf_data,
    install_dir : join_paths(get_option('datadir'), 'dbus-1/services')
)

configure_file (
    input: 'org.lyricsource.Daemon.service.in',
    output: 'org.lyricsource.Daemon.service',
    configuration: conf_data,
    install_dir : join_paths(get_option('datadir'), 'dbus-1/services')
)