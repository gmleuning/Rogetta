#!/usr/bin/env python3
"""Convert Project Gutenberg #10681 (Roget's Thesaurus, 1911) into one
self-contained, offline searchable HTML page.

Usage:  python build_roget.py rogets1911.txt index.html
"""
import json, re, sys
from pathlib import Path

POS_RE = re.compile(r'^(N|V|Adj|Adv|Int|Phr)\.\s')
START_RE = re.compile(r'^(\d+)([a-z]?)\.?\s+(?=\S)')
OPP_RE = re.compile(r'\{\s*(opp|ant)\.\s*([\d,\s&a-z]+?)\s*\}', re.I)


def load(path):
    text = Path(path).read_text(encoding='utf-8').replace('\r', '')
    lines = text.split('\n')
    start = next(i for i, l in enumerate(lines) if l.strip() == 'CLASS I')
    end = next(i for i, l in enumerate(lines) if l.startswith('*** END OF THE PROJECT GUTENBERG'))
    return lines[start:end]


SMALL = {'a', 'an', 'and', 'as', 'by', 'for', 'from', 'in', 'of', 'on', 'or', 'the', 'to', 'with'}


def smart_title(t):
    words = t.lower().split()
    return ' '.join(w if (k and w in SMALL) else w[:1].upper() + w[1:] for k, w in enumerate(words))


def entry_header(lines, i):
    """If line i begins an entry, return (number_of_header_lines, header, rest).
    The em dash may wrap onto the next line or two; never look past a blank line."""
    if not START_RE.match(lines[i]):
        return None
    joined, n = lines[i], 1
    while '—' not in joined and n < 3 and i + n < len(lines) and lines[i + n].strip():
        if POS_RE.match(lines[i + n]):
            break
        joined += ' ' + lines[i + n].strip()
        n += 1
    if '—' not in joined:
        return None
    head, _, rest = joined.partition('—')
    # continuation lines such as "718 equalization; &c 27; ..." have no period
    # and start lowercase; real headers carry an uppercase word, [ or {.
    m = START_RE.match(head)
    after = head[m.end():]
    if not re.match(r'[\[{A-Z]', after):
        return None
    return n, head.strip(), rest.strip()


def parse_header(head):
    m = START_RE.match(head)
    eid = m.group(1) + m.group(2)
    h = head[m.end():]
    opp = None
    om = OPP_RE.search(h)
    if om:
        opp = re.sub(r'^of\s+', '', om.group(2).strip())
        h = OPP_RE.sub('', h)
    glosses = re.findall(r'\[([^\]]*)\]', h)
    name = re.sub(r'\[[^\]]*\]', '', h)
    name = re.sub(r'\s+', ' ', name).strip(' .')
    return eid, name, ' '.join(g.strip() for g in glosses), opp


def parse_body(body_lines):
    """Logical lines: a new one starts at a POS marker or a 5-space indent;
    anything else is a wrapped continuation of the previous one."""
    logical = []
    for raw in body_lines:
        if not raw.strip():
            continue
        if POS_RE.match(raw) or raw.startswith('     ') or not logical:
            logical.append(raw.strip())
        else:
            logical[-1] += ' ' + raw.strip()
    pos = []
    for l in logical:
        m = POS_RE.match(l)
        if m:
            pos.append([m.group(1) + '.', [l[m.end():].strip()]])
        elif pos:
            pos[-1][1].append(l)
        else:
            pos.append(['', [l]])
    return pos


def build(lines):
    entries, path = [], {'cls': '', 'div': '', 'sec': '', 'sub': '', 'subsub': ''}
    i, cur = 0, None
    def close():
        if cur:
            eid, name, gloss, opp, body, p = cur
            entries.append({'id': eid, 'h': name, 'g': gloss, 'o': opp,
                            'p': [x for x in p if x], 'pos': parse_body(body)})
    while i < len(lines):
        l = lines[i]
        s = l.strip()
        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ''
        hm = re.match(r'^(CLASS|DIVISION|SECTION)\s+([IVX]+)\.?$', s)
        if hm:
            close(); cur = None
            label = f'{hm.group(1).title()} {hm.group(2)}: {smart_title(nxt)}'
            key = {'CLASS': 'cls', 'DIVISION': 'div', 'SECTION': 'sec'}[hm.group(1)]
            path[key] = label
            resets = {'cls': ('div', 'sec', 'sub', 'subsub'), 'div': ('sec', 'sub', 'subsub'), 'sec': ('sub', 'subsub')}
            for k in resets[key]:
                path[k] = ''
            i += 2
            continue
        eh = entry_header(lines, i)
        if eh:
            close()
            n, head, rest = eh
            eid, name, gloss, opp = parse_header(head)
            cur = [eid, name, gloss, opp, [rest], [path['cls'], path['div'], path['sec'], path['sub'], path['subsub']]]
            i += n
            continue
        sm = re.match(r'^(\d+)\.\s+(.+)$', s)
        if sm and not lines[i + 1].strip() if i + 1 < len(lines) else False:
            close(); cur = None
            title = sm.group(2).rstrip('.')
            if title.isupper():
                path['sub'], path['subsub'] = smart_title(title), ''
            else:
                path['subsub'] = title
            i += 1
            continue
        if cur:
            cur[4].append(l)
        i += 1
    close()
    return entries


TEMPLATE = Path(__file__).with_name('template.html')

if __name__ == '__main__':
    src, out = sys.argv[1], sys.argv[2]
    entries = build(load(src))
    data = json.dumps(entries, ensure_ascii=False, separators=(',', ':'))
    html = TEMPLATE.read_text(encoding='utf-8').replace('/*__DATA__*/[]', data)
    Path(out).write_text(html, encoding='utf-8')
    print(f'{len(entries)} entries -> {out}')
