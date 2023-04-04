import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import gzip
import boto3
from io import BytesIO


def create_dummy_data(rows=1000):
    data = {
        'id': range(1, rows + 1),
        'name': [f'name_{i}' for i in range(1, rows + 1)],
        'value': [i * 100 for i in range(1, rows + 1)]
    }
    return pd.DataFrame(data)


def save_gz_parquet(df, file_path):
    table = pa.Table.from_pandas(df)
    buffer = BytesIO()
    with gzip.open(buffer, 'wb') as gz_file:
        pq.write_table(table, gz_file)
    with open(file_path, 'wb') as file:
        file.write(buffer.getvalue())


def upload_to_s3(bucket, s3_key, file_path):
    s3 = boto3.client('s3')
    with open(file_path, 'rb') as file:
        s3.upload_fileobj(file, bucket, s3_key)


def main():
    dummy_data = create_dummy_data()

    file_path = 'dummy_data.parquet.gz'
    save_gz_parquet(dummy_data, file_path)

    bucket_name = 'your-bucket-name'
    s3_key = 'path/to/dummy_data.parquet.gz'
    upload_to_s3(bucket_name, s3_key, file_path)


if __name__ == '__main__':
    main()
