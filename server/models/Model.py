from sqlalchemy import Column, Integer, String, DateTime, Float, BLOB, PrimaryKeyConstraint
from .database import Base 

class TbUsers(Base): 
    __tablename__ = 'users' 
    userid = Column(String(255), primary_key=True)
    password = Column(String(255))
    name = Column(String(255))
    
    def __init__(self, userid, password, name): 
        self.userid = userid 
        self.password = password 
        self.name = name
        
    def __repr__(self): 
        return "<TbUsers('%s', '%s', '%s'>" %(self.userid, self.password, self.name)

class TbPeeDetectorData(Base):
    __tablename__ = 'peedetectordata'
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    date = Column(String(20))
    name = Column(String(20))
    gatewayMac = Column(String(17))
    mac = Column(String(17))
    rssi = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)
    connect = Column(String(2))
    wetness = Column(Integer)
    battery = Column(Float)
    temperature = Column(Float)
    inverted = Column(String(2))
    pose = Column(String(2))
    fall = Column(String(2))
    isActive = Column(String(2))

    def __init__(self, date, name, gatewayMac, mac, rssi, x, y, z, connect, wetness, battery, temperature, inverted, pose, fall, isActive):
        self.date = date
        self.name = name
        self.gatewayMac = gatewayMac
        self.mac = mac

        self.rssi = rssi
        self.x = x
        self.y = y
        self.z = z
        self.connect = connect

        self.wetness = wetness
        self.battery = battery
        self. temperature = temperature
        self.inverted = inverted
        self.pose = pose

        self.fall = fall
        self.isActive = isActive
    
    def __repr__(self):
        return "<TbPeeDetectorData('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'>" %(
            self.id, self.date, self.name, self.gatewayMac, self.mac, 
            self.rssi, self.x, self.y, self.z, self.connect, 
            self.wetness, self.battery, self.temperature, self.inverted, self.pose, 
            self.fall, self.isActive)

class TbBandData(Base):
    __tablename__ = 'banddata'
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    date = Column(String(20))
    name = Column(String(20))
    gatewayMac = Column(String(17))
    mac = Column(String(17))
    rssi = Column(Integer)
    activeDuration = Column(Integer)
    steps = Column(Integer)
    calories = Column(Integer)
    distance = Column(Integer)
    heartRate = Column(Integer)
    sleep_min = Column(Integer)

    def __init__(self, date, name, gatewayMac, mac, rssi, activeDuration, steps, calories, distance, heartRate, sleep_min):
        self.date = date
        self.name = name
        self.gatewayMac = gatewayMac
        self.mac = mac

        self.rssi = rssi
        self.activeDuration = activeDuration
        self.steps = steps
        self.calories = calories
        self.distance = distance

        self.heartRate = heartRate
        self.sleep_min = sleep_min
    
    def __repr__(self):
        return "<TbBandData('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'>" %(
            self.id, self.date, self.name, self.gatewayMac, self.mac, 
            self.rssi, self.activeDuration, self.steps, self.calories, self.distance, 
            self.heartRate, self.sleep_min)

class TbIaqData(Base):
    __tablename__ = 'iaqdata'
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    date = Column(String(20))
    name = Column(String(50))
    gatewayMac = Column(String(17))
    mac = Column(String(17))
    rssi = Column(Integer)
    pm_1_0 = Column(Float)
    pm_2_5 = Column(Float)
    pm_10_0 = Column(Float)
    temp_c = Column(Float)
    temp_f = Column(Float)
    humi = Column(Float)
    co_2 = Column(Float)
    tvoc = Column(Float)
    score = Column(Float)

    def __init__(self, date, name, gatewayMac, mac, rssi, pm_1_0, pm_2_5, pm_10_0, temp_c, temp_f, humi, co_2, tvoc, score):
        self.date = date
        self.name = name
        self.gatewayMac = gatewayMac
        self.mac = mac
        self.rssi = rssi
        
        self.pm_1_0 = pm_1_0
        self.pm_2_5 = pm_2_5
        self.pm_10_0 = pm_10_0
        self.temp_c = temp_c
        self.temp_f = temp_f
        
        self.humi = humi
        self.co_2 = co_2
        self.tvoc = tvoc
        self.score = score
    
    def __repr__(self):
        return "<TbIaqData('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s'>" %(
            self.id, self.date, self.name, self.gatewayMac, self.mac, 
            self.rssi, self.pm_1_0, self.pm_2_5, self.pm_10_0, self.temp_c, 
            self.temp_f, self.humi, self.co_2, self.tvoc, self.score)

