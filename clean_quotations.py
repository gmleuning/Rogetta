#!/usr/bin/env python3
"""Normalise the raw quotation file for the Rogetta quotes panel.

Usage:  python clean_quotations.py quotations_raw.md quotations.md

The raw file was hard-wrapped at 72 columns, and several quotes run together
with no blank line between them.  This script

  * un-wraps prose but keeps the line breaks of verse and of separate
    paragraphs;
  * separates quotes that were run together, and attaches each citation;
  * for the Bible/Apocrypha, makes the *book* the author ("Genesis") and the
    chapter:verse the citation, instead of "The Holy Bible The Old Testament".

Output format (one quote per block, blank line between blocks):

    ## Author
    *dates*

    quote text (line breaks kept where they are real)
    — citation          <- optional; always one line, always starts "— "

How wrapped lines are told apart from real ones: a line break is a *soft*
wrap when the line is so full that the first word of the next line could not
have fitted within 72 columns.  Verse blocks (mostly short lines) are stricter:
they also need the next line to start in lower case.
"""
import re, sys
from pathlib import Path

W = 72
TERMINAL = tuple('.!?;:,"”’…\'')   # a citation never ends with these
SENTENCE_END = tuple('.!?"”’…')   # where a text paragraph can end
DATE_RE = re.compile(r'^(c\. |fl\. |\d{3,4}\b)|\bcentur(y|ies)\b|B\.C\.E\.$')
DATE_START = re.compile(r'^(c\. ?|fl\. (c\. )?|ca\. )\d')   # an author's dates, e.g. "c. 650-c. 590 B.C.E."
BIBLE_SECTIONS = {'The Holy Bible The Old Testament': 'Old Testament',
                  'The Apocrypha': 'Apocrypha',
                  'The New Testament': 'New Testament'}


def first_word_len(s):
    return len(s.split(None, 1)[0]) if s.strip() else 0


def is_verse(lines):
    """Verse has several short lines that are neither sentence ends nor
    citations (which end in a digit or a bracket); wrapped prose has none."""
    score = sum(len(l) < 50 and not l.endswith(('.', '!', '?', '”', '’'))
                and not re.search(r'(\d|\])$', l) for l in lines[:-1])
    return score >= 2


def segments(raw):
    """Group raw lines into logical lines (soft wraps joined).  Returns a list
    of lists of raw lines."""
    verse = is_verse(raw)
    segs = [[raw[0]]]
    for prev, nxt in zip(raw, raw[1:]):
        soft = len(prev) + 1 + first_word_len(nxt) > W
        if verse:
            soft = soft and nxt[:1].islower() and prev[-1:] not in '.;:!?'
        if soft:
            segs[-1].append(nxt)
        else:
            segs.append([nxt])
    return segs, verse


def split_hidden_cite(seg):
    """A text paragraph and its citation can look like one wrapped line when
    the text's last line is nearly full.  If the joined line does not end like
    text, split at the last break that follows a sentence end and precedes a
    non-lower-case start."""
    if len(seg) < 2 or seg[-1].endswith(TERMINAL):
        return [seg]
    for k in range(len(seg) - 1, 0, -1):
        if seg[k - 1].endswith(SENTENCE_END) and not seg[k][:1].islower():
            return [seg[:k], seg[k:]]
    return [seg]


def split_quotes(raw):
    """raw lines of one block -> (quotes, carry).  quotes: list of (text, cite).
    carry: raw lines of an unfinished quote at the end of the block (its first
    line(s) were cut off from the rest by a stray blank line), or []."""
    segs, verse = segments(raw)
    expanded = []
    for s in segs:
        expanded.extend(split_hidden_cite(s))
    segs = [' '.join(x.strip() for x in s) for s in expanded]

    def cite_like(i):
        s = segs[i]
        if s.endswith(TERMINAL) or len(s) > 240:
            return False
        if i == len(segs) - 1:
            return len(segs) > 1 or False
        if verse:   # verse lines often lack punctuation: need a strong signature
            return (i > 0 and bool(re.search(r'(\d|\])$', s)) and len(s) >= 8
                    and not segs[i + 1][:1].islower())
        return not segs[i + 1][:1].islower()

    quotes, text = [], []
    for i, s in enumerate(segs):
        if cite_like(i) and text:
            quotes.append(('\n'.join(text), s))
            text = []
        else:
            text.append(s)
    carry = []
    if text:
        if len(text) <= 3 and not text[-1].endswith(TERMINAL) and not re.search(r'(\d|\])$', text[-1]):
            carry = [l for e in expanded[-len(text):] for l in e]
        else:
            quotes.append(('\n'.join(text), ''))
    return quotes, carry


ORD = {'First': '1', 'Second': '2', 'Third': '3', 'Fourth': '4', 'Fifth': '5', 'I': '1', 'II': '2', 'III': '3'}


