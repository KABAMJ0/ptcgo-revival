from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_tool_card

card = PokemonCardDef(
    guid="1548b1bd-e06b-5e05-b461-140a5528ac2f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bombirdier.Name",
    display_name="Bombirdier",
    searchable_by=["Bombirdier", "Basic", "Bombirdier"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=962,
    abilities=[
        Attack(
            title="Knickknack Carrying",
            game_text="Search your deck for up to 3 Pok\u00e9mon Tool cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_tool_card, count=3, minimum=0),
        ),
        Attack(
            title="Clutch",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)