import json
from urllib.request import urlopen


def update_codes():
    remote = 'https://raw.githubusercontent.com/bonusly/gemojione/master'
    data = json.load(urlopen(remote + '/config/index.json'))
    codes = {}
    for emoji in data.values():
        codes[emoji['shortname']] = emoji['moji']
        for alias in emoji['aliases']:
            codes[alias] = emoji['moji']
    with open('sphinxemoji/codes.json', 'w') as output:
        json.dump(codes, output, sort_keys=True, indent=4, ensure_ascii=False)
        output.write('\n')


if __name__ == '__main__':
    update_codes()
