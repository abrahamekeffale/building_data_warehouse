# building_data_warehouse
# Telegram Data Ingestion Project

## Overview

This project is designed to scrape and ingest data from Telegram channels into a PostgreSQL database. The data includes channel titles, usernames, messages, dates, and media paths. The goal is to store this information for further analysis.

## Table of Contents

- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Database Setup](#database-setup)
- [Data Ingestion Script](#data-ingestion-script)
- [Error Handling](#error-handling)
- [License](#license)

## Requirements

- Python 3.x
- PostgreSQL
- Required Python packages:
  - `psycopg2`
  - `csv`

You can install the required Python packages using pip:

```bash
pip install psycopg2
