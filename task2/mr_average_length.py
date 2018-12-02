from mrjob.job import MRJob
import re
from statistics import mean

WORD_RE = re.compile(r"[\w']+")


class MRAvgLen(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield word.lower(), len(word)

    def combiner(self, word, lengths):
        yield None, list(lengths)[0]

    def reducer(self, _, lengths):
        yield "Average length", mean(lengths)


if __name__ == '__main__':
    MRAvgLen.run()
