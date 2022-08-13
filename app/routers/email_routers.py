from fastapi import APIRouter
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr, BaseModel
from typing import List
from app.schemas.email_schemas import EmailSchema, RequestEmail, EmailResponse
import os
from dotenv import dotenv_values

credentials = {
    **dotenv_values(".env"),
    **os.environ,
}


class EmailSchema(BaseModel):
    email: List[EmailStr]


router = APIRouter()


@router.post("/")
async def simple_send(
    request: RequestEmail
):

    message = MessageSchema(
        subject="Colegio Bautista Matagalpa - Sitio Web",
        recipients=[credentials['MAIL_TO']],
        body="Recibido de: " + request.parameter.name + "\n" +
        "Correo: " + request.parameter.email + "\n" + "Télefono: " + request.parameter.phone +
        "\n" + "Mensaje: " + request.parameter.content,

    )

    fm = FastMail(ConnectionConfig(
        MAIL_USERNAME=credentials['MAIL_FROM'],
        MAIL_PASSWORD=credentials['PASSWORD'],
        MAIL_FROM=request.parameter.email,
        MAIL_PORT=credentials['MAIL_PORT'],
        MAIL_SERVER=credentials['MAIL_SERVER'],
        MAIL_FROM_NAME=request.parameter.name,
        MAIL_TLS=True,
        MAIL_SSL=False
    ))
    await fm.send_message(message)
    return EmailResponse(code=200, status="ok", message="Su correo ha sido enviado exitosamente", result=message)
