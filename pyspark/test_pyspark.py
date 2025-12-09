from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, count
import os


class ChargePointsETLJob:
    # These parameters would be passed in as oppose to hard-coded
    input_path = '../data/input/electric-chargepoint-analysis-2017-domestics-incomplete-anomalies.csv'
    output_path = '../data/output/chargepoints-2017-analysis'
    
    def __init__(self):
        self.spark_session = (SparkSession.builder
                                          .master("local[*]")
                                          .appName("ElectricChargePointsETLJob")
                                          .getOrCreate())

    def extract(self):
        # Ensure that the input file exists
        if not os.path.exists(self.input_path):
            return None

        # Read the CSV file in and include the first line as column names
        df = self.spark_session.read.csv(self.input_path, header=True)
        return df


    def transform(self, df):
        if df is None:
            return None
        
        # Logic of the transform aggregation in SQL
        # * Count was not asked for, seems like a useful attribute
        """
        SELECT 
            CPID AS chargepoint_id,
            AVG(PluginDuration) AS avg_duration,
            MAX(PluginDuration) AS max_duration,
            COUNT(*) AS count
        FROM <input-dataframe>
        WHERE PluginDuration IS NOT NULL
        GROUPBY CPID
        """

        df_agg = df.dropna(subset=["PluginDuration"]) \
            .groupBy(col("CPID").alias("chargepoint_id")) \
            .agg(max("PluginDuration").alias("max_duration"),
                 avg("PluginDuration").alias("avg_duration"),
                 count("*").alias("count")
                )
        
        return df_agg


    def load(self, df):
        if df is None:
            return
        
        # Write/Overwrite the dataframe to a parquet file to the output path and filename
        df.write.mode("overwrite").parquet(self.output_path)


    def run(self):
        self.load(self.transform(self.extract()))
