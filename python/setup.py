# coding=utf-8

from setuptools import setup

setup(name=' paquete',
      version='1.0.103',
      packages=['common'],
      data_files=[('common/visualization/templates', ['testblahblabpakcage.html',
                                                      'testblahblabpakcageion.html',
                                                      'testblahblabpakcageplication.html',
                                                      'testblahblabpakcageds.html',
                                                      'testblahblabpakcagenjugation_models.html',
                                                      'testblahblabpakcageresume.html'])],
      include_package_data=True,
      zip_safe=False)
