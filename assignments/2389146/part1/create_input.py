from bs4 import BeautifulSoup
import re
from pathlib import Path

# print(searchResults)
in_dir = Path.cwd() / 'in'
in_dir.mkdir(parents=True, exist_ok=True)
counter = 0
source_dir = Path.cwd() / 'data'
for source in source_dir.iterdir():
    file = open(source, 'r')
    soup = BeautifulSoup(file, 'html.parser')

    searchResults = soup.findAll("div", {"id":re.compile(r'post_message_')})
    # print(searchResults)
    for corp in searchResults:
        if len(corp.findAll("div", {"class":'panel alt2'})) > 0:
            replying_to = ' '.join([i.text for i in corp.findAll("div", {"style":'font-style:italic'})])

            reply = ''.join(corp.findAll(text=True, recursive=False))
            # print(f'replying to: {replying_to}')
            # print(f'reply: {reply}')
            # print('-----------------------------------------')
            to_in_file = open(str(in_dir / f'{counter}_q.txt'),'w')
            to_in_file.write(replying_to)
            to_in_file.close()
            r_in_file = open(str(in_dir / f'{counter}_a.txt'),'w')
            r_in_file.write(reply)
            r_in_file.close()
            counter += 1