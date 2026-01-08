# Screenshots

ใส่ screenshots ของงานที่ทำในโฟลเดอร์นี้

## Screenshots ที่ต้องมี (10 คะแนน)

1. **docker-compose-ps.png** - ผลลัพธ์ `docker-compose ps`
   ```bash
   docker-compose ps
   ```

2. **containers-running.png** - แสดงว่า containers ทำงาน

3. **frontend-app.png** - หน้า Streamlit app (http://localhost:8501)

4. **api-health.png** - ผลลัพธ์ API health check
   ```bash
   curl http://localhost:9000/health
   ```

## วิธีรัน

```bash
# Build และ run
docker-compose up -d --build

# ดู status
docker-compose ps

# ดู logs
docker-compose logs -f

# หยุด
docker-compose down
```

## Troubleshooting

### Build failed
```bash
# ดู logs ของ service ที่มีปัญหา
docker-compose logs api
docker-compose logs frontend
```

### Port already in use
```bash
# ตรวจสอบ port
netstat -an | findstr 9000
netstat -an | findstr 8501

# หยุด container เก่า
docker-compose down
```
