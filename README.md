# metaheuristics-comparison
Comparison of the solutions of different meta-heuristic algorithms to a simple problem.

## Problem
Problem is simple. The algorithm must find a way from a starting point to a destination. The map is defined by the mapX and mapY variables inside scripts.

![Map](map.png?raw=true)

## Solution
The solution candidates are formed of steps. These parts define angles for movement. Step size, candidate size and other parameters special to the algorithm are defined within scripts.

## Harmony Search
Harmony memory size is chosen as 30 and the solution size as 100. HMCR (Harmony Memory Consideration Rate) as 99% and PAR (Pitch Adjust Rate) as 1%.

### Convergence
![Convergence](harmony/solutions.gif?raw=true)

### Loss
![Loss](harmony/loss.gif?raw=true)

## Genetic Algorithm
Population size is chosen as 30 and the gene size as 100. Breeder count as 10. So the remaining 20 of the population is replaced with the children. Children are mutated with the chance of 1%.

### Convergence
![Convergence](genetic/solutions.gif?raw=true)

### Loss
![Loss](genetic/loss.gif?raw=true)

## Differential Evolution
Population size is chosen as 30 and the solution size as 100. Differential constant as 0.1 and Crossover rate 0.5.

### Convergence
![Convergence](differential/solutions.gif?raw=true)

### Loss
![Loss](differential/loss.gif?raw=true)

## Artificial Bee Colony
Worker bee count is selected as 20. Onlooker bee count is selected as 20. Scout limit as 50. Food source count is selected as 30 and the size 100.

### Convergence
![Convergence](abc/solutions.gif?raw=true)

### Loss
![Loss](abc/loss.gif?raw=true)