class TbMaeChulHapGae(Base):
    __tablename__ = 'MaeChulHapGae'
    
    MaeJangCode = Column(String(4))
    MaeChulDate = Column(String(10))
    PosID = Column(String(2))
    JunPyoBunHo = Column(Integer)
    SaWonBunHo = Column(String(7))
    
    GeunMuChaSu = Column(Integer)
    MyungSeSu = Column(Integer)
    HapGaeGumAk = Column(Float)
    DanPumHalIn = Column(Float)
    SilMaeChulDate = Column(String(10))
    
    SilMaeChulTime = Column(String(8))
    MaeChulGuBun = Column(String(1))
    JunSongYeoBu = Column(String(1))
    BonJumJunSongYeoBu = Column(String(1))
    HyunGumGumAk = Column(Float)
    
    SinYongCardGumAk = Column(Float)
    OeSangGumAk = Column(Float)
    SangPumGwonGumAk = Column(Float)
    HalInCuPonGumAk = Column(Float)
    JunJaHwaPeGumAk = Column(Float)
    
    TaSaCuPonGumAk = Column(Float)
    OkCashBag = Column(Float)
    PointCardGumAk = Column(Float)
    ServiceGumAk = Column(Float)
    GiTaGumAk_1 = Column(Float)
    
    GiTaGumAk_2 = Column(Float)
    GiTaGumAk_3 = Column(Float)
    GiTaGumAk_4 = Column(Float)
    GiTaGumAk_5 = Column(Float)
    ReceiveGumAk = Column(Float)
    
    GeoSeuReum = Column(Float)    
    JaSaGoGakCode = Column(String(16))
    TaSaGoGakGuBun = Column(String(16))
    TaSaGoGakCode = Column(String(16))    
    YoungSuJeongImage = Column(BLOB)    
    
    GoGakPointGumAk = Column(Float)
    GoGakPointJumSu = Column(Float)
    GoGakPointSaYongGumAk = Column(Float)
    GoGakPointSaYongJumSu = Column(Float)    
    DeongRokGuBun = Column(String(1))
    
    TableBunHo = Column(String(20))    
    ForignerSu = Column(Integer)
    KoreanSu = Column(Integer)    
    GaekCheong = Column(String(10))    
    GwaSeMaeChulGae = Column(Float)
    
    MyunSeMaeChulGae = Column(Float)
    MyunSeWonGaGae = Column(Float)
    GwaSeWonGaGae = Column(Float)
    GongByungMaeChulGae = Column(Float)
    VATGumAk = Column(Float)
    
    SuSuRyoMaeJangMaeChulGae = Column(Float)
    CardHoeWonMaeChul = Column(Float)
    SaNaeSoBiGumAk = Column(Float)
    SinYongCardMyunSeGumAk = Column(Float)
    SinYongCardGwaSeGumAk = Column(Float)
    
    HyunGumYeongSuJeungMyunSeGumAk = Column(Float)
    HyunGumYeongSuJeungGwaSeGumAk = Column(Float)
    BaeDalGumAk = Column(Float)
    BaeDalHyunGum = Column(Float)
    BaeDalCard = Column(Float)
    
    PointJeokRipGae = Column(Float)
    ImDaeMaeJangMaeChul = Column(Float)    
    RelatedJunPyo = Column(Integer)
    JanDonJukRip = Column(Integer)    
    MaeChulTime = Column(String(2))
    
    RelatedPosID = Column(String(2))    
    SoGaeHalIn = Column(Float)
    HangSaHalIn = Column(Float)
    HalInHapGae = Column(Float)

    __table_args__ = (
        PrimaryKeyConstraint('MaeJangCode', 'MaeChulDate', 'PosID', 'JunPyoBunHo'),
        {},
    )
    
    def __init__(self, 
        MaeJangCode, MaeChulDate, PosID, JunPyoBunHo, SaWonBunHo,
        GeunMuChaSu, MyungSeSu, HapGaeGumAk, DanPumHalIn, SilMaeChulDate,
        SilMaeChulTime, MaeChulGuBun, JunSongYeoBu, BonJumJunSongYeoBu, HyunGumGumAk,
        SinYongCardGumAk, OeSangGumAk, SangPumGwonGumAk, HalInCuPonGumAk, JunJaHwaPeGumAk,
        TaSaCuPonGumAk, OkCashBag, PointCardGumAk, ServiceGumAk, GiTaGumAk_1,
        GiTaGumAk_2, GiTaGumAk_3, GiTaGumAk_4, GiTaGumAk_5, ReceiveGumAk,
        GeoSeuReum, JaSaGoGakCode, TaSaGoGakGuBun, TaSaGoGakCode, YoungSuJeongImage,
        GoGakPointGumAk, GoGakPointJumSu, GoGakPointSaYongGumAk, GoGakPointSaYongJumSu, DeongRokGuBun,
        TableBunHo, ForignerSu, KoreanSu, GaekCheong, GwaSeMaeChulGae,
        MyunSeMaeChulGae, MyunSeWonGaGae, GwaSeWonGaGae, GongByungMaeChulGae, VATGumAk,
        SuSuRyoMaeJangMaeChulGae, CardHoeWonMaeChul, SaNaeSoBiGumAk, SinYongCardMyunSeGumAk, SinYongCardGwaSeGumAk,
        HyunGumYeongSuJeungMyunSeGumAk, HyunGumYeongSuJeungGwaSeGumAk, BaeDalGumAk, BaeDalHyunGum, BaeDalCard,
        PointJeokRipGae, ImDaeMaeJangMaeChul, RelatedJunPyo, JanDonJukRip, MaeChulTime,
        RelatedPosID, SoGaeHalIn, HangSaHalIn, HalInHapGae
        ):
        self.MaeJangCode = MaeJangCode
        self.MaeChulDate = MaeChulDate
        self.PosID = PosID
        self.JunPyoBunHo = JunPyoBunHo
        self.SaWonBunHo = SaWonBunHo
        
        self.GeunMuChaSu = GeunMuChaSu
        self.MyungSeSu = MyungSeSu
        self.HapGaeGumAk = HapGaeGumAk
        self.DanPumHalIn = DanPumHalIn
        self.SilMaeChulDate = SilMaeChulDate
        
        self.SilMaeChulTime = SilMaeChulTime
        self.MaeChulGuBun = MaeChulGuBun
        self.JunSongYeoBu = JunSongYeoBu
        self.BonJumJunSongYeoBu = BonJumJunSongYeoBu
        self.HyunGumGumAk = HyunGumGumAk
        
        self.SinYongCardGumAk = SinYongCardGumAk
        self.OeSangGumAk = OeSangGumAk
        self.SangPumGwonGumAk = SangPumGwonGumAk
        self.HalInCuPonGumAk = HalInCuPonGumAk
        self.JunJaHwaPeGumAk = JunJaHwaPeGumAk
        
        self.TaSaCuPonGumAk = TaSaCuPonGumAk
        self.OkCashBag = OkCashBag
        self.PointCardGumAk = PointCardGumAk
        self.ServiceGumAk = ServiceGumAk
        self.GiTaGumAk_1 = GiTaGumAk_1
        
        self.GiTaGumAk_2 = GiTaGumAk_2
        self.GiTaGumAk_3 = GiTaGumAk_3
        self.GiTaGumAk_4 = GiTaGumAk_4
        self.GiTaGumAk_5 = GiTaGumAk_5
        self.ReceiveGumAk = ReceiveGumAk
        
        self.GeoSeuReum = GeoSeuReum
        self.JaSaGoGakCode = JaSaGoGakCode
        self.TaSaGoGakGuBun = TaSaGoGakGuBun
        self.TaSaGoGakCode = TaSaGoGakCode
        self.YoungSuJeongImage = YoungSuJeongImage
        
        self.GoGakPointGumAk = GoGakPointGumAk
        self.GoGakPointJumSu = GoGakPointJumSu
        self.GoGakPointSaYongGumAk = GoGakPointSaYongGumAk
        self.GoGakPointSaYongJumSu = GoGakPointSaYongJumSu
        self.DeongRokGuBun = DeongRokGuBun
        
        self.TableBunHo = TableBunHo
        self.ForignerSu = ForignerSu
        self.KoreanSu = KoreanSu
        self.GaekCheong = GaekCheong
        self.GwaSeMaeChulGae = GwaSeMaeChulGae
        
        self.MyunSeMaeChulGae = MyunSeMaeChulGae
        self.MyunSeWonGaGae = MyunSeWonGaGae
        self.GwaSeWonGaGae = GwaSeWonGaGae
        self.GongByungMaeChulGae = GongByungMaeChulGae
        self.VATGumAk = VATGumAk
        
        self.SuSuRyoMaeJangMaeChulGae = SuSuRyoMaeJangMaeChulGae
        self.CardHoeWonMaeChul = CardHoeWonMaeChul
        self.SaNaeSoBiGumAk = SaNaeSoBiGumAk
        self.SinYongCardMyunSeGumAk = SinYongCardMyunSeGumAk
        self.SinYongCardGwaSeGumAk = SinYongCardGwaSeGumAk
        
        self.HyunGumYeongSuJeungMyunSeGumAk = HyunGumYeongSuJeungMyunSeGumAk
        self.HyunGumYeongSuJeungGwaSeGumAk = HyunGumYeongSuJeungGwaSeGumAk
        self.BaeDalGumAk = BaeDalGumAk
        self.BaeDalHyunGum = BaeDalHyunGum
        self.BaeDalCard = BaeDalCard
        
        self.PointJeokRipGae = PointJeokRipGae
        self.ImDaeMaeJangMaeChul = ImDaeMaeJangMaeChul
        self.RelatedJunPyo = RelatedJunPyo
        self.JanDonJukRip = JanDonJukRip
        self.MaeChulTime = MaeChulTime
        
        self.RelatedPosID = RelatedPosID
        self.SoGaeHalIn = SoGaeHalIn
        self.HangSaHalIn = HangSaHalIn
        self.HalInHapGae = HalInHapGae
    
    def __repr__(self):
        return "<TbMaeChulHapGae('%s', '%s', '%s', '%s'>" %(self.maeJangCode, self.maeChulDate, self.posID, self.JunPyoBunHo)

