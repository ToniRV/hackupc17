#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: test_face.py
Description: Unittests for Face section of the Cognitive Face API.
"""

import cognitive_face as CF

import util

import bounding_box as bb

import api_key as ak

class TestFace():
    """Unittests for Face section."""
    def __init__(self):
        self.x = 0

    def test_detect(self,img_url):
        """Unittest for `face.detect`."""

        res = CF.face.detect(img_url)
        print(res)

        return res

    def test_find_similars(self, face_id, face_list_id):
        """Unittest for `face.find_similars`."""
        res = CF.face.find_similars(
            face_id,
            face_list_id,
        )
        print(res)
        return res

    def test_group(self):
        """Unittest for `face.group`."""
        temp_face_ids = util.DataStore.face_ids
        temp_face_ids.append(util.DataStore.face_id)
        temp_face_ids.append(util.DataStore.another_face_id)
        res = CF.face.group(temp_face_ids)
        print(res)

    def test_identify(self):
        """Unittest for `face.identify`."""
        CF.util.wait_for_training(util.DataStore.person_group_id)

        res = CF.face.identify(
            util.DataStore.face_ids,
            util.DataStore.person_group_id,
        )
        print(res)

    def test_verify(self):
        """Unittest for `face.verify`."""
        res = CF.face.verify(
            util.DataStore.face_id,
            person_group_id=util.DataStore.person_group_id,
            person_id=util.DataStore.person_id['Dad'],
        )
        print(res)

if __name__ == '__main__':
    test = TestFace()
    KEY = '8a29e79f525e45d9be728e845546daff'
    ak.SubscriptionKey.set(KEY)

    img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection2.jpg'
    test.test_detect(img_url)
