class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        # creating the hashmap of the patterns an easy
        # trick to make this a BFS solution
        for w in wordList:
            for i in range(len(w)):
                pattern = w[: i] + "*" + w[i + 1 :]
                nei[pattern].append(w)

        visit = set([beginWord])
        q = collections.deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                for j in range(len(w)):
                    pattern = w[: j] + "*" + w[j + 1 :]
                    for neiword in nei[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            res += 1
        return 0
        