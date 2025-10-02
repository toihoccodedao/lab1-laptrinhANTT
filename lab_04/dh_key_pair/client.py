from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def generate_client_key_pair(parameters):
    """
    Tạo cặp khóa DH (private và public) cho client dựa trên các tham số đã nhận
    (thường là từ khóa công khai của server).
    """
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_secret(private_key, server_public_key):
    """
    Tính toán khóa bí mật chung bằng cách trao đổi khóa DH.
    """
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    """
    Hàm chính để tải khóa công khai của server, tạo cặp khóa client,
    tính toán khóa bí mật chung và in ra.
    """
    # Load server's public key (từ tệp đã tạo ở phía server)
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    # Trích xuất tham số DH từ khóa công khai của server
    parameters = server_public_key.parameters()
    
    # Tạo cặp khóa DH của client
    private_key, public_key = generate_client_key_pair(parameters)

    # Tính toán khóa bí mật chung
    shared_secret = derive_shared_secret(private_key, server_public_key)

    # In khóa bí mật chung ra màn hình dưới dạng hex
    print("Shared Secret:", shared_secret.hex())

if __name__ == "__main__":
    main()