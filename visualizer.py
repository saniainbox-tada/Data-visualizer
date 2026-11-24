import matplotlib.pyplot as plt
categories= ["Rent","food","Transport","Entertaintment","Savings"]
amount=[12000,5000,5000,1000,2000]
color=["#21519e","#ba2fc2","#c22f7d","#e2e831","#99e831"]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Monthly Budget Breakdown (₹)", fontsize=16, fontweight="bold")
bars = ax1.bar(categories, amount, color=color)
ax1.set_title("Spending by Category")
ax1.set_ylabel("Amount (₹)")
ax1.grid(axis="y", linestyle="--", alpha=0.6)
bars = ax1.bar(categories, amount, color=color)
ax1.set_title("Spending by Category")
ax1.set_ylabel("Amount (₹)")
ax1.grid(axis="y", linestyle="--", alpha=0.6)

ax2.pie(amount, labels=categories, autopct="%1.1f%%", startangle=140, colors=color)
ax2.set_title("Percentage Share")
plt.tight_layout()
plt.savefig("budget_dashboard.png", dpi=300)
print("Chart saved as budget_dashboard.png!")

