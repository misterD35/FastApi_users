from fastapi import APIRouter


router = APIRouter(tags=['INFO'])


@router.get('/info')
async def info():
    return {'message': 'v.1.0.0.'}