import tensorflow as tf

# training data
X = [1., 2., 3.]
Y = [1., 2., 3.]
m = n_samples = len(X)

W = tf.placeholder(tf.float32)

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

hypothesis = tf.mul(X, W)

cost = tf.reduce_sum(tf.pow(hypothesis-Y,2)) / m

# initializaing the variables
init = tf.initialize_all_variables()

# Minimize
# descent = W - tf.mul(0.1,tf.reduce_mean(tf.mul(tf.mul(W, X) - Y), X))
# updaate = W.assign(descent)

# for graphs
W_val = []
cost_val = []

# Launch the graph
sess = tf.Session()
sess.run(init)
for i in range(-30,50):
    print(i*0.1, sess.run(cost, feed_dict={W: i*0.1}))
    W_val.append(i*0.1)
    cost_val.append(sess.run(cost, feed_dict={W: i*0.1}))