from mrjob.job import MRJob
from mrjob.protocol import ReprProtocol
import re

WORD_RE = re.compile(r"[\w]+")


# class WordLen:
#
#     word = ""
#     length = 0
#
#     def __init__(self, word, length):
#         self.word = word
#         self.length = length
#
#     def __gt__(self, other):
#         return len > other.len


class MRWordMaxLen(MRJob):
    OUTPUT_PROTOCOL = ReprProtocol

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            # if len(word) > 0:
            #     self.increment_counter('our_counter', str(len(word)), 1)
            yield word.lower(), len(word)

    def combiner(self, word, lengths):
        yield None, (list(lengths)[0], word)

    def reducer(self, _, words):
        yield "Longest word", max(words)


if __name__ == '__main__':
    MRWordMaxLen.run()
