# OpenTelemetry SQLAlchemy Instrumentation `pyodbc` Bug

This repo is a quick reproduction to show the error that now occurs when
trying to use the OpenTelemetry SQLAlchemy instrumentation with `pyodbc`.
This started after [this pull request][1] was merged.

## Running

The MSSQL database is running from a Docker container. You will need to the ODBC driver installed to be able to connect.

### Installation of Microsoft ODBC Drivers

See [here][2] for Linux instructions and [here][3] for MacOS instructions.

### Execution steps

1. `docker-compose up`
2. `pip install requirements.txt`
3. `python repro.py`

Should see this error: `TypeError: cannot create weak reference to 'pyodbc.Cursor' object`

[1]: https://github.com/open-telemetry/opentelemetry-python-contrib/pull/315
[2]: https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15
[3]: https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver15