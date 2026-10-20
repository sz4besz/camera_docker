FROM ros:humble-ros-base

RUN apt-get update && apt-get install -y \
    ros-humble-realsense2-camera \
    ros-humble-realsense2-description \
    && rm -rf /var/lib/apt/lists/*

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

CMD ["bash"]