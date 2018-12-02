from mrjob.job import MRJob
import re
from mrjob.protocol import ReprProtocol
from statistics import median_high

WORD_RE = re.compile(r"[a-zа-я]\. ?[a-zа-я]\.")


class MRFindAbbr(MRJob):
    OUTPUT_PROTOCOL = ReprProtocol

    counts = []

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield ''.join(word.split()), 1

    def combiner(self, abbr, count):
        s = sum(count)
        self.counts.append(s)
        yield abbr, s

    def reducer(self, abbr, count):
        s = sum(count)
        if s > median_high(self.counts):
            yield abbr, s


if __name__ == '__main__':
    MRFindAbbr.run()
