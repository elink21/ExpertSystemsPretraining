# Dead simple example of a GA pointing the most important sections of the method

from typing import Callable, List, Tuple, Optional
from random import choices, randint, randrange, random
from functools import partial

from collections import namedtuple

# Definitions needed to model the algorithm
Genome = List[int]
Population = List[Genome]


Thing = namedtuple('Thing', ['name', 'value', 'weight'])


# The fitness function model will receive a genome 🧬,
# list of things(population),and a maximum weight ⚖
FitnessFunction = Callable[[Genome], int]
PopulateFunction = Callable[[], Population]
SelectionFunction = Callable[[Population,
                              FitnessFunction], Tuple[Genome, Genome]]
CrossoverFunction = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunction = Callable[[Genome], Genome]


things = [
    Thing('💻', 500, 2200),
    Thing('🎧', 150, 160),
    Thing('☕', 60, 350),
    Thing('📔', 40, 333),
    Thing('♨', 30, 192)
]


def generateGenome(length: int) -> Genome:
    return choices([0, 1], k=length)


def generatePopulation(size: int, genomeLength: int) -> Population:
    return [generateGenome(genomeLength) for _ in range(size)]


def fitnessFunction(genome: Genome, things: List[Thing], weightLimit: int) -> int:
    if len(genome) != len(things):
        raise ValueError("Things and genome size must be the same")

    weight = 0
    value = 0

    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value

        if weight > weightLimit:
            return 0

    return value


def selectionPair(population: Population, fitness_func: fitnessFunction) -> Population:
    return choices(
        population=population,
        weights=[fitness_func(genome) for genome in population],
        k=2
    )


def singlePointCrossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:

    if len(a) != len(b):
        raise ValueError("Genomes must be of the same length")

    if (len(a) < 2):
        return a, b

    crossPoint = randint(0, len(a)-1)
    a, b = a[0:crossPoint] + b[crossPoint:], b[0:crossPoint]+a[crossPoint:]
    return a, b


def mutation(genome: Genome, bitsToMutate: int = 1, probability: float = 0.5) -> Genome:
    for _ in range(bitsToMutate):
        index = randrange(len(genome))
        genome[index] = genome[index] if random(
        ) < probability else int(not(genome[index]))

    return genome


def runEvolution(
        populate_func: PopulateFunction,
        fitness_func: FitnessFunction,
        fitness_limit: int,
        selection_func: SelectionFunction = selectionPair,
        crossover_func: CrossoverFunction = singlePointCrossover,
        mutation_func: MutationFunction = mutation,
        generation_limit: int = 100,) -> Tuple[Population, int]:

    population = populate_func()
    for i in range(generation_limit):
        # We need to sort first so the first solutions will be
        # The more likely to have good genes
        population = sorted(
            population,
            key=lambda genome: fitness_func(genome),
            reverse=True
        )

        # Check if fitness limit was reached
        if(fitness_limit <= fitness_func(population[0])):
            break

        # Keep top 2 solutions for next generation

        nextGeneration = population[0:2]

        # Now a  new generation wil be created using the selection pair, cross and mutation functions
        for j in range((len(population)//2)-1):
            parents = selection_func(population, fitness_func)

            offspringA, offspringB = crossover_func(parents[0], parents[1])

            offspringA = mutation_func(offspringA)
            offspringB = mutation_func(offspringB)

            nextGeneration += [offspringA, offspringB]

        # Updating the generation
        population = nextGeneration

        # Re - sorting the population one last time just for displaying
        population = sorted(
            population,
            key=lambda genome: fitness_func(genome),
            reverse=True
        )

    return population, i


# Now its time to run the model using predefined parameters with the previous functions
population, generations = runEvolution(
    populate_func=partial(generatePopulation, size=10,
                          genomeLength=len(things)),
    fitness_func=partial(fitnessFunction, things=things, weightLimit=3000),
    fitness_limit=740,
    generation_limit=100
)

# Help function to turn genome into thing


def genomeToThing(genome: Genome, things: List[Thing]) -> List[Thing]:
    res = []
    for i, thing in enumerate(things):
        if genome[i] == 1:
            res += thing.name
    return res


print(f"number of generations:{generations}")
print(f"Best solution was: {genomeToThing(population[0],things)}")
