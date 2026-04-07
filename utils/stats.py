import statsmodels.api as sm
from statsmodels.formula.api import ols

def run_anova(df):
    model = ols('Token_Count ~ C(Cultural_Group)', data=df).fit()
    table = sm.stats.anova_lm(model, typ=2)

    eta = table.loc['C(Cultural_Group)', 'sum_sq'] / table['sum_sq'].sum()

    return table, eta