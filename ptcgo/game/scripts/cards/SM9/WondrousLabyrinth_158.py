from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.card_effects.passives_common import attack_cost_modifier, pokemon_of_types
from ptcgo.game.attributes import Rarities, PokemonTypes

card = StadiumCardDef(
    guid="d51677c0-4efd-53b4-b1fb-50b59414cb3e",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WondrousLabyrinth.Name",
    display_name="Wondrous Labyrinth ◇",
    searchable_by=["Wondrous Labyrinth \u25c7", "Stadium", "Prism Star"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=158,
    set_code="SM9",
    rarity=Rarities.Rare,
    passive=attack_cost_modifier(1, pred=lambda p, b: not pokemon_of_types(PokemonTypes.FAIRY.value)(p))
)
