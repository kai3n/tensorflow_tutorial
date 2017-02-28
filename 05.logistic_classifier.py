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
          [2., 3., 5., 7., 2.],
          [2., 4., 5., 5., 5.]]

y_data = [0, 0, 0, 1, 1]

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_uniform([1,len(x_data)], -1.0, 1.0))

h = tf.matmul(W, X)
hypothesis = tf.div(1., 1.+tf.exp(-h))

cost = -tf.reduce_mean(Y*tf.log(hypothesis) + (1-Y)*tf.log(1-hypothesis))

# Minimize
a = tf.Variable(0.1)  # Learning rate, alpha
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

# Before starting, initialize the variables.
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)


for step in range(2001):
    sess.run(train, feed_dict={X:x_data, Y:y_data})

print(sess.run(hypothesis, feed_dict={X:[[1],[1],[2]]})>0.5)
print(sess.run(hypothesis, feed_dict={X:[[1],[6],[7]]})>0.5)
print(sess.run(hypothesis, feed_dict={X:[[1,1],[4,3],[3,5]]})>0.5)
