;; Auto-generated. Do not edit!


(when (boundp 'aruco_mapping::ArucoMarker)
  (if (not (find-package "ARUCO_MAPPING"))
    (make-package "ARUCO_MAPPING"))
  (shadow 'ArucoMarker (find-package "ARUCO_MAPPING")))
(unless (find-package "ARUCO_MAPPING::ARUCOMARKER")
  (make-package "ARUCO_MAPPING::ARUCOMARKER"))

(in-package "ROS")
;;//! \htmlinclude ArucoMarker.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass aruco_mapping::ArucoMarker
  :super ros::object
  :slots (_header _marker_visibile _num_of_visible_markers _global_camera_pose _marker_ids _global_marker_poses ))

(defmethod aruco_mapping::ArucoMarker
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:marker_visibile __marker_visibile) nil)
    ((:num_of_visible_markers __num_of_visible_markers) 0)
    ((:global_camera_pose __global_camera_pose) (instance geometry_msgs::Pose :init))
    ((:marker_ids __marker_ids) (make-array 0 :initial-element 0 :element-type :integer))
    ((:global_marker_poses __global_marker_poses) (let (r) (dotimes (i 0) (push (instance geometry_msgs::Pose :init) r)) r))
    )
   (send-super :init)
   (setq _header __header)
   (setq _marker_visibile __marker_visibile)
   (setq _num_of_visible_markers (round __num_of_visible_markers))
   (setq _global_camera_pose __global_camera_pose)
   (setq _marker_ids __marker_ids)
   (setq _global_marker_poses __global_marker_poses)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:marker_visibile
   (&optional __marker_visibile)
   (if __marker_visibile (setq _marker_visibile __marker_visibile)) _marker_visibile)
  (:num_of_visible_markers
   (&optional __num_of_visible_markers)
   (if __num_of_visible_markers (setq _num_of_visible_markers __num_of_visible_markers)) _num_of_visible_markers)
  (:global_camera_pose
   (&rest __global_camera_pose)
   (if (keywordp (car __global_camera_pose))
       (send* _global_camera_pose __global_camera_pose)
     (progn
       (if __global_camera_pose (setq _global_camera_pose (car __global_camera_pose)))
       _global_camera_pose)))
  (:marker_ids
   (&optional __marker_ids)
   (if __marker_ids (setq _marker_ids __marker_ids)) _marker_ids)
  (:global_marker_poses
   (&rest __global_marker_poses)
   (if (keywordp (car __global_marker_poses))
       (send* _global_marker_poses __global_marker_poses)
     (progn
       (if __global_marker_poses (setq _global_marker_poses (car __global_marker_poses)))
       _global_marker_poses)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; bool _marker_visibile
    1
    ;; int32 _num_of_visible_markers
    4
    ;; geometry_msgs/Pose _global_camera_pose
    (send _global_camera_pose :serialization-length)
    ;; int32[] _marker_ids
    (* 4    (length _marker_ids)) 4
    ;; geometry_msgs/Pose[] _global_marker_poses
    (apply #'+ (send-all _global_marker_poses :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; bool _marker_visibile
       (if _marker_visibile (write-byte -1 s) (write-byte 0 s))
     ;; int32 _num_of_visible_markers
       (write-long _num_of_visible_markers s)
     ;; geometry_msgs/Pose _global_camera_pose
       (send _global_camera_pose :serialize s)
     ;; int32[] _marker_ids
     (write-long (length _marker_ids) s)
     (dotimes (i (length _marker_ids))
       (write-long (elt _marker_ids i) s)
       )
     ;; geometry_msgs/Pose[] _global_marker_poses
     (write-long (length _global_marker_poses) s)
     (dolist (elem _global_marker_poses)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; bool _marker_visibile
     (setq _marker_visibile (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int32 _num_of_visible_markers
     (setq _num_of_visible_markers (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; geometry_msgs/Pose _global_camera_pose
     (send _global_camera_pose :deserialize buf ptr-) (incf ptr- (send _global_camera_pose :serialization-length))
   ;; int32[] _marker_ids
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _marker_ids (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _marker_ids i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; geometry_msgs/Pose[] _global_marker_poses
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _global_marker_poses (let (r) (dotimes (i n) (push (instance geometry_msgs::Pose :init) r)) r))
     (dolist (elem- _global_marker_poses)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get aruco_mapping::ArucoMarker :md5sum-) "e73493d4620efa2f38fe39e7896d4192")
(setf (get aruco_mapping::ArucoMarker :datatype-) "aruco_mapping/ArucoMarker")
(setf (get aruco_mapping::ArucoMarker :definition-)
      "std_msgs/Header header
bool marker_visibile
int32 num_of_visible_markers
geometry_msgs/Pose global_camera_pose
int32[] marker_ids
geometry_msgs/Pose[] global_marker_poses


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :aruco_mapping/ArucoMarker "e73493d4620efa2f38fe39e7896d4192")


