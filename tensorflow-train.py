#/usr/bin/python
#coding=utf-8
"""
@author:luffyren-ubuntu-vm
@date:
@DESC:
使用tensorflow 实现特征行为聚类。
"""
import tensorflow as tf
from random import choice, shuffle
import sys
import json
from numpy import array


def test_tf():
    a = tf.placeholder("float")
    b = tf.placeholder("float")
    y = tf.multiply(a, b)
    sess = tf.Session()
    print sess.run(y, feed_dict={a: 3, b: 3})


def input_mtx():
    """
    加载文件中保存的矩阵，转换成输入。进行聚类
    :return: 返回文件中的向量
    """
    mtx_file = open("data/vector_file.json", 'r')
    #　加载向量
    vec_dict = json.load(mtx_file)
    vectors = []
    for value in vec_dict:
        vectors.append(vec_dict[value])
    mtx_file.close()

    print u"加载向量文件完成"
    # print vectors
    print "向量维度：" + str(len(vectors[0]))
    return vectors


def tf_train():
    """
    使用tensorflow接口进行聚类,使用kmean聚类算法实现。
    注：当前未实现削减无关因素的影响，当前来说，读取注册表内容的API调用非常多，其他的操作相对来说少了很多。
    :return: 
    """
    vectors = input_mtx()
    # 将向量加载到会话中
    tf_vecs = tf.constant(vectors)
    # 当前还不清楚如何取Ｋ值，这里首先就用４
    k = 4
    centroides = tf.Variable(tf.slice(tf.random_shuffle(vectors), [0, 0], [k, -1]))
    expand_vecs = tf.expand_dims(tf_vecs, 0)
    expand_cens = tf.expand_dims(centroides, 1)
    diff = tf.subtract(expand_vecs, expand_cens)
    sqr = tf.square(diff)
    distance = tf.reduce_sum(sqr, 2)
    assignments = tf.argmin(distance, 0)

    #计算图心
    print "compute centroids"
    # means = tf.concat(0, [tf.reduce_mean(tf.gather(vectors, tf.reshape(tf.where(tf.equal(assignments, c)), [1, -1])), reduction_indices=[1])for c in xrange(k)])

    equal_result = tf.equal(assignments, [1])
    reshape_result = tf.reshape(tf.where(equal_result), [1, -1])
    gather_result = tf.gather(vectors, reshape_result)
    reduce_mean = tf.reduce_mean(gather_result, reduction_indices=[1])
    means = tf.concat(0, [reduce_mean, reduce_mean])
    update_centroides = tf.assign(centroides, means)
    init_op = tf.initialize_all_variables()

    # 准备工作就绪 开始
    print "finish initialization... session start..."
    sess = tf.Session()
    sess.run(init_op)
    for step in xrange(100):
        _, centroides_values, assignments_values = sess.run([update_centroides, centroides, assignments])


def tf_kmean(vectors, k):
    """
    K-means clusters
    :param vectors: 
    :param k: 
    :return: 
    """
    no_of_clusters = int(k)
    assert no_of_clusters < len(vectors)

    # 找出向量的维度
    dim = len(vectors[0])
    # 辅助随机地从可得的向量中选取中心点
    vector_indices = list(range(len(vectors)))
    shuffle(vector_indices)
    # 计算图
    # 我们创建了一个默认的计算流的图用于整个算法中，这样就保证了当函数被多次调用
    # 时，默认的图并不会被从上一次调用时留下的未使用的OPS或者Variables挤满
    graph = tf.Graph()
    with graph.as_default():
        # 计算的会话
        sess = tf.Session()
        # #构建基本的计算的元素
        # #首先我们需要保证每个中心点都会存在一个Variable矩阵
        # #从现有的点集合中抽取出一部分作为默认的中心点
        centroids = [tf.Variable((vectors[vector_indices[i]]))
                     for i in range(no_of_clusters)]
        # #创建一个placeholder用于存放各个中心点可能的分类的情况
        centroid_value = tf.placeholder("int32", [dim])
        cent_assigns = []
        for centroid in centroids:
            cent_assigns.append(tf.assign(centroid, centroid_value))
        # #对于每个独立向量的分属的类别设置为默认值0
        assignments = [tf.Variable(0) for i in range(len(vectors))]
        # #这些节点在后续的操作中会被分配到合适的值
        assignment_value = tf.placeholder("int32")
        cluster_assigns = []
        for assignment in assignments:
            cluster_assigns.append(tf.assign(assignment,
                                             assignment_value))
        # 下面创建用于计算平均值的操作节点
        # 输入的placeholder
        mean_input = tf.placeholder("int32", [None, dim])
        # 节点/OP接受输入，并且计算0维度的平均值，譬如输入的向量列表
        mean_op = tf.reduce_mean(mean_input, 0)
        # 用于计算欧几里得距离的节点
        v1 = tf.placeholder("int32", [dim])
        v2 = tf.placeholder("int32", [dim])
        euclid_dist = tf.sqrt(tf.reduce_sum(tf.pow(tf.subtract(
            v1, v2), 2)))
        # #这个OP会决定应该将向量归属到哪个节点
        # #基于向量到中心点的欧几里得距离
        # Placeholder for input
        centroid_distances = tf.placeholder("int32", [no_of_clusters])
        cluster_assignment = tf.argmin(centroid_distances, 0)
        # #初始化所有的状态值
        # #这会帮助初始化图中定义的所有Variables。Variable-initializer应该定
        # ##义在所有的Variables被构造之后，这样所有的Variables才会被纳入初始化
        init_op = tf.initialize_all_variables()
        # 初始化所有的变量
        sess.run(init_op)
        # 集群遍历
        # 接下来在K-Means聚类迭代中使用最大期望算法。为了简单起见，只让它执行固
        # 定的次数，而不设置一个终止条件
        noofiterations = 100
        for iteration_n in range(noofiterations):
            # 期望步骤
            # 基于上次迭代后算出的中心点的未知
            # the _expected_ centroid assignments.
            # 首先遍历所有的向量
            for vector_n in range(len(vectors)):
                vect = vectors[vector_n]
                # 计算给定向量与分配的中心节点之间的欧几里得距离
                distances = [sess.run(euclid_dist, feed_dict={
                v1: vect, v2: sess.run(centroid)})
                     for centroid in centroids]
                # 下面可以使用集群分配操作，将上述的距离当做输入
                assignment = sess.run(cluster_assignment, feed_dict={
                    centroid_distances: distances})
                # 接下来为每个向量分配合适的值
                sess.run(cluster_assigns[vector_n], feed_dict={
                    assignment_value: assignment})
        # 最大化的步骤
        # 基于上述的期望步骤，计算每个新的中心点的距离从而使集群内的平方和最小
        for cluster_n in range(no_of_clusters):
            # 收集所有分配给该集群的向量
            assigned_vects = [vectors[i] for i in range(len(vectors))
                      if sess.run(assignments[i]) == cluster_n]
            # 计算新的集群中心点
            new_location = sess.run(mean_op, feed_dict={
                mean_input: array(assigned_vects)})
            # 为每个向量分配合适的中心点
            sess.run(cent_assigns[cluster_n], feed_dict={
                centroid_value: new_location})

        # 返回中心节点和分组
        centroids = sess.run(centroids)
        assignments = sess.run(assignments)
        return centroids, assignments


def main():
    print "tensorflow surport added"
    test_tf()
    # 开始tensorflow训练
    # tf_train()
    centroids, assginments = tf_kmean(vectors=input_mtx(), k=2)
    print centroids
    return 0


if __name__ == "__main__":
    sys.exit(main())
