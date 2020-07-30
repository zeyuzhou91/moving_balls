import numpy as np
import scipy as sp
import scipy.stats as st
import matplotlib.pyplot as plt


class System:
    def __init__(self, k, i0, pos):
        
        self.k = k      # total number of balls 
        self.i0 = i0    # the position of the left-most occupied integer/box 
        self.pos = pos  # an array of the number of balls on a consecutive sequence of integers/boxes, starting from i0
        if sum(pos) != k:
            raise ValueError('The number of balls specified in pos does not equal to k.')
                
    def move(self):
        """
        Take a ball from the left-most occupied box and place it to the right of 
        a ball chosen uniformly at random from among the k balls. 
        """
        
        ## choose a ball uniformly at random
        c = np.arange(len(self.pos))   
        i = np.random.choice(c, p = self.pos/float(self.k))  # Choose a ball uniformly at random.
                                                             # Equivalently, choose a box according to distribution p.
                                                             # i is the position of the chosen ball/box
        #print('i =', i)
        
        ## move a left-most ball to the box to right of the chosen ball
        self.pos[0] -= 1   # take out one ball from the left-most box
        if i == len(self.pos)-1:  # if the chosen box is the right-most box
            self.pos = np.append(self.pos, 1)   # add one more box to the right and put the ball in it
        else:              
            self.pos[i+1] += 1                  # put the ball in the box right to the chosen box
        if self.pos[0] == 0:      # if the left-most box becomes empty
            self.pos = np.delete(self.pos, 0)   # remove the left-most box
            self.i0 += 1 
        #print('pos =', self.pos)
        #print('i0 =', self.i0)
        return None
    
    
    def plot(self, t, T):
        """
        Plot the current configuration of the system (balls in boxes) on the 
        real line.
        """
        
        plt.figure(1) 
        plt.clf()  # clear the current figure
        plt.ion()  # without this, plt.show() will block the code execution        
        markerline, stemlines, baseline = plt.stem(np.arange(len(self.pos))+self.i0, self.pos, markerfmt=' ')
        plt.setp(stemlines, 'color', 'r', 'linewidth', 5)
        plt.xlim([0, self.k + np.exp(1)/self.k*T*2])
        plt.ylim([0, self.k])        
        #plt.grid()
        plt.ylabel('# of balls')
        plt.title('t =' + str(t))
        plt.show() 
        plt.pause(0.0001) 
        return None
        


if __name__ == "__main__":
    
    k = 100   # total number of balls
    i0 = 0  # the position of the left most occupied integer/box
    pos = np.ones(k)   # the number of balls on a consecutive sequence of intergers/boxes, starting from i0
    G = System(k, i0, pos)
    
    T = 10*k   # time
    for t in range(T):
        G.move()
        G.plot(t, T)
        
