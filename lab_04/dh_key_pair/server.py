from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def generate_dh_parameters():
    """
    Tạo tham số DH với generator là 2 và key size là 2048 bit.
    """
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters

def generate_server_key_pair(parameters):
    """
    Tạo cặp khóa DH (private và public) cho máy chủ dựa trên các tham số đã cho.
    """
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def main():
    """
    Hàm chính để tạo tham số, tạo cặp khóa DH và lưu khóa công khai của máy chủ.
    """
    # 1. Tạo tham số Diffie-Hellman
    parameters = generate_dh_parameters()
    
    # 2. Tạo cặp khóa DH của máy chủ
    private_key, public_key = generate_server_key_pair(parameters)

    # 3. Ghi khóa công khai của máy chủ vào tệp 'server_public_key.pem'
    with open("server_public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
        
if __name__ == "__main__":
    main()