import random
from typing import Dict, Any

class GeneticAlgorithm:
    def __init__(self, population_size: int = 100):
        self.population = []
        self.population_size = population_size

    def evolve(self) -> None:
        """Perform one generation of evolution on the population."""
        for _ in range(self.population_size // 2):
            parent1 = random.choice(self.population)
            parent2 = random.choice(self.population)
            child1 = self.crossover(parent1, parent2)
            child2 = self.mutate(child1)
            self.population.append(child2)

    def crossover(self, parent1: Dict[str, Any], parent2: Dict[str, Any]) -> Dict[str, Any]:
        """Perform a simple crossover between two parents."""
        return {**parent1, **parent2}

    def mutate(self, individual: Dict[str, Any]) -> Dict[str, Any]:
        """Introduce mutations into an individual's genome."""
        mutated = individual.copy()
        for key in mutated:
            if random.random() < 0.1:  # Mutation rate of 10%
                mutated[key] = self.randomize_value(mutated[key])
        return mutated

    def randomize_value(self, value: Any) -> Any:
        """Randomly modify a value."""
        if isinstance(value, int):
            return random.randint(0, 255)
        elif isinstance(value, float):
            return random.uniform(0.0, 1.0)
        else:
            return str(random.choice(["a", "b", "c"]))