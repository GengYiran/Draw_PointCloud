import open3d as o3d
import numpy as np

xyz_path = "raw/gyr_point_clouds/pot_xyz.npy"
rgb_path = "raw/gyr_point_clouds/pot_rgb.npy"

xyz = np.load(xyz_path)
rgb = np.load(rgb_path)

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xyz)
pcd.colors = o3d.utility.Vector3dVector(rgb)

o3d.visualization.draw_geometries_with_editing([pcd])
# pcd.points = o3d.utility.Vector3dVector(xyz)