class TbMaeChulMyungSe(Base):
    __tablename__ = 'MaeChulMyungSe'
    
    MaeJangCode = Column(String(4))
    MaeChulDate = Column(String(10))
    PosID = Column(String(2))
    JunPyoBunHo = Column(Integer)
    BunHo = Column(Integer)
    
    Barcode = Column(String(13))
    SangPumName = Column(String(50))
    DaeBunRyu = Column(String(2))
    JoongBunRyu = Column(String(2))
    SoBunRyu = Column(String(2))
    
    MaeIpDanGa = Column(Float)
    MaeChulDanGa = Column(Float)
    MaeChulSuRyang = Column(Integer)
    HalInHapGae = Column(Float)
    MaeChulGumAk = Column(Float)
    
    HangSaHalIn = Column(Float)
    HalInBiYul = Column(Float)
    DanPumHalIn = Column(Float)
    MyunGwaSe = Column(String(1))
    GwaSeGumAk = Column(Float)
    
    VatGumAk = Column(Float)
    MyunSeGumAk = Column(Float)
    SaWonBunHo = Column(String(7))
    GeunMuChaSu = Column(Integer)
    SilMaeChulDate = Column(String(10))
    
    SilMaeChulTime = Column(String(8))
    PanMaeGuBun = Column(String(1))
    MaeChulGuBun = Column(String(1))
    JunSongYeoBu = Column(String(1))
    BonJumJunSongYeoBu = Column(String(1))
    
    BonJumBalJuYeoBu = Column(String(1))
    SuSuRyoMaeJangCode = Column(String(7))
    SuSuRyoYul = Column(Float)
    GongByungGumAk = Column(Float)
    SangPumGuBun = Column(String(2))
    
    HangSaGumAk = Column(Float)
    HangSaYeoBu = Column(String(1))
    GuRaeChuCode = Column(String(12))
    JaSaGoGakCode = Column(String(16))
    TaSaGoGakGuBun = Column(String(2))
    
    TaSaGoGakCode = Column(String(16))
    DeungRokGuBun = Column(String(1))
    GoGakPointGumAk = Column(Float)
    GoGakPointJumSu = Column(Float)
    TableBunHo = Column(String(20))
    
    GaeCheBunHo = Column(String(12))
    DanMalGiID = Column(String(20))
    PointJukRipYeoBu = Column(String(1))
    PointJukRipYul = Column(Float)
    HyunGumPointGiJun = Column(Integer)
    
    HyunGumPointBase = Column(Integer)
    CardPointGiJun = Column(Integer)
    CardPointBase = Column(Integer)
    HyunGumYoungSuJeongPointGiJun = Column(Integer)
    HyunGumYoungSuJeongPointBase = Column(Integer)
    
    HyunGumPoint = Column(Integer)
    CardPoint = Column(Integer)
    HyunGumYoungSuJeongPoint = Column(Integer)
    HyunGumBiYul = Column(Float)
    CardBiYul = Column(Float)
    
    HyunGumYoungSuJeongBiYul = Column(Float)
    RelatedJunPyo = Column(Integer)
    CardSuSuRyoYul = Column(Float)
    GoGakHyunGumSuSuRyoYul = Column(Float)
    GoGakCardSuSuRyoYul = Column(Float)
    
    HyunGumYoungSuJeungSuSuRyoYul = Column(Float)
    CashBagHyunGumSuSuRyoYul = Column(Float)
    CashBagCardSuSuRyoYul = Column(Float)
    GBCardHyunGumSuSuRyoYul = Column(Float)
    GBCardCardSuSuRyoYul = Column(Float)
    
    BZeroHyunGumSuSuRyoYul = Column(Float)
    BZeroCardSuSuRyoYul = Column(Float)
    BaeDal = Column(String(1))
    HalJeongYul = Column(Integer)
    MaeChulTime = Column(String(2))
    
    RelatedPosID = Column(String(2))
    SoGaeHalIn = Column(Float)
    Plus = Column(String(1))
    Minus = Column(String(1))
    RowDelete = Column(String(1))
    
    GaGyukSuJung = Column(String(1))
    CashBakJeokRipAnHam = Column(String(1))

    __table_args__ = (
        PrimaryKeyConstraint('MaeJangCode', 'MaeChulDate', 'PosID', 'JunPyoBunHo', 'BunHo'),
        {},
    )

    def __init__(self,
        MaeJangCode, MaeChulDate, PosID, JunPyoBunHo, BunHo,
        Barcode, SangPumName, DaeBunRyu, JoongBunRyu, SoBunRyu, 
        MaeIpDanGa, MaeChulDanGa, MaeChulSuRyang, HalInHapGae, MaeChulGumAk,
        HangSaHalIn, HalInBiYul, DanPumHalIn, MyunGwaSe, GwaSeGumAk, 
        VatGumAk, MyunSeGumAk, SaWonBunHo, GeunMuChaSu, SilMaeChulDate,
        SilMaeChulTime, PanMaeGuBun, MaeChulGuBun, JunSongYeoBu, BonJumJunSongYeoBu,
        BonJumBalJuYeoBu, SuSuRyoMaeJangCode, SuSuRyoYul, GongByungGumAk, SangPumGuBun,
        HangSaGumAk, HangSaYeoBu, GuRaeChuCode, JaSaGoGakCode, TaSaGoGakGuBun,
        TaSaGoGakCode, DeungRokGuBun, GoGakPointGumAk, GoGakPointJumSu, TableBunHo,
        GaeCheBunHo, DanMalGiID, PointJukRipYeoBu, PointJukRipYul, HyunGumPointGiJun,
        HyunGumPointBase, CardPointGiJun, CardPointBase, HyunGumYoungSuJeongPointGiJun, HyunGumYoungSuJeongPointBase,
        HyunGumPoint, CardPoint, HyunGumYoungSuJeongPoint, HyunGumBiYul, CardBiYul,
        HyunGumYoungSuJeongBiYul, RelatedJunPyo, CardSuSuRyoYul, GoGakHyunGumSuSuRyoYul, GoGakCardSuSuRyoYul,
        HyunGumYoungSuJeungSuSuRyoYul, CashBagHyunGumSuSuRyoYul, CashBagCardSuSuRyoYul, GBCardHyunGumSuSuRyoYul, GBCardCardSuSuRyoYul,
        BZeroHyunGumSuSuRyoYul, BZeroCardSuSuRyoYul,  BaeDal, HalJeongYul, MaeChulTime,
        RelatedPosID, SoGaeHalIn, Plus, Minus, RowDelete, 
        GaGyukSuJung, CashBakJeokRipAnHam):
        self.MaeJangCode = MaeJangCode
        self.MaeChulDate = MaeChulDate
        self.PosID = PosID
        self.JunPyoBunHo = JunPyoBunHo
        self.BunHo = BunHo
        self.Barcode = Barcode
        self.SangPumName = SangPumName
        self.DaeBunRyu = DaeBunRyu
        self.JoongBunRyu = JoongBunRyu
        self.SoBunRyu = SoBunRyu
        self.MaeIpDanGa = MaeIpDanGa
        self.MaeChulDanGa = MaeChulDanGa
        self.MaeChulSuRyang = MaeChulSuRyang
        self.HalInHapGae = HalInHapGae
        self.MaeChulGumAk = MaeChulGumAk
        self.HangSaHalIn = HangSaHalIn 
        self.HalInBiYul = HalInBiYul
        self.DanPumHalIn = DanPumHalIn
        self.MyunGwaSe = MyunGwaSe
        self.GwaSeGumAk = GwaSeGumAk
        self.VatGumAk = VatGumAk
        self.MyunSeGumAk = MyunSeGumAk
        self.SaWonBunHo = SaWonBunHo
        self.GeunMuChaSu = GeunMuChaSu
        self.SilMaeChulDate = SilMaeChulDate
        self.SilMaeChulTime = SilMaeChulTime 
        self.PanMaeGuBun = PanMaeGuBun
        self.MaeChulGuBun = MaeChulGuBun
        self.JunSongYeoBu = JunSongYeoBu
        self.BonJumJunSongYeoBu = BonJumJunSongYeoBu
        self.BonJumBalJuYeoBu = BonJumBalJuYeoBu
        self.SuSuRyoMaeJangCode = SuSuRyoMaeJangCode
        self.SuSuRyoYul = SuSuRyoYul
        self.GongByungGumAk = GongByungGumAk
        self.SangPumGuBun = SangPumGuBun
        self.HangSaGumAk = HangSaGumAk
        self.HangSaYeoBu = HangSaYeoBu
        self.GuRaeChuCode = GuRaeChuCode
        self.JaSaGoGakCode = JaSaGoGakCode
        self.TaSaGoGakGuBun = TaSaGoGakGuBun
        self.TaSaGoGakCode = TaSaGoGakCode
        self.DeungRokGuBun = DeungRokGuBun
        self.GoGakPointGumAk = GoGakPointGumAk
        self.GoGakPointJumSu = GoGakPointJumSu
        self.TableBunHo = TableBunHo
        self.GaeCheBunHo = GaeCheBunHo
        self.DanMalGiID = DanMalGiID
        self.PointJukRipYeoBu = PointJukRipYeoBu
        self.PointJukRipYul = PointJukRipYul
        self.HyunGumPointGiJun = HyunGumPointGiJun
        self.HyunGumPointBase = HyunGumPointBase
        self.CardPointGiJun = CardPointGiJun
        self.CardPointBase = CardPointBase
        self.HyunGumYoungSuJeongPointGiJun = HyunGumYoungSuJeongPointGiJun
        self.HyunGumYoungSuJeongPointBase = HyunGumYoungSuJeongPointBase
        self.HyunGumPoint = HyunGumPoint
        self.CardPoint = CardPoint
        self.HyunGumYoungSuJeongPoint = HyunGumYoungSuJeongPoint
        self.HyunGumBiYul = HyunGumBiYul
        self.CardBiYul = CardBiYul
        self.HyunGumYoungSuJeongBiYul = HyunGumYoungSuJeongBiYul
        self.RelatedJunPyo = RelatedJunPyo
        self.CardSuSuRyoYul = CardSuSuRyoYul
        self.GoGakHyunGumSuSuRyoYul = GoGakHyunGumSuSuRyoYul
        self.GoGakCardSuSuRyoYul = GoGakCardSuSuRyoYul
        self.HyunGumYoungSuJeungSuSuRyoYul = HyunGumYoungSuJeungSuSuRyoYul
        self.CashBagHyunGumSuSuRyoYul = CashBagHyunGumSuSuRyoYul
        self.CashBagCardSuSuRyoYul = CashBagCardSuSuRyoYul
        self.GBCardHyunGumSuSuRyoYul = GBCardHyunGumSuSuRyoYul
        self.GBCardCardSuSuRyoYul = GBCardCardSuSuRyoYul
        self.BZeroHyunGumSuSuRyoYul = BZeroHyunGumSuSuRyoYul
        self.BZeroCardSuSuRyoYul = BZeroCardSuSuRyoYul
        self.BaeDal = BaeDal
        self.HalJeongYul = HalJeongYul
        self.MaeChulTime = MaeChulTime
        self.RelatedPosID = RelatedPosID
        self.SoGaeHalIn = SoGaeHalIn
        self.Plus = Plus
        self.Minus = Minus
        self.RowDelete = RowDelete
        self.GaGyukSuJung = GaGyukSuJung
        self.CashBakJeokRipAnHam = CashBakJeokRipAnHam

    def __repr__(self):
        return "<TbMaeChulMyungSe('%s', '%s', '%s', '%s', '%s'>" %(self.maeJangCode, self.maeChulDate, self.posID, self.JunPyoBunHo, self.BunHo)

   