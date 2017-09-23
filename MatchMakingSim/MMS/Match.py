# from libs import charactors
import os,sys
script_dir=os.path.dirname(__file__)#abs dir the script in
sys.path.append(os.path.join(script_dir,"libs"))
import charactors

class Match(object):
    def __init__(self,m_filename,w_filename):
        self.men_pool={m[0]:charactors.MalePlayer(*m) for m in readPlayerFile(m_filename)}
        self.women_pool={w[0]:charactors.FemalePlayer(*w) for w in readPlayerFile(w_filename)}
        self.MainM=charactors.MalePlayer()
        self.MainF=charactors.FemalePlayer()
        self.queen=charactors.FemalePlayer(charactors.Woman())
        for mkey,mval in self.men_pool.items():
            for wkey,wval in self.women_pool.items():
                mval.new_girl(wval)

    def kick_start(self,line):
        self.add_player(line)

        self.make_invitation()
        while self.matching_n_reset():
            self.make_invitation()

        self.restore()

    def initialize(self,m_filename,w_filename):
        for m in readPlayerFile(m_filename):
            self.men_pool[m[0]]=charactors.MalePlayer(*m)
        for w in readPlayerFile(w_filename):
            self.women_pool[w[0]]=charactors.FemalePlayer(*w)
        for mkey,mval in self.men_pool.items():
            for wkey,wval in self.women_pool.items():
                mval.new_girl(wval)
        self.queen=charactors.FemalePlayer(charactors.Woman())

    def find_queen(self,a):
        pa=a.check_popularity()
        pb=self.queen.check_popularity()
        alt_a=a.appearence()+a.personality()+a.wealth()
        alt_q=self.queen.appearence()+self.queen.personality()+self.queen.wealth()

        if pa>pb:
            self.queen=a
        elif pa==pb:
            if alt_a>alt_q:
                self.queen=a
            elif alt_a==alt_q:
                self.queen=a if a.id()<self.queen.id() else self.queen

    def make_invitation(self):
        if self.MainM.is_loaded():
            w=self.MainM.dream_girl()
            w.meet(self.MainM)
            w.more_popular()
            self.find_queen(w)
        for k, v in self.men_pool.items():
            if v.is_avail():
                w=v.dream_girl()
                w.meet(v)
                w.more_popular()
                self.find_queen(w)

    def reset_women_pool(self):
        for k,v in self.women_pool.items():
            v.reset()
        if self.MainF.is_loaded():
            self.MainF.reset()
        self.queen=charactors.FemalePlayer(charactors.Woman())

    def matching_n_reset(self):
        the_one=self.queen.she_loves()
        if self.queen.id()==-1:
            print("Congratulation: you found your man. Male: %d"%the_one.id())
            self.MainF.free()
            self.queen.chosen()
            return False

        if the_one.id()==-1:
            print("Congratulation: you just found your woman. Female: %d"%self.queen.id())
            self.MainM.free()
            return False;

        self.queen.chosen()
        the_one.chosen()

        self.reset_women_pool();
        return True

    def add_player(self,line):
        if line[0]:
            id=15
            if self.men_pool.get(id):
                self.men_pool[id].chosen()

            self.MainM=charactors.MalePlayer(-1,*line[1:])
            for k,v in self.women_pool.items():
                self.MainM.new_girl(v)
            if self.MainM.q_size()==100:
                print("Player met all the girls.")
            if self.MainM.expect_check():
                print("Player created.")
            else:
                print("Player's data is corrupted.")

        else:
            id=99
            if self.women_pool.get(id):
                self.women_pool[id].chosen()

            self.MainF=charactors.FemalePlayer(-1,*line[1:])

            for k,v in self.men_pool.items():
                v.new_girl(self.MainF)
            print("Player is introduced.")
            if self.MainF.expect_check():
                print("Player created.")
            else:
                print("Player's data is corrupted.")

    def restore(self):
        for k,v in self.men_pool.items():
            if v.is_avail() is False:
                v.ready()
            v.restore()

        for k,v in self.women_pool.items():
            if v.is_avail() is False:
                v.ready()

        self.reset_women_pool()
        print("***********************************************")


def readPlayerFile(filename,lines=0):
    # take string filename as argument, open the designated file, return tuple line by line
    with open(filename,"r") as f:
        mylist=list()
       # read the whole file
        if lines == 0:
            mylist=[tuple(map(int,i.strip().split(','))) for i in f.readlines()]
        else:
        # read first some lines
            for line in range(lines):
                l=f.readline().strip()
                mylist.append(tuple(map(int,l.split(','))))

    return mylist

