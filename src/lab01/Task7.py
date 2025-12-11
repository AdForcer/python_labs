Cypher_ = input()
FirstLetterID = 0
for Firstletter in Cypher_:
    if Firstletter in "QWERTYUIOPASDFGHJKLZXCVBNM":
        break
    FirstLetterID += 1
Cypher_ = Cypher_[FirstLetterID:]
SecondLetterID = 0
for SecondLetter in Cypher_:
    if SecondLetter in "0123456789":
        SecondLetterID += 1
        break
    SecondLetterID += 1
Step = SecondLetterID
New_String = Cypher_[0] + Cypher_[SecondLetterID]
Cypher_ = Cypher_[SecondLetterID + 1 :]
for ID in range(Step - 1, len(Cypher_), Step):
    New_String += Cypher_[ID]
print(New_String)
