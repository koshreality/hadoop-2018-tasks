# Task 1
Вывод работы над полным файлом:
```sh
root@quickstart:/# time python3 job.py wiki.txt -o result_local
No configs found; falling back on auto-configuration
No configs specified for inline runner
Running step 1 of 1...
Creating temp directory /tmp/job.root.20181130.093624.467590
job output is in result_local
Removing temp directory /tmp/job.root.20181130.093624.467590...

real    2m31.658s
user    2m22.780s
sys     0m4.350s
root@quickstart:/# time python3 job.py -r hadoop hdfs:///user/root/wiki.txt -o hdfs:///user/root/result_hadoop2
No configs found; falling back on auto-configuration
No configs specified for hadoop runner
Looking for hadoop binary in $PATH...
Found hadoop binary: /usr/bin/hadoop
Using Hadoop version 2.7.3
Looking for Hadoop streaming jar in /home/hadoop/contrib...
Looking for Hadoop streaming jar in /usr/lib/hadoop-mapreduce...
Found Hadoop streaming jar: /usr/lib/hadoop-mapreduce/hadoop-streaming.jar
Creating temp directory /tmp/job.root.20181130.093908.776090
Copying local files to hdfs:///user/root/tmp/mrjob/job.root.20181130.093908.776090/files/...
Running step 1 of 1...
  packageJobJar: [] [/usr/lib/hadoop-mapreduce/hadoop-streaming-2.7.3.jar] /tmp/streamjob4772421331792762306.jar tmpDir=null
  Connecting to ResourceManager at quickstart.asus.com/172.17.0.2:8032
  Connecting to ResourceManager at quickstart.asus.com/172.17.0.2:8032
  Total input paths to process : 1
  number of splits:2
  Submitting tokens for job: job_1543570463394_0001
  Submitted application application_1543570463394_0001
  The url to track the job: http://quickstart.asus.com:20888/proxy/application_1543570463394_0001/
  Running job: job_1543570463394_0001
  Job job_1543570463394_0001 running in uber mode : false
```
Таким образом, с использованим локального движка `MRJob` работа выполнялась 2 минуты 31 секунду, а с использованием `hadoop` работа остановилась на последней строке вывода и далее не продолжалась (через 20 минут я остановила контейнер).

