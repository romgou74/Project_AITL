from scipy import stats
import pandas as pd
import scikit_posthocs as sp
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./results/results2.csv", sep=";")

# Example: ANOVA on Flesch Reading Ease
groups = [
    df[df["category"] == "Youth"]["flesch_ease"],
    df[df["category"] == "MiddleAged"]["flesch_ease"],
    df[df["category"] == "Senior"]["flesch_ease"],
]

f_stat, p_value = stats.f_oneway(*groups)

print("ANOVA F-statistic:", f_stat)
print("p-value:", p_value)

posthoc = sp.posthoc_tukey(
    df,
    val_col="flesch_ease",
    group_col="category"
)

print(posthoc)

sns.boxplot(data=df, x="category", y="flesch_ease")
plt.savefig('plot.png')
