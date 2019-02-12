#!/bin/bash

wget https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/dogImages.zip && unzip dogImages.zip && rm dogImages.zip
wget http://vis-www.cs.umass.edu/lfw/lfw.tgz && tar zxf lfw.tgz && rm lfw.tgz