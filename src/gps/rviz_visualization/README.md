## 실행 방법 
roslaunch rviz_visualization pure_pursuit_bag.launch path:={경로파일이름} bag:={bag파일 이름}

위 명령어를 입력하면 gps 데이터를 rosbag으로 받아 waypoints, current pose, target point를 시각해 해줍니다.

### 위 명령어는 아래와 같은 일을 합니다.
1. roscore
2. rosrun tf static_transform_publisher 0 0 0 0 0 0 map base_link 50
3. rviz 실행
4. rviz 왼쪽 패널에서 fixed frame base_link로 변경
5. 왼쪽패널 아래의 add 눌러서 markerArray 추가하고 Marker Topic 알맞은거로 변경
6. rviz_visualization 의 global_map_plotter를 rosrun으로 실행 
7. rviz오른족 패널에서 x,y좌표를 path 파일안에 있는 좌표(utmk)로 이동
8. 안보이면 rviz오른쪽 패널의 Type을 TopDownOrtho로 변경 

만약 visualization-marker-tutorials 가 없으면 아래 명령어 실행

`sudo apt install ros-<ros 버전 eg. melodic>-visualization-marker-tutorials`



----

## waypoint_modify 모듈

rviz 상에서 구한 대략적인 위치정보를 가지고 구간(MODE)를 나누기 쉽게 하는 모듈.

1. 기본 경로 PATH 파일을 준비한다.

2. 구간 Waypoint 정보가 담긴 PATH 파일을 준비한다.

   - 1번 2번 모두 위치는 [rviz_visualization]-[marker] 폴더 안에다가 넣는다.

3. 실행 명령어 (roscore 키고)

   ```sh
   python waypoint_modify.py global_path waypoint_path
   ```

----

## get_index 모듈

PATH Waypoint 중 가장 가까운 Index 를 반환해줌.

마찬가지로 PATH 파일의 위치는 [rviz_visualization]-[marker]  

```
python get_index.py global_path x y
```

 

