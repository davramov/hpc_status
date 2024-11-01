# NERSC Systems Status Dashboard

A Python web application that displays the current status of NERSC systems in a dynamic dashboard, using color-coded indicators for each system. This application uses Quart (an asynchronous Python web framework) and requests to fetch and display the status of NERSC resources.

## Features

Displays the status of each NERSC system with color indicators:

🟢 Green for "active"

🔴 Red for "down"

🟡 Yellow for "degraded"

⚪ Gray for "unknown"

Automatically fetches and updates system statuses from the NERSC API.

## Requirements

Python 3.8 or higher

Quart and requests libraries

## Installation

Clone this repository.

Install dependencies:

```
pip install quart requests
```

## Usage

Run the application:

```
python app.py
```

Access the dashboard:
Open your web browser and go to http://localhost:5000.

The dashboard will display the status of each NERSC system with a color-coded light indicating its current status.

## Project Structure

```
├── app.py             # Main application script
├── README.md          # Project documentation
├── templates
│   └── index.html     # HTML template for the dashboard
└── requirements.txt   # Project dependencies
```
## Code Overview

app.py: Contains the main application logic, including fetching the status of each system from the NERSC API and serving the web page.

templates/index.html: HTML template to display the system status with appropriate color indicators.

Example Output

When you access the dashboard, you should see something like this:

NERSC Systems Status Dashboard
-------------------------------
🟢 Perlmutter: active
🔴 Cori: down
🟡 DNA: degraded
⚪ Unknown system: unknown

Each system's status is color-coded for quick viewing.

## Notes

This app does not require any NERSC login or authentication to check system statuses.

The application fetches system status in real-time from NERSC's open status API.

## Contributing

Feel free to fork this repository, submit pull requests, or report any issues. Contributions are always welcome!

## Future work

Extend this to check the status of other HPC facilities (ALCF, OLCF, ...)