class TVL:
    def __init__(self, name="angel", passion="developing"):
        self.name = name
        self.passion = passion

    def dev(self):
        print("Make a code...")

    def learn(self):
        print("I'm a developer")


ebi = TVL()
abi = TVL()

ebi.name = "Ebi"


print(ebi.name)
print(abi.name)

