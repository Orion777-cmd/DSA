class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dict = defaultdict(list)
        for preq in prerequisites:
            want, must = preq
            if want in course_dict[must]:
                return False
            course_dict[want].append(must)

        visited = set()
        visiting = set()

        def dfs(course):
            if course in visiting:
                # Cycle detected
                return False
            if course in visited:
                return True

            visiting.add(course)

            for preq in course_dict[course]:
                if not dfs(preq):
                    return False

            visiting.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
