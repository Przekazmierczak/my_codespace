"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""

class Solution:
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    def findOrder(self, numCourses, prerequisites):
        courses = {}
        visited = set()
        path = []
        
        for i in range(numCourses):
            courses[i] = set()
            
        for course in prerequisites:
            courses[course[0]].add(course[1])
            
        def dfs(course):
            if not courses[course]:
                if course not in path:
                    path.append(course)
                return True
            if course in visited:
                return False
            
            visited.add(course)
            
            to_remove = []
            for limit in courses[course]:
                if dfs(limit):
                    to_remove.append(limit)
            for course_to_remove in to_remove:
                courses[course].remove(course_to_remove)
                
            if not courses[course]:
                if course not in path:
                    path.append(course)
                return True
            
            return False
        
        for course in courses:
            dfs(course)
        
        for course in courses:
            if courses[course]:
                return []
        return path
        
    
def main():
    numCourses = 3
    prerequisites = [[1,0],[1,2],[0,1]]

    solution = Solution()

    result = solution.findOrder(numCourses, prerequisites)
    
    print(result)


if __name__ == "__main__":
    main()