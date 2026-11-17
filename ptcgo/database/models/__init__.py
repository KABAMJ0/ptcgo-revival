from ptcgo.database.base import Base
from ptcgo.database.models.account import Account
from ptcgo.database.models.inventory import Wallet, Deck, Collection, ArchetypeFlag
from ptcgo.database.models.social import Friendship
from ptcgo.database.models.quests import QuestAccount, DailyQuest, QuestMatchCredit
from ptcgo.database.models.economy import (
    RedemptionCode, CodeRedemptionEntry, ShopItem, TradeOffer, DynamicPage, VersusProgress, DailyLoginProgress
)
from ptcgo.database.models.tournaments import (
    AsyncTournament, TournamentEntry, TournamentLeaderboardClaim
)

for table in Base.metadata.tables.values():
    table.dialect_options["mysql"]["engine"] = "InnoDB"
    table.dialect_options["mysql"]["charset"] = "utf8mb4"
    table.dialect_options["mysql"]["collate"] = "utf8mb4_bin"

__all__ = [
    "Base", "Account", "Wallet", "Deck", "Collection", "ArchetypeFlag", "Friendship",
    "RedemptionCode", "CodeRedemptionEntry", "ShopItem", "TradeOffer", "DynamicPage",
    "VersusProgress", "DailyLoginProgress",
    "QuestAccount", "DailyQuest", "QuestMatchCredit",
    "AsyncTournament", "TournamentEntry", "TournamentLeaderboardClaim"
]
