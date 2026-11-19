from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="cfa9e6fb-4ac9-5e8b-a1b4-e759981e17e8",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    display_name="Charcadet",
    searchable_by=["Charcadet", "Basic", "Charcadet"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="ME2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=935,
    abilities=[
        Attack(
            title="Gather Strength",
            game_text="Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=search_to_hand(predicate=is_basic_energy_card, count=2, minimum=0),
        ),
        Attack(
            title="Chop",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
    ],
)