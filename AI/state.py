import enum


@enum.unique
class PlayerType(enum.Enum):
    Human      = 0
    CPU        = 1
    Demo       = 2
    Unselected = 3


@enum.unique
class Character(enum.Enum):
    Doc        = 0
    Mario      = 1
    Luigi      = 2
    Bowser     = 3
    Peach      = 4
    Yoshi      = 5
    DK         = 6
    Falcon     = 7
    Ganon      = 8
    Falco      = 9
    Fox        = 10
    Ness       = 11
    Icies      = 12
    Kirby      = 13
    Samus      = 14
    Zelda      = 15
    Link       = 16
    YoungLink  = 17
    Pichu      = 18
    Pikachu    = 19
    Jiggs      = 20
    Mewtwo     = 21
    GnW        = 22
    Marth      = 23
    Roy        = 24
    Unselected = 25


@enum.unique
class Stage(enum.Enum):
    PeachCastle = 0
    Rainbow     = 1
    Kongo       = 2
    Japes       = 3
    GreatBay    = 4
    Temple      = 5
    Story       = 6
    Island      = 7
    FoD         = 8
    Greens      = 9
    Corneria    = 10
    Venom       = 11
    Brinstar    = 12
    Depths      = 13
    Onett       = 14
    Fourside    = 15
    Mute        = 16
    BigBlue     = 17
    Pokemon     = 18
    Floats      = 19
    Kingdom     = 20
    Kingdom2    = 21
    Icicle      = 22
    FlatZone    = 23
    Battlefield = 24
    Final       = 25
    DreamLand   = 26
    Island64    = 27
    Kongo64     = 28
    Random      = 29
    Unselected  = 30


@enum.unique
class Menu(enum.Enum):
    Characters = 0
    Stages     = 1
    Game       = 2
    PostGame   = 4


