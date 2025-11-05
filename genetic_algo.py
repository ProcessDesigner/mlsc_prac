import numpy as np
import matplotlib.pyplot as plt

# Fitness function
def f(x):
    return x * (np.sin(10 * np.pi * x) + 1)

# Initialize population
pop = np.random.rand(20)
best = []
lr = 0.5

# GA loop
for gen in range(50):
    fit = f(pop)
    best.append(fit.max())

    # Selection (roulette wheel)
    prob = fit / fit.sum()
    pop = np.random.choice(pop, 20, p=prob)

    # Crossover & Mutation
    for i in range(20):
        if np.random.rand() < 0.8:  # Crossover
            mate = np.random.randint(20)
            pop[i] = (pop[i] + pop[mate]) / 2
        if np.random.rand() < 0.1:  # Mutation
            pop[i] = np.clip(pop[i] + np.random.uniform(-0.1, 0.1), 0, 1)

# Best solution
bx = pop[np.argmax(f(pop))]
print("Best x =", round(bx, 4), "Max f(x) =", round(f(bx), 4))

# Plot fitness over generations
plt.plot(best, 'r-o')
plt.title("Best Fitness Over Generations")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.show()
