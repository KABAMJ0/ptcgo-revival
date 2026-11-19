from ptcgo.game.data_utils import StadiumCardDef, def_for
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_named, stadium_hp_bonus


def ange_floette_playable(board, player_id):
    area = board.find_global_area("activeStadium")
    for stadium in (area.children if area else []):
        return (getattr(def_for(stadium.archetype_id), "display_name", "") or "") \
            == "Prism Tower"
    return False


card = StadiumCardDef(
    guid="e22bce31-6c39-5d34-8c79-32d1d91c5a47",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AngeFloette.Name",
    display_name="Ange Floette",
    searchable_by=["Ange Floette", "Stadium"],
    subtypes=["Stadium"],
    collector_number=75,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    passive=stadium_hp_bonus(150, pokemon_named("Mega Floette")),
    condition=ange_floette_playable,
)
