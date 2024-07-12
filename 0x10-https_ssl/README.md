HTTPS
HTTPS (Hypertext Transfer Protocol Secure) is an extension of HTTP. It is used for secure communication over a computer network and is widely used on the internet. HTTPS encrypts data sent between a user's web browser and a website, providing a secure channel to prevent unauthorized access and tampering.

Two Main Elements of SSL
SSL (Secure Sockets Layer) provides:

Encryption: Protects data privacy by encrypting the data exchanged between the web server and the client, ensuring that it cannot be read by third parties.
Authentication: Ensures that the server the client is communicating with is indeed the correct one, protecting against impersonation and man-in-the-middle attacks.
HAProxy SSL Termination on Ubuntu 16.04
SSL termination refers to the process of decrypting SSL-encrypted traffic at the load balancer level (in this case, HAProxy), which then forwards the unencrypted traffic to the backend servers. This reduces the load on backend servers and centralizes SSL certificate management.
SSL Termination
SSL termination is the process of decrypting SSL-encrypted data on a dedicated server or load balancer, which then forwards the unencrypted data to the backend servers. This process offloads the decryption workload from the backend servers, improving performance and simplifying SSL certificate management.

Bash Function
A Bash function is a reusable block of code within a Bash script that performs a specific task. Functions help to organize and modularize the script.
SSL's Two Main Roles
Encryption: SSL encrypts the data exchanged between the web server and the client. This ensures that even if the data is intercepted by a third party, it cannot be read or tampered with because it is in an encrypted format.
Authentication: SSL provides a mechanism for the client to verify the identity of the server. This prevents impersonation attacks, ensuring that the client is communicating with the intended server.
Purpose of Encrypting Traffic
The primary purpose of encrypting traffic is to protect the confidentiality and integrity of the data being exchanged. Encryption ensures that sensitive information such as passwords, credit card numbers, and personal data are not exposed to unauthorized parties. It also helps to prevent data tampering and eavesdropping by malicious actors.
