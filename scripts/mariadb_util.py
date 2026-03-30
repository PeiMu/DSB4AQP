import mysql.connector


def parse_dat_row(line):
    """Parse a TPC-DS .dat row. Trailing '|' is stripped; empty fields become None (SQL NULL)."""
    line = line.rstrip('\r\n')
    if line.endswith('|'):
        line = line[:-1]
    return [f if f != '' else None for f in line.split('|')]


def bulk_load(cursor, file_path, table_name, batch_size=10000):
    # Determine actual column count from the database table
    cursor.execute('SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = %s', (table_name,))
    num_cols = cursor.fetchone()[0]
    placeholder = '(' + ', '.join(['%s'] * num_cols) + ')'

    count = 0
    batch = []

    with open(file_path, 'r') as f:
        for line in f:
            row = parse_dat_row(line)
            if len(row) < num_cols:
                continue  # skip malformed/empty rows
            batch.append(row[:num_cols])  # trim any extra fields dsdgen may produce
            if len(batch) >= batch_size:
                cursor.executemany('INSERT INTO ' + table_name + ' VALUES ' + placeholder, batch)
                count += len(batch)
                batch = []
                print('.', end='', flush=True)
        if batch:
            cursor.executemany('INSERT INTO ' + table_name + ' VALUES ' + placeholder, batch)
            count += len(batch)

    print('\nLoaded ' + str(count) + ' rows into ' + table_name)


def execute(cursor, cmd, verbose=False):
    try:
        if verbose:
            print(cmd)
        cursor.execute(cmd)
    except Exception as e:
        print(e)


def execute_sql_file(cursor, sql_path, verbose=False, if_not_exists=False):
    with open(sql_path, 'r') as f:
        sql = f.read()
    if if_not_exists:
        sql = sql.replace('CREATE TABLE ', 'CREATE TABLE IF NOT EXISTS ')
    for stmt in sql.split(';'):
        stmt = stmt.strip()
        if stmt and not stmt.startswith('--'):
            execute(cursor, stmt, verbose=verbose)


def connect(user, password, host='localhost', db_name=None):
    kwargs = dict(user=user, password=password, host=host, autocommit=True)
    if db_name is not None:
        kwargs['database'] = db_name
    return mysql.connector.connect(**kwargs)
