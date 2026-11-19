from ptcgo.game.card_effects.support_common import draw_until_effect
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e70789a0-ec5d-5fb7-bddc-294e82a555e0",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cleffa.Name",
    display_name="Cleffa",
    searchable_by=["Cleffa", "Basic", "Cleffa"],
    subtypes=["Basic"],
    collector_number=150,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    family_id=173,
    abilities=[
        Attack(
            title="Grasping Draw",
            game_text="Draw cards until you have 7 cards in your hand.",
            cost={},
            effect=draw_until_effect(7),
        ),
    ],
)