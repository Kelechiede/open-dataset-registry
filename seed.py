from database import SessionLocal, engine
import models
import auth

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

# ── ADMIN ─────────────────────────────────────────────
admin = models.Admin(
    username="kelechi",
    email="info@kelechiededata.org",
    password=auth.hash_password("KelechiRegistry2026!")
)
db.add(admin)
db.commit()

# ── DATASETS ──────────────────────────────────────────
datasets = [
    models.Dataset(
        name="Canadian Housing Market Data 2024",
        source="Canada Mortgage and Housing Corporation",
        format="CSV",
        size="45 MB",
        domain="Real Estate",
        description="Provincial housing prices, sales volume and market trends across Canada from 2015 to 2024",
        tags="housing,real estate,Canada,prices,provincial",
        url="https://www.cmhc-schl.gc.ca"
    ),
    models.Dataset(
        name="Nigerian GDP and Economic Indicators",
        source="World Bank Open Data",
        format="JSON",
        size="12 MB",
        domain="Economics",
        description="GDP growth, inflation, unemployment and trade balance data for Nigeria from 1960 to 2024",
        tags="GDP,Nigeria,economics,World Bank,inflation",
        url="https://data.worldbank.org"
    ),
    models.Dataset(
        name="Global VLC Channel Measurements",
        source="IEEE DataPort",
        format="CSV",
        size="8 MB",
        domain="Digital Communications",
        description="Visible Light Communication channel measurements including BER, SNR and distance parameters",
        tags="VLC,communications,BER,SNR,optical wireless",
        url="https://ieee-dataport.org"
    ),
    models.Dataset(
        name="Oslo Weather and Climate Records",
        source="Norwegian Meteorological Institute",
        format="CSV",
        size="22 MB",
        domain="Climate",
        description="Daily temperature, precipitation and wind speed records for Oslo from 1950 to 2024",
        tags="weather,climate,Oslo,Norway,temperature",
        url="https://www.met.no"
    ),
    models.Dataset(
        name="Newfoundland Fisheries Data",
        source="Fisheries and Oceans Canada",
        format="XLSX",
        size="18 MB",
        domain="Marine Biology",
        description="Fish stock assessments, catch volumes and species distribution in Newfoundland waters",
        tags="fisheries,Newfoundland,Canada,marine,stocks",
        url="https://www.dfo-mpo.gc.ca"
    ),
    models.Dataset(
        name="UCI Machine Learning Repository — Iris",
        source="UCI Machine Learning Repository",
        format="CSV",
        size="< 1 MB",
        domain="Machine Learning",
        description="Classic iris flower dataset with sepal and petal measurements for three species",
        tags="machine learning,classification,iris,UCI,benchmark",
        url="https://archive.ics.uci.edu"
    ),
    models.Dataset(
        name="Toronto Stock Exchange Daily Prices",
        source="TMX Group",
        format="JSON",
        size="156 MB",
        domain="Finance",
        description="Daily open, high, low, close and volume data for TSX-listed companies from 2010 to 2024",
        tags="stocks,TSX,finance,Canada,trading",
        url="https://www.tmx.com"
    ),
    models.Dataset(
        name="Canadian Census Population Data 2021",
        source="Statistics Canada",
        format="CSV",
        size="67 MB",
        domain="Demographics",
        description="Population counts, age distribution, household size and language data by province and territory",
        tags="census,population,Canada,demographics,Statistics Canada",
        url="https://www.statcan.gc.ca"
    ),
]

db.add_all(datasets)
db.commit()
db.close()

print("✅ Database seeded successfully!")
print(f"   Admin:    1")
print(f"   Datasets: {len(datasets)}")