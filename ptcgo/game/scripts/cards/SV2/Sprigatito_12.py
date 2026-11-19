from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="ab7c0ca2-1cbe-55ba-bc9e-4c21a5570002",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name",
    display_name="Sprigatito",
    searchable_by=["Sprigatito", "Basic", "Sprigatito"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=906,
    abilities=[
        Attack(
            title="Gather Sunlight",
            game_text="Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=search_to_hand(predicate=is_basic_energy_card, count=2, minimum=0),
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)