import subprocess
import random
import json
from pathlib import Path
import click

@click.command()
@click.option("--out", type=click.Path(path_type=Path), required=True)
@click.option("--count", type=int, default=200)
def main(out: Path, count: int):
    categories = ["expired", "name_mismatch", "untrusted_root", "signature_failure", "other"]
    messages = []

    for i in range(count):
        cat = random.choice(categories)
        if cat == "expired":
            msg = "error 10 at 0 depth lookup: certificate has expired"
        elif cat == "name_mismatch":
            msg = "error 62 at 0 depth lookup: hostname mismatch"
        elif cat == "untrusted_root":
            msg = "error 20 at 0 depth lookup: unable to get local issuer certificate"
        elif cat == "signature_failure":
            msg = "error 7 at 0 depth lookup: signature verification failed"
        else:
            msg = "error 77 at 0 depth lookup: unknown error condition"
        messages.append({"text": msg, "label": cat})

    out.mkdir(parents=True, exist_ok=True)
    (out / "errors.json").write_text(json.dumps(messages, indent=2))
    click.echo(f"Generated {count} synthetic error messages at {out}/errors.json")

if __name__ == "__main__":
    main()

