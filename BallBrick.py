
class BallBrick:
    def __init__(self,Game,Ball_count,Ball_position,size_martrix):
        self.Game = Game #game at starting position and access anyywhere in the class to change
        self.size_martrix=size_martrix #size of the matrix access any where
        self.Ball_count = Ball_count #ball count
        self.Ball_position = Ball_position #current ball count
        
    #function to take a shot according to the direction it will take direction as a parameter
    
    def TakeShot(self,direction):
        Game[self.size_martrix-1][self.Ball_position]="G" #when the direction is selected set the current ball position as Ground
        temp_ball_position=self.Ball_position #assign ball position to temp_ball_position
        for traverse in range(self.size_martrix-2,-1,-1):#when the shot is taken then the ball traverse from doen to top
            
            #if the direction is Left then reduce temp_ball_position by 1 else if the direction is Right increment by one
            #if the direct is stright we doesnt change the temp_ball_positiion
            if(direction=="LD"):
                temp_ball_position-=1
            elif(direction=="RD"):
                temp_ball_position+=1
            #if temp_ball_position is greater or equal to size of matrix or temp_ball_position less than zero break the loop
            if(temp_ball_position >= self.size_martrix or temp_ball_position < 0):
                break
            #if the ball hit the wall
            if(self.Game[traverse][temp_ball_position]=="W"):
                #if the ball hit the wall in stright direction then break the loop and ball came to down
                if(direction=="ST"):
                    self.Game[traverse][self.Ball_position]="O"
                    break
                #if the ball hit the wall in left or right  then according to that it will travel horizontally in left or right dirction
                for row_traverse in range(1 if direction=="LD" else self.size_martrix-2,self.size_martrix-2 if direction=="LD" else 0,-1 if direction=="RD" else 1):
                    #if the ball hits the wall continuously in left or right direction reduce count and set the ball to initial position
                    if(self.Game[traverse][row_traverse]=="W"):
                        Game[self.size_martrix-1][self.size_martrix//2]="O"
                        self.Ball_count-=1
                        break
                    #if there is an demolishing brick DE thyen the brick destroys entire row and if the ball postion change reduce ball count
                    elif(self.Game[traverse][row_traverse]=="DE"):
                        for i in range(1,len(self.Game[traverse])-2):
                            self.Game[traverse][i]=0
                        if(row_traverse!=self.Ball_position):
                            self.Ball_count-=1
                            self.Ball_position=row_traverse
                        self.Game[self.size_martrix-1][self.Ball_position]="O"
                        break
                    #if there is an demolishing brick DS then it destroys all surrounding bricks and if the ball position changed reduced ball count
                    elif(self.Game[traverse][row_traverse]=="DS"):
                        neighbors=[[1,1],[-1,1],[1,-1],[-1,-1],[0,1],[1,0],[0,-1],[-1,0]]
                        self.Game[traverse][row_traverse]=0
                        for i in neighbors:
                            if(self.Game[traverse+i[0]][row_traverse+i[1]]!="W"):
                                self.Game[traverse+i[0]][row_traverse+i[1]]=0
                        if(row_traverse!=self.Ball_position):
                            self.Ball_count-=1
                            self.Ball_position=row_traverse
                        self.Game[self.size_martrix-1][self.Ball_position]="O"
                        break
                    #if there is an brick with number then reduce with 1
                    elif(self.Game[traverse][row_traverse]!=0):
                        self.Game[traverse][row_traverse]-=1
                        if(row_traverse!=self.Ball_position):
                            self.Ball_count-=1
                            self.Ball_position=row_traverse
                        self.Game[self.size_martrix-1][self.Ball_position]="O"
                        break
            #if the ball doesnt hit the wall
            #if there is an demolishing brick DE thyen the brick destroys entire row and if the ball postion change reduce ball count
            elif(self.Game[traverse][temp_ball_position]=="DE"):
                for i in range(1,len(self.Game[traverse])-2):
                    self.Game[traverse][i]=0
                    if(temp_ball_position!=self.Ball_position):
                        self.Ball_count-=1
                        self.Ball_position=temp_ball_position
                self.Game[self.size_martrix-1][self.Ball_position]="O"
                break
            ##if there is an demolishing brick DS then it destroys all surrounding bricks and if the ball position changed reduced ball count
            elif(self.Game[traverse][temp_ball_position]=="DS"):
                neighbors=[[1,1],[-1,1],[1,-1],[-1,-1],[0,1],[1,0],[0,-1],[-1,0]]
                self.Game[traverse][temp_ball_position]=0
                for i in neighbors:
                    if(self.Game[traverse+i[0]][temp_ball_position+i[1]]!="W"):
                        self.Game[traverse+i[0]][temp_ball_position+i[1]]=0
                if(temp_ball_position!=self.Ball_position):
                    self.Ball_count-=1
                    self.Ball_position=temp_ball_position
                self.Game[self.size_martrix-1][self.Ball_position]="O"
                break
             #if there is an brick with number then reduce with 1
            elif(self.Game[traverse][temp_ball_position]!=0):
                self.Game[traverse][temp_ball_position]-=1
                if(temp_ball_position!=self.Ball_position):
                    self.Ball_count-=1
                    self.Ball_position=temp_ball_position
                self.Game[self.size_martrix-1][self.Ball_position]="O"
                break
        self.printGame()
    #check if the there is any bricks or not
    def isbricks(self):
        for i in range(1,self.size_martrix-1):
            for j in range(1,self.size_martrix-1):
                if(self.Game[i][j]!=0):
                    return False
        return True
    #take a move by entering direction
    def Move(self):
        while(1):
            direction = input("Enter the direction in which ball need to traverse : ")
            self.TakeShot(direction)
            if(self.Ball_count==0 or self.isbricks()):
                break
    #print the game
    def printGame(self):
        for each_row in self.Game:
            for each in each_row:
                if(each==0):
                    print("  ",end=" ")
                else:
                    if(len(str(each))==1):
                        print(" "+str(each),end=" ")
                    else:
                        print(each,end=" ")
            print("\n")
        if(self.Ball_count>=0 and self.isbricks()):
            print("You win HURRAY..!!")
        elif(self.Ball_count==0):
            print("Game over")
        else:
            print("Ball count is :",self.Ball_count)
    
        
                    
        

if __name__ == "__main__":
    size_martrix=int(input("Enter the size of the NxN Matrix : "))
    Game=[]
    Game.append(['W']*size_martrix)
    for each_raw in range(1,size_martrix-1):
        Game.append(['W']+[0]*(size_martrix-2)+['W'])
    Game.append(['W'] +['G']*(size_martrix-2)+['W'])
    Ball_position=size_martrix//2
    Game[size_martrix-1][Ball_position]="O"
    total_bricks=0
    while(1):
        X,Y,type=input("Enter the brick's and the brick type : ").split()
        X,Y=int(X),int(Y)
        if(type.isdigit()):
            type=int(type)
        Game[X][Y]=type
        tocontinue=input("Do you want to continue(Y or N) : ")
        if(tocontinue=="N"):
            break
    ball_count=int(input("Enter ball count : "))
    BallBrickGame=BallBrick(Game,ball_count,Ball_position,size_martrix)
    BallBrickGame.printGame()
    BallBrickGame.Move()
        
    
    


