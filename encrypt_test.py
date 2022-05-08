from encrypt import encrypt, decrypt

def test_encrypt_decrypt():

    seed = 147
    message = "Hello, world!"

    encrypted = encrypt(message, seed)

    assert message != encrypted

    decrypted = decrypt(encrypted, seed)

    assert message == decrypted

    different_seed = 148

    different_decrypted = decrypt(encrypted, different_seed)

    assert message != different_decrypted