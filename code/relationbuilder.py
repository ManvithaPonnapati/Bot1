#print ("Hi")
# This script generates the relations between the objects and sends all the relations as outputs
import pickle

# relation(object1, object2)
relationKB={}
objectKB={}

# method: learn
# learns the relation between two objects and stores in the knowledge base(KB)
def learn(relation, object1, object2):
	if relation in relationKB.keys():
		args = (object1,object2)
		if not args in relationKB.get(relation):
			relationKB.get(relation).append(args)
	else:
		relationKB.update({relation:[(object1,object2)]})
	
	if object1 in objectKB.keys():
		if object2 in objectKB.get(object1):
			if relation not in objectKB.get(object1).get(object2):
				objectKB.get(object1).get(object2).append(relation)
		else:
			objectKB.get(object1).update({object2:[relation]})
	objectKB.update({objec1:{object2:[relation]}})
# end of learn function. 


# method: load KB
def loadKB():
	relationKBFile = "./relationKB.rkb"
	objectKBFile = "./objectKB.okb"
	loadKB(relationKBFile, objectKBFile)
# end of function loadKB
def loadKB(relationKBFile, object0KBFile):
	with open(relationKBFile,'r') as fp:
		relationKB = pickle.load(fp)
	fp.close()
	
	with open(objectKBFile,'r') as fp:
		objectKB = pickle.load(fp)
	fp.close()
# end of method loadKB from file names given

# method: dump the knowledge learnt into a pickle file
def dumpKB():
	relationKBFile = "./relationKB.rkb"
	objectKBFile = "./objectKB.okb"
	dumpKB(relationKBFile, objectKBFile)
# end of method dumpKB 

def dumpKB(relationKBFile, object0KBFile):
	with open(relationKBFile,'w') as fp:
		pickle.dump(relationKB,fp)
	fp.close()
	
	with open(objectKBFile,'w') as fp:
		pickle.dump(objectKB,fp)
	fp.close()
# end of method loadKB from file names given
