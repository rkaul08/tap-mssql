"""mssql entry point."""

from __future__ import annotations

from tap_mssql.tap import Tapmssql

if __name__ == "__main__":
    # Create tap instance with parse_env_config=False
    tap = Tapmssql(parse_env_config=False)
    tap.cli()

Tapmssql.cli()
