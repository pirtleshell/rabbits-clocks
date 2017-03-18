
# rabbits clock's archive retrieval

> an example of fetching web.archive.org material and generating new pages

## What

Rabbit's clocks was a website showcasing wooden machines and clocks made by rabbit.
These scripts collect the archived webpage and builds a database of objects used to generate pages for a new webpage.

It is archived [here](https://web.archive.org/web/20101206093122/http://flashpages.prodigy.net/rpirtle/index.html).

## How to Enact

`fetch.py` goes and crawls the Archive and stores the information in `out.json`.
You edit it's `main` to choose which data you're looking for.
Scan your JSON and edit if needed; save it as the file you put into `build.py`.
It takes the data and `template.txt` and fills it for each object.

This one does `clocks` and will soon do `machines`.

Run the following sequence:
* fetch
* edit out.json, save as clock.json
* build - you may need to create the directories `build/images` for downloading to work right.

## License

This is by [Robert Pirtle](https://pirtle.xyz/). Its licence is [MIT](https://choosealicense.com/licenses/mit).
