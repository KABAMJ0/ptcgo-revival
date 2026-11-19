from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_tool_card
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="8a16c0d7-1561-59f5-829f-1d81ec286bc7",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    display_name="Meltan",
    searchable_by=["Meltan", "Basic", "Meltan"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=808,
    abilities=[
        Attack(
            title="Knickknack Carrying",
            game_text="Search your deck for a Pok\u00e9mon Tool card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.METAL: 1},
            effect=search_to_hand(is_tool_card, count=1, minimum=1, reveal=True),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)