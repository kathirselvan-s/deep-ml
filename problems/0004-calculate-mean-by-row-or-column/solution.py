import torch

def calculate_matrix_mean(matrix, mode: str) -> torch.Tensor:
    """
    Calculate mean of a 2D matrix per row or per column using PyTorch.
    """
    a_t = torch.as_tensor(matrix, dtype=torch.float)

    if mode == "row":
        return torch.mean(a_t, dim=1)

    elif mode == "column":
        return torch.mean(a_t, dim=0)

    else:
        raise ValueError("Mode must be 'row' or 'column'")