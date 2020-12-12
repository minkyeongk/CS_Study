class Node(object):
    def __init__(self, key, data=None):
        self.key = key      # 키가 인덱스 역할을 해주나?
        self.data = data        # end_flag
        self.children = {}

# 이 오브젝트 뭐지?
class Trie(object):
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        cur_node = self.root

        for c in string:        # c가 문잔데?
            if c not in cur_node.children:
                cur_node.children[c] = Node(c)
            cur_node = cur_node.children[c]
            cur_node.data = string

    # return이 true, false라서 있는지 없는지만 체크가능한건가, 애초에 이 자료구조가 그런건가
    def search(self, string):
        cur_node = self.root
        for c in string:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                return False
        if cur_node.data != None:
            return True

    def starts_with(self, prefix):
        cur = self.root
        result = []
        subt = None

        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
                subt = cur
            else:
                return None

        q = list(subt.children.values())

        while q:
            cur = q.pop(0)
            if cur.data != None:        # 마지막 문자이면
                result.append(cur.data)
            q += list(cur.children.values())

        return result

t = Trie()
words = ["romane", "romanus", "romulus", "ruben", 'rubens', 'ruber', 'rubicon', 'ruler']
for w in words:
    t.insert(w)

print(t.search("romulus"))
print(t.search("ruler"))
print(t.search("rulere"))
print(t.search("romunus"))
print(t.starts_with("ro"))
print(t.starts_with("rube"))