class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[(target-p)/s for p,s in sorted(zip(position,speed))]
        currentTime=0
        fleetNum=0
        for t in time[::-1]:
            if t>currentTime:
                fleetNum+=1
                currentTime=t
        return fleetNum

        