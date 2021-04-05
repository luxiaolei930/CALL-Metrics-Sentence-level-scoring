export CUDA_VISIBLE_DEVICES=0
python -m bleurt.finetune \
	  -init_bleurt_checkpoint=bleurt/zh_checkpoint \
	    -model_dir=my_new_bleurt_checkpoint \
	      -train_set=bleurt/zh_data/wmt_train.jsonl \
	        -dev_set=bleurt/zh_data/wmt_dev.jsonl \
		  -num_train_steps=2000
