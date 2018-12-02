from mrjob.job import MRJob
import re
from mrjob.protocol import ReprProtocol
import pymorphy2
from statistics import mean

WORD_RE = re.compile(r"[A-Za-zА-Яа-я][a-zа-я]+")


class MRFindNames(MRJob):
    OUTPUT_PROTOCOL = ReprProtocol

    def mapper(self, _, line):
        prob_threshold = 0.7
        morph = pymorphy2.MorphAnalyzer()

        for word in WORD_RE.findall(line):
            for p in morph.parse(word):
                if 'Name' in p.tag and p.score >= prob_threshold:
                    yield p.normal_form, p.score

    def reducer(self, name, scores):
        yield name, mean(scores)


if __name__ == '__main__':
    MRFindNames.run()
