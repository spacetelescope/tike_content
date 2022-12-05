from astrocut import CutoutFactory

def get_cube_fn(camera_ccd, sector=55):
    # In the filename, the sector has two leading zeros, i.e. 0055
    cube_fn = f"s3://stpubdata/tess/public/mast/tess-s{sector:04d}-{camera_ccd}-cube.fits"
    return cube_fn

def get_cutouts(target_list, target_dict):
    factory = CutoutFactory()
    for target_name in target_list:
        coord, cam_ccd = target_dict[target_name]
        print(f"Starting {target_name}")
        factory.cube_cut(cube_file = get_cube_fn(cam_ccd) # Get the cube filename for this camera/ccd
                        ,coordinates=coord # Use the coordinates for the target
                        ,cutout_size=10
                        ,target_pixel_file=f"{target_name}.fits"); # Name the output file the target name
        print(f"Finished {target_name}\n")