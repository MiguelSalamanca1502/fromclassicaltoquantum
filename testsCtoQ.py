import unittest
import numpy as np
import ctoquantum as cq


class TestClassicaltoQuantum(unittest.TestCase):

    def testMarbles(self):
        mat = np.array([[0, 1, 0],
                        [1, 0, 0],
                        [0, 0, 1]])
        state = np.array([[1],
                          [0],
                          [0]])
        t = 2
        res = np.array([[1],
                        [0],
                        [0]])

        self.assertTrue(
            np.testing.assert_almost_equal(cq.marbles(mat, state, t), res) is None
        )

    def testMultSlits(self):
        mat = np.array([[0, 0, 0, 0, 0, 0],
                        [1 / 2, 0, 0, 0, 0, 0],
                        [1 / 2, 0, 0, 0, 0, 0],
                        [0, 1 / 2, 0, 1, 0, 0],
                        [0, 1 / 2, 1 / 2, 0, 1, 0],
                        {0, 0, 1 / 2, 0, 0, 1}])
        state = np.array([[1],
                          [0],
                          [0],
                          [0],
                          [0],
                          [0]])
        t = 3
        res = np.array([[0.],
                        [0.],
                        [0.],
                        [0.25],
                        [0.5],
                        [0.25]])

        self.assertTrue(
            np.testing.assert_almost_equal(cq.multSlits(mat, state, t), res) is None
        )

    def testQuantumMiltiSlits(self):
        mat = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                        [1/np.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
                        [1/np.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
                        [0, (-1+1j)/np.sqrt(6), 0, 1, 0, 0, 0, 0],
                        [0, (-1-1j)/np.sqrt(6), 0, 0, 1, 0, 0, 0],
                        [0, (1-1j)/np.sqrt(6), (-1+1j)/np.sqrt(6), 0, 0, 1, 0, 0],
                        [0, 0, (-1-1j)/np.sqrt(6), 0, 0, 0, 1, 0],
                        [0, 0, (1-1j)/np.sqrt(6), 0, 0, 0, 0, 1]])
        state = np.array([[1],
                          [0],
                          [0],
                          [0],
                          [0],
                          [0],
                          [0],
                          [0]])
        t = 2
        res = np.array([[0.+0.j],
                        [0.+0.j],
                        [0.+0.j],
                        [0.16666667+0.j],
                        [0.16666667+0.j],
                        [0.+0.j],
                        [0.16666667+0.j],
                        [0.16666667+0.j]])


        self.assertTrue(
            np.testing.assert_almost_equal(cq.quantumMultSlits(mat, state, t), res) is None
        )

if __name__ == '__main__':
    unittest.main()
