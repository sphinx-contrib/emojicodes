import json
import urllib.request


def update_codes():
    url = ('https://raw.githubusercontent.com/gitlabhq/gitlabhq'
           '/master/fixtures/emojis/index.json')
    data = json.load(urllib.request.urlopen(url))
    codes = {emoji['shortname']: emoji['moji'] for emoji in data.values()}
    with open('sphinxemoji/codes.json', 'w') as output:
        json.dump(codes, output, sort_keys=True, indent=4, ensure_ascii=False)
        output.write('\n')


if __name__ == '__main__':
    update_codes()
