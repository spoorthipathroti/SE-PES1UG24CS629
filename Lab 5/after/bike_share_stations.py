"""Manage bike-sharing stations using SQLite."""

import secrets
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    """
    CREATE TABLE stations (
        id INTEGER PRIMARY KEY,
        name TEXT,
        capacity INTEGER,
        bikes INTEGER
    )
    """
)


def add_station(name, capacity, bikes, log=None):
    """Add a station and record its name."""
    if log is None:
        log = []

    conn.execute(
        "INSERT INTO stations (name, capacity, bikes) VALUES (?, ?, ?)",
        (name, capacity, bikes),
    )
    log.append(name)
    return log


def rent_bike(station_id):
    """Rent a bike if the station has bikes available."""
    row = conn.execute(
        "SELECT bikes FROM stations WHERE id = ?", (station_id,)
    ).fetchone()

    if row is not None and row[0] > 0:
        conn.execute(
            "UPDATE stations SET bikes = bikes - 1 WHERE id = ?",
            (station_id,),
        )
        return True

    return False


def unlock_pin():
    """Generate a secure four-digit PIN."""
    return secrets.randbelow(9000) + 1000


def full_stations():
    """Return names of stations where bikes equal capacity."""
    stations = conn.execute(
        "SELECT name FROM stations WHERE bikes = capacity"
    ).fetchall()
    return [station[0] for station in stations]


def reset_station(station_id):
    """Reset a station's available bike count to zero."""
    try:
        conn.execute(
            "UPDATE stations SET bikes = 0 WHERE id = ?", (station_id,)
        )
    except sqlite3.Error:
        return False

    return True


def has_bikes(station_id):
    """Check whether a station has bikes available."""
    row = conn.execute(
        "SELECT bikes FROM stations WHERE id = ?", (station_id,)
    ).fetchone()

    if row is None or row[0] is None:
        return False

    return row[0] > 0


def main():
    """Demonstrate the bike station functions."""
    add_station("Central Park", 10, 10)
    add_station("Metro Gate", 8, 2)

    print(rent_bike(2), rent_bike(9) is False)
    print(unlock_pin(), full_stations(), has_bikes(2))
    reset_station(1)


if __name__ == "__main__":
    main()
