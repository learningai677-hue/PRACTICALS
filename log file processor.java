// Log File Processing using Hadoop MapReduce

// Step 1 - Import Required Libraries

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;

import org.apache.hadoop.fs.Path;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Job;

import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;

import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;


// Step 2 - Create Main Class

public class LogProcessor {


    // Step 3 - Mapper Class

    public static class LogMapper
            extends Mapper<Object, Text, Text, IntWritable> {

        private final static IntWritable one = new IntWritable(1);

        private Text logLevel = new Text();


        // Map Function

        public void map(
                Object key,
                Text value,
                Context context
        ) throws IOException, InterruptedException {

            // Convert line into string

            String line = value.toString();

            // Check log levels

            if (line.contains("ERROR")) {

                logLevel.set("ERROR");

                context.write(logLevel, one);
            }

            else if (line.contains("WARNING")) {

                logLevel.set("WARNING");

                context.write(logLevel, one);
            }

            else if (line.contains("INFO")) {

                logLevel.set("INFO");

                context.write(logLevel, one);
            }
        }
    }


    // Step 4 - Reducer Class

    public static class LogReducer
            extends Reducer<Text, IntWritable, Text, IntWritable> {

        private IntWritable result = new IntWritable();


        // Reduce Function

        public void reduce(
                Text key,
                Iterable<IntWritable> values,
                Context context
        ) throws IOException, InterruptedException {

            int sum = 0;

            // Count occurrences

            for (IntWritable val : values) {

                sum += val.get();
            }

            result.set(sum);

            // Display output

            context.write(key, result);
        }
    }


    // Step 5 - Main Function

    public static void main(String[] args)
            throws Exception {

        Configuration conf = new Configuration();

        Job job = Job.getInstance(conf, "log processor");

        job.setJarByClass(LogProcessor.class);

        job.setMapperClass(LogMapper.class);

        job.setCombinerClass(LogReducer.class);

        job.setReducerClass(LogReducer.class);

        job.setOutputKeyClass(Text.class);

        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(
                job,
                new Path(args[0])
        );

        FileOutputFormat.setOutputPath(
                job,
                new Path(args[1])
        );

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}