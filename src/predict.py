import json
from pathlib import Path
import click
import joblib

@click.command()
@click.option("--model", type=click.Path(path_type=Path), required=True)
@click.option("--message", type=str, required=True)
def main(model: Path, message: str):
    
    pipeline = joblib.load(model)
    pred = pipeline.predict([message])[0]
    probs = pipeline.predict_proba([message])[0]
    classes = pipeline.classes_
    result = {c: float(p) for c, p in zip(classes, probs)}

    output = {
        "message": message,
        "predicted_category": pred,
        "probabilities": result
    }
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
