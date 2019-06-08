import json
from urllib.request import urlopen


def update_codes():
    remote = 'https://gitlab.com/gitlab-org/gitlab-ce/raw/master'
    data = json.load(urlopen(remote + '/fixtures/emojis/index.json'))
    codes = {emoji['shortname']: emoji['moji'] for emoji in data.values()}
    aliases = json.load(urlopen(remote + '/fixtures/emojis/aliases.json'))
    for alias, original in aliases.items():
        codes[':%s:' % alias] = codes[':%s:' % original]
    with open('sphinxemoji/codes.json', 'w') as output:
        json.dump(codes, output, sort_keys=True, indent=4, ensure_ascii=False)
        output.write('\n')


if __name__ == '__main__':
    update_codes()
