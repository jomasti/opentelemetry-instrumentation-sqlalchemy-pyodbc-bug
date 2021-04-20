# OpenTelemetry SQLAlchemy Instrumentation `pyodbc` Bug

This repo is a quick reproduction to show the error that now occurs when
trying to use the OpenTelemetry SQLAlchemy instrumentation with `pyodbc`.
This started after [this pull request][1] was merged.

## Execution steps

1. `docker-compose up`
2. `pip install requirements.txt`
3. `python repro.py`

Should see this error: `TypeError: cannot create weak reference to 'pyodbc.Cursor' object`

[1]: https://github.com/open-telemetry/opentelemetry-python-contrib/pull/315
