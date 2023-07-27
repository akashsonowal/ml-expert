import numpy as np 

class SVD:
    def __init__(self, n_components=None):
        self.n_components = n_components
    
    def fit_transform(self, X):
        # X doesn't need to be 0-centered
        U, sigma, Vh = np.linalg.svd(X, full_matrices=True, compute_uv=True) 
        # It's not necessary to compute the full matrix of U or V as we are interested till rank of original data
        
        if self.n_components is not None:
            U = U[:, : self.n_components]
            sigma = sigma[ : self.n_components]

        X_svd = np.dot(U, np.diag(sigma, ))
        return X_svd

if __name__ == "__main__":
    from sklearn import datasets 
    data = datasets.load_iris()
    X = data.data
    y = data.target 

    svd = SVD(2)
    X_projected = svd.fit_transform(X)

    print("Shape of X:", X.shape)
    print("Shape of transformed X:", X_projected.shape)