@enum.unique
class ActionState(enum.Enum):
    DeadDown                = 0x0000
    DeadLeft                = 0x0001
    DeadRight               = 0x0002
    DeadUp                  = 0x0003
    DeadUpStar              = 0x0004
    DeadUpStarIce           = 0x0005
    DeadUpFall              = 0x0006
    DeadUpFallHitCamera     = 0x0007
    DeadUpFallHitCameraFlat = 0x0008
    DeadUpFallIce           = 0x0009
    DeadUpFallHitCameraIce  = 0x000A
    Sleep                   = 0x000B
    Rebirth                 = 0x000C
    RebirthWait             = 0x000D
    Wait                    = 0x000E
    WalkSlow                = 0x000F
    WalkMiddle              = 0x0010
    WalkFast                = 0x0011
    Turn                    = 0x0012
    TurnRun                 = 0x0013
    Dash                    = 0x0014
    Run                     = 0x0015
    RunDirect               = 0x0016
    RunBrake                = 0x0017
    KneeBend                = 0x0018
    JumpF                   = 0x0019
    JumpB                   = 0x001A
    JumpAerialF             = 0x001B
    JumpAerialB             = 0x001C
    Fall                    = 0x001D
    FallF                   = 0x001E
    FallB                   = 0x001F
    FallAerial              = 0x0020
    FallAerialF             = 0x0021
    FallAerialB             = 0x0022
    FallSpecial             = 0x0023
    FallSpecialF            = 0x0024
    FallSpecialB            = 0x0025
    DamageFall              = 0x0026
    Squat                   = 0x0027
    SquatWait               = 0x0028
    SquatRv                 = 0x0029
    Landing                 = 0x002A
    LandingFallSpecial      = 0x002B
    Attack11                = 0x002C
    Attack12                = 0x002D
    Attack13                = 0x002E
    Attack100Start          = 0x002F
    Attack100Loop           = 0x0030
    Attack100End            = 0x0031
    AttackDash              = 0x0032
    AttackS3Hi              = 0x0033
    AttackS3HiS             = 0x0034
    AttackS3S               = 0x0035
    AttackS3LwS             = 0x0036
    AttackS3Lw              = 0x0037
    AttackHi3               = 0x0038
    AttackLw3               = 0x0039
    AttackS4Hi              = 0x003A
    AttackS4HiS             = 0x003B
    AttackS4S               = 0x003C
    AttackS4LwS             = 0x003D
    AttackS4Lw              = 0x003E
    AttackHi4               = 0x003F
    AttackLw4               = 0x0040
    AttackAirN              = 0x0041
    AttackAirF              = 0x0042
    AttackAirB              = 0x0043
    AttackAirHi             = 0x0044
    AttackAirLw             = 0x0045
    LandingAirN             = 0x0046
    LandingAirF             = 0x0047
    LandingAirB             = 0x0048
    LandingAirHi            = 0x0049
    LandingAirLw            = 0x004A
    DamageHi1               = 0x004B
    DamageHi2               = 0x004C
    DamageHi3               = 0x004D
    DamageN1                = 0x004E
    DamageN2                = 0x004F
    DamageN3                = 0x0050
    DamageLw1               = 0x0051
    DamageLw2               = 0x0052
    DamageLw3               = 0x0053
    DamageAir1              = 0x0054
    DamageAir2              = 0x0055
    DamageAir3              = 0x0056
    DamageFlyHi             = 0x0057
    DamageFlyN              = 0x0058
    DamageFlyLw             = 0x0059
    DamageFlyTop            = 0x005A
    DamageFlyRoll           = 0x005B
    LightGet                = 0x005C
    HeavyGet                = 0x005D
    LightThrowF             = 0x005E
    LightThrowB             = 0x005F
    LightThrowHi            = 0x0060
    LightThrowLw            = 0x0061
    LightThrowDash          = 0x0062
    LightThrowDrop          = 0x0063
    LightThrowAirF          = 0x0064
    LightThrowAirB          = 0x0065
    LightThrowAirHi         = 0x0066
    LightThrowAirLw         = 0x0067
    HeavyThrowF             = 0x0068
    HeavyThrowB             = 0x0069
    HeavyThrowHi            = 0x006A
    HeavyThrowLw            = 0x006B
    LightThrowF4            = 0x006C
    LightThrowB4            = 0x006D
    LightThrowHi4           = 0x006E
    LightThrowLw4           = 0x006F
    LightThrowAirF4         = 0x0070
    LightThrowAirB4         = 0x0071
    LightThrowAirHi4        = 0x0072
    LightThrowAirLw4        = 0x0073
    HeavyThrowF4            = 0x0074
    HeavyThrowB4            = 0x0075
    HeavyThrowHi4           = 0x0076
    HeavyThrowLw4           = 0x0077
    SwordSwing1             = 0x0078
    SwordSwing3             = 0x0079
    SwordSwing4             = 0x007A
    SwordSwingDash          = 0x007B
    BatSwing1               = 0x007C
    BatSwing3               = 0x007D
    BatSwing4               = 0x007E
    BatSwingDash            = 0x007F
    ParasolSwing1           = 0x0080
    ParasolSwing3           = 0x0081
    ParasolSwing4           = 0x0082
    ParasolSwingDash        = 0x0083
    HarisenSwing1           = 0x0084
    HarisenSwing3           = 0x0085
    HarisenSwing4           = 0x0086
    HarisenSwingDash        = 0x0087
    StarRodSwing1           = 0x0088
    StarRodSwing3           = 0x0089
    StarRodSwing4           = 0x008A
    StarRodSwingDash        = 0x008B
    LipStickSwing1          = 0x008C
    LipStickSwing3          = 0x008D
    LipStickSwing4          = 0x008E
    LipStickSwingDash       = 0x008F
    ItemParasolOpen         = 0x0090
    ItemParasolFall         = 0x0091
    ItemParasolFallSpecial  = 0x0092
    ItemParasolDamageFall   = 0x0093
    LGunShoot               = 0x0094
    LGunShootAir            = 0x0095
    LGunShootEmpty          = 0x0096
    LGunShootAirEmpty       = 0x0097
    FireFlowerShoot         = 0x0098
    FireFlowerShootAir      = 0x0099
    ItemScrew               = 0x009A
    ItemScrewAir            = 0x009B
    DamageScrew             = 0x009C
    DamageScrewAir          = 0x009D
    ItemScopeStart          = 0x009E
    ItemScopeRapid          = 0x009F
    ItemScopeFire           = 0x00A0
    ItemScopeEnd            = 0x00A1
    ItemScopeAirStart       = 0x00A2
    ItemScopeAirRapid       = 0x00A3
    ItemScopeAirFire        = 0x00A4
    ItemScopeAirEnd         = 0x00A5
    ItemScopeStartEmpty     = 0x00A6
    ItemScopeRapidEmpty     = 0x00A7
    ItemScopeFireEmpty      = 0x00A8
    ItemScopeEndEmpty       = 0x00A9
    ItemScopeAirStartEmpty  = 0x00AA
    ItemScopeAirRapidEmpty  = 0x00AB
    ItemScopeAirFireEmpty   = 0x00AC
    ItemScopeAirEndEmpty    = 0x00AD
    LiftWait                = 0x00AE
    LiftWalk1               = 0x00AF
    LiftWalk2               = 0x00B0
    LiftTurn                = 0x00B1
    GuardOn                 = 0x00B2
    Guard                   = 0x00B3
    GuardOff                = 0x00B4
    GuardSetOff             = 0x00B5
    GuardReflect            = 0x00B6
    DownBoundU              = 0x00B7
    DownWaitU               = 0x00B8
    DownDamageU             = 0x00B9
    DownStandU              = 0x00BA
    DownAttackU             = 0x00BB
    DownFowardU             = 0x00BC
    DownBackU               = 0x00BD
    DownSpotU               = 0x00BE
    DownBoundD              = 0x00BF
    DownWaitD               = 0x00C0
    DownDamageD             = 0x00C1
    DownStandD              = 0x00C2
    DownAttackD             = 0x00C3
    DownFowardD             = 0x00C4
    DownBackD               = 0x00C5
    DownSpotD               = 0x00C6
    Passive                 = 0x00C7
    PassiveStandF           = 0x00C8
    PassiveStandB           = 0x00C9
    PassiveWall             = 0x00CA
    PassiveWallJump         = 0x00CB
    PassiveCeil             = 0x00CC
    ShieldBreakFly          = 0x00CD
    ShieldBreakFall         = 0x00CE
    ShieldBreakDownU        = 0x00CF
    ShieldBreakDownD        = 0x00D0
    ShieldBreakStandU       = 0x00D1
    ShieldBreakStandD       = 0x00D2
    FuraFura                = 0x00D3
    Catch                   = 0x00D4
    CatchPull               = 0x00D5
    CatchDash               = 0x00D6
    CatchDashPull           = 0x00D7
    CatchWait               = 0x00D8
    CatchAttack             = 0x00D9
    CatchCut                = 0x00DA
    ThrowF                  = 0x00DB
    ThrowB                  = 0x00DC
    ThrowHi                 = 0x00DD
    ThrowLw                 = 0x00DE
    CapturePulledHi         = 0x00DF
    CaptureWaitHi           = 0x00E0
    CaptureDamageHi         = 0x00E1
    CapturePulledLw         = 0x00E2
    CaptureWaitLw           = 0x00E3
    CaptureDamageLw         = 0x00E4
    CaptureCut              = 0x00E5
    CaptureJump             = 0x00E6
    CaptureNeck             = 0x00E7
    CaptureFoot             = 0x00E8
    EscapeF                 = 0x00E9
    EscapeB                 = 0x00EA
    Escape                  = 0x00EB
    EscapeAir               = 0x00EC
    ReboundStop             = 0x00ED
    Rebound                 = 0x00EE
    ThrownF                 = 0x00EF
    ThrownB                 = 0x00F0
    ThrownHi                = 0x00F1
    ThrownLw                = 0x00F2
    ThrownLwWomen           = 0x00F3
    Pass                    = 0x00F4
    Ottotto                 = 0x00F5
    OttottoWait             = 0x00F6
    FlyReflectWall          = 0x00F7
    FlyReflectCeil          = 0x00F8
    StopWall                = 0x00F9
    StopCeil                = 0x00FA
    MissFoot                = 0x00FB
    CliffCatch              = 0x00FC
    CliffWait               = 0x00FD
    CliffClimbSlow          = 0x00FE
    CliffClimbQuick         = 0x00FF
    CliffAttackSlow         = 0x0100
    CliffAttackQuick        = 0x0101
    CliffEscapeSlow         = 0x0102
    CliffEscapeQuick        = 0x0103
    CliffJumpSlow1          = 0x0104
    CliffJumpSlow2          = 0x0105
    CliffJumpQuick1         = 0x0106
    CliffJumpQuick2         = 0x0107
    AppealR                 = 0x0108
    AppealL                 = 0x0109
    ShoulderedWait          = 0x010A
    ShoulderedWalkSlow      = 0x010B
    ShoulderedWalkMiddle    = 0x010C
    ShoulderedWalkFast      = 0x010D
    ShoulderedTurn          = 0x010E
    ThrownFF                = 0x010F
    ThrownFB                = 0x0110
    ThrownFHi               = 0x0111
    ThrownFLw               = 0x0112
    CaptureCaptain          = 0x0113
    CaptureYoshi            = 0x0114
    YoshiEgg                = 0x0115
    CaptureKoopa            = 0x0116
    CaptureDamageKoopa      = 0x0117
    CaptureWaitKoopa        = 0x0118
    ThrownKoopaF            = 0x0119
    ThrownKoopaB            = 0x011A
    CaptureKoopaAir         = 0x011B
    CaptureDamageKoopaAir   = 0x011C
    CaptureWaitKoopaAir     = 0x011D
    ThrownKoopaAirF         = 0x011E
    ThrownKoopaAirB         = 0x011F
    CaptureKirby            = 0x0120
    CaptureWaitKirby        = 0x0121
    ThrownKirbyStar         = 0x0122
    ThrownCopyStar          = 0x0123
    ThrownKirby             = 0x0124
    BarrelWait              = 0x0125
    Bury                    = 0x0126
    BuryWait                = 0x0127
    BuryJump                = 0x0128
    DamageSong              = 0x0129
    DamageSongWait          = 0x012A
    DamageSongRv            = 0x012B
    DamageBind              = 0x012C
    CaptureMewtwo           = 0x012D
    CaptureMewtwoAir        = 0x012E
    ThrownMewtwo            = 0x012F
    ThrownMewtwoAir         = 0x0130
    WarpStarJump            = 0x0131
    WarpStarFall            = 0x0132
    HammerWait              = 0x0133
    HammerWalk              = 0x0134
    HammerTurn              = 0x0135
    HammerKneeBend          = 0x0136
    HammerFall              = 0x0137
    HammerJump              = 0x0138
    HammerLanding           = 0x0139
    KinokoGiantStart        = 0x013A
    KinokoGiantStartAir     = 0x013B
    KinokoGiantEnd          = 0x013C
    KinokoGiantEndAir       = 0x013D
    KinokoSmallStart        = 0x013E
    KinokoSmallStartAir     = 0x013F
    KinokoSmallEnd          = 0x0140
    KinokoSmallEndAir       = 0x0141
    Entry                   = 0x0142
    EntryStart              = 0x0143
    EntryEnd                = 0x0144
    DamageIce               = 0x0145
    DamageIceJump           = 0x0146
    CaptureMasterhand       = 0x0147
    CapturedamageMasterhand = 0x0148
    CapturewaitMasterhand   = 0x0149
    ThrownMasterhand        = 0x014A
    CaptureKirbyYoshi       = 0x014B
    KirbyYoshiEgg           = 0x014C
    CaptureLeadead          = 0x014D
    CaptureLikelike         = 0x014E
    DownReflect             = 0x014F
    CaptureCrazyhand        = 0x0150
    CapturedamageCrazyhand  = 0x0151
    CapturewaitCrazyhand    = 0x0152
    ThrownCrazyhand         = 0x0153
    BarrelCannonWait        = 0x0154
    Wait1                   = 0x0155
    Wait2                   = 0x0156
    Wait3                   = 0x0157
    Wait4                   = 0x0158
    WaitItem                = 0x0159
    SquatWait1              = 0x015A
    SquatWait2              = 0x015B
    SquatWaitItem           = 0x015C
    GuardDamage             = 0x015D
    EscapeN                 = 0x015E
    AttackS4Hold            = 0x015F
    HeavyWalk1              = 0x0160
    HeavyWalk2              = 0x0161
    ItemHammerWait          = 0x0162
    ItemHammerMove          = 0x0163
    ItemBlind               = 0x0164
    DamageElec              = 0x0165
    FuraSleepStart          = 0x0166
    FuraSleepLoop           = 0x0167
    FuraSleepEnd            = 0x0168
    WallDamage              = 0x0169
    CliffWait1              = 0x016A
    CliffWait2              = 0x016B
    SlipDown                = 0x016C
    Slip                    = 0x016D
    SlipTurn                = 0x016E
    SlipDash                = 0x016F
    SlipWait                = 0x0170
    SlipStand               = 0x0171
    SlipAttack              = 0x0172
    SlipEscapeF             = 0x0173
    SlipEscapeB             = 0x0174
    AppealS                 = 0x0175
    Zitabata                = 0x0176
    CaptureKoopaHit         = 0x0177
    ThrownKoopaEndF         = 0x0178
    ThrownKoopaEndB         = 0x0179
    CaptureKoopaAirHit      = 0x017A
    ThrownKoopaAirEndF      = 0x017B
    ThrownKoopaAirEndB      = 0x017C
    ThrownKirbyDrinkSShot   = 0x017D
    ThrownKirbySpitSShot    = 0x017E
    Unselected              = 0x8000


@enum.unique
class BodyState(enum.Enum):
    Normal     = 0
    Invincible = 1
    Intangible = 2


'''Some general states'''
def is_spawning(state):
    if state is ActionState.RebirthWait:
        return True
    else:
        return False

def can_move(state):
    if state is ActionState.Wait or\
        state is ActionState.Landing:
        return True
    else:
        return False

def can_getupattack(state):
    if state is ActionState.DownWaitU or\
        state is ActionState.DownWaitD:
        return True
    else:
        return False

def is_dying(state):
    if state is ActionState.DeadDown or\
        state is ActionState.DeadLeft or\
        state is ActionState.DeadRight or\
        state is ActionState.DeadUp or\
        state is ActionState.DeadUpStar or\
        state is ActionState.DeadUpStarIce or\
        state is ActionState.DeadUpFall or\
        state is ActionState.DeadUpFallHitCamera or\
        state is ActionState.DeadUpFallHitCameraFlat or\
        state is ActionState.DeadUpFallIce or\
        state is ActionState.DeadUpFallHitCameraIce:
        return True
    else:
        return False


class State:
    '''Databag that is handled by StateManager.'''
    pass
