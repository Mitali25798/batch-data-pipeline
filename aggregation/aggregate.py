from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, sum as spark_sum, col, year
import os

INTERMEDIATE_PATH = '/app/data/intermediate/'
PROCESSED_PATH = '/app/data/processed/'

def run_aggregation():
    print("Starting PySpark aggregation...")

    spark = SparkSession.builder.appName("BankDataAggregation").getOrCreate()

    for file in os.listdir(INTERMEDIATE_PATH):
        if file.startswith("preprocessed_") and file.endswith(".csv"):
            df = spark.read.option("header", "true").csv(os.path.join(INTERMEDIATE_PATH, file), inferSchema=True)
            df = df.withColumn("Year", year("Date"))

            # 1. Daily avg transaction value per domain
            daily_avg = df.groupBy("Date", "Domain").agg(avg("Value").alias("avg_value"))
            daily_avg.write.csv(os.path.join(PROCESSED_PATH, "daily_avg_value_per_domain"), header=True, mode="overwrite")

            # 2. Yearly avg transaction value per city
            yearly_avg = df.groupBy("Location", "Year").agg(avg("Value").alias("yearly_avg_value"))
            yearly_avg.write.csv(os.path.join(PROCESSED_PATH, "yearly_avg_value_per_city"), header=True, mode="overwrite")

            # 3. Domain priority list by total transaction count
            priority = df.groupBy("Domain").agg(
                spark_sum("Transaction_count").alias("total_count")
            ).orderBy(col("total_count").desc())

            priority.write.csv(
                os.path.join(PROCESSED_PATH, "domain_priority_list"),
                header=True,
                mode="overwrite"
            )

            # 4. Avg transaction count per city
            avg_count = df.groupBy("Location").agg(avg("Transaction_count").alias("avg_count"))
            avg_count.write.csv(os.path.join(PROCESSED_PATH, "avg_transaction_count_per_city"), header=True, mode="overwrite")

            print(f"Aggregated: {file}")
    spark.stop()
    print("Aggregation complete.")

if __name__ == "__main__":
    run_aggregation()
