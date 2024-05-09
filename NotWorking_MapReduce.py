from mrjob.job import MRJob
import sys
import json

class WordCount(MRJob):
  #create a mapper()
  def mapper(self, _, line):
    for word in line.strip().split(' '):
      if len(word) > 0:
       yield (word, 1)

  #create a reducer()
  def reducer(self, word, count):
    yield (word, sum(count))

task0 = WordCount(args = ['book.txt'])
task0.sandbox(stdin=sys.stdin, stdout=sys.stdout)

with task0.make_runner() as runner:
    runner.run()
    output = []
    for line in runner.cat_output():
        key, value = task0.parse_output_line(line.decode('utf-8'))
        output.append((key, value))

output = sorted(output, key = lambda x: -x[1]) # sort the ouput in descending order