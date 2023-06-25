import skfuzzy
import numpy as np
class FuzzyController:
    """
    #todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        pass

    def close_L_membership(self,dist):
        if(dist<=50 and dist>=0):
            return 1- (dist/50)
        return 0
    def moderate_L_membership(self,dist):
        if(dist<=50 and dist>=35):
            return (dist/15 - 7/3)
        if(dist<= 65 and dist>50):
            return (13/3-dist/15)
        return 0
    def far_L_membership(self,dist):
        if(dist>=50 and dist<=100):
            return (dist/50)-1
        return 0
    def close_R_membership(self,dist):
        if(dist<=50 and dist>=0):
            return 1- (dist/50)
        return 0
    def moderate_R_membership(self,dist):
        if(dist<=50 and dist>=35):
            return (dist/15 - 7/3)
        if(dist<= 65 and dist>50):
            return (13/3-dist/15)
        return 0
    def far_R_membership(self,dist):
        if(dist>=50 and dist<=100):
            return (dist/50)-1
        return 0


    def high_right_membership(self,dist):
        if(dist>= -50 and dist<=-20):
            return (dist/30 +50/30)
        if(dist>-20 and dist<= -5):
            return ((-dist)/15-1/3)
        return 0
    def low_right_membership(self,dist):
        if(dist>=-20 and dist<=-10):
            return dist/10 +2
        if(dist> -10 and dist <= 0):
            return -dist/10
        return 0
    def nothing_membership(self,dist):
        if(dist>= -10 and dist<= 0 ):
            return dist/10 +1
        if(dist>0 and dist <=10):
            return 1-dist/10
        return 0
    def low_left_membership(self,dist):
        if(dist>=0 and dist<= 10):
            return dist/10
        if(dist>10 and dist<=20):
            return 2-dist/10
        return 0
    def high_left_membership(self,dist):
        if(dist>=5 and dist <=20):
            return dist/15-1/3
        if(dist>20 and dist<=50):
            return 50/30-dist/30
        return 0
    def decide(self, left_dist,right_dist):
        """
        main method for doin all the phases and returning the final answer for rotation
        """
        low_right = min(self.close_L_membership(left_dist),self.moderate_R_membership(right_dist))
        high_right = min(self.close_L_membership(left_dist),self.far_R_membership(right_dist))
        low_left = min(self.moderate_L_membership(left_dist),self.close_R_membership(right_dist))
        high_left = min(self.far_L_membership(left_dist),self.close_R_membership(right_dist))
        nothing = min(self.moderate_L_membership(left_dist),self.moderate_R_membership(right_dist))

        X = []
        start = -50
        end = 50
        while (start < end):
            X.append(start)
            start = start + 0.1


        a=0.0
        b=0.0
        for x in X:
            curr_low_right = min(low_right,self.low_right_membership(x))
            curr_low_left = min(low_left,self.low_left_membership(x))
            curr_high_right = min(high_right,self.high_right_membership(x))
            curr_high_left = min(high_left,self.high_left_membership(x))
            curr_nothing = min(nothing,self.nothing_membership(x))
            mem = max(curr_low_right,curr_low_left,curr_high_right,curr_high_left,curr_nothing)
            a=a+mem *0.1 * x
            b =b+mem *0.1
        if(b!= 0):
            return float(a)/float(b)
        return 0

        # print((skfuzzy.centroid(X,mem)))
        # print("--------------------")
        # print("-------------------------")
        # return skfuzzy.centroid(X,mem)
        # return np.sum(skfuzzy.centroid(X,mem))/(skfuzzy.centroid(X,mem).size)
        # print("---------------------------------")
        # return skfuzzy.centroid(X,mem)

        # def max_function(x):
        #     return max(min(low_right, self.low_right_membership(x)),
        #            min(high_right, self.high_right_membership(x)),
        #            min(low_left, self.low_left_membership(x)),
        #            min(high_left, self.high_left_membership(x)),
        #            min(nothing, self.nothing_membership(x)))
        #
        # x = -50
        # b = +50
        # makhraj = 0.0
        # soorat = 0.0
        # while x < b:
        #     x = x + 0.1
        #     makhraj = makhraj + max_function(x) * 0.1
        #     soorat = soorat + max_function(x) * 0.1 * x
        # if makhraj != 0:
        #     print(float(soorat)/float(makhraj))
        #     print("---------------------------")
        #     return float(soorat) / float(makhraj)
        # return 0