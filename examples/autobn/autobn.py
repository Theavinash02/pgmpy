import numpy as np

class AutoBN:
    def __init__(self,model = "gpt-4o-mini", n_iterations = 3, n_blueprints = 3, n_fixattempt = 1):
        self.model = model
        self.n_iterations = n_iterations
        self.n_blueprints = n_blueprints
        self.n_fixattempt = n_fixattempt

        self.trace = [] # History of all attempts[config, score, error]
        self.best_model = None
        self.best_score = -np.inf
        self.best_config = None
