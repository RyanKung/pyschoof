from support.running import AlgorithmRunner
from .reduced_computation_schoof import reduced_computation_schoof_algorithm
from .naive_schoof import naive_schoof_algorithm


def reduced_schoof():
    runner = AlgorithmRunner(
        reduced_computation_schoof_algorithm,
        algorithm_version="$Rev$"
    )
    runner.run()


def naive_schoof():
    runner = AlgorithmRunner(
        naive_schoof_algorithm,
        algorithm_version="$Rev$"
    )
    runner.run()
