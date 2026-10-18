import torch

def reshape_matrix(a, new_shape) -> torch.Tensor:
    """
    Reshape a 2D matrix to the requested shape.
    Return an empty tensor if the element counts mismatch.
    """
    a_t = torch.as_tensor(a, dtype=torch.float)

    if a_t.numel() != new_shape[0] * new_shape[1]:
        return torch.tensor([])

    return a_t.reshape(new_shape)