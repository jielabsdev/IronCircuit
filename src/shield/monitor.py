import ironcircuit

class AgentShield:
    def __init__(self, max_tokens: float):
        self.policy = ironcircuit.Policy(max_tokens, True)
        self.monitor = ironcircuit.Monitor(self.policy)

    def check(self, tokens: float) -> bool:
        return self.monitor.check_usage(tokens)
