import random

import numpy as np

def generate_client_resources(num_clients, mode="moderate"):
    """
    """
    resources = {}

    for cid in range(num_clients):
        r = random.random()

        if mode == "mild":
            compute_power = random.uniform(0.8, 1.2)
            bandwidth = random.uniform(0.8, 1.2)
            budget = random.uniform(0.8, 1.2)

        elif mode == "moderate":
            if r < 0.3:
                compute_power = random.uniform(0.3, 0.6)
                bandwidth = random.uniform(0.3, 0.6)
                budget = random.uniform(0.3, 0.6)
            elif r < 0.7:
                compute_power = random.uniform(0.7, 1.0)
                bandwidth = random.uniform(0.7, 1.0)
                budget = random.uniform(0.7, 1.0)
            else:
                compute_power = random.uniform(1.2, 2.0)
                bandwidth = random.uniform(1.2, 2.0)
                budget = random.uniform(1.2, 2.0)

        elif mode == "severe":
            if r < 0.5:
                compute_power = random.uniform(0.15, 0.4)
                bandwidth = random.uniform(0.15, 0.4)
                budget = random.uniform(0.15, 0.4)
            elif r < 0.8:
                compute_power = random.uniform(0.6, 1.0)
                bandwidth = random.uniform(0.6, 1.0)
                budget = random.uniform(0.6, 1.0)
            else:
                compute_power = random.uniform(1.5, 3.0)
                bandwidth = random.uniform(1.5, 3.0)
                budget = random.uniform(1.5, 3.0)
        else:
            raise ValueError(f"Unknown resource mode: {mode}")

        resources[cid] = {
            "compute_power": compute_power,
            "bandwidth": bandwidth,
            "budget": budget,
        }

    return resources


def calibrate_resource_budget(resources, group_param_counts, layer_budget):
    """
    """
    avg_params = np.mean(list(group_param_counts.values()))
    calibrated = {}

    for cid, res in resources.items():
        compute_power = res["compute_power"]
        bandwidth = res["bandwidth"]

        avg_cost = avg_params / bandwidth + avg_params / compute_power
        real_budget = res["budget"] * avg_cost * layer_budget

        calibrated[cid] = {
            "compute_power": compute_power,
            "bandwidth": bandwidth,
            "budget": real_budget,
        }

    return calibrated
