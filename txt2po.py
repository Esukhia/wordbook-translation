from pathlib import Path

import polib


def find_sents(infile):
    dump = Path(infile).read_text().splitlines()
    sents = [s for s in dump if s.strip()] 
    # code to identify sentences in source file
    return sents


def create_po(infile, outfile):
    in_file = Path(infile)
    out_file = Path(outfile)    

    sents = find_sents(in_file)

    po = polib.POFile()
    for sent in sents:
        entry = polib.POEntry(
                # other arguments are: msgid, msgid, msgtxt, comment, tcomment            
                msgid=sent,
                msgstr=sent
            )
        po.append(entry)
    
    po.save(out_file)


if __name__ == '__main__':
    input = "wordbook.txt"
    output = "wordbook.po"

    create_po(input, output)