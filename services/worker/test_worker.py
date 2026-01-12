import unittest
import worker
import os
import nc_py_api

class TestWorker(unittest.TestCase):
    def setUp(self):
            worker.detector = worker.NudeDetector()
 
    def test_fast_score_negative_result1(self):
        score, detections = worker.fast_score( os.path.join("dataset","5343696085626589446.jpg"))
        self.assertEqual(score, 0)
        self.assertIsNotNone(detections)
    def test_fast_score_negative_result2(self):
        score, detections = worker.fast_score( os.path.join("dataset","5343823384162276397.jpg"))
        self.assertEqual(score, 0)
        self.assertIsNotNone(detections)

    def test_fast_score_positive_result(self):
        score, detections = worker.fast_score( os.path.join("dataset","P6260250.JPG"))
        self.assertGreater(score, 0.3)
        self.assertIsNotNone(detections)
    def test_fast_score_positive_contains_result(self):
        score, detections = worker.fast_score( os.path.join("dataset","P6260250.JPG"))
        findedG = findedB = False
        for item in detections:
            findedB = "BUTTOCKS_EXPOSED" in item
            findedG = "FEMALE_GENITALIA_EXPOSED" in item
        self.assertFalse(findedB)
        self.assertFalse(findedG)

    def test_fast_score_negative_contains_result(self):
        score, detections = worker.fast_score( os.path.join("dataset","IMG_0605.JPG"))
        findedG = findedB = False
        for item in detections:
            findedM = "'MALE_GENITALIA_EXPOSED', " in item
        self.assertFalse(findedM)


    def test_fast_score_one_positive_result(self):
        count = 0
        files = os.listdir("dataset")
        for item in files:
            score, detections = worker.fast_score( os.path.join("dataset",item) )
            if score > worker.SAFE_T:
                    count+=1
        self.assertEqual(count,3)

    def test_add_all_taga_to_nc(self):
        worker.nc = nc_py_api.Nextcloud(nextcloud_url=os.environ['NEXTCLOUD_URL'] , nc_auth_user=os.environ['NEXTCLOUD_USERNAME'], nc_auth_pass= os.environ['NEXTCLOUD_PASSWORD'])
        worker.add_tag_to_nc()
    
if __name__ == '__main__':
    unittest.main()
