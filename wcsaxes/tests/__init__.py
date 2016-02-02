import os
from distutils.version import LooseVersion

import matplotlib

MPL_VERSION = LooseVersion(matplotlib.__version__)

ROOT = os.path.dirname(__file__)

if MPL_VERSION >= LooseVersion('1.5.0'):
    baseline_dir = os.path.join(ROOT, 'baseline_images', '1.5.0')
else:
    baseline_dir = os.path.join(ROOT, 'baseline_images', 'initial')
