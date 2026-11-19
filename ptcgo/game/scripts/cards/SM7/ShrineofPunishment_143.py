from ptcgo.game.data_utils import StadiumCardDef, unimplemented, Ability, Triggers
from ptcgo.game.card_effects.support_common import counters_each_in_play
from ptcgo.game.card_effects.pokemon import has_pokemon_subtype
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="f3eb7eaf-99b4-5356-9f22-2039c546c38f",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShrineofPunishment.Name",
    display_name="Shrine of Punishment",
    searchable_by=["Shrine of Punishment", "Stadium"],
    subtypes=["Stadium"],
    collector_number=143,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Shrine of Punishment",
        trigger=Triggers.BETWEEN_TURNS,
        effect=counters_each_in_play(1, lambda p: has_pokemon_subtype(p, "GX", "EX", "ex")),
    )
)
