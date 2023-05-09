from unittest import TestCase, main
from whiteboard import solution


class WhiteboardTestCase(TestCase):
    
    def test_1_dup_on_ends(self):
        self.assertEqual(solution([2,1,3,4,2]), 2)
    
    def test_2_dup_in_middle(self):
        self.assertEqual(solution([8,5,2,5,4]), 5)

    def test_3_zero_dup(self):
        self.assertEqual(solution([0,0,1,2,3]),  0) 

    def test_4_negatives(self):
        self.assertEqual(solution([-3,-5,-7,-7]),  -7) 



if __name__ == "__main__":
    main()