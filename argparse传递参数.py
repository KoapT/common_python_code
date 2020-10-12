#! /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--use-gpu",
                        action="store_true",  # 默认False，调用时遇到该参数则触发成为True，不能另赋值
                        help="Use gpu or cpu to test.")
    parser.add_argument('--example',
                        type=str,
                        default='',
                        help='RoadLine, HumanSeg or ACE2P')
                        
    return parser.parse_args()
 # 使用： args = get_arguments()
 #		 args.use_gpu, args.example

if __name__ == '__main__':
    args = get_arguments()
    if args.use_gpu:
    	print('OK')
    else:
    	print('NO')
        
    print(vars(args))
    print(args.__dict__)