Вывод работы над урезанным файлом:
```sh
root@quickstart:/# time python3 job.py wiki_trunc.txt -o result_local_trunc
No configs found; falling back on auto-configuration
No configs specified for inline runner
Running step 1 of 1...
Creating temp directory /tmp/job.root.20181130.102456.531217
job output is in result_local_trunc
Removing temp directory /tmp/job.root.20181130.102456.531217...

real    0m5.355s
user    0m4.850s
sys     0m0.270s
root@quickstart:/# time python3 job.py -r hadoop hdfs:///user/root/wiki_trunc.txt -o hdfs:///user/root/result_hadoop_trunc
No configs found; falling back on auto-configuration
No configs specified for hadoop runner
Looking for hadoop binary in $PATH...
Found hadoop binary: /usr/bin/hadoop
Using Hadoop version 2.7.3
Looking for Hadoop streaming jar in /home/hadoop/contrib...
Looking for Hadoop streaming jar in /usr/lib/hadoop-mapreduce...
Found Hadoop streaming jar: /usr/lib/hadoop-mapreduce/hadoop-streaming.jar
Creating temp directory /tmp/job.root.20181130.102522.646751
Copying local files to hdfs:///user/root/tmp/mrjob/job.root.20181130.102522.646751/files/...
Running step 1 of 1...
  packageJobJar: [] [/usr/lib/hadoop-mapreduce/hadoop-streaming-2.7.3.jar] /tmp/streamjob2174481882788953920.jar tmpDir=null
  Connecting to ResourceManager at quickstart.asus.com/172.17.0.2:8032
  Connecting to ResourceManager at quickstart.asus.com/172.17.0.2:8032
  Total input paths to process : 1
  number of splits:2
  Submitting tokens for job: job_1543573375942_0001
  Submitted application application_1543573375942_0001
  The url to track the job: http://quickstart.asus.com:20888/proxy/application_1543573375942_0001/
  Running job: job_1543573375942_0001
  Job job_1543573375942_0001 running in uber mode : false
   map 0% reduce 0%
  Task Id : attempt_1543573375942_0001_m_000001_0, Status : FAILED
Container killed on request. Exit code is 137
Container exited with a non-zero exit code 137
Killed by external signal

   map 50% reduce 0%
   map 100% reduce 0%
   map 100% reduce 100%
  Job job_1543573375942_0001 completed successfully
  Output directory: hdfs:///user/root/result_hadoop_trunc
Counters: 51
        File Input Format Counters
                Bytes Read=2700352
        File Output Format Counters
                Bytes Written=824890
        File System Counters
                FILE: Number of bytes read=2916012
                FILE: Number of bytes written=6207956
                FILE: Number of large read operations=0
                FILE: Number of read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=2700568
                HDFS: Number of bytes written=824890
                HDFS: Number of large read operations=0
                HDFS: Number of read operations=9
                HDFS: Number of write operations=2
        Job Counters
                Data-local map tasks=2
                Failed map tasks=1
                Launched map tasks=3
                Launched reduce tasks=1
                Other local map tasks=1
                Total megabyte-milliseconds taken by all map tasks=562487296
                Total megabyte-milliseconds taken by all reduce tasks=12053504
                Total time spent by all map tasks (ms)=549304
                Total time spent by all maps in occupied slots (ms)=549304
                Total time spent by all reduce tasks (ms)=11771
                Total time spent by all reduces in occupied slots (ms)=11771
                Total vcore-milliseconds taken by all map tasks=549304
                Total vcore-milliseconds taken by all reduce tasks=11771
        Map-Reduce Framework
                CPU time spent (ms)=9090
                Combine input records=199390
                Combine output records=50284
                Failed Shuffles=0
                GC time elapsed (ms)=1867
                Input split bytes=216
                Map input records=50
                Map output bytes=8192039
                Map output materialized bytes=2916018
                Map output records=199390
                Merged Map outputs=2
                Physical memory (bytes) snapshot=1016483840
                Reduce input groups=40362
                Reduce input records=50284
                Reduce output records=40362
                Reduce shuffle bytes=2916018
                Shuffled Maps =2
                Spilled Records=100568
                Total committed heap usage (bytes)=837812224
                Virtual memory (bytes) snapshot=8408776704
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
job output is in hdfs:///user/root/result_hadoop_trunc
Removing HDFS temp directory hdfs:///user/root/tmp/mrjob/job.root.20181130.102522.646751...
Removing temp directory /tmp/job.root.20181130.102522.646751...

real    5m29.175s
user    0m33.100s
sys     0m4.950s
```
С использованием `MRJob` работа завершилась за 5 секунд, с использованием `hadoop` -- за 5 с половиной минут, при этом большую часть времени выполнение висело на той же строке, что и в первом случае, а впоследствии в выводе одновременно появилась как информация об ошибке:
```sh
Task Id : attempt_1543573375942_0001_m_000001_0, Status : FAILED
Container killed on request. Exit code is 137
Container exited with a non-zero exit code 137
```
так и информация об успешном завершении работы:
```sh
   map 0% reduce 0%
   map 50% reduce 0%
   map 100% reduce 0%
   map 100% reduce 100%
  Job job_1543573375942_0001 completed successfully
 ```
Из полученных результатов можно сделать вывод о нецелесообразности использования `hadoop` на локальной машине, поскольку он не дает выигрыша во времени и усложняет процесс работы.
Я думаю, что даже если бы работа завершилась нормально, по крайней мере на небольшом файле `hadoop` бы проиграл во времени работы из-за накладных расходов.