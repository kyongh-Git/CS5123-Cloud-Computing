Yonghwan Kim A11746276 Assignment2

Contents

Task1
Mapper: t1mapper.py
Reducer: t1reducer.py
output result: Task1Output.txt

Task2
Mapper: t2mapper.py
Reducer: t2reducer.py
output result: Task2Output.txt

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Command to copy local input files to hdfs
hdfs dfs -put /home/cloud/inputs /user/cloud

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Task 1

Command to run mapreduce
hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -file /home/t1mapper.py -mapper /home/t1mapper.py -file /home/t1reducer.py -reducer /home/t1reducer.py -input /user/cloud/inputs/* -output /user/cloud/output1

Command to sample bottom 50 outputs
hdfs dfs -text /user/cloud/output1/part-00000 | tail -50

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Task 2

Command to run mapreduce
hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -file /home/t2mapper.py -mapper /home/t2mapper.py -file /home/t2reducer.py -reducer /home/t2reducer.py -input /user/cloud/inputs/* -output /user/cloud/output2

Command to get result of mapreduce
hdfs dfs -text /user/cloud/output2/part-00000
