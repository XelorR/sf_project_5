from pprint import pprint
import warnings

warnings.filterwarnings("ignore")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import (
    roc_auc_score,
    roc_curve,
    classification_report,
)


def describe_nums(df: pd.DataFrame, sort_by="unique"):
    return (
        df.nunique()
        .to_frame()
        .rename(columns={0: "unique"})
        .join(df.isna().sum().to_frame().rename(columns={0: "n/a count"}))
        .join(df.describe().T, how="left")
        .sort_values([sort_by], ascending=False)
        .style.bar(["mean"])
        .background_gradient(subset=["50%"], cmap="viridis")
        .background_gradient(subset=["std"], cmap="Reds")
        .bar("unique", color="lightblue")
    )


def show_IQR(series, bins_n=None):

    perc_25 = series.quantile(0.25, interpolation="midpoint")
    perc_75 = series.quantile(0.75, interpolation="midpoint")
    IQR = perc_75 - perc_25

    print(
        f"Unique values count: {series.nunique()}",
        f"\nQ1: {perc_25}\nQ3: {perc_75}\nIQR: {IQR}",
        f"\nOutliers borders: [{perc_25 - 1.5*IQR}, {perc_75 + 1.5*IQR}]",
    )

    fig, axes = plt.subplots(ncols=2, figsize=(16, 6))
    sns.distplot(series.values, bins=bins_n, color="#50248f", ax=axes[0]).set(
        xlabel=series.name,
        ylabel="Quantity (frequency)",
        title=series.name + " distribution\n",
    )

    sns.boxplot(series.values, color="#38d1ff", ax=axes[1]).set(
        xlabel=series.name, title=series.name + " distribution\n"
    )

    plt.show()


def show_boxplots(df, cat, numeric):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(
        x=cat,
        y=numeric,
        data=df,
        ax=ax,
    )
    ax.set_title("Boxplot for: " + cat + " vs " + numeric)
    plt.show()


def show_classification_details(y_tr, y_pr):

    roc_auc = roc_auc_score(y_tr, y_pr)
    fpr, tpr, threshold = roc_curve(y_tr, y_pr)

    plt.figure()
    plt.plot([0, 1], label="Baseline", linestyle="--")
    plt.plot(fpr, tpr, label="Regression")
    plt.title("Logistic Regression ROC AUC = %0.3f" % roc_auc)
    plt.ylabel("True Positive Rate")
    plt.xlabel("False Positive Rate")
    plt.legend(loc="lower right")
    plt.show()
    pprint(classification_report(y_tr, y_pr).split("\n"))
