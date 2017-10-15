#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: test_face_list.py
Description: Unittests for Face List section of the Cognitive Face API.
"""

import uuid
import cognitive_face as CF
import util

class FaceList(object):
    """ Face List section."""

    def add_face(self):
        """ `face_list.add_face` and `face_list.delete_face`."""
        image = '{}PersonGroup/Family1-Dad/Family1-Dad3.jpg'.format(
            util.BASE_URL_IMAGE)

        res = CF.face_list.add_face(image, util.DataStore.face_list_id)
        print(res)
        self.assertIsInstance(res, dict)

        self.persisted_face_id = res['persistedFaceId']

    def delete_face(self, persisted_face_id):
        """ `face_list.delete_face`."""
        res = CF.face_list.delete_face(
            util.DataStore.face_list_id,
            persisted_face_id,
        )
        print(res)
        self.assertIsInstance(res, dict)

    def create_face_list(self):
        """ `face_list.create`, `face_list.update` and
        `face_list.delete`.
        """
        face_list_id = str(uuid.uuid1())

        res = CF.face_list.create(face_list_id)
        print(res)
        self.assertIsInstance(res, dict)

        res = CF.face_list.update(face_list_id, 'test')
        print(res)
        self.assertIsInstance(res, dict)

        res = CF.face_list.delete(face_list_id)
        print(res)
        self.assertIsInstance(res, dict)

    def get_face_list(self):
        """ `face_list.get`."""
        res = CF.face_list.get(util.DataStore.face_list_id)
        print(res)
        self.assertIsInstance(res, dict)

    def lists(self):
        """ `face_list.lists`."""
        res = CF.face_list.lists()
        print(res)
        self.assertIsInstance(res, list)
