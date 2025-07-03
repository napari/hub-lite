import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _():
    # file to explore
    file_final_plugins_after_fetch = "../_build/data/final_plugins.csv"
    file_post_static = "../build/data/post_create_static_html_files.csv"
    return (file_final_plugins_after_fetch,)


@app.cell
def _(file_final_plugins_after_fetch, pd):
    df = pd.read_csv(file_final_plugins_after_fetch)
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
