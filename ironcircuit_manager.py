import ironcircuit, functools, json, os, threading

class CircuitBreakerError(Exception): pass

class IronCircuitManager:
    def __init__(self, policy_path='policy.json', state_path='state.json'):
        self.state_path = os.path.join(os.getcwd(), state_path)
        self.policy_path = os.path.join(os.getcwd(), policy_path)
        self.lock = threading.Lock()
        self.reload_policy()

    def reload_policy(self):
        policy_data = self._load_json(self.policy_path, {'max_tokens': 1000.0, 'fail_closed': True})
        state_data = self._load_json(self.state_path, {'usage': 0.0})
        self.monitor = ironcircuit.Monitor(
            ironcircuit.Policy(policy_data['max_tokens'], policy_data['fail_closed']),
            state_data['usage']
        )

    def reset_usage(self):
        with self.lock:
            self.reload_policy()
            # We could extend the monitor to allow explicit reset, but for now re-init works
            self.save_state()

    def _load_json(self, path, default):
        try:
            if os.path.exists(path):
                with open(path, 'r') as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError): pass
        return default

    def save_state(self):
        with self.lock:
            try:
                with open(self.state_path, 'w') as f:
                    json.dump({'usage': self.monitor.get_usage()}, f)
            except IOError: pass

    def protect(self, token_cost):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if not self.monitor.check_usage(token_cost):
                    raise CircuitBreakerError('Limit exceeded.')
                self.save_state()
                return func(*args, **kwargs)
            return wrapper
        return decorator
