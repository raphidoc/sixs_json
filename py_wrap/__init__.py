import os

package_dir = os.path.dirname(__file__)
rel_path = os.path.join('..', '6sV2.1', 'sixsV2.1')
abs_path = os.path.abspath(os.path.join(package_dir, rel_path))

sixs_path = abs_path