import torch

def linear_regression_normal_equation(X, y) -> torch.Tensor:
    """
    Solve linear regression via the normal equation using PyTorch.
    X: Tensor or convertible of shape (m,n); y: shape (m,) or (m,1).
    Returns a 1-D tensor of length n, rounded to 4 decimals.
    """
    X_t = torch.as_tensor(X, dtype=torch.float)
    y_t = torch.as_tensor(y, dtype=torch.float).reshape(-1, 1)
    X_transpose = X_t.T
    XtX = X_transpose @ X_t
    XtX_inv = torch.linalg.pinv(XtX)
    Xty = X_transpose @ y_t
    theta = XtX_inv @ Xty
    theta = theta.flatten()
    theta = torch.round(theta * 10000) / 10000
    return theta