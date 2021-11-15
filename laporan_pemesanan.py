from os import write
import uvicorn
import json
from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

with open("laporan_pemesanan.json","r") as read_file:
	data_laporan = json.load(read_file)

app = FastAPI() 

@app.get("/")
def root():
	return ("Bagian Laporan Pemesanan")

@app.get("/laporan_pemesanan")
async def read_all_orders():
	return data_laporan

@app.get("/laporan_pemesanan/{user_id}")
async def read_orders_user(user_id : int):
	return data_laporan["laporan pemesanan"][user_id - 1]
	
@app.get("/laporan_pemesanan/{user_id}/{order_id}")
async def read_order(user_id : int, order_id : int):
	return data_laporan["laporan pemesanan"][user_id - 1]["order"][order_id - 1]

@app.get("/laporan_pemesanan/{user_id}/{order_id}/{detail}")
async def read_order_detail(user_id : int, order_id : int, detail : str):
	if detail == "paket":
		return data_laporan["laporan pemesanan"][user_id - 1]["order"][order_id - 1]["paket"]
	elif detail == "pembayaran":
		return data_laporan["laporan pemesanan"][user_id - 1]["order"][order_id - 1]["status bayar"]
	elif detail == "CV" or "cv" or "Cv" or "cV" :
		return data_laporan["laporan pemesanan"][user_id - 1]["order"][order_id - 1]["status CV"]
	else:
		return "masukan tidak valid!"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)