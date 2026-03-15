import statsmodels.api as sm

exog,endog=sm.add_constant(x),y
model=sm.GLM(endog,exog,
             family=sm.families.Poisson(link=sm.families.links.log))
result=model.fit()