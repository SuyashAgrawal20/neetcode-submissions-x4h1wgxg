class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i in range(len(equations)):
            a, b = equations[i]
            value = values[i]
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))
        
        def dfs(current: str, target: str, visited: set) -> float:
            if current in visited:
                return -1.0
            
            visited.add(current)

            if current == target:
                return 1.0
            
            for neighbor, weight in graph[current]:
                result = dfs(neighbor, target, visited)

                if (result != -1.0):
                    return weight * result
            return -1.0

        answers = []

        for numerator, denominator in queries:
            if numerator not in graph or denominator not in graph:
                answers.append(-1.0)
            else:
                answers.append(dfs(numerator, denominator, set()))
        return answers