def clean_book(p):
    p = p.strip(' ,')
    p = re.sub(r'^The (\w+) Book of Moses, Called ', '', p)
    p = re.sub(r'^The (First|Second) Book of the (Kings|Chronicles|Maccabees)$', lambda m: ORD[m[1]] + ' ' + m[2], p)
    p = re.sub(r'^The (First|Second) Book of (Samuel)$', lambda m: ORD[m[1]] + ' ' + m[2], p)
    p = re.sub(r';\s*or,.*$', '', p)                       # "Ecclesiastes; or, The Preacher"
    p = re.sub(r'^The (Proverbs|Song of Solomon)$', r'\1', p)
    p = re.sub(r'^The Lamentations of Jeremiah$', 'Lamentations', p)
    p = re.sub(r'^The Book of the Prophet ', '', p)
    p = re.sub(r'^The Book of ', '', p)
    p = re.sub(r'^The Gospel According to Saint ', '', p)
    p = re.sub(r'^The (First|Second) Epistle (?:of Paul the Apostle )?(?:to the |to )?(\w+)$',
               lambda m: ORD[m[1]] + ' ' + m[2], p)
    p = re.sub(r'^The (First|Second) Epistle General of ', lambda m: ORD[m[1]] + ' ', p)
    p = re.sub(r'^The Epistle of Paul (?:the Apostle )?to (?:the )?', '', p)
    p = re.sub(r'^The General Epistle of ', '', p)
    p = re.sub(r'^The Revelation of Saint John the Divine$', 'Revelation', p)
    p = re.sub(r'^The Acts of the Apostles$', 'Acts', p)
    p = re.sub(r'^(I{1,3}) (\w+)$', lambda m: ORD[m[1]] + ' ' + m[2], p)
    p = re.sub(r'^The Wisdom of Jesus the Son of Sirach, or ', '', p)
    p = re.sub(r'^Solomon$', 'Wisdom of Solomon', p)
    p = re.sub(r'^The Wisdom of Solomon$', 'Wisdom of Solomon', p)
    return p


def bible_ref(cite):
    """-> (book or None, ref)"""
    m = re.match(r'^(.*?)[,\s]*chapter (\d+), verses? (.+)$', cite)
    if m:
        return clean_book(m[1]), f'{m[2]}:{m[3]}'
    m = re.match(r'^(.*?)[,\s]*(\d+:\d+.*)$', cite)
    if m:
        return (clean_book(m[1]) if m[1].strip() else None), m[2]
    return None, cite


def parse(md):
    """-> list of sections: (author, dates, [(text, cite), ...])"""
    lines = md.replace('﻿', '').replace('\r', '').split('\n')
    sections, cur, block = [], None, []

    def flush():
        nonlocal block, cur
        b, block = block, []
        if not b or cur is None:
            return
        prev = cur['blocks'][-1] if cur['blocks'] else None
        if prev and DATE_START.match(b[0]) and len(prev[-1]) < 60 and not prev[-1].endswith(TERMINAL):
            # an author heading that lost its "## ": the name ended the previous block
            name = prev.pop()
            if not prev:
                cur['blocks'].pop()
            cur = {'author': name, 'dates': b[0], 'blocks': []}
            sections.append(cur)
            b = b[1:]
        elif (prev and b[0][:1].islower()
              and (len(prev[-1]) + 1 + first_word_len(b[0]) > W or not prev[-1].endswith(TERMINAL))):
            prev.extend(b)       # a wrapped tail that was cut off by a stray blank line
            return
        if b:
            cur['blocks'].append(b)

    i = 0
    while i < len(lines):
        l = lines[i].rstrip()
        if l.startswith('## '):
            flush()
            cur = {'author': l[3:].strip(), 'dates': '', 'blocks': []}
            sections.append(cur)
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines):
                d = lines[j].strip()
                if re.fullmatch(r'\*[^*].*\*', d):
                    cur['dates'] = d[1:-1]; i = j
                elif len(d) < 60 and DATE_RE.search(d) and not d.startswith('## '):
                    cur['dates'] = d; i = j
        elif not l.strip():
            flush()
        elif cur is not None:
            block.append(l)
        i += 1
    flush()

    out = []
    for s in sections:
        quotes, carry = [], []
        for b in s['blocks']:
            qs, carry_next = split_quotes(carry + b)
            quotes.extend([t, c] for t, c in qs)
            carry = carry_next
        if carry:      # nothing followed it: keep it as a quote of its own
            quotes.append([' '.join(l.strip() for l in carry), ''])
        # a one-line block that is only a citation belongs to the quote before it
        merged = []
        for text, cite in quotes:
            if (merged and not cite and '\n' not in text and len(text) < 90
                    and not text.endswith(TERMINAL) and not merged[-1][1]):
                merged[-1][1] = text
            else:
                merged.append([text, cite])
        out.append((s['author'], s['dates'], merged))
    return out


def biblify(sections):
    out = []
    for author, dates, quotes in sections:
        label = BIBLE_SECTIONS.get(author)
        if not label:
            out.append((author, dates, quotes))
            continue
        book, pending, groups = None, [], []     # groups: [book, [(text, ref)]]
        for text, cite in quotes:
            b, ref = bible_ref(cite) if cite else (None, '')
            if b:
                book = b
                for t, r in pending:
                    groups.append([b, [(t, r)]])
                pending = []
            if book is None:
                pending.append((text, ref))
            elif groups and groups[-1][0] == book:
                groups[-1][1].append((text, ref))
            else:
                groups.append([book, [(text, ref)]])
        for book, qs in groups:
            # merge consecutive groups of the same book created by 'pending'
            if out and out[-1][0] == book and out[-1][1] == label:
                out[-1][2].extend(qs)
            else:
                out.append((book, label, list(qs)))
    return out


def render(sections):
    chunks = []
    for author, dates, quotes in sections:
        head = f'## {author}\n' + (f'*{dates}*\n' if dates else '')
        body = []
        for text, cite in quotes:
            body.append(text + (f'\n— {cite}' if cite else ''))
        chunks.append(head + '\n' + '\n\n'.join(body) + '\n')
    return '\n'.join(chunks)


if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    sections = biblify(parse(Path(src).read_text(encoding='utf-8')))
    Path(dst).write_text(render(sections), encoding='utf-8', newline='\n')
    n = sum(len(q) for _, _, q in sections)
    print(f'{len(sections)} sections, {n} quotes -> {dst}')
