from litestar.config.cors import CORSConfig

cors_config = CORSConfig(
    allow_origins=["http://localhost:5173", "http://localhost:5174"],
    allow_methods=["*"],
    allow_credentials=True,
)
