from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

class JobAggregator:
    """
    Reads a CSV, aggregates job titles, and returns the result as a Python dictionary.
    """
    
    def __init__(self, spark_session: SparkSession, input_path: str):
        """Initializes the job with a SparkSession and input file path."""
        self.spark = spark_session
        self.input_path = input_path
        
    def extract_and_aggregate(self):
        """
        Reads the CSV file and aggregates job titles.
        """
        # 1. Extract: Read CSV (assumes 'name' and 'job_title' columns)
        try:
            df = (self.spark.read
                      .option("header", "true")
                      .option("inferSchema", "true") 
                      .csv(self.input_path))
        except Exception as e:
            print(f"Error reading file {self.input_path}: {e}")
            return None

        # 2. Transform: Group and Count
        # We group by the 'job_title' column and count the number of occurrences.
        agg_df = (df.groupBy(col("job_title"))
                    .agg(count("*").alias("job_count"))
                    .orderBy(col("job_count").desc()))
        
        return agg_df