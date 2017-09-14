import pickle

class PickleOperations:
    a = 1
    b = 2

    def write(self):
        fp = open('picklesample1.txt','w')
        pickle.dump([1,2,3,4,5,6,6,6], fp)
        fp.close()

    def read(self):
        fp = open('picklesample1.txt', 'r')
        content = pickle.load(fp)
        fp.close()
        print "Inside read method \n"
        print content,type(content)

    def serialize_write_ex(self):
        _obj = PickleOperations()
        fp = open('serializeObj.txt', 'w')
        pickle.dump(_obj, fp)
        fp.close()

    def serialize_read_ex(self):
        fp = open('serializeObj.txt', 'r')
        content = pickle.load(fp)
        print "\n deserialized object a = " + str(content.a)
        print "\n deserialized object b = " + str(content.b)
        fp.close()
        print content,type(content)



_obj = PickleOperations()
_obj.write()
_obj.read()

_obj.serialize_write_ex()
_obj.serialize_read_ex()