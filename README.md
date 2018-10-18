# Lyricsources Standalone

Lyricsources is a lyric downloader dbus service from osdlyrics.
Building and installation

```
$ meson build --prefix ~/.local/
$ ninja -C build install
```

## DBus Interface

It exposes it's services on org.lyricsource.LyricSourcePlugin.[plugin_name] which you check on D-feet
The interface org.osdlyrics.LyricSourcePlugin is responsible for managing the searches and downloads.

## License

This project is licensed under the GNU General Public License v3.0 License - see the LICENSE file for details
