# Batch Data Pipeline for Large-Scale Financial Transactions

## 1. Introduction

This application implements a batch-processing data pipeline to analyze a synthetic banking dataset using a modular architecture based on Python, Docker, and PySpark. The system simulates the data flow of a financial institution, where raw transactional data is ingested, preprocessed, and then aggregated to derive meaningful insights. The project demonstrates core data engineering practices, including containerized microservices, data cleansing, and scalable computation.

## 2. Functional Overview

The application is designed to process a large Excel-based dataset from a hypothetical bank. It is divided into three core components:

* **Ingestion Module**: Converts the raw Excel data into structured CSV format.
* **Preprocessing Module**: Cleans and normalizes the data by handling missing values, correcting data types, and standardizing column names.
* **Aggregation Module**: Utilizes PySpark to compute analytical insights, including average transaction values and domain-level activity prioritization.

All outputs are saved in a structured format for further reporting or visualization.

## 3. Dataset Description

The dataset, `bankdataset.xlsx`, is a synthetically generated file consisting of over one million transaction records from a fictional government-aided bank, REC-SSEC Bank. The data captures the following fields:

* **Date**: Date of transaction.
* **Domain**: Type of business domain performing the transaction.
* **Location**: City or region of the transaction.
* **Value**: Total monetary value of the transactions.
* **Count**: Total number of transactions.

## 4. Software Architecture

The system is implemented using a containerized microservices architecture and includes the following components:

* **Python 3.12**: Core programming language used for data ingestion and preprocessing.
* **Pandas**: Data analysis library used for loading and transforming CSV data.
* **PySpark (Spark 3.5)**: Employed for distributed aggregation tasks on large datasets.
* **Docker**: Used to isolate each component into its own environment.
* **Docker Compose**: Manages the multi-container orchestration.

## 5. Folder Structure

```
BATCH_DATA_PIPELINE/
│
├── data/
│   ├── raw/                        # Contains raw Excel file
│   ├── intermediate/              # Contains ingested and preprocessed CSVs
│   └── processed/                 # Contains final output reports
│
├── ingestion/                     # Excel to CSV microservice
├── preprocessing/                # Data cleaning microservice
├── aggregation/                  # PySpark analytics microservice
│
├── docker-compose.yml            # Orchestration file for all services
├── requirements.txt              # Global Python dependency file
└── README.md                     # Project documentation
```

## 6. System Requirements

To execute the project, the following software must be installed:

* Docker Desktop (latest stable version)
* Python 3.12+
* Git (for repository cloning)
* Text editor or IDE (e.g., VS Code, PyCharm)

Minimum hardware specifications:

* 8 GB RAM (recommended for running Spark container)
* 2 CPU cores

## 7. Installation Instructions

1. Clone the project repository to your local system:

   ```
   git clone https://github.com/Mitali25798/batch-data-pipeline.git
   cd batch_data_pipeline
   ```

2. Place the dataset file `bankdataset.xlsx` in the following location:

   ```
   data/raw/bankdataset.xlsx
   ```

## 8. Running the Application

Ensure Docker Desktop is running. Then follow the steps below:

### Step 1: Build the Docker Images

```
docker-compose build
```

### Step 2: Run the Ingestion Service

This reads the Excel file and converts it to CSV format.

```
docker-compose run ingestion
```

### Step 3: Run the Preprocessing Service

This cleans and normalizes the ingested data.

```
docker-compose run preprocessing
```

### Step 4: Run the Aggregation Service

This performs PySpark-based aggregations and saves results.

```
docker-compose run aggregation
```

## 9. Output Description

The final output is stored in the `data/processed/` directory, organized into subfolders representing different analytical outputs:

* `daily_avg_value_per_domain/`: Daily average transaction value grouped by domain.
* `yearly_avg_value_per_city/`: Yearly average transaction value grouped by city.
* `domain_priority_list/`: Domains ranked by total number of transactions.
* `avg_transaction_count_per_city/`: Average transaction count grouped by city.

Each subfolder contains CSV files that represent the computed analytics results.

## 10. Troubleshooting

* **Timeout during image pull**: Retry `docker-compose build` or use a faster/stable internet connection.
* **TLS handshake failure**: Ensure Docker can access Docker Hub or change DNS settings.
* **Missing column errors**: Ensure the preprocessing step successfully normalized column names.
* **Memory errors with Spark**: Close unused applications or allocate more memory to Docker.

## 11. Conclusion

This batch-processing data pipeline demonstrates the end-to-end process of transforming raw transactional data into usable analytical insights. Through containerization, the application ensures modularity, reproducibility, and scalability for handling large-scale datasets. The design is well-suited for academic purposes, prototyping, and extension into real-world data engineering pipelines.

## 12. References

https://www.kaggle.com/datasets/ksabishek/massive-bank-dataset-1-million-rows?resource=download

https://spark.apache.org/docs/latest/api/python/index.html

https://docs.docker.com/


