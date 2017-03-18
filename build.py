import json
import datetime as date

import md

class Post(object):
    def __init__(self, item, template):
        self.template = template;
        self.name = item['name']
        self.type = item['type'] if 'type' in dir(item) else 'clocks'
        self.cover_image = item['cover_image']
        self.content = item['content']
        images = [
            '/images/' + img.split('/')[-1]
            for img in item['images_renamed']
        ]
        self.images = '\n'.join([md.image(img) for img in images])
    def __str__(self):
        current_time = str(date.datetime.now())[:-7]
        return self.template.format(item=self, current_time=current_time)


def main():
    with open('clocks.json', 'r') as f:
        clocks = json.loads(f.read())

    with open('template.txt', 'r') as f:
        template = f.read()

    for clock in clocks:
        filename = clock['slug'] + '.md'
        post = str(Post(clock, template))
        with open('build/' + filename, 'w') as f:
            f.write(post)

if __name__ == '__main__':
    main()
