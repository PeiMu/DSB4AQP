import io
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import util


def bulk_load_from_csv_file(cursor, csv_file, tmp_file, table_name, delimiter):
    # Split the csv file into batches to load incrementally.
    batch_size = 100000
    count = 0
    with open(csv_file) as fin:
        while True:
            batch = []
            for _ in range(batch_size):
                line = fin.readline()
                if not line:  # Reliable EOF check
                    break
                batch.append(line)
            
            if not batch:
                break  # Exit when no more data
    
            # Use StringIO instead of writing to disk
            csv_buffer = io.StringIO(''.join(batch))
            cursor.copy_expert(
                f"COPY {table_name} FROM STDIN WITH (FORMAT CSV, DELIMITER '{delimiter}', HEADER FALSE)",
                csv_buffer
            )
            count += len(batch)
            print('.', end='', flush=True)
    
    print(f'Loaded {count} rows from {csv_file} to {table_name}')


def load_from_csv_file(cursor, csv_file, table_name, delimiter):
    try:
        with open(csv_file, 'r') as file:
            cursor.copy_expert(
                f"COPY {table_name} FROM STDIN WITH (FORMAT CSV, DELIMITER '{delimiter}', HEADER FALSE)",
                file
            )
    except Exception as e:
        print(f"ERROR loading {csv_file}: {e}")
        raise  # Re-raise to halt execution


def execute(cursor, cmd, verbose = False):
	try:
		if verbose:
			print(cmd)
		cursor.execute(cmd)
	except Exception as e:
		print(e)

def connect(user, password, db_name=None, host=None, port=None):
	conn = None
	try:
		kwargs = dict(user=user, password=password)
		if db_name is not None:
			kwargs['database'] = db_name
		if host is not None:
			kwargs['host'] = host
		if port is not None:
			kwargs['port'] = port
		conn = psycopg2.connect(**kwargs)
		conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

	except Exception as e:
		print(e)

	return conn

def restart_server(pg_service_name = 'postgresql-x64-13'):
	stop_server(pg_service_name)
	start_server(pg_service_name)

def stop_server(pg_service_name = 'postgresql-x64-13'):

	cmd = 'net stop ' + pg_service_name
	util.run_cmd(cmd)

def start_server(pg_service_name = 'postgresql-x64-13'):

	cmd = 'net start ' + pg_service_name
	util.run_cmd(cmd)

if __name__ == '__main__':
	pg_service_name = 'postgresql-x64-13'
	start_server(pg_service_name)
