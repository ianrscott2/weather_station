#!/bin/sh

USER_DIR='/home/pi' 

case "$1" in
  restart)
	pid=`ps -ef | grep weatherStation | grep python | grep -v grep | awk '{ print $2 }'`
	if [ "$pid" ];  then
    		echo "Restarting WeatherStation and killing PID $pid"
    		kill $pid
	fi
	python $USER_DIR/weather_station/weatherStation_main.py /home/pi/weather_station 7x5in &
  ;;
  start)
	pid=`ps -ef | grep weatherStation | grep python | grep -v grep | awk '{ print $2 }'`
	if [ "$pid" ];  then
    		echo "WeatherStation is running, won't start"
	else
        	echo "Starting Weather Station"
	        python $USER_DIR/weather_station/weatherStation_main.py /home/pi/weather_station 7x5in &
	fi
  ;;
  stop)
	pid=`ps -ef | grep weatherStation | grep python | grep -v grep | awk '{ print $2 }'`
	if [ "$pid" ];  then
    		echo "Killing WeatherStation, PID $pid"
    		kill $pid
        else
    		echo "Can't find WeatherStation PID"
	fi
  ;;
esac