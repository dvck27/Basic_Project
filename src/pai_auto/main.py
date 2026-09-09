from __future__ import annotations

import os
import webbrowser
from threading import Timer

import uvicorn


def main() -> None:
    host = os.getenv("PAI_AUTO_HOST", "127.0.0.1")
    port = int(os.getenv("PAI_AUTO_PORT", "8765"))
    if os.getenv("PAI_AUTO_NO_BROWSER", "0") != "1":
        Timer(1.0, lambda: webbrowser.open(f"http://{host}:{port}")).start()
    uvicorn.run("pai_auto.app:app", host=host, port=port, reload=False)


if __name__ == "__main__":
    main()
