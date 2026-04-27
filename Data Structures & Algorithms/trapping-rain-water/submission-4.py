class Solution:
    def trap(self, height: List[int]) -> int:
        qty = 0
        l_height = None
        l_id = None
        temp_qty = 0

        # Left to right till same or higher high
        for i in range(len(height)):
            if not l_height:
                l_height = height[i]
                l_id = i
                continue

            if height[i] >= l_height:
                qty += temp_qty
                temp_qty = 0
                l_height = height[i]
                l_id = i

            else:
                temp_qty += (l_height - height[i])

        # If no higher high, check right to left for pending part
        if temp_qty:
            temp_qty = 0
            l_height = None
            pending = height[l_id:][::-1]
            for i in range(len(pending)):
                if not l_height:
                    l_height = pending[i]
                    continue
                
                if pending[i] >= l_height:
                    qty += temp_qty
                    temp_qty = 0
                    l_height = pending[i]

                else:
                    temp_qty += (l_height - pending[i])
        
        return qty
