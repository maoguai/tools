from idautils import *
from idaapi import *
import time
from time import strftime
import re
import copy


########################### MAIN ###########################
def find_loop_helper(block, parent_node, depth, record_loop, func_dict, funcea):
	loop = False
	if block.startEA in parent_node:
		if block.startEA not in record_loop:
			record_loop[block.startEA] = set()
		func_dict[block.startEA] = funcea
		record_loop[block.startEA].add(depth - parent_node[block.startEA] + 1)
		#f.write('loop: %x\n' %block.startEA)
		loop = True
	if loop == False:
		depth = depth + 1
		parent_node[block.startEA] = depth
		for succ_bl in block.succs():
			tmp_parent = copy.copy(parent_node)
			tmp_depth = depth
			find_loop_helper(succ_bl, tmp_parent, tmp_depth, record_loop, func_dict, funcea)


if __name__ == '__main__':
	#ea = SegByBase(SegByName(".text"))
	switch_list = []
	block_list = []
	block_func = {}
	v_filename = 'F:\PIE.txt'
	record_loop = {}
	func_dict = {}
	f = open(v_filename, "w")

	#for funcea in Functions(SegStart(ea), SegEnd(ea)):
	for funcea in Functions():
		func = idaapi.get_func(funcea)
		fc = idaapi.FlowChart(func)
		init_block = fc[0]
		parent_dict = {}	
		depth = 0
		find_loop_helper(init_block, parent_dict, depth, record_loop, func_dict, funcea)
	
	numOfDepth = {}
	for re in record_loop:
		numOfDepth[re] = len(record_loop[re])
		maxNumOfDepth = sorted(numOfDepth.iteritems(), key=lambda d: d[1], reverse = True)
	for key_value in maxNumOfDepth:
		f.write('loop_addr: %x ' % key_value[0])
		f.write('func: %x ' % func_dict[key_value[0]])
		f.write('numOfDepth: %d ' % key_value[1])
		f.write('\n')
	f.close()
