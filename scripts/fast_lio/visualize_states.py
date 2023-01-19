#%matplotlib widget

from datetime import datetime, timedelta
import os
import copy
 
import mav_bag_plot.bag_loader as bag_loader
from mav_bag_plot.msg_plotter import vis_states, vis_odom

min_range = 1.0


def main():
    #compare_updates()    
    #compare_corrupted_bag()
    compare_updated_bag()
    
def compare_updates():
    paths = ["/home/lucas/bags/gtsam_fusion/original_prediction_update.bag",
             #"/home/lucas/bags/gtsam_fusion/new_prediction_update.bag",
             #"/home/lucas/bags/gtsam_fusion/new_prediction_update2.bag",
             "/home/lucas/bags/gtsam_fusion/missing_pcl_with_gtsam4.bag",
             "/home/lucas/bags/gtsam_fusion/missing_pcl_with_gtsam4.bag"
             ]
   
    names = [
             "Original",
             #"Try1",
             #"Try2",
             "Try3",
             "CleanedUp4"
             ]
    
    vis_odom(paths, names)
def compare_corrupted_bag():
    paths = [
             "/home/lucas/bags/gtsam_fusion/original.bag",
             "/home/lucas/bags/gtsam_fusion/missing_pcl_no_gps.bag",
             "/home/lucas/bags/gtsam_fusion/missing_pcl_with_gtsam3.bag",
             "/home/lucas/bags/gtsam_fusion/missing_pcl_with_gtsam4.bag"
             ]
   
    names = [
             "Original",
             "Corrupted",
             "GTSAM FB 3",
             "GTSAM FB 4",
             ]
    #vis_states(paths, names)
    vis_odom(paths, names)
    
def compare_updated_bag():
    dir = "/home/lucas/bags/gtsam_fusion/"
    paths = [
             "/home/lucas/bags/gtsam_fusion/original.bag",
             #"/home/lucas/bags/gtsam_fusion/missing_pcl_no_gps.bag",
             "/home/lucas/bags/gtsam_fusion/evaluate_update0.bag",
             "/home/lucas/bags/gtsam_fusion/fix_timing0.bag",
             ]
    names = ["origin (uncorrupted) bag",
             #"standard LIO rerun",
             "Current GTSAM update",
             "Fixed timing"
             ]
             
    topics = ['/kolibri/mav_state_estimator/optimization',
              #'/Gnss',
              '/Odometry']
    topic_names = [": Pose Graph",
                 #": GNSS",
                 ": LIO"]          
    
    identifier = ["original.", "evaluate_update0", "fix_timing0"]
    files = bag_loader.find_files(dir, identifier)
    bags = bag_loader.load_bags(files, topics)
    names = [os.path.basename(file)[:-3] for file in files]
    
    vis_odom(bags, names, topics = topics)
    vis_states(bags, names, topics = topics, topic_names = topic_names)


if __name__ == "__main__":
    main()