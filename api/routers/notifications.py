from fastapi import APIRouter

router = APIRouter()


@router.get("/notifications")
async def list_notification():
    pass


@router.post("/notifications")
async def create_notifications():
    pass


@router.patch("/notifications/{busanduser_id}")
async def update_notifications():
    pass


@router.delete("/notifications/{busanduser_id}")
async def delete_busanduser():
    pass
