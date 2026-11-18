from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import named_exactly

card = PokemonCardDef(
    guid="cf658580-4663-545b-a736-1f966e27d998",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drakloak.Name",
    display_name="Drakloak",
    searchable_by=["Drakloak", "Stage 1", "Drakloak"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dreepy.Name",
    family_id=885,
    abilities=[
        Attack(
            title="Summon",
            game_text="Search your deck for a Dreepy and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(named_exactly("dreepy"), count=1),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=40,
        ),
    ],
)