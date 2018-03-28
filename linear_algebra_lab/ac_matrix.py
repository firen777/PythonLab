"""
Reviewing Linear Algebra and play with OO in Python in the process.

[Underscore and stuffs](https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-a-single-and-a-double-underscore-before-an-object-name)
['Private' field](https://stackoverflow.com/questions/2064202/private-members-in-python)
"""
import sys

class AC_Matrix:
    def __init__(self, *mat):
        """Constructor of AC_Matrix class
        
        Arguments:
        mat: list of vectors. Notice every list item is a column instead of row. 
        
        For example:
        ```
        i1 j1 k1
        i2 j2 k2
        i3 j3 k3
        ```

        Should be passed as:
        ```
        mat = [i1,i2,i3],[j1,j2,j3],[k1,k2,k3]
        ```

        """
        num_count = len(mat[0])
        
        for li in mat:
            if len(li) != num_count:
                raise ValueError("Invalid Matrix format:\none or more of the vecotrs has different number of dimension")
        
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

    try:
        mat1 = AC_Matrix([1,2,3])
    except ValueError as e:
        print(e)
    print(mat1)


if __name__ == "__main__":
    main(sys.argv)
