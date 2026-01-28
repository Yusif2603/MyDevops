# 1. Настройки провайдера
provider "aws" {
  region = "eu-central-1" # Франкфурт
}

# 2. Создаем Security Group (открываем порты 80 для сайта и 22 для SSH)
resource "aws_security_group" "my_sg" {
  name        = "yusif-proxy-sg"
  description = "Allow HTTP and SSH"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

 ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# 3. Создаем сам сервер
resource "aws_instance" "my_server" {
  ami           = "ami-0084a47cc718c111a" # Ubuntu 24.04
  instance_type = "t3.micro"
  key_name      = "yusif-new-key" # Убедись, что этот ключ у тебя создан в AWS консоли
  vpc_security_group_ids = [aws_security_group.my_sg.id]

  # Передаем скрипт настройки из соседнего файла
  user_data = file("user_data.sh")

  tags = {
    Name = "Yusif-Super-Server"
 }
}

# 4. Выводим IP адрес после запуска, чтобы не искать его
output "server_public_ip" {
  value = aws_instance.my_server.public_ip
}