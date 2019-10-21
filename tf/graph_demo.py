from __future__ import absolute_import, division, print_function
import tensorflow as tf

# a = tf.placeholder(dtype=tf.float32, shape=(), name='a')
# b = tf.constant([[2, 3], [4, 5]], dtype=tf.float32)
# c = tf.multiply(a, b)
#
# init = tf.global_variables_initializer()
#
# with tf.Session() as sess:
#     sess.run(init)
#     print(sess.run([c, ], feed_dict={'a:0': 2}))
#
#     # for op in tf.get_default_graph().get_operations():
#     #     print(op)
#
#     # for node in tf.get_default_graph().as_graph_def().node:
#     #     print(node)


dataset = tf.data.Dataset.range(6)
dataset = dataset.batch(4)

iter = dataset.make_one_shot_iterator()
get_next = iter.get_next()
with tf.Session() as sess:
    print(sess.run(get_next))  # [0 1 2 3]
    print(sess.run(get_next))  # [4 5]

a = [1, 2, 3]
print(a*2)

a = 'test'
print(a.encode('utf-8'))

print('hello world')

print('merge more code')

print('b2')

print('b2 flow')

print('b3')

print('b3 flow')
