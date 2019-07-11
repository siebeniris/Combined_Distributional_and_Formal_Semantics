import json

datafile= 'data/aijwikinerenwp2'

def load_file(file, sentencefile,jsonfile):
    data=[]
    with open(file) as input:
        with open(sentencefile,'w') as output:

            for line in input:
                entries = []
                sentence = []
                line=line.split()
                if line !=[]:
                    for entry in line:
                        word,tag, iob = entry.split('|')
                        entries.append((word,tag,iob))
                        sentence.append(word)
                if sentence!=[]:
                    output.write(' '.join(sentence)+'\n')
                if entries!=[]:
                    data.append(entries)
    with open(jsonfile, 'w')as output:
        json.dump(data, output)


if __name__ == '__main__':
    load_file(datafile, 'data/sentences.txt', 'data/entries.json')
