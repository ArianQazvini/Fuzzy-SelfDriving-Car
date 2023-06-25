class FuzzyGasController:
    """
    # emtiazi todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        pass

    def close_dist_membership(self,dist):
        if(dist>=0 and dist<=50):
            return 1-dist/50
        return 0

    def moderate_dist_membership(self,dist):
        if(dist>=40 and dist<=50):
            return dist/10-4
        if(dist>=50 and dist<=100):
            return 2-dist/50
        return 0
    def far_dist_membership(self,dist):
        if(dist>=90 and dist<= 200):
            return (dist/110) - (9/11)
        if(dist>=200):
            return 1
        return 0

    def low_speed_membership(self,speed):
        if(speed>=0 and speed<=5):
            return speed/5
        if(speed>=5 and speed<=10):
            return 2-speed/5
        return 0

    def medium_speed_membership(self,speed):
        if(speed>=0 and speed<=15):
            return speed/15
        if(speed>=15 and speed<= 30):
            return 2-speed/15
        return 0
    def high_speed_membership(self,speed):
        if(speed>=25 and speed<=30):
            return speed/5 -5
        if(speed>=30 and speed<=90):
            return 1.5-speed/60
        return 0
    def decide(self, center_dist):
        """
        main method for doin all the phases and returning the final answer for gas
        """
        low_speed = self.close_dist_membership(center_dist)
        med_speed = self.moderate_dist_membership(center_dist)
        high_speed = self.far_dist_membership(center_dist)

        X = []
        start = 0.0
        end = 90.0
        while (start < end):
            X.append(start)
            start = start + 0.1


        a=0.0
        b=0.0
        for x in X:
            curr_low_speed = min(low_speed,self.low_speed_membership(x))
            curr_med_speed = min(med_speed,self.medium_speed_membership(x))
            curr_high_speed = min(high_speed,self.high_speed_membership(x))
            mem = max(curr_low_speed,curr_med_speed,curr_high_speed)
            a=a+mem *0.1 * x
            b =b+mem *0.1
        if(b!= 0):
            return float(a)/float(b)
        return 0

