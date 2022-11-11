import open3d as o3d
# visualization of point clouds.
path = "d6_3D_t450711240.ply"
pcd = o3d.io.read_point_cloud(path)
o3d.visualization.draw_geometries([pcd])