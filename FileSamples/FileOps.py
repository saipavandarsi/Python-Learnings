# we can have r/w/a modes when we have a file operations


class FileOps:
    count = 0

    def write_file(self):
        fp = open('myfile.txt.txt','w')
        fp.write('hi shruthi \n hi how are you ')
        fp.close()

    def read_file(self):
        file = open('myfile.txt.txt','r')
        content = file.readlines()
        print content
        for line in content :
            print line
            if(line in 'hi'):
                count = self.count +1
        return self.count

    def find_word(self,word):
        line,pos,count = 0,0,0
        content = open('myfile.txt.txt','r').readlines()
        for ln in content:
            line += 1
            if word in ln:
                pos = ln.find(word)
                if(pos):
                    count = count+1
                print line,pos,count




_file = FileOps()
#_file.write_file()
val = _file.read_file()
_file.find_word('hi')
print val