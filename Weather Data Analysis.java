// Weather Data Analysis using Hadoop MapReduce

// Step 1 - Import Required Libraries

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;

import org.apache.hadoop.fs.Path;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Job;

import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;

import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;


// Step 2 - Create Main Class

public class WeatherAnalysis {


    // Step 3 - Mapper Class

    public static class WeatherMapper
            extends Mapper<Object, Text, Text, Text> {


        // Map Function

        public void map(
                Object key,
                Text value,
                Context context
        ) throws IOException, InterruptedException {

            // Input format:
            // Date Temperature DewPoint WindSpeed

            String line = value.toString();

            String[] data = line.split(" ");

            if (data.length == 4) {

                String date = data[0];

                String temperature = data[1];

                String dewpoint = data[2];

                String windspeed = data[3];

                // Send all values to reducer

                context.write(
                        new Text(date),
                        new Text(
                                temperature + "," +
                                dewpoint + "," +
                                windspeed
                        )
                );
            }
        }
    }


    // Step 4 - Reducer Class

    public static class WeatherReducer
            extends Reducer<Text, Text, Text, Text> {


        // Reduce Function

        public void reduce(
                Text key,
                Iterable<Text> values,
                Context context
        ) throws IOException, InterruptedException {

            double tempSum = 0;

            double dewSum = 0;

            double windSum = 0;

            int count = 0;


            // Calculate total values

            for (Text val : values) {

                String[] parts = val.toString().split(",");

                tempSum += Double.parseDouble(parts[0]);

                dewSum += Double.parseDouble(parts[1]);

                windSum += Double.parseDouble(parts[2]);

                count++;
            }


            // Calculate averages

            double avgTemp = tempSum / count;

            double avgDew = dewSum / count;

            double avgWind = windSum / count;


            // Display final output

            context.write(
                    key,
                    new Text(
                            "Average Temperature = " + avgTemp +
                            ", Average Dew Point = " + avgDew +
                            ", Average Wind Speed = " + avgWind
                    )
            );
        }
    }


    // Step 5 - Main Function

    public static void main(String[] args)
            throws Exception {

        Configuration conf = new Configuration();

        Job job = Job.getInstance(conf, "weather analysis");

        job.setJarByClass(WeatherAnalysis.class);

        job.setMapperClass(WeatherMapper.class);

        job.setReducerClass(WeatherReducer.class);

        job.setOutputKeyClass(Text.class);

        job.setOutputValueClass(Text.class);

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