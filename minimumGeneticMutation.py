class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        if endGene not in bank:
            return -1
        
        def bfs(source, target, count):
            queue = [(source, count)]
            
            while queue:
                gene, count = queue.pop(0)
                
                if gene == target:
                    return count
                
                for i in range(len(gene)):
                    for nucleotide in ['A', 'C', 'G', 'T']:
                        new_gene = gene[:i] + nucleotide + gene[i+1:]
                        
                        if new_gene in bank:
                            bank.remove(new_gene)
                            queue.append((new_gene, count + 1))
            
            return -1
        
        return bfs(startGene, endGene, 0)
            
