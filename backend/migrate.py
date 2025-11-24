#!/usr/bin/env python3
"""
Database migration helper script.
Run this script to apply pending migrations.
"""

import subprocess
import sys
import os

def run_command(command):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return None

def main():
    # Change to backend directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("Checking for pending migrations...")

    # Check current revision
    current = run_command("python -m alembic current")
    if current is None:
        print("Failed to check current revision")
        return

    print(f"Current revision: {current.strip()}")

    # Check for pending migrations
    history = run_command("python -m alembic history")
    if history is None:
        print("Failed to check migration history")
        return

    print("Migration history:")
    print(history)

    # Apply migrations
    print("Applying migrations...")
    result = run_command("python -m alembic upgrade head")
    if result is None:
        print("Failed to apply migrations")
        return

    print("Migrations applied successfully!")
    print(result)

if __name__ == "__main__":
    main()
