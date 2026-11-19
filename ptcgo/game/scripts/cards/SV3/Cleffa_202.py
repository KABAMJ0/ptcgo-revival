from ptcgo.game.card_effects.support_common import draw_until_effect
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dad0b74f-d599-5be1-bb2b-385c68fa3067",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cleffa.Name",
    display_name="Cleffa",
    searchable_by=["Cleffa", "Basic", "Cleffa"],
    subtypes=["Basic"],
    collector_number=202,
    set_code="SV3",
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