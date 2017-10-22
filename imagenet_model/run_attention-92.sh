#!/bin/sh
TOOLS=caffe/build/tools

GLOG_logtostderr=1 $TOOLS/caffe train -solver Attention-92-solver.prototxt  
echo 'Done.'