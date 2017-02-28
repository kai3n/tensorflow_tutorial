import tensorflow as tf

# x1_data = [1, 0, 3, 0, 5]
# x2_data = [0, 2, 0, 4, 0]
# y_data = [1, 2, 3, 4, 5]
#
# W1 = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
# W2 = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

# x_data = [[1., 0., 3., 0., 5.],
#           [0., 2., 0., 4., 0.]]
# y_data = [1, 2, 3, 4, 5]
#
# W = tf.Variable(tf.random_uniform([1,2], -1.0, 1.0))
#
# b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
# hypothesis = tf.matmul(W, x_data) + b

x_data = [[1., 1., 1., 1., 1.],
          [1., 0., 3., 0., 5.],
          [0., 2., 0., 4., 0.]]

y_data = [1, 2, 3, 4, 5]

W = tf.Variable(tf.random_uniform([1,3], -1.0, 1.0))

hypothesis = tf.matmul(W, x_data)

cost = tf.reduce_mean(tf.square(hypothesis - y_data))

# Minimize
a = tf.Variable(0.1)  # Learning rate, alpha
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

# Before starting, initialize the variables.
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)


for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(cost), sess.run(W))

