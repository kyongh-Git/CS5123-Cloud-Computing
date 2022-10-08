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
hdfs dfs -put /home/kyongh/cloud/inputs /user/kyongh/cloud

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Task 1

Command to run mapreduce
hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -file /home/kyongh/t1mapper.py -mapper /home/kyongh/t1mapper.py -file /home/kyongh/t1reducer.py -reducer /home/kyongh/t1reducer.py -input /user/kyongh/cloud/inputs/* -output /user/kyongh/cloud/output1

Command to sample bottom 50 outputs
hdfs dfs -text /user/kyongh/cloud/output1/part-00000 | tail -50

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Task 2

Command to run mapreduce
hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -file /home/kyongh/t2mapper.py -mapper /home/kyongh/t2mapper.py -file /home/kyongh/t2reducer.py -reducer /home/kyongh/t2reducer.py -input /user/kyongh/cloud/inputs/* -output /user/kyongh/cloud/output2

Command to get result of mapreduce
hdfs dfs -text /user/kyongh/cloud/output2/part-00000
