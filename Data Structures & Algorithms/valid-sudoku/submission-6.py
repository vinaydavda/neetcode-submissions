class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # My solution by inspiring answer from chatgpt
        rows = [[] for _ in range(9)]  # Used list instead of set
        cols = [[] for _ in range(9)]  # Used list instead of set
        boxes = {}  # Used my approach of dictionary instead of set

        for row in range(9):
            for col in range(9):
                check_val = board[row][col]
                
                if board[row][col] == '.':
                    continue
                
                # Check row
                if check_val in rows[row]:
                    return False
                rows[row].append(check_val)
                
                # Check column
                if check_val in cols[col]:
                    return False
                cols[col].append(check_val)

                # Check box
                box_id = str(row // 3) + str(col // 3)  # Not used this AI hard calc -> (r // 3) * 3 + (c // 3)
                if box_id not in boxes:
                    boxes[box_id] = []

                if check_val in boxes[box_id]:
                    return False
                boxes[box_id].append(check_val)

        return True

        # My Solution
        # valid = True
        # boxes = []
        # box_init = [0, 0, 0, 3, 3, 3, 6, 6, 6]

        # for i in range(9):
        #     temp_row = [i for i in board[i] if i != '.']
        #     if len(set(temp_row)) != len(temp_row):
        #         valid = False
        #         break
        #     row = board[i]
        #     c = box_init[i]
        #     for j in range(0, 9, 3):
        #         if i % 3 == 0:
        #             boxes.append(row[j:j + 3])
        #         else:
        #             boxes[c].extend(row[j:j + 3])
        #             c += 1

        #     temp_ver_row = [row[i] for row in board if row[i] != '.']
        #     if len(set(temp_ver_row)) != len(temp_ver_row):
        #         valid = False
        #         break

        # print(boxes)
        # for i in range(9):
        #     print('-> ', i)
        #     temp_box_row = boxes[i]
        #     temp_box_row = [x for x in temp_box_row if x != '.']
        #     if len(set(temp_box_row)) != len(temp_box_row):
        #         valid = False
        #         break

        # return valid