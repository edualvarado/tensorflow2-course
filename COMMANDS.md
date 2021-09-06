## Commands

* Is TF2 working under GPU? `print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))`
* Is TF1 working under GPU? `sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))`



