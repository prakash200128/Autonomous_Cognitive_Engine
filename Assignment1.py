# 1. MEMORY CLASS

class Memory:
    def __init__(self):
        self.data = None

    def store(self, info):
        self.data = info
        print(f"Memory stored: {info}")

    def retrieve(self):
        print("Memory retrieved:")
        return self.data

    def clear(self):
        self.data = None
        print("Memory cleared")


# 2. TOOL CLASSES

class Tool:
    def use(self, input_text):
        raise NotImplementedError("Child classes must override this method")


class SearchTool(Tool):
    def use(self, input_text):
        # Simulated search result
        return f"Search results for '{input_text}': [Result1, Result2]"


class SummaryTool(Tool):
    def use(self, input_text):
        # Very simple summary
        return f"Summary: {input_text[:20]}..."


# 3. AGENT CLASS

class Agent:
    def __init__(self, name, role, memory, tools):
        self.name = name
        self.role = role
        self.memory = memory
        self.tools = tools

    def think(self):
        print(f"{self.name} is thinking...")
        stored_info = self.memory.retrieve()
        return f"Thinking based on memory: {stored_info}"

    def act(self, task):
        print(f"{self.name} is acting...")
        results = []

        for tool in self.tools:
            result = tool.use(task)
            results.append(result)

        return results

    def run(self, task):
        print(f"Agent {self.name} running...\n")
        thinking_output = self.think()
        print(thinking_output)

        action_output = self.act(task)
        print("\nAction Results:")
        for r in action_output:
            print("-", r)

memory = Memory()
memory.store("Python OOP concepts")

tools = [SearchTool(), SummaryTool()]

agent = Agent("Alpha", "Assistant Agent", memory, tools)

agent.run("Explain Object Oriented Programming in Python")
