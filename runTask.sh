hadoop dfs -rm -R result_candidatePairs
hadoop dfs -rm -R result_freqPairs
rm outputCandidate.txt

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
	-D stream.map.input.field.separator=EOF \
	-D mapred.map.tasks=2 \
	-file job1mapper.py -mapper job1mapper.py \
	-file job1reducer.py -reducer job1reducer.py \
	-input basketInput \
	-output result_candidatePairs

hadoop dfs -copyToLocal result_candidatePairs/part-00000 outputCandidate.txt

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
	-D stream.map.input.field.separator=EOF \
	-D mapred.map.tasks=20 \
	-file outputCandidate.txt \
	-file job2mapper.py -mapper job2mapper.py \
	-file job2reducer.py -reducer job2reducer.py \
	-input basketInput \
	-output result_freqPairs