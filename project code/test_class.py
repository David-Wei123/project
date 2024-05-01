import cv2
import numpy
import unittest

class Table:
    def init(self):
        pass
    def getRawNum(self):
        return 0
    def getCalNum(self):    
        return 0

class Recogniser:
    def init(self):
        pass
    def MakePhoto(self):
        pass
    def Recognise(self,frame):
        t = Table
        return t
        
class TestRecogniser(unittest.TestCase):
    def setUp(self):
        pass



    def test_ckech_empty_frame_recognition(self):
        r = Recogniser
        size = 200, 200, 3
        f =  np.zeros(size, dtype=np.uint8)
        t = r.Recognise(f)

        self.assertEqual(t.getCalNum(), 0)
        self.assertEqual(t.getRawNum(), 0)

    def test_ckech_empty_table_recognition(self):
        r = Recogniser
        f =  cv2.imread('empty_table_10_10.jpg')
        t = r.Recognise(f)

        self.assertEqual(t.getCalNum(), 10)
        self.assertEqual(t.getRawNum(), 10)


if name == "main":
#    r = Recogniser
#    r.MakePhoto
    unittest.main()