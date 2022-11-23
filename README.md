# About EYAPS

**iosEnv** was written to quickly get information regarding path of installed iOS application using applicationState.db file

## Usage

Print the help to get all necessary information

```bash
$ python3 iosEnv.py
usage: iosEnv.py [-h] [--file FILE] [--app APP]

iOS installed application parser

optional arguments:
  -h, --help   show this help message and exit
  --file FILE  Specify the applicationState.db file
  --app APP    Focus on this specific application
```

The **--file** option is mandatory and represent the applicationState.db file. This file could be retrieve on a jailbreaked device at: */private/var/mobile/Library/FrontBoard/applicationState.db*
More information regarding the *applicationState.db* file on [https://abrignoni.blogspot.com/2018/12/identifying-installed-and-uninstalled.html](https://abrignoni.blogspot.com/2018/12/identifying-installed-and-uninstalled.html)

Once specified, iosEnv will parse the complete file:

```bash
$ python3 iosEnv.py [--file applicationState.db
[...]
Processing: com.apple.tips
 > ID: 82
 > BundlePath: /private/var/containers/Bundle/Application/9928D570-0223-4F8E-BD32-BE733FDCEC33
 > CachesDirectory: /private/var/mobile/Containers/Data/Application/AF099880-BC30-4420-9FEC-13BEB77E8A75/Library/Caches
 > LibraryDirectory: /private/var/mobile/Containers/Data/Application/AF099880-BC30-4420-9FEC-13BEB77E8A75/Documents
 > DocumentDirectory: /private/var/mobile/Containers/Data/Application/AF099880-BC30-4420-9FEC-13BEB77E8A75/Library

Processing: com.highaltitudehacks.DVIAswiftv2
 > ID: 149
 > BundlePath: /private/var/containers/Bundle/Application/5C816470-885B-459C-A6E5-9E3031E9B44A
 > CachesDirectory: /private/var/mobile/Containers/Data/Application/C7C6A9F5-B915-4C11-890C-B52C5736382B/Library/Caches
 > LibraryDirectory: /private/var/mobile/Containers/Data/Application/C7C6A9F5-B915-4C11-890C-B52C5736382B/Documents
 > DocumentDirectory: /private/var/mobile/Containers/Data/Application/C7C6A9F5-B915-4C11-890C-B52C5736382B/Library
 [...]
```

## Author

Régis SENET ([rsenet](https://github.com/rsenet))


## Contributing

Bug reports and pull requests are welcome on [GitHub](https://github.com/rsenet/iosEnv).

## Thanks
[https://abrignoni.blogspot.com/2018/12/identifying-installed-and-uninstalled.html](https://abrignoni.blogspot.com/2018/12/identifying-installed-and-uninstalled.html)
[https://www.magnetforensics.com/blog/ios-tracking-bundle-ids-for-containers-shared-containers-and-plugins/](https://www.magnetforensics.com/blog/ios-tracking-bundle-ids-for-containers-shared-containers-and-plugins/)
[https://abrignoni.blogspot.com/2019/09/ios-snapshots-triage-parser-working.html](https://abrignoni.blogspot.com/2019/09/ios-snapshots-triage-parser-working.html)
[https://book.hacktricks.xyz/mobile-pentesting/ios-pentesting/ios-hooking-with-objection](https://book.hacktricks.xyz/mobile-pentesting/ios-pentesting/ios-hooking-with-objection)


## License

The project is available as open source under the terms of the [GPLv3](https://www.gnu.org/licenses/quick-guide-gplv3.en.html)

