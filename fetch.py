import json
import datetime as date
import urllib.request as req
from bs4 import BeautifulSoup

archive = 'https://web.archive.org/web/'

def strip_archive_url(archive_url):
    return archive_url[archive_url.find('http'):]

def get_clock_data(original_url, name):
    print('fetching', original_url)
    with req.urlopen(archive + original_url) as old:
        soup = BeautifulSoup(old.read(), 'lxml')

    clock_images = [src for src in
        [strip_archive_url(i.attrs['src']) for i in soup.findAll('img')]
        if 'rpirtle' in src
    ]

    content = ' '.join([
            '\n\n'.join([line for line in l if line is not ''])
            for l in [tag.text.split('\n') for tag in soup.findAll('table')[3:]]
        ]
    )
    back = '\nback to the CLOCKS page'
    content = content.replace(back, '')

    data = {
        'name': name.title(),
        'original_url': original_url,
        'images': clock_images,
        'content': content,
        'slug': name.lower().replace(' ', '-').replace('_', '-')
    }
    return data

def fetch_clocks_from_archive():
    clock_url = archive + \
    'http://flashpages.prodigy.net/rpirtle/_upages/page2.html'
    with req.urlopen(clock_url) as web:
        soup = BeautifulSoup(web.read(), 'lxml')

    clock_images = soup.findAll('img')[6:28]
    x = soup.findAll('a')

    data = []
    # a = x[9]
    for a in x[8:28]:
        original_url = strip_archive_url(a.attrs['href'])
        name = original_url.split('detail_')[-1][:-5].replace('_', ' ')
        print('\n\n' + name.title())

        cover_image = strip_archive_url(a.img.attrs['src']).split('/')[-1]
        item = get_clock_data(original_url, name)

        item['cover_image'] = cover_image
        data.append(item)
    return data


def download_images(data):
    """
    downloads all images in each item (looks for list under `images`)
    """
    for i, item in enumerate(data):
        data[i]['images_renamed'] = []
        for j, src in enumerate(item['images']):
            ext = '.' + src.split('.')[-1].lower()
            filename = 'images/' + item['slug'] + '-' + str(j + 1) + ext
            if (j == 0):
                data[i]['cover_image'] = filename
            # with open('build/' + filename, 'wb') as f:
            #     f.write(req.urlopen(archive + src).read())
            # print('downloaded and saved', filename)
            data[i]['images_renamed'].append(filename)

def save_json(data, filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=2))
    return True;

def main():
    # download_images([{'name': 'bear', 'images': ['http://placebear.com/400/200']}])

    # clock_data = fetch_clocks_from_archive()
    # for clock in clock_data:
    #     clock['type'] = 'clock'
    # save_json(clock_data, 'out.json')

    with open('out.json') as f:
        clock_data = json.loads(f.read())

    download_images(clock_data)
    save_json(clock_data, 'out.json')

if __name__ == '__main__':
    main();
