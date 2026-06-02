from pydantic import BaseModel, EmailStr


class SignupRequest(BaseModel):
    name: str
    phone: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class AuthResponse(BaseModel):
    status: bool
    message: str


class LoginResponse(BaseModel):
    status: bool
    access_token: str
    token_type: str