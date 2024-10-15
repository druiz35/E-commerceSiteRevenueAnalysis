import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import pandas as pd
import plotly.express as px


def plot_freight_value_weight_relationship(data): 
    sns.scatterplot(data=data, x="product_weight_g", y="freight_value")

def plot_global_amount_order_status(df): 
    _, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    elements = [x.split()[-1] for x in df["order_status"]]

    wedges, autotexts = ax.pie(df["Ammount"], textprops=dict(color="w"))

    ax.legend(
        wedges,
        elements,
        title="Order Status",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
    )

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title("Order Status Total")

    my_circle = plt.Circle((0, 0), 0.7, color="white")
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    plt.show()

def plot_real_vs_predicted_delivered_time(data): 
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)

    _, ax1 = plt.subplots(3, 1, figsize=(15, 6))

    years = [2016, 2017, 2018]


    for i in range(3):
        subax = ax1[i]
        year = years[i]

        sns.lineplot(data=data[f"Year{year}_real_time"], marker="o", sort=False, ax=subax)
        subax.twinx()
        g = sns.lineplot(
            data=data[f"Year{year}_estimated_time"], marker="o", sort=False, ax=subax
        )
        g.set_xticks(range(len(data)))
        g.set_xticklabels(data.month.values)
        g.set(xlabel="month", ylabel="Average days delivery time", title="some title")
        subax.set_title(f"Average days delivery time by month in {year}")
        subax.legend(["Real time", "Estimated time"])

    plt.tight_layout()
    plt.show()

def plot_revenue_by_month_year(data): 
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)

    _, ax1 = plt.subplots(3, 1, figsize=(15, 6))
    years = [2016, 2017, 2018]
    for i in range(3):
        subax = ax1[i]
        year = years[i]
        
        sns.lineplot(data=data[f"Year{year}"], marker="o", sort=False, ax=subax)
        subax2 = subax.twinx()

        sns.barplot(data=data, x="month", y=f"Year{year}", alpha=0.5, ax=subax2)
        subax.set_title(f"Revenue by month in {year}")

    plt.tight_layout()
    plt.show()

def plot_revenue_per_state(data): 
    fig = px.treemap(
        data, path=["customer_state"], values="Revenue", width=800, height=400
    )
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    fig.show()

def plot_top_10_least_revenue_categories(data): 
    _, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    elements = [x.split()[-1] for x in data["Category"]]

    revenue = data["Revenue"]
    wedges, autotexts = ax.pie(revenue, textprops=dict(color="w"))

    ax.legend(
        wedges,
        elements,
        title="Top 10 Revenue Categories",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
    )

    plt.setp(autotexts, size=8, weight="bold")
    my_circle = plt.Circle((0, 0), 0.7, color="white")
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    ax.set_title("Top 10 Least Revenue Categories ammount")

    plt.show()

def plot_top_10_revenue_categories(data): 
    fig = px.treemap(data, path=["Category"], values="Num_order", width=800, height=400)
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    fig.show()

def plot_top_10_revenue_categories_ammount(data): 
    # Plotting the top 10 revenue categories ammount
    _, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    elements = [x.split()[-1] for x in data["Category"]]

    revenue = data["Revenue"]
    wedges, autotexts = ax.pie(revenue, textprops=dict(color="w"))

    ax.legend(
        wedges,
        elements,
        title="Top 10 Revenue Categories",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
    )

    plt.setp(autotexts, size=8, weight="bold")
    my_circle = plt.Circle((0, 0), 0.7, color="white")
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    ax.set_title("Top 10 Revenue Categories ammount")

    plt.show()

def plot_delivery_date_difference(data): 
    sns.barplot(data=data, x="Delivery_Difference", y="State").set(
        title="Difference Between Delivery Estimate Date and Delivery Date"
    )

def plot_order_amount_per_day_with_holidays(data, holidays_data): 
    matplotlib.rc_file_defaults()   
    sns.set_style(style=None, rc=None)

    _, ax1 = plt.subplots(figsize=(12, 6))
    holidays = pd.to_datetime(holidays_data["order_day"])
    data["order_day"] = pd.to_datetime(data["order_day"])
    sns.lineplot(data=data, x="order_day", y="order_count", color="green", ax=ax1)
    for holiday in holidays:
        plt.axvline(x=holiday, linestyle="dotted")
    ax1.set(xlabel=None, ylabel=None)
    plt.show()    