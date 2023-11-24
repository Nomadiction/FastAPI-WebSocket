from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse
from func import permute_name, extraction
import uvicorn


app = FastAPI()


@app.get("/")
def root():
    return FileResponse("public/index1.html")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Принимаем соединение WebSocket
    await websocket.accept()
    
    while True:
        data = []
        
        # Получаем текстовое сообщение от клиента
        name = await websocket.receive_text()
        age = await websocket.receive_text()
        
        print(f"Got name: {name}")
        print(f"Got age: {age}")
        
        values = {'name': name, 'age': int(age)}
       
        data.append(values)       
        print(data)
        
        extracted_data = extraction(data)
        
        for name, age in extracted_data:
            intermediate_results, final_result = permute_name(name, age)
            count = 1

            # Отправляем промежуточные результаты клиенту
            for result in intermediate_results:
                message = f"red|count: {count} - permute value: {result}\r"
                print(message, end='', flush=True)
                
                # Отправляем сообщение клиенту
                await websocket.send_text(message)
                count += 1
            
            # Отправляем сообщение клиенту
            await websocket.send_text(f"{name}")
            await websocket.send_text(f"green|Final result: {final_result}")
            
            print("Processing final result:", final_result)   
    


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8800, reload=True)



