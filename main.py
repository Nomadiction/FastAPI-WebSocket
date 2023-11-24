from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from fastapi.responses import FileResponse
import uvicorn
from func import permute_name, extraction


class Person(BaseModel):
    name: str
    age: int

 
app = FastAPI()


@app.get("/")
def root():
    return FileResponse("public/index.html")


@app.post("/data")
def recieve(person: Person):
       
    data = [{"name": person.name, "age": person.age}]
    
    print(data)
    
    return {"message": f"Данные получены: {data}"}



@app.websocket("/websocket")
async def websocket_endpoint(websocket: WebSocket):
    # Принимаем соединение WebSocket
    await websocket.accept()
    
    while True:
        # Получаем текстовое сообщение от клиента
        data = await websocket.receive_text()
        print(f"Got name: {data}")
        
        # extracted_data = extraction(data)
        
        # for name, age in extracted_data:
        #     intermediate_results, final_result = permute_name(name, age)
        #     count = 1

        #     # Отправляем промежуточные результаты клиенту
        #     for result in intermediate_results:
        #         message = f"red|count: {count} - permute value: {result}\r"
        #         print(message, end='', flush=True)
                
        #         # Отправляем сообщение клиенту
        #         await websocket.send_text(message)
        #         count += 1
            
        #     # Отправляем сообщение клиенту
        #     await websocket.send_text(f"{name}")
        #     await websocket.send_text(f"green|Final result: {final_result}")
            
        #     print("Processing final result:", final_result)   


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)