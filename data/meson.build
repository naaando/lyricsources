configure_file (
    input: 'org.lyricsources.Config.service.in',
    output: 'org.lyricsources.Config.service',
    configuration: conf_data,
    install_dir : join_paths(get_option('datadir'), 'dbus-1/services')
)

configure_file (
    input: 'org.lyricsources.Daemon.service.in',
    output: 'org.lyricsources.Daemon.service',
    configuration: conf_data,
    install_dir : join_paths(get_option('datadir'), 'dbus-1/services')
)
