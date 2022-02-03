import unittest
from meme_generator import MemeGenerator


class MyTestCase(unittest.TestCase):
    def test_size_path_exists(self):
        in_path = ('/Users/jaredthacker/intermediate_python/project_2'
                   '/src/_data/photos/dog/xander_1.jpg')
        out_path = ('../memes')
        my_generator = MemeGenerator(out_path)
        img = MemeGenerator.load(in_path)
        res_img = MemeGenerator.resize(img, width=200)
        cap_img = MemeGenerator.add_caption(res_img, 'here i am, this is me', 'me')

        cap_img.save(my_generator.out_path + '/cap.png')
        img.close()

    def test_make_meme(self):
        in_path = '/Users/jaredthacker/memes/IMG_1295.PNG'
        out_path = '/Users/jaredthacker/memes/altered_memes/cap.png'
        my_generator = MemeGenerator(out_path)
        saved_image_path = my_generator.make_meme(in_path, 'so good', 'me')
        print(saved_image_path)


if __name__ == '__main__':
    unittest.main()
