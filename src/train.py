import json
from pathlib import Path
import click
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

@click.command()
@click.option("--data", type=click.Path(path_type=Path), required=True)
@click.option("--out", type=click.Path(path_type=Path), required=True)
def main(data: Path, out: Path):
    """
    Train a Naïve Bayes classifier on error messages.
    """
    records = json.loads(data.read_text())
    texts = [r["text"] for r in records]
    labels = [r["label"] for r in records]

    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("nb", MultinomialNB())
    ])

    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    report = classification_report(y_test, y_pred, digits=3)
    out.mkdir(parents=True, exist_ok=True)
    (out / "report.txt").write_text(report)
    joblib.dump(pipeline, out / "model.joblib")

    click.echo("Training complete. Report saved.")

if __name__ == "__main__":
    main()
