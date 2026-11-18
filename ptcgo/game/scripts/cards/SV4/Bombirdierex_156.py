from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.card_effects.support_common import (
    is_basic, remove_self_from_play, search_to_bench,
)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import (
    is_basic, remove_self_from_play, search_to_bench,
)

card = PokemonCardDef(
    guid="c72ee44d-e61b-5e21-920d-f630048b0fa5",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bombirdierex.Name",
    display_name="Bombirdier ex",
    searchable_by=["Bombirdier ex", "Basic", "ex", "Bombirdierex"],
    subtypes=["Basic", "ex"],
    collector_number=156,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=962,
    abilities=[
        Attack(
            title="Fast Carrier",
            game_text="If you go first, you can use this attack during your first turn. Search your deck for up to 3 Basic Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            usable_first_turn=True,
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(is_basic, count=3),
        ),
        Attack(
            title="Shadowy Wind",
            game_text="You may put this Pok\u00e9mon and all attached cards into your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=remove_self_from_play(destination="hand",
                                         with_attachments="same", optional=True),
        ),
    ],
)