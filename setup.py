# coding=utf-8

from setuptools import setup

setup(name='ktt-common',
      version='1.0.99',
      packages=['common', 'common.apps', 'common.data', 'common.features', 'common.linguistics', 'common.visualization', 'common.models'],
      data_files=[('common/visualization/templates', ['common/visualization/templates/concordance.html',
                                                      'common/visualization/templates/disambiguation.html',
                                                      'common/visualization/templates/paradigm_application.html',
                                                      'common/visualization/templates/pending_words.html',
                                                      'common/visualization/templates/rae_verb_conjugation_models.html',
                                                      'common/visualization/templates/token_type_resume.html'])],
      include_package_data=True,
      zip_safe=False)
