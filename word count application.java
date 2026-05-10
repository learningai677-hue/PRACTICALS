// Word Count using Hadoop MapReduce

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

public class WordCount {


    // Step 3 - Mapper Class

    public static class TokenizerMapper
            extends Mapper<Object, Text, Text, IntWritable> {

        // Create constant integer value 1

        private final static IntWritable one = new IntWritable(1);

        private Text word = new Text();


        // Map Function

        public void map(
                Object key,
                Text value,
                Context context
        ) throws IOException, InterruptedException {

            // Convert line into words

            String[] words = value.toString().split(" ");

            // Traverse each word

            for (String w : words) {

                word.set(w);

                // Send word and count to reducer

                context.write(word, one);
            }
        }
    }


    // Step 4 - Reducer Class

    public static class IntSumReducer
            extends Reducer<Text, IntWritable, Text, IntWritable> {

        private IntWritable result = new IntWritable();


        // Reduce Function

        public void reduce(
                Text key,
                Iterable<IntWritable> values,
                Context context
        ) throws IOException, InterruptedException {

            int sum = 0;

            // Count occurrences of each word

            for (IntWritable val : values) {

                sum += val.get();
            }

            result.set(sum);

            // Display final word count

            context.write(key, result);
        }
    }


    // Step 5 - Main Function

    public static void main(String[] args)
            throws Exception {

        Configuration conf = new Configuration();

        Job job = Job.getInstance(conf, "word count");

        job.setJarByClass(WordCount.class);

        job.setMapperClass(TokenizerMapper.class);

        job.setCombinerClass(IntSumReducer.class);

        job.setReducerClass(IntSumReducer.class);

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