from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import named

card = PokemonCardDef(
    guid="07355528-e9e4-5515-b7b9-c760e07d9a92",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysLapras.Name",
    display_name="Misty's Lapras",
    searchable_by=["Misty's Lapras", "Basic", "MistysLapras"],
    subtypes=["Basic"],
    collector_number=194,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=131,
    abilities=[
        Attack(
            title="Swim Together",
            game_text="Search your deck for up to 3 Misty's Pok\u00e9mon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_hand(named("misty's"), count=3, reveal=True),
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)