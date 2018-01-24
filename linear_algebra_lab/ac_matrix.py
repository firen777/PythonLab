"""
Reviewing Linear Algebra and play with OO in Python in the process.

[Underscore and stuffs](https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-a-single-and-a-double-underscore-before-an-object-name)
['Private' field](https://stackoverflow.com/questions/2064202/private-members-in-python)
"""
import sys

class AC_Matrix:
    def __init__(self, mat=[[1,0,0],[0,1,0],[0,0,1]]):
        self.mat = mat

    def __str__(self):
        # str_result = "["
        # for v in self.mat:
        #     str_result = str_result + "["
        #     for n in v:
        #         str_result = str_result + str(n) + ","
        #     str_result = str_result[:-1] + "],"
        # str_result = str_result[:-1] + "]"
        # return str_result
        return str(self.mat)


def trans_factory(mat=[[1,0,0],[0,1,0],[0,0,1]]):
    """
    Linear transformation function factory
    
    Arguments:
    mat: matrix, default [1 0 0],[0 1 0],[0 0 1] //3d ID matrix
    
    Returns:
    Linear transformation function
    """
    def helper(vec_mat):
        print('foo')
    return helper

###Main Function###
def main(argv):
    vec1 = [1,2]
    mat1 = [[1,2],[1,2]]
    print(mat1[0][0])
    test_func = trans_factory()
    test_func(mat1)

    mat1 = AC_Matrix(mat = [[1,0,0],[0,2.9,300]])
    print(mat1)


if __name__ == "__main__":
    main(sys.argv)
