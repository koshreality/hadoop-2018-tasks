from mrjob.job import MRJob
import re
from mrjob.protocol import ReprProtocol

WORD_RE = re.compile(r"[A-Za-zА-Яа-я][\w]+")


class MRCapitalGT10(MRJob):
    OUTPUT_PROTOCOL = ReprProtocol

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            if 'Я' >= word[0] >= 'А' or 'Z' >= word[0] >= 'A':
                yield word.lower(), True
            else:
                yield word.lower(), False

    def reducer(self, word, counts):
        starts_with_a_capital_letter_count = 0
        total_number_of_using = 0

        for starts_with_a_capital in counts:
            total_number_of_using += 1

            if starts_with_a_capital:
                starts_with_a_capital_letter_count += 1

        if total_number_of_using > 10 and starts_with_a_capital_letter_count > total_number_of_using / 2:
            yield word, (starts_with_a_capital_letter_count, total_number_of_using)


if __name__ == '__main__':
    MRCapitalGT10.run()
