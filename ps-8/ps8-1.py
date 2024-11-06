import jax.numpy as jnp
from jax import grad, hessian
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('survey.csv')

age = jnp.array(df['age'])
prob = jnp.array(df['recognized_it'])

def logistic_model(x, params):
    beta0 = params[0]
    beta1 = params[1]
    return 1 / (1 + jnp.exp(-(beta0 + beta1 * x)))

def negative_log_likelihood(params, *args):
    age = args[0]
    decision = args[1]
    p = logistic_model(age, params=params)
    return -jnp.sum(decision * jnp.log(0.01 + p*0.99) + (1 - decision) * jnp.log(1 - p*0.99)) + 0.0001*(params[0]**2 + params[1]**2)

xpath = []
def squirrel(xk):
    global xpath
    xpath.append(np.array(xk))

initial_params = jnp.array([0.1, -0.01])

result = minimize(negative_log_likelihood,
                  initial_params, args=(age,prob),jac=grad(negative_log_likelihood), tol=1e-6, callback=squirrel)

hess = hessian(lambda params: negative_log_likelihood(params, age, prob))(result.x)
cov_matrix = jnp.linalg.inv(hess)
errors = jnp.sqrt(jnp.diag(cov_matrix))

print("maximum likelihood values for beta0 and beta1 is",result.x)
print("formal errors for beta0 and beta1:", errors)
print("covariance matrix for beta0 and beta1", cov_matrix)

x1 = np.arange(0,80,1)
plt.plot(x1,logistic_model(x1,[result.x[0], result.x[1]]),label="logistic_regression")
plt.plot(age,prob,"+",label="real data")
plt.xlabel("age")
plt.ylabel("choice(1 for yes)")
plt.legend()
plt.savefig("8-1-1.png")
plt.clf()
