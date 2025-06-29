from typing import Dict, cast

import pandas as pd
from sklearn.metrics import accuracy_score, classification_report


def get_classification_metrics_df(
    y_true, y_pred, model_name: str, average: str = "weighted"
) -> pd.DataFrame:
    report = cast(
        Dict[str, Dict[str, float]],
        classification_report(y_true, y_pred, output_dict=True),
    )

    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": report[f"{average} avg"]["precision"],
        "recall": report[f"{average} avg"]["recall"],
        "f1-score": report[f"{average} avg"]["f1-score"],
    }

    return pd.DataFrame(metrics, index=pd.Index([model_name]))


def get_train_test_metrics_df(
    y_test, y_test_pred, model_name, y_train, y_train_pred, average="weighted"
):
    train_df = get_classification_metrics_df(
        y_train, y_train_pred, model_name, average=average
    )
    train_df.columns = pd.MultiIndex.from_product([["train"], train_df.columns])

    test_df = get_classification_metrics_df(
        y_test, y_test_pred, model_name, average=average
    )
    test_df.columns = pd.MultiIndex.from_product([["test"], test_df.columns])

    return pd.concat([train_df, test_df], axis=1)


def get_per_class_metrics_df(y_true, y_pred, model_name, id2label):
    report = cast(
        Dict[str, Dict[str, float]],
        classification_report(y_true, y_pred, output_dict=True),
    )

    df = pd.DataFrame(report).drop(columns=["accuracy"]).T

    df.index = [i if not str(i).isdigit() else id2label[int(i)] for i in df.index]

    df.index = pd.MultiIndex.from_product(
        [[model_name], df.index], names=["model", "class"]
    )

    return df
