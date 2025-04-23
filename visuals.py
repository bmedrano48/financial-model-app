import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter

def plot_distributions(values, title, xlabel=None):
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(values, kde=True, ax=ax, bins=30, color="skyblue")
    ax.set_title(title)
    
    # Format x-axis to show values in $X million
    def millions_formatter(x, pos):
        return f'${x / 1e6:.1f}M'
    ax.xaxis.set_major_formatter(FuncFormatter(millions_formatter))
    
    if xlabel:
        ax.set_xlabel(xlabel)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    # Show summary stats
    summary = pd.Series(values).describe(percentiles=[0.25, 0.5, 0.75])
    st.write("Summary Statistics")
    st.dataframe(summary.to_frame(name=title))
