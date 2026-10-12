class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        answer=[0]*n
        cash=[0]*(n+1)
        for i in bookings:
            cash[i[0]-1]+=i[2]
            cash[i[1]]-=i[2]
        now=0
        for i in range(n):
            answer[i]=now+cash[i]
            now=answer[i]
        return answer