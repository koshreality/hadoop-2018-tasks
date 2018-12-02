from mrjob.job import MRJob
import re
from mrjob.protocol import ReprProtocol

WORD_RE = re.compile(r"[A-Za-z]+")


class MRMostFreq(MRJob):
    OUTPUT_PROTOCOL = ReprProtocol

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield word.lower(), 1

    def combiner(self, word, counter):
        yield None, (sum(counter), word)

    def reducer(self, _, words):
        yield "The most frequent word", max(words)[1]


if __name__ == '__main__':
    MRMostFreq.run()
