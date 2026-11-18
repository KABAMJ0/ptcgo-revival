from ptcgo.game.data_utils import SupporterCardDef, def_for
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import extra_prize_on_ko, named

_REQUIRED_IN_PLAY = ("N's Darmanitan", "N's Zoroark ex", "N's Vanilluxe",
                     "N's Klinklang", "N's Reshiram", "N's Zekrom")


def _anthea_playable(board, player_id):
    """Only with all six named N's Pokemon in play at once."""
    names = {(getattr(def_for(p.archetype_id), "display_name", "") or "")
             for p in board.pokemon_in_play(player_id)}
    return all(name in names for name in _REQUIRED_IN_PLAY)


card = SupporterCardDef(
    guid="65d89447-d8f7-51a7-adaf-0999518118d6",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntheaConcordia.Name",
    display_name="Anthea & Concordia",
    searchable_by=["Anthea & Concordia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=182,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    condition=_anthea_playable,
    effect=extra_prize_on_ko(named("N's"), 3),
)
