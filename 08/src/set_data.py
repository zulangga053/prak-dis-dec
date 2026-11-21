from sqlmodel import Field, Session, SQLModel, create_engine


class Produk(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    kode_sku: str = Field(max_length=6)
    nama_produk: str = Field(max_length=100)
    stok: int
    harga: float
    tersedia: bool


engine = create_engine("sqlite:///inventaris.db")


def insert_initial_data():
    daftar_produk = [
        Produk(kode_sku="PRD001", nama_produk="Keyboard", stok=15, harga=1250000.0, tersedia=True),
        Produk(kode_sku="PRD002", nama_produk="Mouse Wireless Logitech MX Master 3S", stok=8, harga=1599000.5, tersedia=True),
        Produk(kode_sku="PRD003", nama_produk="USB-C Hub", stok=0, harga=650000.0, tersedia=False),
        Produk(kode_sku="PRD004", nama_produk="Monitor LG UltraGear 24 Inch", stok=5, harga=2350000.75, tersedia=True),
        Produk(kode_sku="PRD005", nama_produk="Laptop Stand Aluminium", stok=20, harga=185000.0, tersedia=True),
    ]

    with Session(engine) as session:
        for item in daftar_produk:
            session.add(item)
        session.commit()
        print("Berhasil memasukkan 5 data produk ke database inventaris.db!")


if __name__ == "__main__":
    insert_initial_data()