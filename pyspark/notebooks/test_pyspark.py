from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, count

class ChargePointsETLJob:
    input_path = '../data/input/electric-chargepoint-analysis-2017-domestics-incomplete-anomalies.csv'
    output_path = '../data/output/chargepoints-2017-analysis'
    
    def __init__(self):
        self.spark_session = (SparkSession.builder
                                          .master("local[*]")
                                          .appName("ElectricChargePointsETLJob")
                                          .getOrCreate())

    def extract(self):
        df = self.spark_session.read.csv(self.input_path, header=True)
        return df

    def transform(self, df):
        if df is None:
            return None
        
        df_agg = df.dropna(subset=["PluginDuration"]) \
            .groupBy(col("CPID").alias("chargepoint_id")) \
            .agg(max("PluginDuration").alias("avg_duration"),
                 avg("PluginDuration").alias("max_duration"),
                 count("*").alias("count")
                )
        
        return df_agg
        

    def load(self, df):
        if df is None:
            return
        
        df.write.mode("overwrite").parquet(self.output_path)


    def run(self):
        self.load(self.transform(self.extract()))
