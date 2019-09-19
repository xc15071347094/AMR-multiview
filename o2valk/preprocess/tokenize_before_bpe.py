import argparse
import stanfordnlp

# stanfordnlp.download('en', force=True)
nlp = stanfordnlp.Pipeline(processors='tokenize', lang='en', tokenize_pretokenized=True)

parser=argparse.ArgumentParser()
parser.add_argument('-target')
args=parser.parse_args()

tokenized_target=[]

with open(args.target, 'r') as input:
    for line in input.readlines():
        sent=nlp(line)
        for i,sentence in enumerate(sent.sentences):
            tokenized_target+=[token.text for token in sentence.tokens]

with open(args.target, 'w') as output:
    output.writelines('\n'.join(tokenized_target))


