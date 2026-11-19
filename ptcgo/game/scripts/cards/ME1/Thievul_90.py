from ptcgo.game.card_effects.support_common import draw_until_effect
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect

card = PokemonCardDef(
    guid="45a4ba1c-9c22-51f2-aae3-8b3d8fb6787a",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thievul.Name",
    display_name="Thievul",
    searchable_by=["Thievul", "Stage 1", "Thievul"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="ME1",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name",
    family_id=827,
    abilities=[
        Attack(
            title="Greedy Hunt",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=draw_until_effect(6, optional=True),
        ),
        Attack(
            title="Pitch-Black Fangs",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)