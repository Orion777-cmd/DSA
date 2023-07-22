class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict_ = defaultdict(list)
        for path in paths:
            directory , *files = path.split()
            for file in files:
                filename, content = file.split('(')
                dict_[content].append(directory + '/' + filename)
        return [path for path in dict_.values() if len(path)>1]
        
