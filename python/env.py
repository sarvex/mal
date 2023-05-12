# Environment

class Env():
    def __init__(self, outer=None, binds=None, exprs=None):
        self.data = {}
        self.outer = outer or None

        if binds:
            for i in range(len(binds)):
                if binds[i] == "&":
                    self.data[binds[i+1]] = exprs[i:]
                    break
                else:
                    self.data[binds[i]] = exprs[i]

    def find(self, key):
        if key in self.data: return self
        elif self.outer:     return self.outer.find(key)
        else:                return None

    def set(self, key, value):
        self.data[key] = value
        return value

    def get(self, key):
        if env := self.find(key):
            return env.data[key]
        else:
            raise Exception(f"'{key}' not found")
