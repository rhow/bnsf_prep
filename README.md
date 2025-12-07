# bnsf_prep

Running PySpark in docker

```
sudo apt install docker-compose
```

Start the PySpark instance
```
docker-compose up -d
```

Look for the token in the docker logs
```
docker logs pyspark_local
```

In the pyspark empty directory `mkdir`
```
mkdir notebooks data/input data/output
```

In a browser put in the following URL
```
http://localhost:8888/
```

Upload the `test_pyspark.py` ETL class
Upload the CSV data to the `data/input` directory

In a new notebook, execute the magic `%run` command to load the class
```
%run test_pyspark.py
```

The following executes the pipeline
```
pipeline = ChargePointsETLJob()

print("Starting ETL job...")
pipeline.run()
print("ETL job finished successfully.")
```