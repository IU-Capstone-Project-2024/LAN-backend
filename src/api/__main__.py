import os
import sys
from pathlib import Path

import uvicorn

# Change dir to project root (three levels up from this file)
os.chdir(Path(__file__).parents[2])
# Get arguments from command
args = sys.argv[1:]

ssl_args = (
    [
        "--ssl-ca-certs=./certs/certificate_ca.crt",
        "--ssl-keyfile=./certs/certificate.key",
        "--ssl-certfile=./certs/certificate.crt",
    ]
    if os.getenv("PROD")
    else []
)

uvicorn.main.main(
    [
        "src.api.app:app",
        "--use-colors",
        "--proxy-headers",
        "--forwarded-allow-ips=*",
        *ssl_args,
        *args,
    ]
)
