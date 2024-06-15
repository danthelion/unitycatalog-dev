import polars as pl

df = pl.DataFrame(
    {
        "foo": [1, 2, 3, 4, 5],
        "bar": [6, 7, 8, 9, 10],
        "ham": ["a", "b", "c", "d", "e"],
    }
)

table_path = "s3://datawarehouse/test"

df.write_delta(
    table_path,
    storage_options={
        "endpoint_url": "http://localhost:9000",
        "AWS_REGION": "us-east-1",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "AWS_ALLOW_HTTP": "true",
        "AWS_S3_ALLOW_UNSAFE_RENAME": "true"
    },
)
